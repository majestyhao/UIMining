# -*- coding: utf-8 -*-
__author__ = 'hao'
import xml.etree.cElementTree as ET
import re
import csv

tree = ET.ElementTree(file='/home/hao/Downloads/apktool/crackme0502/res/layout/activity_main.xml')
app_name = 'crame0502'
root = tree.getroot()

#for child_of_root in root:
    #print child_of_root, child_of_root.attrib

text_pattern = re.compile(r'.*?(text|hint).*?')
csv_file = open('text.csv', 'wb')
#csv_file_writer = csv.writer(csv_file)
csv_file.write(app_name)
for elem in tree.iter():
    flag = False
    for elem_attrib in elem.attrib:
        if re.search(text_pattern, elem_attrib):
            print elem.attrib[elem_attrib]
            csv_file.write(',' + elem.attrib[elem_attrib].encode('utf-8'))
            break
csv_file.write('\n')
csv_file.close()
