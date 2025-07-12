from flask import render_template
from app import app

@app.route('/business-insurance')  
def businessInsurance():     
      data = {
       'headTitle': 'Business Insurance',
       'title': 'insurance',
       'subTitle': 'Business insurance',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/insur-three-icon/style.css"/>',
      }
      return render_template('Insurance/businessInsurance.html', **data)

@app.route('/car-insurance')  
def carInsurance():     
      data = {
       'headTitle': 'Car insurance',
       'title': 'insurance',
       'subTitle': 'Car insurance',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/insur-three-icon/style.css"/>',
      }
      return render_template('Insurance/carInsurance.html', **data)

@app.route('/fire-insurance') 
def fireInsurance():     
      data = {
       'headTitle': 'Fire Insurance',
       'title': 'Insurance',
       'subTitle': 'Fire insurance',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/insur-three-icon/style.css"/>',
      }
      return render_template('Insurance/fireInsurance.html', **data)

@app.route('/health-insurance') 
def healthInsurance():     
      data = {
       'headTitle': 'Health Insurance',
       'title': 'insurance',
       'subTitle': 'Health insurance',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/insur-three-icon/style.css"/>',
      }
      return render_template('Insurance/healthInsurance.html', **data)

@app.route('/home-insurance') 
def homeInsurance():     
      data = {
       'headTitle': 'Home Insurance',
       'title': 'Insurance',
       'subTitle': 'Home insurance',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/insur-three-icon/style.css"/>',
      }
      return render_template('Insurance/homeInsurance.html', **data)

@app.route('/insurance-01')
def insurance01():     
      data = {
       'headTitle': 'insurance 01',
       'title': 'Insurance One',
       'subTitle': 'Insurance one',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('Insurance/insurance01.html', **data)

@app.route('/insurance-02')
def insurance02():     
      data = {
       'headTitle': 'insurance 02',
       'title': 'insurance two',
       'subTitle': 'Insurance two',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('Insurance/insurance02.html', **data)

@app.route('/insurance-03')
def insurance03():     
      data = {
       'headTitle': 'insurance 03',
       'title': 'insurance',
       'subTitle': 'Insurance three',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('Insurance/insurance03.html', **data)

@app.route('/life-insurance')
def lifeInsurance():     
      data = {
       'headTitle': 'life Insurance',
       'title': 'Insurance',
       'subTitle': 'Life insurance',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/insur-three-icon/style.css"/>',
      }
      return render_template('Insurance/lifeInsurance.html', **data)

@app.route('/marriage-insurance')
def marriageInsurance():     
      data = {
       'headTitle': 'Marriage Insurance',
       'title': 'Insurance',
       'subTitle': 'Marriage insurance',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/insur-three-icon/style.css"/>',
      }
      return render_template('Insurance/marriageInsurance.html', **data)

@app.route('/travel-insurance')
def travelInsurance():     
      data = {
       'headTitle': 'Travel Insurance',
       'title': 'Insurance',
       'subTitle': 'Travel insurance',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('Insurance/travelInsurance.html', **data)