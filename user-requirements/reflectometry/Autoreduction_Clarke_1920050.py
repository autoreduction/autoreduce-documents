
import INTER_autoreduce_longscript as autored

## Function which can be used to setup some defaults for different experiment types.
autored.exptype='solid_liquid' ## For air_liquid experiment

autored.savepath='U:/Clarke/Nov19/autoreduce_data/'

reload(autored)

# run this first:
# to create transmission workspace
autored.INTERtrans('56895+56908',outname='TRANS') ## Si
autored.INTERtrans('56895+56908','56899',outname='TRANS_2') ## Si
autored.INTERtrans('56900+56912',outname='TRANS_Fraggle') ## Si
autored.INTERtrans('56916+56904','56917+56905',outname='TRANS_Si') ## Si
autored.INTERtrans('56976+57001',outname='TRANS_Grover') ## Si

Fraggle_list=list(range(56901,56904))+list(range(56913,56916))+list(range(56926,56929))+list(range(56934,56938))+list(range(56943,56946))+list(range(56949,56952))+list(range(56955,56958))+list(range(56964,56967))+list(range(56973,56980))+list(range(56989,56992))+list(range(56998,57001))
BBird_list=list(range(56896,56899))+list(range(56909,56912))+list(range(56920,56926))+list(range(56938,56941))+list(range(56946,56949))+list(range(56952,56955))+list(range(56958,56964))+list(range(56970,56973))+list(range(56986,56989))+list(range(56995,56998))
Si_list=list(range(56906,56908))+list(range(56918,56920))+list(range(56929,56932))+list(range(56941,56943))+list(range(5692956932,56916))+list(range(56941,56942))
Grover_list=list(range(56980,56983))+list(range(56992,56995))+list(range(57002,57005))

autored.autoreduce(1920050,'19_3',['TRANS','TRANS_2','TRANS_2'],runRange=BBird_list)
autored.autoreduce(1920050,'19_3',['TRANS_Fraggle','TRANS_Fraggle','TRANS_Fraggle'],runRange=Fraggle_list)
autored.autoreduce(1920050,'19_3',['TRANS_Si','TRANS_Si','TRANS_Si'],runRange=Si_list)
autored.autoreduce(1920050,'19_3',['TRANS_Grover','TRANS_Grover','TRANS_Grover'],runRange=Grover_list)

### run here for keeping autoreduction in the background:
start = autored.latest_run()
print start
oldList=[]
start=48500
while 1:
    now = autored.latest_run()
    oldList=[]
    if now != start:
        oldList = autored.autoreduce(1920050,'19_3',['TRANS','TRANS_2','TRANS_2'])
    time.sleep(10)
############

#####


# Quick to sort the last ones:
def QuickRef(runs,trans=['TRANS','TRANS_2','TRANS_2']):
	i=0
	for run in runs:
		Load(Filename=str(run)+'.raw', OutputWorkspace=str(run)+'.raw')
		ReflectometryReductionOneAuto(InputWorkspace=str(run)+'.raw', FirstTransmissionRun=trans[i], OutputWorkspaceBinned=str(run)+'_IvsQ_binned', OutputWorkspace=str(run)+'_IvsQ', OutputWorkspaceWavelength=str(run)+'_IvsLam')
		i=i+1
	CloneWorkspace(InputWorkspace=str(runs[0])+'_IvsQ',OutputWorkspace='currentSum')
	if len(runs) > 1:
		for j in range(1,len(runs)):
			Stitch1D(LHSWorkspace='currentSum', RHSWorkspace=str(runs[j])+'_IvsQ', OutputWorkspace='currentSum',Params='-0.017732')
		RenameWorkspace(InputWorkspace='currentSum', OutputWorkspace=str(runs[0])+'_'+str(runs[-1])[-2:])
		SaveAscii(InputWorkspace=str(runs[0])+'_'+str(runs[-1])[-2:],Filename=autored.savepath+str(runs[0])+'_'+str(runs[-1])[-2:]+'.dat',Separator='Space',ColumnHeader=False,ScientificFormat=True,WriteSpectrumID=False)
	else:
		SaveAscii(InputWorkspace=str(runs[0])+'_IvsQ_binned',Filename=autored.savepath+str(runs[0])+'_'+str(runs[0])+'_IvsQ_binned.dat',Separator='Space',ColumnHeader=False,ScientificFormat=True,WriteSpectrumID=False)
####

### Write the three runs in you want together:
QuickRef([56938,56939,56940])
QuickRef([56946,56947,56948])

QuickRef([56935,56936,56937])
QuickRef([56943,56944,56945])