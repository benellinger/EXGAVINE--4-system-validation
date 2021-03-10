# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 00:13:57 2020

@author: uranus
"""

import glob
import os
import shutil

# folders = glob.glob('data2\*')
# for folder in folders:
#     condition = folder.split('\\')[1]
#     print(condition)
#     files = os.listdir(folder)
#     for file in files:
#         parts = file.split('_')
#         new_name = parts[0] + '_' + condition + '_' + parts[1] + '_' + parts[2]
#         os.rename(folder + '\\' + file, folder + '\\' + new_name)


# all_files = glob.glob('data2\\*\\*', recursive=True)
# for file in all_files:
#     if 'Kinect' in file:
#         shutil.move(file, 'data\\ki')
#     elif 'Real' in file:
#         shutil.move(file, 'data\\rs')#

files = glob.glob('data/qu/*.tsv')
i = 0
for file in files:
    new_name = list(file)
    new_name[-5] = str(i)
    new_name = "".join(new_name)
    os.rename(file, new_name)
    i += 1
    if i == 5:
        i = 0
    print(new_name)