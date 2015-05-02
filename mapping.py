import pandas as pd
import csv
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt


def filenames(mypath):
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    return onlyfiles
def plot_all():
    for i in range(1,8):
        #can modify to get a single day or as many days as required
        mypath='Data/Day'+str(i)+'/Buses/'
        files=filenames(mypath)
        for bus_id in files:
            #can modify to specific buses
        
            df=pd.read_csv(mypath+bus_id)
            longitude=df['longitude']
            for i in range(0,len(longitude)):
                if(longitude[i]==0.0):
                    del longitude[i]
            
            latitude=df['latitude']
            for i in range(0,len(latitude)):
                if(latitude[i]==0.0):
                    del latitude[i]
                    
            plt.plot(longitude,latitude)
    plt.title('Mapping based on all the buses for one week')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.show()
    
        

plot_all()            
