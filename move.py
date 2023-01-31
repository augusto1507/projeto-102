import os
import shutil

#origem
from_dir = "C:/Users/jucel/OneDrive/Área de Trabalho/games guto/projeto 102"
#destino
to_dir = "C:/Users/jucel/OneDrive/Área de Trabalho/games guto/projeto 102 2"

lista_arquivos = os.listdir(from_dir)

for file_name in lista_arquivos:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == "":
        continue

    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir +"/"+ file_name
        path2 = to_dir +"/"+ "arquivos de image"
        path3=to_dir+"/"+"arquivos de image"+"/"+file_name

        if os.path.exists(path2):
            print("movendo...")
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("movendo...")
            shutil.move(path1,path3)