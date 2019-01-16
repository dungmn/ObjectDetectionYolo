import numpy as np
import cv2
import os, glob

DIR = 'obj_gt'
ddict = {'car':0,'light':1,'moto':2}

sz = (320,480)


def getCoods(lines):
    coods = {}
    coods['c'] = ddict[lines[0]]

    l = int(lines[1])
    t = int(lines[2])
    w = int(lines[3]) - l
    h = int(lines[4]) - t

    coods['x_c'] = (l + w/2)/sz[1]
    coods['y_c'] = (t + h/2)/sz[0]

    coods['w'] = w/sz[1]
    coods['h'] = h/sz[0]

    return coods

gt_paths = glob.glob('./annotation/*.txt')

# with open('files/test.txt','r') as f:
#     gt_paths = f.readlines()

for p in gt_paths:
    data = []
    path = p.strip('\n')
    filename = path.split('/')[-1]
    with open(path,'r') as f:
        for line in f:
            lines = line.split()
            if lines[0] in ddict:
                coods = getCoods(lines[:5])
                s = '{} {} {} {} {}\n'.format(coods['c'],coods['x_c'],coods['y_c'],coods['w'],coods['h'])
                data.append(s)
    with open(os.path.join(DIR,filename),'w') as f:
        f.writelines(data)
