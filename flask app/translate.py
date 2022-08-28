
import hashlib
password = 'pa$$w0rd'
h = hashlib.md5(password.encode())
print(h.hexdigest())
from logging import debug
from pydoc import render_doc
from flask import Flask , render_template, request
from textblob import TextBlob
app=Flask(__name__)
@app.route('/')
def welcome():
    return render_template('transl.html')


@app.route('/translate',methods=['post'])
def translate():
    
    lang1= request.form.get('from_language')
    data1= str(request.form.get('write'))
    lang2= request.form.get('to_language')
    data = TextBlob(data1)
    trans=data.translate(from_lang=lang1,to=lang2)
    num_ch=len(data1)
    num_word=len(data.words)
    return render_template('transl.html',translation_text=f" {data1} : {trans} ")



app.run(debug=True)  




