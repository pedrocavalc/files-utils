
import os
import glob
import shutil

path_detectron = ''
path_gt = '' 

if os.path.exists('path_gt/') == False:
    os.mkdir('path_gt/')

files_gt = glob.glob(path_gt + '*')
lista_gt = [elemento.split('/')[-1] for elemento in files_gt]

files_detectron = glob.glob(path_detectron + '*')
list_detectron = [elemento.split('/')[-1] for elemento in files_detectron]
list_detectron_split = [elemento.split('_')[0] + '_' + elemento.split('_')[1] + '.png'
                        for elemento in list_detectron]

write = [shutil.copy2(arquivo, '/media/sharkoon/2ABC5B1607B8F25D/Sharkoon_Tools/Detectron2/datasets/lungs/split_automatic/braga')
         for arquivo in files_gt if arquivo.split('/')[-1] not in list_detectron_split]