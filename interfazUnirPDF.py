import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfWriter, PdfReader
import os

def unir_pdf(archivo1, archivo2):
    # Generar nombre de archivo para el resultado
    resultado = "resultado.pdf"
    contador = 1
    while os.path.exists(resultado):
        resultado = f"resultado_{contador}.pdf"
        contador += 1

    # Abrir los archivos PDF
    with open(archivo1, 'rb') as file1, open(archivo2, 'rb') as file2:
        # Leer los archivos PDF
        pdf_reader1 = PdfReader(file1)
        pdf_reader2 = PdfReader(file2)

        # Crear el escritor de PDF
        pdf_writer = PdfWriter()

        # Adjuntar páginas del primer PDF
        for page in pdf_reader1.pages:
            pdf_writer.add_page(page)

        # Adjuntar páginas del segundo PDF
        for page in pdf_reader2.pages:
            pdf_writer.add_page(page)

        # Guardar el resultado en un nuevo archivo
        with open(resultado, 'wb') as result_file:
            pdf_writer.write(result_file)

        return resultado

def adjuntar_pdf():
    archivo1 = filedialog.askopenfilename(title="Seleccionar primer archivo PDF")
    archivo2 = filedialog.askopenfilename(title="Seleccionar segundo archivo PDF")

    if archivo1 and archivo2:
        resultado = unir_pdf(archivo1, archivo2)
        tk.messagebox.showinfo("Éxito", f"PDFs unidos correctamente y guardados como '{resultado}'")

# Crear la ventana principal
root = tk.Tk()
root.title("Unir PDFs")

# Botón para adjuntar PDFs
btn_adjuntar = tk.Button(root, text="Adjuntar PDFs", command=adjuntar_pdf)
btn_adjuntar.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()