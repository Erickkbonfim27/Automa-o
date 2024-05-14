import os
from tkinter.filedialog import askdirectory

path = askdirectory(title='Selecione uma pasta')

lista_arquivos = os.listdir(path)

locals = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx, .xls, .csv"],
    "pdfs": [".pdf, .txt"],
    "videos": [".mp4, .mp3, .mov"]
}
for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{path}/{arquivo}")
    for pasta in locals:
        if extensao in locals[pasta]:
            if not os.path.exists(f"{path}/{pasta}"):
                os.mkdir(f"{path}/{pasta}")
            os.rename(f"{path}/{arquivo}", f"{path}/{pasta}/{arquivo}")
