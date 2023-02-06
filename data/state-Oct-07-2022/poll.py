#!/usr/bin/python3 -u
import subprocess
import pandas as pd
import numpy as np
import time
from os import path
from joblib import Memory
#folder="/home/pi/"
memory = Memory("cacheEUI",verbose=0)
myip = None
with open('./myip', 'r') as ipfile:
    line = ipfile.readline().rstrip()
    while line:
        if not "0:ff:fe00" in line:
            myip = line
            break
        line = ipfile.readline().rstrip()
print("myip",[myip])

@memory.cache
def EUI_mem(ip):
    try:
        coap_timeout = pd.read_csv('./parameters.csv').coap_timeout.values[0] # how many seconds before break reading
        temp = subprocess.check_output('coap-client -a '+myip+' -m get -B '+str(coap_timeout)+' coap://['+ip+']/sensors/EUI', shell=True, text=True)
        return temp.split(': ')[1].rstrip()
    except:
        return np.nan

def EUI(ip):
    temp = EUI_mem.call_and_shelve(ip)
    temp_res = temp.get()
    if pd.isna(temp_res):
        temp.clear()
        return np.nan
    else:
        return temp_res


polled='polled.csv'
while True:
    start_time = time.time()
#    threshold_hours = pd.read_csv('./parameters.csv').threshold_hours.values[0] # how many hours back we want to keep polling (last seen)
#    threshold_seconds = threshold_hours * 3600
    coap_timeout = pd.read_csv('./parameters.csv').coap_timeout.values[0] # how many seconds before break reading
    freq_node_read = pd.read_csv('./parameters.csv').freq_node_read[0]
#    subprocess.run('./cleanmulticastlog.sh')
#    log = pd.read_csv('./multicast.csv')
#    log['timestamp'] = pd.to_datetime(log.timestamp, unit='s')
#    log['duplicate']=~log['flag'].isna()
#    log.drop(columns=['flag'],inplace=True)
#    poll_candidates = pd.DataFrame(log.timestamp.max()-log.groupby('ip',sort=['timestamp']).last()['timestamp']).rename(columns={'timestamp':'last_seen'})
#    poll_candidates = poll_candidates.join(pd.DataFrame(log.timestamp.max()-log.groupby('ip',sort=['timestamp']).first()['timestamp']).rename(columns={'timestamp':'first_seen'}))
#    poll_candidates['last_seen'] = poll_candidates['last_seen'].apply(lambda x: x.total_seconds())
#    poll_candidates['first_seen'] = poll_candidates['first_seen'].apply(lambda x: x.total_seconds())
    to_poll = pd.read_csv('routersANDchildren.csv',header=None,index_col=False,names=['ip'],squeeze=False)
    #to_poll = poll_candidates[poll_candidates['last_seen']<threshold_seconds]
    to_poll['EUI'] =[EUI(i) for i in to_poll['ip'].values]
    print(to_poll.to_string())
    #to_poll = to_poll.reset_index()
    to_poll.dropna(subset=['EUI'],inplace=True)
#    print('prima')
#    print(to_poll.to_string())
#    to_poll = to_poll.sort_values(by="last_seen").groupby("EUI").first()
#    print('dopo')
#    print(to_poll.to_string())
#    to_poll = to_poll.reset_index()
    to_poll.to_csv('to_poll.csv',index=False)
    endpoints=['Temperature','Humidity','IR','Vis','Batt']
    #temp_data = {}
#    print(to_poll)
    #to_poll = pd.read_csv('to_poll.csv') # inside the loop so it's always up to date
    frequency_s = pd.read_csv('parameters.csv').freq_polling.values[0]
    def rotate(l, n):
        return l[n:] + l[:n]
    def read_endpoint(endpoint):
        try:
            temp = subprocess.check_output('coap-client -a '+myip+' -m get '+'-B '+str(coap_timeout)+' coap://['+row.ip+']/sensors/'+endpoint, shell=True, text=True).rstrip()
            l = temp.strip(',').split(',')
            #print('qua',l)
            first = 0
            for item in [(i, j) for i, j in enumerate(l)]:
                if item[1][0]!='a':
                    first = item[0]
                    break
            l = rotate(l,first)
            temp = [a.strip('a') for a in l]
            #print('fine lettora')
            #print(temp)
        except:
            temp = [np.nan]
        return temp
    for index, row in to_poll.iterrows():
        for endpoint in endpoints:
            now = time.time()
            temp = read_endpoint(endpoint)
            temp_time = [now-freq_node_read*times for times in range(0,len(temp))]
            #temp_data[endpoint]={'values':temp,'time':[now-freq_node_read*times for times in range(0,len(temp))]}
            #print(temp)
            if not path.exists(polled):
                with open(polled, 'w') as p:
                    p.write('timestamp,ip,EUI,endpoint,value\n')
            with open(polled, "a") as p:
                for i in range(len(temp)):
                    p.write(str(temp_time[i])+','+row.ip+','+str(row.EUI)+','+endpoint+','+str(temp[i])+'\n')
    time.sleep(max(0,frequency_s-(time.time()-start_time)))
