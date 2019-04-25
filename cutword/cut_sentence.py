import jieba
from flask import Flask,render_template,request,session,redirect,url_for,g
import os
import json

'''
#A.添加连词 e.g: '区块', '链' -> '区块链'
#维护 userdict.txt 参考：1.https://www.cnblogs.com/adienhsuan/p/5674033.html 2./usr/local/lib/python3.5/dist-packages/jieba/dict.txt
jieba.load_userdict('userdict_cut.txt')
#B.分词 e.g: '喝咖啡' -> '喝', '咖啡'
needCut='userdict_join.txt'
fn=open(needCut,"r")
for line in fn.readlines():
  c = line.replace('\n','').split(' ')
  jieba.suggest_freq((c[0], c[1]), True) #并加每个词词频
  jieba.add_word(c[0], freq = 20000, tag = None)
  jieba.add_word(c[1], freq = 20000, tag = None)
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

#http://127.0.0.1:5000/cut_sentence/
@app.route('/cut_sentence/',methods=['GET','POST'])
def question():
  #A.添加连词 e.g: '区块', '链' -> '区块链'
  #维护 userdict.txt 参考：1.https://www.cnblogs.com/adienhsuan/p/5674033.html 2./usr/local/lib/python3.5/dist-packages/jieba/dict.txt
  jieba.load_userdict('userdict_join.txt')
  #B.分词 e.g: '喝咖啡' -> '喝', '咖啡'
  needCut='userdict_cut.txt'
  fn=open(needCut,"r")
  for line in fn.readlines():
    c = line.replace('\n','').split(' ')
    jieba.suggest_freq((c[0], c[1]), True) #并加每个词词频
    jieba.add_word(c[0], freq = 20000, tag = None)
    jieba.add_word(c[1], freq = 20000, tag = None)
  if request.method == 'GET':	
    return render_template('cut_sentence.html')
  elif request.method == 'POST':
    question = request.form.get('question')
    print(question)
    return json.dumps({'sentence':question,'cut_sentence':[word for word in jieba.cut(question)]},ensure_ascii=False)

if __name__ == '__main__':
  app.run(host="0.0.0.0",port=5001)

#print([word for word in jieba.cut("我可以吃水果么?")])
