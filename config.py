import os


class Config:
    SECRET_KEY = os.urandom(24)

    GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID')
    GITHUB_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET')
    GITHUB_API_BASE_URL = os.environ.get('GITHUB_API_BASE_URL')
    GITHUB_AUTHORIZE_URL = os.environ.get('GITHUB_AUTHORIZE_URL')
    GITHUB_ACCESS_TOKEN_URL = os.environ.get('GITHUB_ACCESS_TOKEN_URL')
