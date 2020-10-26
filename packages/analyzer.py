#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:33:14 2020

@author: yueshan
"""

import rosbag
import numpy as np
from collections import defaultdict

bag = rosbag.Bag('/data/example_rosbag_H3.bag')

def printresult(dt_list):
    dt=np.array(dt_list)
    print('num message:', len(dt_list)+1)
    print('   period:')
    print('      min:',np.min(dt).secs+np.around(np.min(dt).nsecs/1e9,decimals=2))
    print('      max:',np.max(dt).secs+np.around(np.max(dt).nsecs/1e9,decimals=2))
    print('      average:',np.mean(dt).secs+np.around(np.mean(dt).nsecs/1e9,decimals=2))
    print('      median:',np.median(dt).secs+np.around(np.median(dt).nsecs/1e9,decimals=2))
    pass

#topics=['/tesla/camera_node/camera_info','/tesla/line_detector_node/segment_list','/tesla/wheels_driver_node/wheels_cmd']
info=defaultdict(list)
'''
camera_num=0
line_num=0
wheels_num=0
camera_dt=np.zeros((1,0))
line_dt=np.zeros((1,0))
wheels_dt=np.zeros((1,0))
camera_last=0
line_last=0
wheels_last=0
'''
last_t=defaultdict(int)
for topic, msg, t in bag.read_messages():
    if last_t[topic]!=0:
        info[topic].append(t-last_t[topic])
    last_t[topic]=t
    
'''    
    if topic=='/tesla/camera_node/camera_info':
        camera_num+=1
        if camera_last==0:
            camera_last=t
        else:
            camera_dt=np.append(camera_dt,t-camera_last)
    elif topic=='/tesla/line_detector_node/segment_list':
        line_num+=1
        if line_last==0:
            line_last=t
        else:
            line_dt=np.append(line_dt,t-line_last)
    else:
        wheels_num+=1
        if wheels_last==0:
            wheels_last=t
        else:
            wheels_dt=np.append(wheels_dt,t-wheels_last)
'''   
for topic in info.keys():
    print(topic)
    printresult(info[topic])
    
'''
print(topics[0])
printresult(camera_num,camera_dt)

print(topics[1])
printresult(line_num,line_dt)

print(topics[2])
printresult(wheels_num,wheels_dt)
'''
bag.close()

