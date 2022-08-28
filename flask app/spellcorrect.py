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
    return render_template('spellcorrect.html')


@app.route('/correct',methods=['post'])
def translate():
    
    
    data1= str(request.form.get('write'))
    
    data = TextBlob(data1)
    corr=data.correct()
    num_ch=len(data1)
    num_word=len(data.words)
    return render_template('spellcorrect.html',correct_text=f" {data1} :-  {corr} ")



app.run(debug=True)  