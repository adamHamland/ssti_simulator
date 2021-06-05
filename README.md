# SSTI_SIMULATOR

Learn all about a common Python Flask web vulnerability through this interactive simulator.

# Getting Started  

The following isntructions are for setting up on a Debain/Ubuntu based Linux machine. For additional setup help, see the Flask documentation https://flask.palletsprojects.com/en/2.0.x/  

First install python3 and pip3 (Python's module manager) if you do not have them on your machine:  
`sudo apt install python3`  
`sudp apt install python3-pip`

Next install Flask:  
`pip3 install flask`

To start this Flask project, you need to set the FLASK_APP environment variable:  
`export FLASK_APP=ssti_server.py`

Now all thats left is to run the server:  
`flask run`
