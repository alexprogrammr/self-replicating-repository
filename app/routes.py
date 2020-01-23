from app import app, oauth
from flask import url_for, redirect, render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/authorize')
def authorize():
    redirect_url = url_for('authorize_callback', _external=True)
    return oauth.github.authorize_redirect(redirect_url)


@app.route('/authorize/callback')
def authorize_callback():
    return oauth.github.authorize_access_token()
