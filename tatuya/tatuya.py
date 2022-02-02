#!/usr/bin/env python
# -*- coding: utf-8 -*-

#モジュールのインポート
from flask import Flask,render_template
from flask import request
import jaconv

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


    #藤原竜也への変換
    hiragana = range(0x3041, 0x3096 + 1)  # ひらがなの範囲
    katakana = range(0x30A0, 0x30FA + 1)  # カタカナの範囲

    def isHiragana(c):
        return ord(c) in hiragana

    def isKatakana(c):
        return ord(c) in katakana

    def unvoiced(c):
        if isHiragana(c):              # ひらがなの場合
            hk = jaconv.hira2hkata(c)      # 半角ｶﾀｶﾅに変換
            zk = jaconv.h2z(hk[0])         # 一文字目だけを全角カタカナに戻す
            c = jaconv.kata2hira(zk)       # ひらがなに戻す
        elif isKatakana(c):            # カタカナの場合
            hk = jaconv.z2h(c)             # 半角ｶﾀｶﾅに変換
            c = jaconv.h2z(hk[0])          # 一文字目だけを全角カタカナに戻す
        return c

    def tatsuya(text):

        return ''.join(unvoiced(c) + '゛' for c in text if c not in 'ﾞﾟ゛゜')

    text = tatsuya(content)
    length = len(content)
    return render_template('test.html', result=text, result2=length)

#pythonで実行されたときに処理をする
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)