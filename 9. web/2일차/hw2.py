from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/pizzaTest')
def pizzaTest():
    return render_template('pizzaTest.html')
    
@app.route('/pizzaProc')
def pizzaProc():
    cusname = request.args['cusname']
    mobile = request.args['mobile']
    email = request.args['email']
    size = request.args['size']
    topping = request.args.getlist('topping')
    topping = ','.join(topping)
    time = request.args['time']
    needs = request.args['needs']
    return render_template('pizzaProc.html', cusname=cusname, mobile=mobile, email=email, size=size, topping=topping, time=time, needs=needs)

if __name__ == '__main__':
    app.run( host = '0.0.0.0', port=4000, debug=True)