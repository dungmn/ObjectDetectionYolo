import sys
import os
import glob
import xml.etree.ElementTree as ET


# change directory to the one with the files to be changed
path_to_folder = './annotation'
#print(path_to_folder)
os.chdir(path_to_folder)

# old files (xml format) will be moved to a "backup" folder
## create the backup dir if it doesn't exist already
if not os.path.exists("backup"):
  os.makedirs("backup")

# create VOC format files
xml_list = glob.glob('*.xml')
if len(xml_list) == 0:
  print("Error: no .xml files found in ground-truth")
  sys.exit()
for tmp_file in xml_list:
  #print(tmp_file)
  # 1. create new file (VOC format)
  print(tmp_file)
  with open(tmp_file.replace(".xml", ".txt"), "a") as new_f:
    root = ET.parse(tmp_file).getroot()
    for obj in root.findall('object'):
      obj_name = obj.find('name').text
      poly = obj.find('polygon')
      point = poly.findall('pt')
      print(point[0].find('x').text)
      left = point[0].find('x').text
      top = point[0].find('y').text
      right = point[2].find('x').text
      bottom = point[2].find('y').text

      new_f.write("%s %s %s %s %s\n" % (obj_name, left, top, right, bottom))
  # 2. move old file (xml format) to backup
  os.rename(tmp_file, "backup/" + tmp_file)
print("Conversion completed!")
