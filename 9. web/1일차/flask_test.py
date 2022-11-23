from flask import Flask, render_template, request
import sys

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>hello flask</h1>" # response 할 내용

@app.route("/test")
def test():
    return "<h1>test flask</h1>"

@app.route("/aa")
def aa():
    return render_template('a.html')

@app.route("/div")
def div():
    return render_template('div.html')

@app.route("/img")
def img():
    return render_template('img.html')

@app.route("/anchor")
def anchor():
    return render_template('anchor.html')

@app.route("/ul")
def ul():
    return render_template('ul.html')

@app.route("/table")
def table():
    return render_template('table.html')

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/formproc")
def formproc():
    print(request.args) # get요청의 query string 데이터 추출
    myname = request.args["myname"]
    myage = request.args["myage"]
    return render_template("formproc.html", myname=myname,
                           myage=myage, test='hello')
    # return f"<h1>이름:{myname} 나이:{myage}</h1>"

@app.route("/quiz1")
def quiz1():
    return render_template('quiz1.html')

@app.route("/calcproc")
def calcproc():
    print(request.args) # get요청의 query string 데이터 추출
    num1 = request.args["num1"]
    num2 = request.args["num2"]
    return f"<h1>합은: {int(num1)+int(num2)}</h1>"




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True) # debug=True ; 코드변경 시, 자동 디버그.