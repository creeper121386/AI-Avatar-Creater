from . import crawl
from flask import render_template,request
@crawl.route('/',methods=['GET'])
def crawl_main():
    return render_template('crawl.html')
@crawl.route('/',methods=['POST'])
def data_load():
    data = request.form
    print(request.form)
    return data;

    
