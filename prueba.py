import PySimpleGUI as sg

layout = [
    [sg.Text("¿Cuál es tu nombre?")],
    [sg.InputText()],
    [sg.Button("Aceptar"), sg.Button("Cancelar")]
]

window = sg.Window("Ejemplo de PySimpleGUI", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Cancelar":
        break
    elif event == "Aceptar":
        print(f"Hola, {values[0]}")

window.close()