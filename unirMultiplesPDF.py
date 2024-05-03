import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfWriter, PdfReader
import os

def unir_pdf(archivos):
    resultado = "resultado.pdf"
    contador = 1
    while os.path.exists(resultado):
        resultado = f"resultado_{contador}.pdf"
        contador += 1

    pdf_writer = PdfWriter()

    for archivo in archivos:
        with open(archivo, 'rb') as file:
            pdf_reader = PdfReader(file)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

    with open(resultado, 'wb') as result_file:
        pdf_writer.write(result_file)

    return resultado

def adjuntar_pdf():
    archivos = filedialog.askopenfilenames(title="Seleccionar archivos PDF")

    if archivos:
        resultado = unir_pdf(archivos)
        tk.messagebox.showinfo("Éxito", f"PDFs unidos correctamente y guardados como '{resultado}'")

root = tk.Tk()
root.title("Unir PDFs")

btn_adjuntar = tk.Button(root, text="Adjuntar PDFs", command=adjuntar_pdf)
btn_adjuntar.pack(pady=20)

root.mainloop()


En que orden toma los archivos????