
import INTER_autoreduce_longscript as autored

## Function which can be used to setup some defaults for different experiment types.
autored.exptype='solid_liquid' ## For air_liquid experiment

autored.savepath='U:/King/November2019/autoreduce_data/'

reload(autored)

# run this first:
# to create transmission workspace

autored.INTERtrans('50490+50546+50585+50604',outname='TRANS_1_old') ## 
autored.INTERtrans('50491+50542+50581+50600+50617','50492',outname='TRANS_2_old') ## 
autored.INTERtrans('56418+56432+56446','56352+56396+56400+56414+56428+56442+56456+56480',outname='TRANS_1') ## 
autored.INTERtrans('56353+56464','56354',outname='TRANS_2') ## 
autored.INTERtrans('56353+56464','56489',outname='TRANS_3') ## 

runlist=list(range(56404,56411)+range(56419,56425)+range(56433,56439)+range(56447,56453)+range(56468,56480))
print runlist
autored.autoreduce(1920432,'19_3',['TRANS_2'],runRange=runlist) 
autored.autoreduce(1920432,'19_3',['TRANS_1','TRANS_2','TRANS_3']) 

### Need to rerun with the single runs using the correct transmission.

## run here for keeping autoreduction in the background:
#start = autored.latest_run()
#print start
#oldList=[]
#start=48500
#while 1:
#    now = autored.latest_run()
#    oldList=[]
#    if now != start:
#        oldList = autored.autoreduce(1920432,'19_3',['TRANS_1','TRANS_2','TRANS_2'])
#    time.sleep(5)
#############

runs=[56409,56410,56423,56424,56437,56438,56451,56452]
for i in runs:
    Load(Filename=str(i)+'.raw', OutputWorkspace=str(i)+'.raw')
    ReflectometryReductionOneAuto(InputWorkspace=str(i)+'.raw', ThetaIn=1.5, WavelengthMin=1.5, FirstTransmissionRun='TRANS_2', OutputWorkspaceBinned=str(i)+'_IvsQ_binned', OutputWorkspace=str(i)+'_IvsQ', OutputWorkspaceWavelength=str(i)+'_IvsLam')
    SaveAscii(InputWorkspace=str(i)+'_IvsQ_binned',Filename=autored.savepath+str(i)+'_IvsQ_binned.dat',Separator='Space',ColumnHeader=False,ScientificFormat=True,WriteSpectrumID=False)
#

## Event slicing:
autored.savepath='U:/King/November2019/autoreduce_data/time-slices/'
runlist=list(range(56404,56411)+range(56419,56425)+range(56433,56439)+range(56447,56453)+range(56468,56480))
for run in runlist:
    autored.EventRefEdit(run,time=60*15,save=True,DB='TRANS_2')
    autored.EventRefEdit(run,time=60*10,save=True,DB='TRANS_2')
    autored.EventRefEdit(run,time=60*5,save=True,DB='TRANS_2')
    autored.EventRefEdit(run,time=60*30,save=True,DB='TRANS_2')
    autored.EventRefEdit(run,time=60*60,save=True,DB='TRANS_2')
#


