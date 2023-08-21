import PySimpleGUI as sg
import os

path = os.getcwd()
os.chdir(path+'\Resources')
#'A: prima optiune', 'B: a doua optiune', 'C: a treia optiune'
file_list_column = [
    [sg.Listbox(values=[], enable_events=True,
                size=(40, 20), key="-FILE LIST-")],
]

image_viewer_column = [
    [sg.Text("Choose instrument:")],
    [sg.DD(["Chitara", "Pian"], default_value='Chitara', key='-CI-')],
    [sg.Text("Choose a song:")],
    [sg.Multiline(size=(50, 4), key="-TEXT-", justification='c')],
##   [sg.Text('Press/hold Q to quit the program', key='-TEXT2-')],
    [sg.Button('Open', key='-RUN-')],
]

layout = [
    [sg.Column(file_list_column, element_justification='c'),
     sg.VSeparator(),
     sg.Column(image_viewer_column, element_justification='c'), ]
]

folLocPian = r'C:\Users\prefe\PycharmProjects\pythonProject\Resources\pian'
folLocChitara = r'C:\Users\prefe\PycharmProjects\pythonProject\Resources\chitara'

Pianfiles = os.listdir(folLocPian)
Chitarafiles = os.listdir(folLocChitara)

Pianfiles = [
    Pianfile for Pianfile in Pianfiles
    if os.path.isfile(os.path.join(folLocPian, Pianfile))
    and Pianfile.lower().endswith(".pdf")
]

Chitarafiles = [
    Chitarafile for Chitarafile in Chitarafiles
    if os.path.isfile(os.path.join(folLocChitara, Chitarafile))
    and Chitarafile.lower().endswith(".pdf")
]

def callback(var, index, mode):
    window.write_event_value("Instrument", window['-CI-'].TKStringVar.get())

window = sg.Window("MusicPlayerDemo", layout, size=(625, 250), finalize=True)
window['-CI-'].TKStringVar.trace("w", callback)

#songsChitara = ("Ac: prima optiune","Bc: a doua optiune","Cc: a treia optiune")
#songsPian = ("Ap: prima optiune","Bp: a doua optiune","Cp: a treia optiune")

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-FILE LIST-":
        try:
            if (values["-FILE LIST-"][0] == 'A: prima optiune'):
                filename = 'descriere prima optiune'
            if (values["-FILE LIST-"][0] == 'B: a doua optiune'):
                filename = 'descriere a doua optiune'
            if (values["-FILE LIST-"][0] == 'C: a treia optiune'):
                filename = 'descriere a treia optiune'
            window['-TEXT-'].update(filename)
##            window['-TEXT2-'].update(filename=filename)
        except:
            pass
    elif event == '-RUN-':
        if (values["-FILE LIST-"][0] == 'Ac: prima optiune'):
                os.startfile('testPhoto.png')
        print("manualUpdate")
    elif event == 'Instrument':
        if values['-CI-'] == 'Chitara':
            window['-FILE LIST-'].update(Chitarafiles)
            print("autoUpdate")
        elif values['-CI-'] == "Pian":
            window['-FILE LIST-'].update(Pianfiles)

window.close()
