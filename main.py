import pyperclip
import PySimpleGUI as sg

layout = [[sg.Text("Clipboard Manager")], [sg.InputText(pyperclip.paste())], [sg.Button("OK")]]

window = sg.Window("Diflux", return_keyboard_events=True, use_default_focus=True).Layout(layout)

while True:
    event, values = window.read()
    print(event)
    if event == "OK" or event == sg.WIN_CLOSED or event == "Escape:9":
        break

window.close()
