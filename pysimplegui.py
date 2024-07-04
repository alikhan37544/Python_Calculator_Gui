import PySimpleGUI as sg

# Function to perform calculations
def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error"

# Define the layout for the calculator
layout = [
    [sg.Input(size=(20, 1), key='-INPUT-', justification='right')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
    [sg.Button('0'), sg.Button('.'), sg.Button('='), sg.Button('+')],
    [sg.Button('Clear'), sg.Button('Exit')]
]

# Create the window
window = sg.Window('Calculator', layout)

# Event loop
current_expression = ''
while True:
    event, values = window.read()
    
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Clear':
        current_expression = ''
        window['-INPUT-'].update(current_expression)
    
    elif event == '=':
        current_expression = calculate(current_expression)
        window['-INPUT-'].update(current_expression)
    
    else:
        current_expression += event
        window['-INPUT-'].update(current_expression)

window.close()
~