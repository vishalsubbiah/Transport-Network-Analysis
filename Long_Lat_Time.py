import pandas as pd
import csv
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt


def filenames(mypath):
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    return onlyfiles

def timestamp():
    for i in range(1,8):
    #i=1
        mypath='G:/dream/Programming/Projects/On Git/Transport Network Analysis/Data/Day'+str(i)+'/Buses/'
        files=filenames(mypath)
        for bus_id in files:
            try:
    #bus_id='45224220493.csv'
                df=pd.read_csv(mypath+bus_id)
                longitude=df['longitude']
                latitude=df['latitude']
                seconds=df['seconds']
                for i in range(0,len(longitude)):
                    if(longitude[i]==0.0):
                        del longitude[i]
                        del latitude[i]
                        del seconds[i]
                        
                for i in range(0,len(latitude)):
                    if(latitude[i]==0.0):
                        del longitude[i]
                        del latitude[i]
                        del seconds[i]

                time_start=seconds[1]
                for i in range(1,len(longitude)-1):
                    if(longitude[i]==longitude[i+1] and latitude[i]==latitude[i+1]):
                        time_stop=seconds[i+1]
                    else:
                        time_stop=seconds[i]
                        if(time_stop-time_start>=15 and time_stop-time_start<=1000):
                            if(time_stop-time_start<=40):
                                print "Bus Stop"
                                #add to file with headers
                            if(time_stop-time_start>=60):
                                print 'signal'
                                #add to file with headers
                            time_stamp_path=mypath+'timestamps/timestamp_'+bus_id
                            f=open(time_stamp_path,'a')
                            f.writelines(str(latitude[i-1])+','+str(longitude[i-1])+','+str(time_start)+','+str(time_stop)+','+str(time_stop-time_start)+'\n')
                            f.close()                
                        time_start=seconds[i]
            except KeyError:
                pass
    print "timestamp done!"    
'''
    plt.figure(1)
    
    plt.subplot(511)
    plt.title('longitude Vs seconds')
    plt.xlabel('seconds')
    plt.ylabel('longitude')
    plt.plot(seconds,longitude)
    
    plt.subplot(513)
    plt.title('latitude Vs seconds')
    plt.xlabel('seconds')
    plt.ylabel('latitude')
    plt.plot(seconds,latitude)
    
    plt.subplot(515)
    plt.title('longitude Vs latitude')
    plt.xlabel('latitude')
    plt.ylabel('longitude')
    plt.plot(latitude,longitude)
    
    plt.show()
'''           
timestamp()


