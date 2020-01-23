import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)

    GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME', 'alexprogrammr')
    GITHUB_REPONAME = os.environ.get('GITHUB_REPONAME', 'self-replicating-repository')

    GITHUB_API_BASE_URL = os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')
    GITHUB_AUTHORIZE_URL = os.environ.get('GITHUB_AUTHORIZE_URL', 'https://github.com/login/oauth/authorize')
    GITHUB_ACCESS_TOKEN_URL = os.environ.get('GITHUB_ACCESS_TOKEN_URL', 'https://github.com/login/oauth/access_token')

    GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID')
    GITHUB_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET')
