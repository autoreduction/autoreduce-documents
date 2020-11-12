#############
import urllib2
import xml.dom.minidom as minidom
import numpy as np
import datetime

############


def INTERexptype():
    if exptype=='air_liquid':
        cutoff=[2.1,1.5,1.5,1.5,1.5]
    elif exptype=='solid-liquid':
        cutoff=[1.5,1.5,1.5,1.5,1.5]
    else:
        cutoff=[1.5,1.5,1.5,1.5,1.5]
    return cutoff
###

def INTERsearch(RBno, cycle='',runrange=[],diagnostics=False):
    print 'Loading journal for cycle', cycle
    #xmldoc = minidom.parse(file=urllib2.urlopen('http://data.isis.rl.ac.uk/journals/ndxinter/journal_'+str(cycle)+'.xml'))
    xmldoc = minidom.parse(file=open('//isis/inst$/NDXINTER/Instrument/logs/journal/journal_'+str(cycle)+'.xml'))
    explist=[]
    testing=[]
    angles=[]
    numbers=[]
    badruns=[]
    rbnumber = xmldoc.getElementsByTagName('experiment_identifier')
    for i in range(0, len(rbnumber)):
        test = rbnumber[i].childNodes[0].nodeValue
        if test == str(RBno):
            explist.append(i)
    print 'RB', RBno, 'contains', len(explist), 'runs in cycle', cycle
    
    titles = xmldoc.getElementsByTagName('title')
    detectorcheck = xmldoc.getElementsByTagName('number_detectors')
    for i in list(explist):
        text = titles[i].childNodes[0].nodeValue
        test = detectorcheck[i].childNodes[0].nodeValue
        runno = rbnumber[i].parentNode.getAttribute('name')
        runnostrip = int(runno[5:])
        if runrange and runnostrip not in runrange: 
            if diagnostics:
                print runno, text, 'is outside specified run range and will not be reduced.'            
            badruns.append(i)       
        else:
            if 'th=' in text and int(test) < 20:
                badruns.append('y')
            else:
                if diagnostics:
                    print runno, text, 'is not formatted correctly for NR data on the point detector and will not be reduced.'            
                badruns.append(i)

    for i in reversed(range(len(explist))):
        if badruns[i] != 'y':        
            explist.remove(explist[i])  
   
    runs = xmldoc.getElementsByTagName('run_number')        
    for i in list(explist):
        #runno = rbnumber[i].parentNode.getAttribute('name')
        runno = runs[i].childNodes[0].nodeValue
        numbers.append(int(runno))
        text = titles[i].childNodes[0].nodeValue
        name, theta = text.split('th=', 1)
        testing.append(str(int(runno))+'~ '+str(text))
        #angles.append(theta)
    
    runlist = testing

    return runlist


####
try:
    from mantidplot import *
except ImportError:
    canMantidPlot = False #

#import ui_refl_window
#import refl_save
#import refl_choose_col
#import refl_options
import glob
import string
import csv
import os
import re
import time
import string
from operator import itemgetter
import itertools
from PyQt4 import QtCore, QtGui
from mantid.simpleapi import *
from isis_reflectometry.quick import *
from isis_reflectometry.convert_to_wavelength import ConvertToWavelength
from isis_reflectometry import load_live_runs
from isis_reflectometry.combineMulti import *
import mantidqtpython
from mantid.api import Workspace, WorkspaceGroup, CatalogManager, AlgorithmManager

def all_subdirs_of(b='.'):
  result = []
  for d in os.listdir(b):
    bd = os.path.join(b, d)
    if os.path.isdir(bd): result.append(bd)
  return result

def latest_run():  
    latest=all_subdirs_of(r'//isis/inst$/ndxinter/instrument/data/')
    newest = max(glob.iglob(max(latest)+'/*.nxs'), key=os.path.getctime)
    return int(string.rstrip(string.lstrip(os.path.basename(newest),'INTER'),'.nxs'))


def make_tuples(rlist):
    # sort runs into tuples: run number, title, theta
    tup = ()
    for idx in rlist:
        split_title = re.split("th=|~", idx)
        if len(split_title) != 3:
            split_title = re.split("~", idx)
            if len(split_title) != 2:
                logger.warning('cannot transfer ' +  idx+ ' title is not in the right form ')
            else:
                theta = 0
                split_title.append(theta) # Append a dummy theta value.
                tup = tup + (split_title,)
        else:
            tup = tup + (split_title,) # Tuple of lists containing (run number, title, theta)

    tupsort = sorted(tup, key=itemgetter(1, 2))
    print tupsort
    return tupsort
###


def sort_runs(tupsort):
    # sort tuples of runs into groups beloning to one sample title
    row = 0
    complete_list=[]
    for _key, group in itertools.groupby(tupsort, lambda x: x[1]): # now group by title
        col = 0
        run_angle_pairs_of_title = list() # for storing run_angle pairs all with the same title
        for object in group:  # loop over all with equal title
            one_sample=[]
            run_no = object[0]
            angle = object[-1]
            run_angle_pairs_of_title.append((run_no, angle))
        #print  run_angle_pairs_of_title, "here"
        for angle_key, group in itertools.groupby(run_angle_pairs_of_title, lambda x: x[1]):
            runnumbers = "+".join(["%s" % pair[0] for pair in group])
           
            #if col >= 11:
                #col = 0
                #print "hello"
            #else:
            one_sample.append((runnumbers,angle_key))
            print one_sample
            #col = col + 5
            #print col
        row = row + 1
        complete_list.append(one_sample)
        print complete_list
    sortedList = sorted(complete_list, key=lambda runno: runno[0])
    return sortedList
###


def autoreduce(RBno,cycle, transRun=[], runRange=[], oldList=[], auto=0, angles=[], diagnostics=False):
    if not runRange:
        rlist = INTERsearch(RBno, cycle, diagnostics=diagnostics) 
    else:
        rlist = INTERsearch(RBno, cycle, runRange, diagnostics=diagnostics) 
    tupsort = make_tuples(rlist)
    sortedList = sort_runs(tupsort)
    
    newList = [item for item in sortedList if item not in oldList]
    
    for sample in newList:
        wq_list=[]
        overlapLow=[]
        overlapHigh=[]
        index=0
        for item in sample:
            runno = item[0]
            angle = item[1]
            runnos=string.split(runno,'+')
            runnos = [int(i) for i in runnos] # check if runs have been added together
            
            try:
                angle=float(angle)
            except ValueError:
                angle=0.0
                print "Could not determine theta! Skipping run."
                        
            if len(runRange) and not len(set(runRange) & set(runnos)):
                angle=0.0 # will be skipped below
            
            if float(angle)>0.0:
                ws = ConvertToWavelength.to_workspace(runno+'.raw', ws_prefix="")
                if not mtd.doesExist(runno+'_IvsQ'):
                    th = angle
                    #if len(transRun)>1 and index>0:
                    if len(transRun)>1:
                        if not angles:
                            angle=angle
                        else:
							try:
								angle=angles[index]
							except:
								print("Not enough angles specified.")
							#angle=angles[1]
                        try:
							transmRun=transRun[index]
							cutoff = INTERexptype()[index]
							print(cutoff,"=cutoff")
							ReflectometryReductionOneAuto(InputWorkspace=ws, FirstTransmissionRun=transmRun, WavelengthMin=cutoff, thetaIn=angle, OutputWorkspaceBinned=runno+'_IvsQ_binned', OutputWorkspace=runno+'_IvsQ', OutputWorkspaceWavelength=runno+'_IvsLam')
							wq=mtd[runno+'_IvsQ']
							th = angle
                        except:
                            print("Not enough transmission runs specified or transmission workspace doesn't exist, for run "+str(ws))
                    else:
                        if not angles:
                            angle=angle
                        #else:
                            #angle=angles[0]
                        #cutoff = INTERexptype()
                        cutoff = INTERexptype()[index]
                        print(cutoff,"=cutoff")
                        ReflectometryReductionOneAuto(InputWorkspace=ws, FirstTransmissionRun=transRun[0], thetaIn=angle, WavelengthMin=cutoff, OutputWorkspaceBinned=runno+'_IvsQ_binned', OutputWorkspace=runno+'_IvsQ', OutputWorkspaceWavelength=runno+'_IvsLam') 
                        wq=mtd[runno+'_IvsQ']
                        th = angle
                else:
                    wq=mtd[runno+'_IvsQ']
                    th=angle
                wq_list.append(runno+'_IvsQ')
                inst = wq.getInstrument()
                lmin = 1.8 #inst.getNumberParameter('LambdaMin')[0] + 1
                lmax = 15 #inst.getNumberParameter('LambdaMax')[0] - 2
                qmin = 4 * math.pi / lmax * math.sin(th * math.pi / 180)
                qmax = 4 * math.pi / lmin * math.sin(th * math.pi / 180)
                overlapLow.append(qmin)
                overlapHigh.append(qmax)
                dqq = NRCalculateSlitResolution(Workspace=wq)
            index=index+1
        if len(wq_list):
            w1 = getWorkspace(wq_list[0])
            w2 = getWorkspace(wq_list[-1])
            Qmin = min(w1.readX(0))
            Qmax = max(w2.readX(0))
            Qmax = 0.3

               
            #print Qmin, Qmax, dqq 
            #print overlapHigh
            if len(wq_list)>1:
                outputwksp = string.split(wq_list[0],sep='_')[0] + '_' + string.split(wq_list[-1],sep='_')[0][3:]
            else:
                outputwksp = string.split(wq_list[0],sep='_')[0] + '_IvsQ_binned'
                SaveAscii(InputWorkspace=outputwksp,Filename=savepath+outputwksp+'.dat',Separator='Space',ColumnHeader=False,ScientificFormat=True,WriteSpectrumID=False)      
            if not mtd.doesExist(outputwksp):
                wcomb = combineDataMulti(wq_list,outputwksp , overlapLow, overlapHigh,Qmin, Qmax, -dqq, 0, keep=True)
                SaveAscii(InputWorkspace=outputwksp,Filename=savepath+outputwksp+'.dat',Separator='Space',ColumnHeader=False,ScientificFormat=True,WriteSpectrumID=False)
            
    return sortedList

#############################
def INTERtrans(run1,run2=False,outname=False, scale=False):
    Load(run1+'.raw',OutputWorkspace=run1)
    CreateTransmissionWorkspaceAuto(run1, OutputWorkspace='TRANS_'+str(run1), StartOverlap=10, EndOverlap=12)
    if run2:
        Load(run2+'.raw',OutputWorkspace=run2) 
        CreateTransmissionWorkspaceAuto(run2, OutputWorkspace='TRANS_'+str(run2), StartOverlap=10, EndOverlap=12)
        Stitch1D(LHSWorkspace='TRANS_'+str(run1),RHSWorkspace='TRANS_'+str(run2), StartOverlap=10, EndOverlap=12,ScaleRHSWorkspace=scale,OutputWorkspace='TRANS_'+str(run1)+'_'+str(run2))
        if outname:
            CloneWorkspace('TRANS_'+str(run1)+'_'+str(run2),OutputWorkspace=str(outname))
    else:
        if outname:
            CloneWorkspace('TRANS_'+str(run1),OutputWorkspace=str(outname))
    #
###

import math as m

def EventRefEdit(runno,DB='TRANS',nslices=None,time=None,start=0,stop=0,diagnostics=False,save=False,dqq=False,lam_max=False,output_workspace_name=False,savepath=""):         
    '''This allows you to specify a total number of slices (nslices), or a specific time per slice in seconds (time), as well as the existing specific start/stop times.'''
    if runno==0:
        runno='currentrun'
        Load(Filename=current, OutputWorkspace=runno, LoadMonitors=True)
    else:
        runno=str(runno)
        Load(Filename=runno, OutputWorkspace=runno, LoadMonitors=True)
    w1=mtd[runno]
    angle=w1.getRun().getLogData('theta').value[-1]
    total = w1.getRun().getLogData('gd_prtn_chrg').value
    end = w1.getRun().getLogData('duration').value
    
    #cutoff = INTERexptype()
    cutoff = INTERexptype()[0]
    if not lam_max:
        LowP=4*m.pi*m.sin(angle/180*m.pi)/17
    else:
        LowP=4*m.pi*m.sin(angle/180*m.pi)/lam_max
	
    HighP=4*m.pi*m.sin(angle/180*m.pi)/cutoff
    if not dqq:
        dqq = NRCalculateSlitResolution(Workspace=runno)
    Param=str(LowP)+',-'+str(dqq)+','+str(HighP)    
    if not output_workspace_name:
        output_workspace_name = runno+'_'+str(start)+'_'+str(stop)+'_IvsQ'
    if not nslices:
        if not time:
                if stop==0:
                    stoptime=end
                else:
                    stoptime=stop
                FilterByTime(InputWorkspace=runno, OutputWorkspace=runno+'_filter', StartTime=start, StopTime=stoptime)
                wt=mtd[runno+'_filter']
                slice = wt.getRun().getLogData('gd_prtn_chrg').value
                fraction = slice/total 
                Scale(InputWorkspace=runno+'_monitors',Factor=fraction,OutputWorkspace='mon_slice')
                Rebin(InputWorkspace=runno+'_filter', OutputWorkspace=runno+'_'+str(start)+'_'+str(stop), Params='0,100,100000', PreserveEvents=False)
                Rebin(InputWorkspace='mon_slice', OutputWorkspace='mon_rebin', Params='0,100,100000', PreserveEvents=False)
                AppendSpectra(InputWorkspace1='mon_rebin', InputWorkspace2=runno+'_'+str(start)+'_'+str(stop), OutputWorkspace=runno+'_'+str(start)+'_'+str(stop), MergeLogs=False)
                ReflectometryReductionOneAuto(InputWorkspace=runno+'_'+str(start)+'_'+str(stop), FirstTransmissionRun=DB, WavelengthMin=cutoff, OutputWorkspaceBinned=runno+'_'+str(start)+'_'+str(stop)+'_IvsQ_binned',\
                    OutputWorkspace=str(output_workspace_name)+"slice_"+str(i+1)+"_of_"+str(slices),OutputWorkspaceWavelength=runno+'_'+str(start)+'_'+str(stop)+'_lam',MomentumTransferStep=str(dqq*-1))
                #CropWorkspace()    
                
                if save:
                    SaveAscii(InputWorkspace=str(output_workspace_name)+"slice_"+str(i+1)+"_of_"+str(slices),Filename=savepath+runno+'_'+str(start)+'_'+str(stop)+'.dat',Separator='Space',ColumnHeader=False,ScientificFormat=True,WriteSpectrumID=False)
                if not diagnostics:
                    DeleteWorkspace(runno+'_'+str(start)+'_'+str(stop)+'_lam')
                    DeleteWorkspace(runno+'_'+str(start)+'_'+str(stop)+'_IvsQ')
                    DeleteWorkspace(runno+'_'+str(start)+'_'+str(stop))
                    DeleteWorkspace(runno+'_filter')
                    DeleteWorkspace('mon_slice')
                    DeleteWorkspace('mon_rebin')
                    try:
                        DeleteWorkspace(runno+'_'+str(start)+'_'+str(stop)+'_IvsQ')
                    except:
                        pass
    if nslices:
        timings=end/nslices #time for each slice
        slices=nslices #total no of slices
    if time:
        #slices=int(end/time)
        slices =int(end / time) + (end % time > 0)
        timings=time
    if nslices or time:
       for i in range(0,slices):
           FilterByTime(InputWorkspace=runno, OutputWorkspace=runno+'_filter_'+str(i+1), StartTime=i*timings, StopTime=(i+1)*timings)
           wt=mtd[runno+'_filter_'+str(i+1)]
           slice = wt.getRun().getLogData('gd_prtn_chrg').value
           fraction = slice/total
           Scale(InputWorkspace=runno+'_monitors',Factor=fraction,OutputWorkspace='mon_slice')
           Rebin(InputWorkspace=runno+'_filter_'+str(i+1), OutputWorkspace=runno+'_slice_'+str(i+1), Params='0,100,100000', PreserveEvents=False)
           Rebin(InputWorkspace='mon_slice', OutputWorkspace='mon_rebin', Params='0,100,100000', PreserveEvents=False)
           AppendSpectra(InputWorkspace1='mon_rebin', InputWorkspace2=runno+'_slice_'+str(i+1), OutputWorkspace=runno+'_slice_'+str(i+1), MergeLogs=False)
           ReflectometryReductionOneAuto(InputWorkspace=runno+'_slice_'+str(i+1), FirstTransmissionRun=DB, WavelengthMin=cutoff, OutputWorkspaceBinned=runno+'_slice_'+str(i+1)+'of'+str(slices)+'_IvsQ_binned',\
                    OutputWorkspaceWavelength=runno+'_slice_'+str(i+1)+'of'+str(slices)+'_lam',OutputWorkspace=str(output_workspace_name)+"slice_"+str(i+1)+"_of_"+str(slices),MomentumTransferStep=str(dqq))
           #Rebin(runno+'_slice_'+str(i+1)+'of'+str(slices)+'_ref',Params=Param,OutputWorkspace=runno+'_slice_'+str(i+1)+'of'+str(slices)+'_ref')
           Grouping=str(output_workspace_name)+"slice_"+str(i+1)+"_of_"+str(slices)
           if save:
               SaveAscii(InputWorkspace=str(output_workspace_name)+"slice_"+str(i+1)+"_of_"+str(slices),Filename=savepath+str(output_workspace_name)+"slice_"+str(i+1)+"_of_"+str(slices)+'_t='+str(timings)+'sec.dat',Separator='Space',ColumnHeader=False,ScientificFormat=True,WriteSpectrumID=False)
           if not diagnostics:
               #DeleteWorkspace(runno+'_slice_'+str(i+1)+'of'+str(slices)+'_lam')
               #DeleteWorkspace(runno+'_slice_'+str(i+1)+'of'+str(slices)+'_IvsQ')
               DeleteWorkspace(runno+'_slice_'+str(i+1))
               DeleteWorkspace(runno+'_filter_'+str(i+1))
               DeleteWorkspace('mon_slice')
               DeleteWorkspace('mon_rebin')
    if nslices:
        for i in range(0,slices):
            GroupWorkspaces(Grouping,OutputWorkspace=str(output_workspace_name)+"_all_"+str(slices)+'_slices')
    if time:
        for i in range(0,slices):
            GroupWorkspaces(Grouping,OutputWorkspace=str(output_workspace_name)+"_all_"+str(slices)+'_slices')

def Single_Slice(runno=0,DB="",start=0,stop=0,save=False,diagnostics=False,lam_max=17.0,lam_min=1.0,total=0,dqq=0.02,output_workspace_name="",i=1,slices=1,savepath="",savename=False):
    FilterByTime(InputWorkspace=runno, OutputWorkspace=runno+'_filter', StartTime=start, StopTime=stop)
    wt=mtd[runno+'_filter']
    slice = wt.getRun().getLogData('gd_prtn_chrg').value
    fraction = slice/total 
    Scale(InputWorkspace=runno+'_monitors',Factor=fraction,OutputWorkspace='mon_slice')
    Rebin(InputWorkspace=runno+'_filter', OutputWorkspace=runno+'_'+str(start)+'_'+str(stop), Params='0,20,100000', PreserveEvents=False)
    Rebin(InputWorkspace='mon_slice', OutputWorkspace='mon_rebin', Params='0,20,100000', PreserveEvents=False)
    AppendSpectra(InputWorkspace1='mon_rebin', InputWorkspace2=runno+'_'+str(start)+'_'+str(stop), OutputWorkspace=runno+'_'+str(start)+'_'+str(stop), MergeLogs=False)
    print(runno+'_'+str(start)+'_'+str(stop))
    wt=mtd[runno+'_'+str(start)+'_'+str(stop)]
    start_run_time=wt.getRun().getLogData("start_time").value
    start_run_time=start_run_time.replace("T"," ")
    start_run_time=datetime.datetime.strptime(start_run_time, '%Y-%m-%d %H:%M:%S')
    start_slice_time=start_run_time+datetime.timedelta(seconds=start)
    start_slice_time=str(start_slice_time).replace(":","-")
    
    ReflectometryReductionOneAuto(InputWorkspace=runno+'_'+str(start)+'_'+str(stop), FirstTransmissionRun=DB, WavelengthMin=lam_min, WavelengthMax=lam_max, MomentumTransferStep=str(dqq), OutputWorkspaceBinned=str(output_workspace_name)+"slice_"+str(i+1)+"_of_"+str(slices),\
        OutputWorkspace=str(output_workspace_name)+"slice_"+str(i+1)+"_of_"+str(slices)+"_unbinned",OutputWorkspaceWavelength=runno+'_'+str(start)+'_'+str(stop)+'_lam')    
    
    if save:
        #print(str(output_workspace_name)+"slice_"+str(i+1)+"_of_"+str(slices))
        if not savename:
            savename=str(output_workspace_name)+'_'+str(start)+'_'+str(stop)
        else: 
            savename=str(output_workspace_name)+"_t="+str(start_slice_time)
        SaveAscii(InputWorkspace=str(output_workspace_name)+"slice_"+str(i+1)+"_of_"+str(slices),Filename=str(savepath)+str(savename)+'.dat',Separator='Space',ColumnHeader=False,ScientificFormat=True,WriteSpectrumID=False)
    if not diagnostics:
        #DeleteWorkspace(runno+'_'+str(start)+'_'+str(stop)+'_lam')
        DeleteWorkspace(str(output_workspace_name)+"slice_"+str(i+1)+"_of_"+str(slices)+"_unbinned")
        DeleteWorkspace(runno+'_'+str(start)+'_'+str(stop))
        DeleteWorkspace(runno+'_filter')
        DeleteWorkspace('mon_slice')
        RemoveLogs(str(output_workspace_name)+"slice_"+str(i+1)+"_of_"+str(slices)) #Without this the workspaces get LARGE
        try:
            DeleteWorkspace('mon_rebin')
        except:
            pass

def Time_Slice(runno,DB='TRANS',nslices=None,time=None,start=0,stop=0,diagnostics=False,save=False,dqq=False,lam_max=17.0,lam_min=1.0,output_workspace_name=False,savepath=""):         
    #This allows you to specify a total number of slices (nslices), or a specific time per slice in seconds (time), as well as the existing specific start/stop times.
    if runno==0:
        runno='currentrun'
        Load(Filename=current, OutputWorkspace=runno, LoadMonitors=True)
    else:
        runno=str(runno)
        Load(Filename=runno, OutputWorkspace=runno, LoadMonitors=True)
    w1=mtd[runno]
    angle=w1.getRun().getLogData('theta').value[-1]
    total = w1.getRun().getLogData('gd_prtn_chrg').value
    end = w1.getRun().getLogData('duration').value
    
    LowP=4*m.pi*m.sin(angle/180*m.pi)/lam_max
    HighP=4*m.pi*m.sin(angle/180*m.pi)/lam_min
    if not dqq:     
        dqq = NRCalculateSlitResolution(Workspace=runno)
    Param=str(LowP)+',-'+str(dqq)+','+str(HighP)    
    if not output_workspace_name:
        output_workspace_name = runno+'_'+str(start)+'_'+str(stop)
    if not nslices:
        if not time:
                if stop==0:
                    stoptime=end
                else:
                    stoptime=stop
                #FilterByTime(InputWorkspace=runno, OutputWorkspace=runno+'_filter', StartTime=start, StopTime=stoptime)
                #wt=mtd[runno+'_filter']
                Single_Slice(runno=runno,DB=DB,start=start,stop=stoptime,save=save,diagnostics=diagnostics,lam_max=lam_max,lam_min=lam_min,total=total,dqq=dqq,output_workspace_name=output_workspace_name,i=0,slices=1,savepath=savepath)

    if nslices:
        timings=end/nslices #time for each slice
        slices=nslices #total no of slices
    if time:
        #slices=int(end/time)
        slices =int(end / time) + (end % time > 0)
        timings=time
    if nslices or time:
       for i in range(0,slices):
           start=i*timings
           stoptime=(i+1)*timings
           Single_Slice(runno=runno,DB=DB,start=start,stop=stoptime,save=save,diagnostics=diagnostics,lam_max=lam_max,lam_min=lam_min,total=total,dqq=dqq,output_workspace_name=output_workspace_name,i=i,slices=slices,savepath=savepath,savename=True)
       groupname=""
       for i in range(0,slices):
            Grouping=str(output_workspace_name)+"slice_"+str(i+1)+"_of_"+str(slices)
            groupname=groupname+str(Grouping)+","
       GroupWorkspaces(groupname,OutputWorkspace=str(output_workspace_name)+"_all_"+str(slices)+'_slices')
