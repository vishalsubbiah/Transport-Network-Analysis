import os
import os.path
import shutil
  

def folder_create():
    directorys=['Data']
    for i in range(1,8):
        directorys.append(directorys[0]+'/Day'+str(i))
        directorys.append(directorys[0]+'/Day'+str(i)+'/Buses')
        directorys.append(directorys[0]+'/Day'+str(i)+'/Buses'+'/timestamps')
        directorys.append(directorys[0]+'/Day'+str(i)+'/Buses'+'/timestamps'+'/BusStops')
        directorys.append(directorys[0]+'/Day'+str(i)+'/Buses'+'/timestamps'+'/Signals')

    for directory in directorys:
        if not os.path.exists(directory):
            os.makedirs(directory)

folder_create()

def move(src,dest):
    shutil.move(src,dest)

def file_transfer():
    for i in range(1,8):
        if(os.path.isfile('data/Day'+str(i)+'/2014-03-0'+str(i)+'.csv')):
            print('File exists')
        else:
            move('2014-03-0'+str(i)+'.csv','Data/Day'+str(i))

file_transfer()
