from ntpath import join
import os
import glob
import shutil

outpath = 'images'
if not os.path.exists(outpath):
    os.mkdir(outpath)

files = glob.glob('images-20220411T210040Z-001/images/*/*')
print(len(files))
for arquivo in files:
    nome_arquivo = arquivo.split('/')[-1]
    nome_pasta = arquivo.split('/')[-2]
    arquivo_out = os.path.join(outpath,f'{nome_pasta}_{nome_arquivo}')
    shutil.copy2(arquivo,arquivo_out)
