from importlib.metadata import files
import os
import glob
from natsort import natsorted
from sys import path
path_gt = 'gt/*'
path_result = 'results_binary/*'
files_result = natsorted(glob.glob(path_gt))
file_list = [arquivo.split('/')[-1] for arquivo in files_result]
files_gt = natsorted(glob.glob(path_result))
for file in files_gt:
    if file.split('/')[-1] in file_list:
        print(file.split('/')[-1])
    

