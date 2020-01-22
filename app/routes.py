from app import app, oauth
from flask import url_for, redirect


@app.route('/')
@app.route('/index')
def index():
    return "Hello World"


@app.route('/authorize')
def authorize():
    redirect_url = url_for('authorize_callback', _external=True)
    return oauth.github.authorize_redirect(redirect_url)


@app.route('/authorize/callback')
def authorize_callback():
    token = oauth.github.authorize_access_token()
    return token
