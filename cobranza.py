from flask import render_template
from app import app

@app.route('/cart')
def cart():     
      data = {
       'headTitle': 'Cart',
       'title': 'cobranza',
       'subTitle': 'Cart',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('cobranza/cart.html', **data)

@app.route('/check-out')
def checkOut():     
      data = {
       'headTitle': 'Checkout',
       'title': 'cobranza',
       'subTitle': 'Checkout',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/nice-select/nice-select.css"/>',

      }
      return render_template('cobranza/checkOut.html', **data)

@app.route('/contact')
def contact():     
      data = {
       'headTitle': 'Contact',
       'title': 'Contact',
       'subTitle': 'Contact',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true', 
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('cobranza/contact.html', **data)

@app.route('/insurance-details')
def insuranceDetails():     
      data = {
       'headTitle': 'about',
       'title': 'About',
       'subTitle': 'About us',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('cobranza/insuranceDetails.html', **data)

@app.route('/product-details')
def productDetails():     
      data = {
       'headTitle': 'Product details',
       'title': 'cobranza',
       'subTitle': 'Product details',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('cobranza/productDetails.html', **data)

@app.route('/products')
def products():     
      data = {
       'headTitle': 'Products',
       'title': 'cobranza',
       'subTitle': 'Products',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/nice-select/nice-select.css"/>',
      }
      return render_template('cobranza/products.html', **data)

@app.route('/pagos')
def pagos():     
      data = {
       'headTitle': 'Pagos',
       'title': 'cobranza',
       'subTitle': 'Pagos',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/nice-select/nice-select.css"/>',
      }
      return render_template('cobranza/pagos.html', **data)
