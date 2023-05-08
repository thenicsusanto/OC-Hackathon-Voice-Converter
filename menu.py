import PySimpleGUI as psg
def select_language():
    menu_def = [['Select Language', [
    'ES - Spanish',
    'FR - French',
    'ID - Indonesian',
    'JA - Japanese',
    'KO - Korean',
    'RU - Russian',
    'ZH - Chinese (simplified)', ]]]
    layout = [[psg.Menu(menu_def)],
    [psg.Multiline("", key='-IN-',
    expand_x=True, expand_y=True)],
    [psg.Text("", key='-TXT-',
    expand_x=True, font=("Arial Bold", 14))]
    ]
    window = psg.Window("Menu", layout, size=(715, 300))
    while True:
        event, values = window.read()
        print(event, values)
        if event != psg.WIN_CLOSED:
            window['-TXT-'].update("Current Language:" + values[0])
            if values[0] == "PT-BR - Portuguese (Brazilian)":
                return "PT-BR"
            return values[0][:2]
        if event == psg.WIN_CLOSED:
            return values[0]
