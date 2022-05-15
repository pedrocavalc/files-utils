
import os
import glob
import shutil

path_detectron = '20000iter/results_binary/'
path_gt = 'gt/'

if not os.path.exists('20000iter/gt_train'):
    os.mkdir('20000iter/gt_train')

files_gt = glob.glob(path_gt + '*')
lista_gt = [elemento.split('/')[-1] for elemento in files_gt]

files_detectron = glob.glob(path_detectron + '*')
list_detectron = [elemento.split('/')[-1] for elemento in files_detectron]
list_detectron_split = [elemento.split('_')[0] + '_' + elemento.split('_')[1] + '.png'
                        for elemento in list_detectron]

write = [shutil.copy2(arquivo, '20000iter/gt_train')
         for arquivo in files_gt if arquivo.split('/')[-1] in list_detectron_split]