import pandas as pd
import csv
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
#http://gis.stackexchange.com/questions/8650/how-to-measure-the-accuracy-of-latitude-and-longitude
# from the above link, we see that 5th decimal gives change of about a meter.
def plot_all():

    for i in range(1,2):
        mypath_Terminals='G:/dream/Programming/Projects/On Git/Transport Network Analysis/Data/Day'+str(i)+'/Buses/timestamps/BusStops/Terminals_test.csv'    
        df_Terminals=pd.read_csv(mypath_Terminals)
        longitude_Terminals=df_Terminals['longitude']
        latitude_Terminals=df_Terminals['latitude']
        for i in range(0,len(longitude_Terminals)):
            longitude_Terminals[i]=round(longitude_Terminals[i],4)
            latitude_Terminals[i]=round(latitude_Terminals[i],4)
        
        plt.figure(1)        
        plt.scatter(latitude_Terminals,longitude_Terminals)
        
    plt.title('Terminals based on all the buses for one week')
    plt.xlabel('latitude')
    plt.ylabel('longitude')
    plt.show()
    
    for i in range(1,2):
        mypath_BusStops='G:/dream/Programming/Projects/On Git/Transport Network Analysis/Data/Day'+str(i)+'/Buses/timestamps/BusStops/nodes_test.csv'
        df_BusStops=pd.read_csv(mypath_BusStops)
        longitude_BusStops=df_BusStops['longitude']
        latitude_BusStops=df_BusStops['latitude']
        for i in range(0,len(longitude_Terminals)):
            longitude_BusStops[i]=round(longitude_BusStops[i],4)
            latitude_BusStops[i]=round(latitude_BusStops[i],4)
        
        plt.figure(2)        
        plt.scatter(latitude_BusStops,longitude_BusStops)

    plt.title('Bus Stops based on all the buses for one week')
    plt.xlabel('latitude')
    plt.ylabel('longitude')
    plt.show()
    
    for i in range(1,2):
        mypath_Signals='G:/dream/Programming/Projects/On Git/Transport Network Analysis/Data/Day'+str(i)+'/Buses/timestamps/Signals/nodes_test.csv'
        df_Signals=pd.read_csv(mypath_Signals)
        longitude_Signals=df_Signals['longitude']
        latitude_Signals=df_Signals['latitude']
        for i in range(0,len(longitude_Terminals)):
            longitude_Signals[i]=round(longitude_Signals[i],4)
            latitude_Signals[i]=round(latitude_Signals[i],4)
        plt.figure(3)        
        plt.scatter(latitude_Signals,longitude_Signals)

    plt.title('Signals based on all the buses for one week')
    plt.xlabel('latitude')
    plt.ylabel('longitude')
    plt.show()
    
    
        
plot_all()
