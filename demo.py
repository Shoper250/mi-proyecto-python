from flask import render_template
from app import app

@app.route('/')
@app.route('/index')   
def index():     
      data = {
       'headTitle': 'BeSeguro',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('demo/index.html', **data)

@app.route('/index-one-page')
def indexOnePage():     
      data = {
       'headTitle': 'BeSeguro',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
       'footer': 'true',
      }
      return render_template('demo/indexOnePage.html', **data)

@app.route('/index-2')
def index2():     
      data = {
       'headTitle': 'BeSeguro',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('demo/index2.html', **data)

@app.route('/index2-one-page')
def index2OnePage():     
      data = {
       'headTitle': 'BeSeguro',
       'footer': 'true',
      }
      return render_template('demo/index2OnePage.html', **data)

@app.route('/index-3')
def index3():     
      data = {
       'headTitle':'Home Three',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('demo/index3.html', **data)

@app.route('/index3-one-page')
def index3OnePage():     
      data = {
       'headTitle': 'Home Three',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('demo/index3OnePage.html', **data)

@app.route('/index-4')
def index4():     
      data = {
       'headTitle': 'Home Four',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/> <link rel="stylesheet" href="/static/vendors/insur-three-icon/style.css"/>',
       'css2':'<link rel="stylesheet" href="/static/css/color-2.css"/>',
      }
      return render_template('demo/index4.html', **data)

@app.route('/index4-one-page')
def index4OnePage():     
      data = {
       'headTitle': 'Home Four',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/> <link rel="stylesheet" href="/static/vendors/insur-three-icon/style.css"/>',
       'css2':'<link rel="stylesheet" href="/static/css/color-2.css"/>',
      }
      return render_template('demo/index4OnePage.html', **data)

@app.route('/index-5')
def index5():     
      data = {
       'headTitle': 'BeSeguro',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/> <link rel="stylesheet" href="/static/vendors/insur-three-icon/style.css"/>',
       'css2':'<link rel="stylesheet" href="/static/css/color-3.css"/>',
      }
      return render_template('demo/index5.html', **data)

@app.route('/index5-one-page')
def index5OnePage():     
      data = {
       'headTitle': 'BeSeguro',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/> <link rel="stylesheet" href="/static/vendors/insur-three-icon/style.css"/>',
       'css2':'<link rel="stylesheet" href="/static/css/color-3.css"/>',
      }
      return render_template('demo/index5OnePage.html', **data)

@app.route('/index-6')
def index6():     
      data = {
       'headTitle': 'BeSeguro',
       'css':'<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet"> <link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/> ',
       'css2':'<link rel="stylesheet" href="/static/css/color-4.css"/>',
      }
      return render_template('demo/index6.html', **data)

@app.route('/index6-one-page')
def index6OnePage():     
      data = {
       'headTitle': 'BeSeguro',
       'css':'<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet"> <link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/> ',
       'css2':'<link rel="stylesheet" href="/static/css/color-4.css"/>',
      }
      return render_template('demo/index6OnePage.html', **data)


@app.route('/index-7')
def index7():     
      data = {
       'headTitle': 'Home Seven',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
       'css2':'<link rel="stylesheet" href="/static/css/color-5.css"/>',
      }
      return render_template('demo/index7.html', **data)

@app.route('/index7-one-page')
def index7OnePage():     
      data = {
       'headTitle': 'Home Seven',
       'css':'<link rel="stylesheet" href="/static/vendors/insur-three-icon/style.css"/>',
       'css2':'<link rel="stylesheet" href="/static/css/color-5.css"/>',
      }
      return render_template('demo/index7OnePage.html', **data)

@app.route('/index-boxed')
def indexBoxed():     
      data = {
       'headTitle': 'insurance',
       'header':'true',
       'strickyheader':'true',
       'bodyClass': 'boxed-wrapper',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('demo/indexBoxed.html', **data)

@app.route('/index-dark')
def indexDark():     
      data = {
       'headTitle': 'BeSeguro',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
       'css2':'<link rel="stylesheet" href="/static/css/insur-dark.css"/>',
       'footer': 'true',
      }
      return render_template('demo/indexDark.html', **data)

@app.route('/index-Rtl')
def indexRtl():     
      return render_template('demo/indexRtl.html')