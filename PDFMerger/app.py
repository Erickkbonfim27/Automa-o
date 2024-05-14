import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("Arquivos")
lista_arquivos.sort()
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"Arquivos/{arquivo}")

merger.write("PDF Final.pdf")