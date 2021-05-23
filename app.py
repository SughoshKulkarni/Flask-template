from flask import Flask, make_response, request, send_file, render_template, url_for
from functions.sample_function import *
import os

# Naming the flask application
app = Flask(__name__)


# You can setup routes with this decorator
@app.route('/') # This will be the root link of the web-app. Ex: 127.0.0.0.1:5000/
def index():
    return render_template('home.html') # Returns home page html


@app.route('/another_page', methods=["POST","GET"])
def another():
    text = 'Some text'
    return render_template('another.html', text = text)

@app.route('/output',methods=["POST","GET"])
def dir_listing():
    BASE_DIR = 'static/downloads/'

    # Joining the base and the requested path
    abs_path = os.path.join(os.path.dirname(app.instance_path),BASE_DIR)
    print(abs_path)
    print(type(abs_path))
    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template('downloads.html', files=sorted(files,reverse=True),path=abs_path)


# Create your own route and add a extension like below. Use the below format to add your function
@app.route('/sample_function', methods=["POST","GET"])
def sample_function():
    # You can name your function
    # Below is the syntax to request for the excel file (or any file) for processing
    request_file = request.files['data_file']
    print('This is the file name {}'.format(request_file))
    # Checks if the file is available in the form. If does not exists, it returns "No file"
    if not request_file:
        return "No file"
    # The output of the function is stored in this variable
    result = sample(request_file)
    
    # This return calls the dir_listing() function which leads to the output page with the file link to download
    return dir_listing()

if __name__ == '__main__':
    app.run(debug=True) # debug=True helps in visualizing any errors that come up when running the app.