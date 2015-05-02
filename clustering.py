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

for i in range(1,2):
    #can modify for specific No. of days
    mypath_Terminals='G:/dream/Programming/Projects/On Git/Transport Network Analysis/Data/Day'+str(i)+'/Buses/timestamps/BusStops/Terminals.csv'    
    df_terminals=pd.read_csv(mypath_Terminals)
    coordinates_terminals=df_terminals.as_matrix(columns=['longitude','latitude'])

    db=DBSCAN(eps=0.01,min_samples=1).fit(coordinates_terminals)
    labels=db.labels_
    num_clusters=len(set(labels))-(1 if -1 in labels else 0)
    clusters = pd.Series([coordinates_terminals[labels==k] for k in xrange(num_clusters)])
    print('Number of clusters: '+str(num_clusters))
    print 'No of Depots in Chennai are 27 to 40 (Source:Times of India and Wikipedia)'

    longitude=[]
    latitude=[]
    for j, cluster in clusters.iteritems():
        if(len(cluster)<3):
            representative_point=(cluster[0][1],cluster[0][0])
        else:
            representative_point=getNearestPoint(cluster,getCentroid(cluster))
        longitude.append(representative_point[0])
        latitude.append(representative_point[1])
        
    rs_terminals = pd.DataFrame({'longitude':longitude,'latitude':latitude})
    print rs_terminals


    mypath_busStops='G:/dream/Programming/Projects/On Git/Transport Network Analysis/Data/Day'+str(i)+'/Buses/timestamps/BusStops/nodes.csv'    
    df_busStops=pd.read_csv(mypath_busStops)
    coordinates_busStops=df_busStops.as_matrix(columns=['longitude','latitude'])

    db=DBSCAN(eps=0.001,min_samples=1).fit(coordinates_busStops)
    labels=db.labels_
    num_clusters=len(set(labels))-(1 if -1 in labels else 0)
    clusters = pd.Series([coordinates_busStops[labels==k] for k in xrange(num_clusters)])
    print('Number of clusters: '+str(num_clusters))
    print 'No. of Bus Stops'

    longitude=[]
    latitude=[]
    for j, cluster in clusters.iteritems():
        if(len(cluster)<3):
            representative_point=(cluster[0][1],cluster[0][0])
        else:
            representative_point=getNearestPoint(cluster,getCentroid(cluster))
        longitude.append(representative_point[0])
        latitude.append(representative_point[1])
        
    rs_busStops = pd.DataFrame({'longitude':longitude,'latitude':latitude})
    print rs_busStops


    
    mypath_Signals='G:/dream/Programming/Projects/On Git/Transport Network Analysis/Data/Day'+str(i)+'/Buses/timestamps/Signals/nodes.csv'    
    df_signals=pd.read_csv(mypath_Signals)
    coordinates_signals=df_signals.as_matrix(columns=['longitude','latitude'])

    db=DBSCAN(eps=0.001,min_samples=1).fit(coordinates_signals)
    labels=db.labels_
    num_clusters=len(set(labels))-(1 if -1 in labels else 0)
    clusters = pd.Series([coordinates_signals[labels==k] for k in xrange(num_clusters)])
    print('Number of clusters: '+str(num_clusters))
    print 'No of signals'

    longitude=[]
    latitude=[]
    for i, cluster in clusters.iteritems():
        if(len(cluster)<3):
            representative_point=(cluster[0][1],cluster[0][0])
        else:
            representative_point=getNearestPoint(cluster,getCentroid(cluster))
        longitude.append(representative_point[0])
        latitude.append(representative_point[1])
        
    rs_signals = pd.DataFrame({'longitude':longitude,'latitude':latitude})
    print rs_signals
    #plt.figure()
    rs_scatter_signals=plt.scatter(rs_signals['longitude'],rs_signals['latitude'],c='b',marker='x',s=20,label='signals')
    rs_scatter_busStops=plt.scatter(rs_busStops['longitude'],rs_busStops['latitude'],c='r',marker='o',s=20,label='bus stops')
    rs_scatter_terminals=plt.scatter(rs_terminals['longitude'],rs_terminals['latitude'],c='g',marker='s',s=20,label='terminals')
    #df_scatter=plt.scatter(df_terminals['longitude'],df_terminals['latitude'],c='k')
    plt.title('nodes for a single day')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.show()
            
    
    
