from flask import Flask, render_template, request
import productdbhandlePool as p
import pandas as pd
# from flask_paginate import Pagination, get_page_args

app = Flask( __name__ ) 

@app.route('/') 
def root():
    return render_template("main.html")  #response

@app.route('/main') 
def root():
    return render_template("main.html")
    

@app.route('/insertProduct')
def insertProduct():
    return render_template('insertProduct.html')

@app.route('/insertProductProc') 
def insertProductProc():
    name = request.args['name']
    quantity = int(request.args['quantity']) 
    date = request.args['date']
    result=p.insert_product_pool(name, quantity, date)
    return render_template('insertProductProc.html', result = result)

@app.route('/productView') 
def productView():
    data = p.select_all_product_pool()
    return render_template('productView.html', data = data)

@app.route('/searchProduct') 
def searchProduct():
    return render_template('searchProduct.html')

@app.route('/searchProc') 
def searchProc():
    name = request.args['name']
    result=p.select_product_pool(name)
    print(len(result))
    return render_template('searchProc.html', result = result)

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/updateProc')
def updateProc():
    name = request.args.get('name')
    new_name = request.args.get('new_name')
    new_quantity = request.args.get('new_quantity')
    new_date = request.args.get('new_date')
    result = p.update_product_pool(name, new_name, new_quantity, new_date)
    return render_template("updateProc.html", result=result)


if __name__ =='__main__':
    app.run( host='0.0.0.0', port=4000, debug=True) #0.0.0.0-클라이언트에 있는 ip address가 뭐든 상관없이 웹서버가 응답해주겠다 #port번호- 프로세서 식별자, 4000- 내가 4000번 포트로 대기하겠다
    #웹서버 구동...requests 처리
