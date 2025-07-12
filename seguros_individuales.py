from flask import render_template
from app import app

@app.route('/autos')
def autos():     
      data = {
       'headTitle': 'Autos',
       'title': 'seguros individuales',
       'subTitle': 'Autos',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('seguros_individuales/autos.html', **data)

@app.route('/salud')
def salud():     
      data = {
       'headTitle': 'Salud',
       'title': 'seguros individuales',
       'subTitle': 'Salud',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('seguros_individuales/salud.html', **data)

@app.route('/ahorroeinv')
def ahorroeinv():     
      data = {
       'headTitle': 'ahorroeinv',
       'title': 'seguros individuales',
       'subTitle': 'ahorroeinv',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('seguros_individuales/ahorroeinv.html', **data)

@app.route('/hogar')
def hogar():     
      data = {
       'headTitle': 'hogar',
       'title': 'seguros individuales',
       'subTitle': 'hogar',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('seguros_individuales/hogar.html', **data)

@app.route('/travel')
def travel():     
      data = {
       'headTitle': 'viajero',
       'title': 'seguros individuales',
       'subTitle': 'viajero',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('seguros_individuales/travel.html', **data)

@app.route('/vida')
def vida():     
      data = {
       'headTitle': 'vida',
       'title': 'seguros individuales',
       'subTitle': 'vida',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('seguros_individuales/vida.html', **data)