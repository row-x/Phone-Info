import os, platform
os.system('git pull')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from pni import pni
    menu()
elif bit == '32bit':
    from pni import pni
    pni()






