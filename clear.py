from importlib.metadata import files
import os
import glob
from natsort import natsorted
from sys import path
path_gt = 'GT_lung_bin-20220411T205845Z-001/g/*'
path_dataset = 'images-20220411T210040Z-001/images'
files_gt = natsorted(glob.glob(path_gt))
for pasta in files_gt:
    arquivos = natsorted(glob.glob(pasta + '/*'))
    nome_pasta = pasta.split('/')[-1]
    arquivos_dataset = natsorted(glob.glob( os.path.join(path_dataset, nome_pasta,'*') ))

    lista_dataset = [elemento.split('/')[-1] for elemento in arquivos_dataset]
    list_del = [os.remove(arquivo) for arquivo in arquivos if arquivo.split('/')[-1] not in lista_dataset] 
    