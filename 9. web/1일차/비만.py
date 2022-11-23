from flask import Flask, url_for
from flask import render_template
app = Flask(__name__)

def bmiproc():

    height = int(request.args['height'])
    weight = int(request.args['weight'])
    stdW = (height - 100) * 0.85
    

    if :
        sss
    else:
        result = "비만"
        sajin = "static\image\비만.jpg"

@app.route('/bmiproc')
def bmiproc():
    #함수설계: SRC, devide by conquer
    height = int(request.args['height'])
    weight = int(request.args['weight'])
    stdW = (height - 100) * 0.85