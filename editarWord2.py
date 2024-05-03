import os
from docx import Document

def reemplazar_palabra_en_word(docx_path, palabra_buscar, palabra_reemplazar):
    resultado = "documentoModificado.docx"
    contador = 100
    while os.path.exists(resultado):
        resultado = f"documentoModificado_{contador}.docx"
        contador += 1

    doc = Document(docx_path)

    for para in doc.paragraphs:
        if palabra_buscar in para.text:
            para.text = para.text.replace(palabra_buscar, palabra_reemplazar)

    doc.save(resultado)
    return resultado

# Ejemplo de uso
docx_path = "archivoPrueba2.docx"  # Ruta del archivo Word original
palabra_buscar = "Date"
palabra_reemplazar = "23/09/05"
resultado = reemplazar_palabra_en_word(docx_path, palabra_buscar, palabra_reemplazar)
print(f"El archivo modificado se ha guardado como {resultado}")