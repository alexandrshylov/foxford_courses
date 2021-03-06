from platform import machine
from sys import platform, exit
from time import sleep


def system_platform():
    '''Selects driver depending on platform'''

    if platform.startswith('win'):
        return 'modules/driver/win/chromedriver.exe'
    elif platform.startswith('darwin'):
        return 'modules/driver/darwin/chromedriver'
    elif platform.startswith('linux'):
        if machine().endswith('64'):
            return 'modules/driver/linux/x64/chromedriver'
        else:
            return 'modules/driver/linux/x86/chromedriver'
    else:
        print("Ошибка идентификации системы.")
        sleep(1)
        exit(0)
