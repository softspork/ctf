# var
debug_menu = 0
html_tag = 'h3'
key = 'hash'

import requests, sys, hashlib, time

def blue(text):
    return "\033[94m" + text +  "\033[0m"
def green(text):
    return "\033[92m" + text +  "\033[0m"
def red(text):
    return "\033[91m" + text +  "\033[0m"

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit('\nYou need ' + blue('beautifulsoup4') + ' and ' + blue('lxml') + '\n' + 
                green(' run ') + 'python3 -m pip install beautifulsoup4 lxml\n')

def error():
    script = sys.argv[0]
    print('\n<Usage>\npython3 ' + script +' http://' + blue('<ip>') + ':' + blue('<port>') + '\n')
    sys.exit()

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
    start = time.time()
    receive = s.get(rhost)
    end = time.time()

    status = str(receive.status_code)

    if status == "200":
        status = green(status)
        print('.get \ ' + status)
        print('time \ ' + str(end-start)[0:6] + ' sec')
    else:
        status = red(status)
        print('.GET \ ' + status)
        sys.exit()

    print('\n' +  receive.text)

    # find html_tag
    soup = BeautifulSoup(receive.text, 'lxml')
    for elements in soup.find_all([html_tag]):
            found = elements.text.strip()
            print('find \ ' + html_tag + ' ' + green(found))

    # hash it with md5
    emdee5 = hashlib.md5(found.encode('utf-8')).hexdigest()
    print('\n.md5 \ ' + html_tag + " " + blue(emdee5))

    # playload
    payload = {
        key: emdee5,
    }

    # post request
    start2 = time.time()
    send= s.post(rhost, payload)
    end2 = time.time()

    print('\nPOST \ ' + send.request.url)
    print('POST \ ' + send.request.body )
    print('time \ ' + str(end2-start2)[0:6] + ' sec' + '\n')

    for header, value in send.request.headers.items():
        print('head \ ' + header + ': ' + value)

    print('\n' + send.text.strip('\n'))

    # print flag
    soup2 = BeautifulSoup(send.text , 'lxml')
    
    for flags in soup2.find_all(['p']):
        if len(flags.text.strip()) < 20:
            print('\nflag \ ' + red(flags))
        elif len(flags.text.strip()) > 20:
            print('\nflag \ ' + green(flags.text.strip()))
    
    print('took \ ' + str((end-start)+(end2-start2))[0:6] + ' sec')

else:
    error()