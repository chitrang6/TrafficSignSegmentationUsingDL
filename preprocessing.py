# Author:- Chitrang Talaviya
# This code contains the reading and parsing of the XML files for the bounding boxes generated and created using LabelImg software written in python. The bounding boxes and annotations are done by me 
# on the custom data-set collected by me in San Jose. 

import os 
from bs4 import BeautifulSoup
import pandas as pd



currPath = os.getcwd()
filepath = currPath + '/video3/'

csvfile = currPath + '/video3.csv'


data = []

for filename in os.listdir(filepath):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(filepath, filename)
    xml = ""
    with open(fullname) as f:
    	xml = f.readlines()
    xml = ''.join([line.strip('\t') for line in xml])

    annotation = BeautifulSoup(xml, "lxml")


    objs = annotation.findAll('object')
    
    for obj in objs:
    	obj_names = obj.findChildren('name')
    	for name_tag in obj_names:
    		labelname = str(name_tag.contents[0])
    		fname = annotation.findChild('filename').contents[0]
    		fpath = annotation.findChild('path').contents[0]
    		bbox = obj.findChildren('bndbox')[0]
    		xmin = int(bbox.findChildren('xmin')[0].contents[0])
    		print (xmin)
    		ymin = int(bbox.findChildren('ymin')[0].contents[0])
    		print (ymin)
    		xmax = int(bbox.findChildren('xmax')[0].contents[0])
    		print (xmax)
    		ymax = int(bbox.findChildren('ymax')[0].contents[0])
    		print (ymax)
    		data.append([fpath,fname,labelname, xmin, ymin, xmax, ymax])
df = pd.DataFrame(data, columns=['fpath', 'fname' ,'labelname' , 'xmin', 'ymin', 'xmax', 'ymax'])


df.to_csv(csvfile, index=False)
