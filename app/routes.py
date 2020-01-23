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
    oauth.github.authorize_access_token()

    github_username = app.config['GITHUB_USERNAME']
    github_reponame = app.config['GITHUB_REPONAME']
    fork_repo_endpoint = f'/repos/{github_username}/{github_reponame}/forks'

    response = oauth.github.post(fork_repo_endpoint)
    if not response.ok:
        return 'Something went wrong...'

    forked_repo_url = response.json()['html_url']
    return redirect(forked_repo_url)
