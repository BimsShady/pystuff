from vmanage.api.authentication import Authentication
from vmanage.api.central_policy import CentralPolicy
#from vmanage.api.cluster import Cluster
from vmanage.api.device_templates import DeviceTemplates
#from vmanage.api.device import Device
#from vmanage.api.feature_templates import FeatureTemplates
#from vmanage.api.local_policy import LocalPolicy
#from vmanage.api.monitor_network import MonitorNetwork
#from vmanage.api.policy_definitions import PolicyDefinitions
#from vmanage.api.policy_lists import PolicyLists
#from vmanage.api.policy_updates import PolicyUpdates
#from vmanage.api.security_policy import SecurityPolicy
#import meraki
import os
import msvcrt
import getpass
import datetime

#api_security_policy = SecurityPolicy(session, host=host)
#output_object = api_security_policy.get_security_policy()
#for json_object in output_object:
#    for attribute, value in json_object.items():
#        if(attribute == 'policyName' or attribute == 'policyId'):
#            print(value)



session = Authentication
host = ''
output = 'Terminal'
output_path = 'C:/temp/apy_output/'

def out_data(data, *filename):
    if (output == 'Terminal'):
        print(data)
    else:
        f=open(output_path + filename[0] + str(datetime.datetime.now().strftime('_%d%m%y_%H%M%S')) + '.json', 'a')
        f.write(str(data))
        f.close()

def edit_filepath():
    os.system('cls')
    print('Output Filepath (Format: C:/temp/apy_output/')
    new_filepath = input('')
    return new_filepath

def print_fill(rows):
    n = rows
    while n < (os.get_terminal_size().lines - 1):
        print('')
        n += 1

def navigate(nav_item, menu_variable):
    global output
    global output_path
    match (nav_item):
        case '0':
            menu_variable = '0'
            print('vManage / Meraki API Access')
            print('1 vManage')
            print('2 Meraki')
            print('3 Output')
            print_fill(5)
            print('Please enter a number or hit q to quit:')
            input_key(menu_variable)
        case '0.1':
            menu_variable = '0.1'
            global session
            global host
            print_fill(0)
            user = input('Please enter the username: ')
            print_fill(0)
            password = getpass.getpass('Please enter the password: ')
            print_fill(0)
            host = input('Please enter the host: ')
            print_fill(0)
            os.system('cls')
            print ('Authenticating...')
            session = Authentication(host=host, user=user, password=password, validate_certs=False).login()
            os.system('cls')
            print('vManage')
            print('1 Policy')
            print('2 Template')
            print('3 Device')
            print('4 Monitor')
            print_fill(6)
            print('Please enter a number, hit c to go back and hit q to quit:')
            input_key(menu_variable)
        case '0.1.1':
            menu_variable = '0.1.1'
            print('vManage Policy')
            print('1 Central Policy')
            print('2 Local Policy')
            print('3 Security Policy')
            print('4 Policy Definitions')
            print('5 Policy Lists')
            print('6 Policy Updates')
            print_fill(8)
            print('Please enter a number, hit c to go back and hit q to quit:')
            input_key(menu_variable)
        case '0.1.1.1':
            menu_variable = '0.1.1.1'
            print('vManage Central Policy')
            api_central_policy = CentralPolicy(session, host=host)
            print('1 Get Central Policy')
            print_fill(3)
            print('Please enter a number, hit c to go back and hit q to quit:')
            input_key(menu_variable)
        case '0.1.1.1.1':
            menu_variable = '0.1.1.1.1'
            out_data(api_central_policy.get_central_policy(), 'CentralPolicy')
            navigate(menu_variable[:-4], menu_variable)
        case '0.1.2':
            menu_variable = '0.1.2'
            print('vManage Template')
            print('1 Device Templates')
            print('2 Feature Templates')
            print_fill(4)
            print('Please enter a number, hit c to go back and hit q to quit:')
            input_key(menu_variable)
        case '0.1.2.1':
            api_device_templates = DeviceTemplates(session, host=host)
            menu_variable = '0.1.2.1'
            print('vManage Template')
            print('1 Device Templates')
            print('2 Device Template List')
            print('3 Template Attachments')
            print('4 Template Input')
            print('5 Attachments')
            print('6 Device Running Config')
            print_fill(8)
            print('Please enter a number, hit c to go back and hit q to quit:')
            input_key(menu_variable)
        case '0.1.2.1.6':
            menu_variable = '0.1.2.1.6'
            print('Device Running Config')
            out_data(api_device_templates.get_device_running_config(input('Please enter a Device UUID: ')), 'RunningConfig')
            navigate(menu_variable[:-4], menu_variable)
        case '0.1.2.2':
            pass
        case '0.2':
            menu_variable = '0.2'
            print('Meraki')
            print('1 I')
            print('2 don\'t')
            print('3 know')
            print('4 yet')
            print_fill(6)
            print('Please enter a number, hit c to go back and hit q to quit:')
            input_key(menu_variable)
        case '0.3':
            menu_variable = '0.3'
            os.system('cls')

            output_selected = 'Terminal'
            while True:
                print('Output')
                if (output_selected == 'Terminal'):
                    if (output == 'Terminal'):
                        string = '* Terminal'
                    else:
                        string = 'Terminal'
                    print('\x1b[30;102m' + string + '\x1b[0m')
                else:
                    if (output == 'Terminal'):
                        print('* Terminal')
                    else:
                        print('Terminal')
                if (output_selected == 'Filepath'):
                    if(output == 'Filepath'):
                        string = '* Filepath: ' + output_path
                    else:
                        string = 'Filepath: ' + output_path
                    print('\x1b[30;102m' + string + '\x1b[0m')
                else:
                    if (output == 'Filepath'):
                        print('* Filepath: ' + output_path)
                    else:
                        print('Filepath: ' + output_path)
                print_fill(4)
                print("Press 'a' to select the active Entry, 'Enter' to edit, 'c' to go back and 'q' to exit.")
                match ord(msvcrt.getch()):
                    case 13:#enter
                        if (output_selected == 'Filepath'):
                            output_path = edit_filepath()
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
                    case 97:#a
                        output = output_selected
                        os.system('cls')
                    case 99:#c
                        break
                        os.system('cls')
                    case _:
                        pass
            input_key(menu_variable)
        case _:
            print('Invalid Menu!')
            navigate('0', '0')
    return menu_variable
            
def input_key(menu_variable):
    match (msvcrt.getch().decode('ASCII').upper()):
        case 'Q':
            exit()
        case 'C':
            navigate(menu_variable[:-2], menu_variable)
        case '1':
            navigate(menu_variable + '.1', menu_variable)
        case '2':
            navigate(menu_variable + '.2', menu_variable)
        case '3':
            navigate(menu_variable + '.3', menu_variable)
        case '4':
            navigate(menu_variable + '.4', menu_variable)
        case '5':
            navigate(menu_variable + '.5', menu_variable)
        case '6':
            navigate(menu_variable + '.6', menu_variable)
        case _:
            print('Invalid input!')
    return menu_variable

navigate('0', '0')