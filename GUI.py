import PySimpleGUI as sg

layout = [[sg.Text("JakeTheAssistant")], [sg.Button("Start")]]

# Create the window
window = sg.Window("JakeTheAssistant", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Start": 
        #to_be_continued#
        
        
    if event == sg.WIN_CLOSED:
        break
window.close()
