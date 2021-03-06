from flask import Flask
from config import Config
from authlib.integrations.flask_client import OAuth


app = Flask(__name__)
app.config.from_object(Config)

oauth = OAuth(app)
oauth.register(
    name='github',
    client_kwargs={
        'scope': 'public_repo',
    }
)


from app import routes
