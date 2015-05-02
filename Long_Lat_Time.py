import pandas as pd
import csv
import os
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt

def add_headers(filename):
    fieldnames=['longitude','latitude','Time_Start','Time_Stop','TimeTaken']
    with open(filename,'a') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        
def filenames(mypath):
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    return onlyfiles

def timestamp():
    for i in range(1,8):
        #can modify to get a single day or as many days as required
        mypath='G:/dream/Programming/Projects/On Git/Transport Network Analysis/Data/Day'+str(i)+'/Buses/'
        files=filenames(mypath)
        #files=['40205020800.csv']
        for bus_id in files:
            #can modify to specific buses
            try:
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
    
                time_stamp_path=mypath+'timestamps/BusStops/Terminals_test.csv'
                f=open(time_stamp_path,'a')
                f.close()
                if(os.path.getsize(time_stamp_path)==0):
                    print "Empty File"
                    add_headers(time_stamp_path)

                f=open(time_stamp_path,'a+')
                f.writelines(str(longitude[1])+','+str(latitude[1])+','+str(seconds[1])+','+str(seconds[2])+','+'\n')
                f.writelines(str(longitude[len(longitude)-2])+','+str(latitude[len(latitude)-2])+','+str(seconds[len(latitude)-2])+','+str(seconds[len(latitude)-1])+','+'\n')
                f.close()
                time_start=seconds[1]
                for i in range(1,len(longitude)-1):
                #print i
                    if(longitude[i]==longitude[i+1] and latitude[i]==latitude[i+1]):
                        time_stop=seconds[i+1]
                    else:
                        time_stop=seconds[i]
                        if(time_stop-time_start>=15.0 and time_stop-time_start<=250.0):
                            print 'bus has stopped'
                            if(time_stop-time_start<=30):
                                print "Bus Stop"
                                time_stamp_path=mypath+'timestamps/BusStops/nodes_test.csv'
                                f=open(time_stamp_path,'a')
                                f.close()
                                if(os.path.getsize(time_stamp_path)==0):
                                    print "Empty File"
                                    add_headers(time_stamp_path)
                                f=open(time_stamp_path,'a')   
                                f.writelines(str(longitude[i-1])+','+str(latitude[i-1])+','+str(time_start)+','+str(time_stop)+','+str(time_stop-time_start)+'\n')
                                f.close()
                            #add to file with headers

                            if(time_stop-time_start>30):
                                print 'signal'
                                time_stamp_path=mypath+'timestamps/Signals/nodes_test.csv'
                                f=open(time_stamp_path,'a')
                                f.close()
                                if(os.path.getsize(time_stamp_path)==0):
                                    print "Empty File"
                                    add_headers(time_stamp_path)
                                f=open(time_stamp_path,'a')   
                                f.writelines(str(longitude[i-1])+','+str(latitude[i-1])+','+str(time_start)+','+str(time_stop)+','+str(time_stop-time_start)+'\n')
                                f.close()
                            #add to file with headers              
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


