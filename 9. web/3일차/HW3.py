from flask import Flask, render_template, request
import hw_dbhandle as d
import pandas as pd
# from flask_paginate import Pagination, get_page_args

app = Flask( __name__ ) 

@app.route('/') 
def root():
    return '<h1>hello</h1>'  #response


@app.route('/insertProduct')
def insertProduct():
    return render_template('insertProduct.html')

@app.route('/insertProductProc') 
def insertProductProc():
    name = request.args['name']
    quantity = int(request.args['quantity']) 
    date = request.args['date']
    result=d.insertProductDB(name, quantity, date)
    return render_template('insertProductProc.html', result = result)

if __name__ =='__main__':
    app.run( host='0.0.0.0', port=4000, debug=True) #0.0.0.0-클라이언트에 있는 ip address가 뭐든 상관없이 웹서버가 응답해주겠다 #port번호- 프로세서 식별자, 4000- 내가 4000번 포트로 대기하겠다
    #웹서버 구동...requests 처리
