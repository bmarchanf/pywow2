from PyPDF2 import PdfWriter, PdfReader

def unir_pdf(archivo1, archivo2):

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
        with open('resultado.pdf', 'wb') as result_file:
            pdf_writer.write(result_file)

# Ejemplo de uso
archivo1 = "apuntes clase.pdf"
archivo2 = "espectro electromagnetico.pdf"
unir_pdf(archivo1, archivo2)