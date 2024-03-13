import msvcrt
import os

output = 'Terminal'
output_selected = 'Terminal'
filepath = ''

def edit_filepath():
    os.system('cls')
    print('Output Filepath (Format: C:/temp/output/)')
    x = input('')
    return x

while True:
    os.system('cls')
    print('Output')
    if (output_selected == 'Terminal'):
        if(output == 'Terminal'):
            string = '* Terminal'
        else:
            string = 'Terminal'
        print('\x1b[30;102m' + string + '\x1b[0m')
    else:
        if (output =='Terminal'):
            print('* Terminal')
        else:
            print('Terminal')
    if (output_selected == 'Filepath'):
        if(output == 'Filepath'):
            string = '* Filepath: ' + filepath
        else:
            string = 'Filepath: ' + filepath
        print('\x1b[30;102m' + string + '\x1b[0m')
    else:
        if (output == 'Filepath'):
            print('* Filepath: ' + filepath)
        else:
            print('Filepath: ' + filepath)
    print("Press 'a' to select the active Entry, 'Enter' to edit, 'c' to go back and 'q' to exit.")
    match ord(msvcrt.getch()):
        case 13:#enter
            if (output_selected == 'Filepath'):
                filepath = edit_filepath()
            os.system('cls')
        case 72:#up
            if(output_selected == 'Terminal'):
                pass
            else:
                output_selected = 'Terminal'
            os.system('cls')
        case 80:#down
            if(output_selected == 'Filepath'):
                pass
            else:
                output_selected = 'Filepath'
            os.system('cls')
        #a 97
        case 97:#a
            output = output_selected
        case _:
            pass