from flask import render_template
from app import app

@app.route('/news')
def news():     
      data = {
       'headTitle': 'News',
       'title': 'news',
       'subTitle': 'Latest news',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('news/news.html', **data)

@app.route('/newsCarousel')
def newsCarousel():     
      data = {
       'headTitle': 'Cart',
       'title': 'Shop',
       'subTitle': 'Cart',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('news/newsCarousel.html', **data)

@app.route('/newsDetails')
def newsDetails():     
      data = {
       'headTitle': 'News details',
       'title': 'News details',
       'subTitle': 'News details',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('news/newsDetails.html', **data)

@app.route('/newsSidebar')
def newsSidebar():     
      data = {
       'headTitle': 'News right sidebar',
       'title': 'news sidebar',
       'subTitle': 'News right sidebar',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('news/newsSidebar.html', **data)

@app.route('/newsSidebarLeft')
def newsSidebarLeft():     
      data = {
       'headTitle': 'News left sidebar',
       'title': 'news sidebar',
       'subTitle': 'News left sidebar',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('news/newsSidebarLeft.html', **data)