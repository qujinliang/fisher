'''
    Created by qjl on 2018-04-25
'''

from flask import Flask



__author__ = 'qjl'
# 核心对象
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)