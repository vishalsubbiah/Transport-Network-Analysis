import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle

def getCentroid(points):
    n=points.shape[0]
    sum_lon=np.sum(points[:,1])
    sum_lat=np.sum(points[:,0])
    return (sum_lon/n,sum_lat/n)

def getNearestPoint(set_of_points, point_of_reference):
    closest_point = None
    closest_dist = None
    for point in set_of_points:
        point = (point[1], point[0])
        dist = great_circle(point_of_reference, point).meters
        if (closest_dist is None) or (dist < closest_dist):
            closest_point = point
            closest_dist = dist
    return closest_point
counta=[]
countb=[]
for i in range(7,8):
    #can modify for specific No. of days
    mypath_Terminals='Data/Day'+str(i)+'/Buses/timestamps/BusStops/Terminals.csv'    
    df_terminals=pd.read_csv(mypath_Terminals)
    coordinates_terminals=df_terminals.as_matrix(columns=['latitude','longitude'])

    db=DBSCAN(eps=0.010,min_samples=1).fit(coordinates_terminals)
    labels=db.labels_
    num_clusters=len(set(labels))-(1 if -1 in labels else 0)
    clusters = pd.Series([coordinates_terminals[labels==k] for k in xrange(num_clusters)])
    print('Number of clusters: '+str(num_clusters))
    print 'No of Depots in Chennai are 25 to 27 (Source:Times of India and Wikipedia)'

    longitude_terminals=[]
    latitude_terminals=[]
    for j, cluster in clusters.iteritems():
        if(len(cluster)<3):
            representative_point=(cluster[0][1],cluster[0][0])
        else:
            representative_point=getNearestPoint(cluster,getCentroid(cluster))
        longitude_terminals.append(representative_point[0])
        latitude_terminals.append(representative_point[1])
        
    rs_terminals = pd.DataFrame({'longitude':longitude_terminals,'latitude':latitude_terminals})
    #print rs_terminals


    mypath_busStops='Data/Day'+str(i)+'/Buses/timestamps/BusStops/nodes.csv'    
    df_busStops=pd.read_csv(mypath_busStops)
    coordinates_busStops=df_busStops.as_matrix(columns=['latitude','longitude'])

    db=DBSCAN(eps=0.0024,min_samples=3).fit(coordinates_busStops)
    labels=db.labels_
    num_clusters=len(set(labels))-(1 if -1 in labels else 0)
    clusters = pd.Series([coordinates_busStops[labels==k] for k in xrange(num_clusters)])
    print('Number of clusters: '+str(num_clusters))
    print 'No. of Bus Stops'

    longitude_busStops=[]
    latitude_busStops=[]
    for j, cluster in clusters.iteritems():
        if(len(cluster)<3):
            representative_point=(cluster[0][1],cluster[0][0])
        else:
            representative_point=getNearestPoint(cluster,getCentroid(cluster))
        longitude_busStops.append(representative_point[0])
        latitude_busStops.append(representative_point[1])
        
    rs_busStops = pd.DataFrame({'longitude':longitude_busStops,'latitude':latitude_busStops})
    #print rs_busStops


    
    mypath_Signals='Data/Day'+str(i)+'/Buses/timestamps/Signals/nodes.csv'    
    df_signals=pd.read_csv(mypath_Signals)
    coordinates_signals=df_signals.as_matrix(columns=['latitude','longitude'])

    db=DBSCAN(eps=0.0052,min_samples=3).fit(coordinates_signals)
    labels=db.labels_
    num_clusters=len(set(labels))-(1 if -1 in labels else 0)
    clusters = pd.Series([coordinates_signals[labels==k] for k in xrange(num_clusters)])
    print('Number of clusters: '+str(num_clusters))
    print 'No of signals'

    longitude_signals=[]
    latitude_signals=[]
    for i, cluster in clusters.iteritems():
        if(len(cluster)<3):
            representative_point=(cluster[0][1],cluster[0][0])
        else:
            representative_point=getNearestPoint(cluster,getCentroid(cluster))
        longitude_signals.append(representative_point[0])
        latitude_signals.append(representative_point[1])
        
    
    for s in range(0,len(longitude_busStops)-2):
        if(longitude_busStops[s] in longitude_signals and latitude_busStops[s] in latitude_signals):
            del longitude_busStops[s]
            del latitude_busStops[s]
            #print s
            
    rs_terminals = pd.DataFrame({'longitude':longitude_terminals,'latitude':latitude_terminals})
    rs_busStops = pd.DataFrame({'longitude':longitude_busStops,'latitude':latitude_busStops})
    rs_signals = pd.DataFrame({'longitude':longitude_signals,'latitude':latitude_signals})

    #verification with Day1 data
    
    count=0
    for i in range(0,len(longitude_signals)):
        if(longitude_signals[i]>=79.960886 and longitude_signals[i]<=80.462872 and latitude_signals[i]>=12.855486 and latitude_signals[i]<=13.143142):
            count=count+1
    print str(count)+' signals'
    counta.append(count)
    
    count1=0
    for i in range(0,len(longitude_busStops)):
        if(longitude_busStops[i]>=79.960886 and longitude_busStops[i]<=80.462872 and latitude_busStops[i]>=12.855486 and latitude_busStops[i]<=13.143142):
            count1=count1+1
    print str(count1)+'bus stops'
    countb.append(count1)
    #end_verification

    #print rs_signals
    
    #plt.figure()

    rs_scatter_signals=plt.scatter(rs_signals['latitude'],rs_signals['longitude'],c='b',marker='x',s=20,label='signals')
    rs_scatter_busStops=plt.scatter(rs_busStops['latitude'],rs_busStops['longitude'],c='r',marker='o',s=20,label='bus stops')
    rs_scatter_terminals=plt.scatter(rs_terminals['latitude'],rs_terminals['longitude'],c='g',marker='s',s=20,label='terminals')
    #df_scatter=plt.scatter(df_terminals['longitude'],df_terminals['latitude'],c='k')
    plt.title('nodes for a single day')
    plt.ylabel('Longitude')
    plt.xlabel('Latitude')
    plt.legend()
    plt.show()
#print(sum(counta)/7)
#print(sum(countb)/7)
    
    
