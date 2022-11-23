from flask import Flask, url_for
from flask import render_template
app = Flask(__name__)


@app.route('/showImg')
def showImg():
    return render_template('showImg.html')

if __name__ == '__main__' :
    app.run(host = '0.0.0.0', port = 80, debug = True)

app.run()
