#!/usr/bin/env python
# -*- coding: utf-8 -*-

#flaskモジュールのインポート
from flask import Flask,render_template
from flask import request


#flaskオブジェクトの作成
app = Flask(__name__)

#htmlファイルの値を受け取る
@app.route('/', methods=['GET'])
def get():
    return render_template('form.html')

#postのときの処理	
@app.route('/', methods=['POST'])
def post():
    content = request.form['content']
    
    #特定の条件下だけ別の画面を出す
    if content == 'パンが食べたい。':
        return render_template('special.html')
    
    else:
        return render_template('request.html')

#pythonで実行されたときに処理をする
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)