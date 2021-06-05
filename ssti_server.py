from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route('/')
def landing_page():
    landing_template = f'''<p>Welcome to my website! Check out my about page 
    by adding in '/about' to the url :)</p>'''
    return render_template_string(landing_template)

@app.route('/about')
def about_page():
    about_template = f'''<p>I am a pretty good programmer but this is the 
    only page I have made.</p>'''
    return render_template_string(about_template)

@app.route('/<path:path>')
def undefined_route_vulnerable_page(path):
    undefined_route_template = f''' <p>I am a good programer! I made this nice 
    page incase you made a typo in the URL. '{path}' is not a page I have made,
     maybe you misspelled the URL?</p>'''
    return render_template_string(undefined_route_template)
