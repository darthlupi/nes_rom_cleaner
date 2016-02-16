#!/usr/bin/python
from os import listdir,rename
from os.path import isfile, join 

rom_path = "/home/pi/RetroPie/roms/nes/"	
rom_list = []

#Create a list of zip files that should be roms...
for f in listdir(rom_path):
  if isfile(join(rom_path, f) ):
    if '.zip' in f:
     rom_list.append(f) 

#Sort the rom list:)
rom_list.sort()
#List of just the rom name minus meta data and extention.
rom_names = []
#The rom name we will be deriving from some simple splits.
rname = ""
#Loop through the sorted list of files and print the rom's name.
for r in rom_list:
  if '(' in r:
    rname = r.split('(')[0]
  elif '.zip' in r:
    rname =  r.split('.zip')[0]
  #Append to the list of rom names and file names
  rom_names.append([rname,r])

#New dictionary for containing lists of roms based on name.
rom_dict = {}
for r in rom_names:
  #If rom name is in rom_dict append the filename to the end of the list.
  if r[0] not in rom_dict:
    rom_dict[r[0]] = [r[1]]
  else:
    rom_dict[r[0]].append(r[1]) 

#This is the list of files we are keeping :)
keeper_files = []
#Print the rom names and their totals.
for name,files in rom_dict.iteritems():
  #Loop through the files and append only the US or European version if they are available.
  #If those versions are not found then just append everything. 
  if any('(U)' in s for s in files):
    for f in files:
      if '(U)' in f:
        keeper_files.append(f)
        break
  elif any('(E)' in s for s in files):
    for f in files:
      if '(E)' in f:
        keeper_files.append(f)
        break
  else:
    for f in files:
      if 'Pirate' not in f and 'Hack' not in f and '(Alt)' not in f:
        keeper_files.append(f)
        #break

for f in keeper_files:
  rename(rom_path+f,rom_path+'good_roms/'+f) 


print "Total roms: " + str(len(rom_list) ) + " Total roms keeping: " + str(len(keeper_files) )
