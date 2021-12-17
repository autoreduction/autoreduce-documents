
import INTER_autoreduce_longscript as autored

## Function which can be used to setup some defaults for different experiment types.
autored.exptype='air_liquid' ## For air_liquid experiment

autored.savepath='U:/King/Jun19/autoreduce_data/'

reload(autored)

# run this first:
# to create transmission workspace
autored.INTERtrans('53953+53959+53965','53954+53960+53966',outname='TRANS_noSM') ## 
#autored.INTERtrans('53953+53959+53965','53958+53964+53970',outname='TRANS_noSM2') ## 
autored.INTERtrans('53956+53962+53968','53957+53963+53969',outname='TRANS_SM') ##
#autored.INTERtrans('53955+53961+53967','53957+53963+53969',outname='TRANS_SM2') ##
#autored.INTERtrans('53956+53962+53968','53955+53961+53967',outname='TRANS_SM3') ##  #This one would need to be scaled.

autored.autoreduce(1910442,'19_1',['TRANS_SM','TRANS_noSM']) 


### run here for keeping autoreduction in the background:
start = autored.latest_run()
print start
oldList=[]
start=48500
while 1:
    now = autored.latest_run()
    oldList=[]
    if now != start:
        oldList = autored.autoreduce(1910442,'19_1',['TRANS_SM','TRANS_noSM'])
    time.sleep(5)
############


