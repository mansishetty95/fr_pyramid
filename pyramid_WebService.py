# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:08:35 2020

@author: mansi
"""

from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def form():
    return render_template('template.html')

@app.route('/', methods=['POST'])
def pyramid():
    s = request.form['text']
    d = {}
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
            
    sorted_d = sorted(d.items(), key=lambda x: x[1])        
    
    for k in range(len(sorted_d)):
        if k+1 != sorted_d[k][1]:
            res = 'False'
            return res
    res = 'True'
    return res
    
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
