from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import yaml

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

app = Flask(__name__, static_url_path='/static')

with open('info.yaml') as yaml_file:
    my_yaml = yaml.load(yaml_file)

@app.route('/cv')
def curriculum():
    template = env.get_template('index.html')
    image_file = url_for('static', filename=my_yaml['fotografia'])
    my_style = url_for('static', filename='bootstrap.css')
    return template.render(my_data=my_yaml, image_file=image_file, my_style=my_style)

@app.route('/')
def index():
    template = env.get_template('home.html')
    image_file = url_for('static', filename=my_yaml['fotografia'])
    my_style = url_for('static', filename='bootstrap.css')
    return template.render(my_data=my_yaml, image_file=image_file, my_style=my_style)

if __name__ == '__main__':
    app.run(debug=True)
    TEMPLATES_AUTO_RELOAD = True