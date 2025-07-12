from flask import render_template
from app import app

@app.route('/about')
def about():     
      data = {
       'headTitle': 'about',
       'title': 'About',
       'subTitle': 'About us',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'counterOne':'false', 
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/about.html', **data)

@app.route('/error-page')
def errorPage():     
      data = {
       'headTitle': '404 Error',
       'title': '404 error',
       'subTitle': '404 error',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/errorPage.html', **data)

@app.route('/faq')
def faq():     
      data = {
       'headTitle': 'FAQ',
       'title': 'FAQS',
       'subTitle': 'FAQS',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',  
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/faq.html', **data)

@app.route('/makea-claim-death')
def makeaClaimDeath():     
      data = {
       'headTitle': 'Make a Claim',
       'title': 'Make a Claim',
       'subTitle': 'Death claim',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/insur-three-icon/style.css"/>',
      }
      return render_template('pages/makeaClaimDeath.html', **data)

@app.route('/makea-claim-group')
def makeaClaimGroup():     
      data = {
       'headTitle': 'Make a claim',
       'title': 'Make a claim',
       'subTitle': 'Group & pension claims',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'counterone':'false', 
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/makeaClaimGroup.html', **data)

@app.route('/makea-claim-loan')
def makeaClaimLoan():     
      data = {
       'headTitle': 'Make a claim',
       'title': 'Make a claim',
       'subTitle': 'Loan against insurance policy',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'counterone':'false', 
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/makeaClaimLoan.html', **data)

@app.route('/makea-claim-maturity')
def makeaClaimMaturity():     
      data = {
       'headTitle': 'Make a claim',
       'title': 'Make a claim',
       'subTitle': 'Maturity claims',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'counterone':'false', 
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/makeaClaimMaturity.html', **data)

@app.route('/makea-claim-other')
def makeaClaimOther():     
      data = {
       'headTitle': 'Make a claim',
       'title': 'Make a claim',
       'subTitle': 'Other claims',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'counterone':'false', 
       'css':'<link rel="stylesheet" href="/static/vendors/insur-three-icon/style.css"/>',
      }
      return render_template('pages/makeaClaimOther.html', **data)

@app.route('/policy-proposal')
def policyProposal():     
      data = {
       'headTitle': 'Policy proposal',
       'title': 'Policy proposal',
       'subTitle': 'Policy proposal',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/nice-select/nice-select.css"/>',
      }
      return render_template('pages/policyProposal.html', **data)

@app.route('/portfolio')
def portfolio():     
      data = {
       'headTitle': 'Portfolio',
       'title': 'Portfolio',
       'subTitle': 'Our portfolio',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/portfolio.html', **data)

@app.route('/portfolio-carousel')
def portfolioCarousel():     
      data = {
       'headTitle': 'portfolio carousel',
       'title': 'portfolio carousel',
       'subTitle': 'Portfolio carousel',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/portfolioCarousel.html', **data)

@app.route('/portfolio-details')
def portfolioDetails():     
      data = {
       'headTitle': 'Portfolio Details',
       'title': 'portfolio Details',
       'subTitle': 'Portfolio details',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/portfolioDetails.html', **data)

@app.route('/pricing')
def pricing():     
      data = {
       'headTitle': 'Pricing',
       'title': 'Pricing',
       'subTitle': 'Pricing plans',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/pricing.html', **data)

@app.route('/sign-in')
def signin():     
      data = {
       'headTitle': 'Sign In',
       'title': 'Login register',
       'subTitle': 'Login register',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/signin.html', **data)

@app.route('/team-carousel')
def teamCarousel():     
      data = {
       'headTitle': 'Team Carousel',
       'title': 'Team',
       'subTitle': 'Team carousel',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/teamCarousel.html', **data)

@app.route('/team-details')
def teamDetails():     
      data = {
       'headTitle': 'Team Details',
       'title': 'Team details',
       'subTitle': 'Team details',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/teamDetails.html', **data)

@app.route('/team-page')
def teamPage():     
      data = {
       'headTitle': 'Team Page',
       'title': 'Team',
       'subTitle': 'Our team',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/teamPage.html', **data)

@app.route('/testimonial')
def testimonial():     
      data = {
       'headTitle': 'Testimonials',
       'title': 'Testimonials',
       'subTitle': 'Testimonials',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/testimonial.html', **data)

@app.route('/testimonial-carousel')
def testimonialCarousel():     
      data = {
       'headTitle': 'Testimonials carousel',
       'title': 'Testimonials',
       'subTitle': 'Testimonials carousel',
       'header':'true',
       'strickyheader':'true',
       'footer': 'true',
       'css':'<link rel="stylesheet" href="/static/vendors/ion.rangeSlider/css/ion.rangeSlider.min.css"/>',
      }
      return render_template('pages/testimonialCarousel.html', **data)
