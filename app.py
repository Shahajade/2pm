#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def bob():
    return render_template("abc.html")
@app.route("/detail",methods=['GET','POST'])
def abc():
    if(request.method=='POST'):      
        a=int(request.form['num1'])
        b=int(request.form['num2'])
        total=a+b
        return render_template("abc.html",mobile=total)   
app.run()


# In[ ]:




