# Installation

The application can be run either locally or deployed in the cloud. Current document provides instructions for deployment application to [Heroku](https://heroku.com).

## Prerequisites

- [Git](https://git-scm.com/) and [GitHub](https://github.com) account
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and [Heroku](https://heroku.com) account
- [Python 3.8](https://www.python.org/)

## Local Installation

Get OAuth credentials from GitHub application:

- Visit https://github.com/settings/applications/new to create new application on GitHub
- Fill application name field with any name
- Fill *Homepage URL* field with `http://localhost:5000`
- Fill *Authorization callback URL* field with `http://localhost:5000/authorize/callback`
- Save *Client ID* and *Client Secret* as they are needed for the next steps

Clone the repository:

```
$ git clone https://github.com/alexprogrammr/self-replicating-repository.git
```

Create and activate virtual environment:

```
$ cd self-replicating-repository
$ python3 -m venv venv
$ source venv/bin/activate
```

Install required dependencies:

```
$ python3 -m pip install -r requirements.txt
```

Set environment variables with your own values:

```
$ export GITHUB_CLIENT_ID=<YOUR_CLIENT_ID>
$ export GITHUB_CLIENT_SECRET=<YOUR_CLIENT_SECRET>
$ export OAUTHLIB_INSECURE_TRANSPORT=1
```

Please note, that setting *OAUTHLIB_INSECURE_TRANSPORT* variable to 1 is only needed for local deployment because the local server only supports HTTP while OAuth2 normally works over HTTPS protocol.

Run the application:

```
$ flask run
```

Go to http://localhost:5000 to check that you can successfully replicate the repository.

## Heroku Installation

Create Heroku application:

- Login to [Heroku](https://heroku.com) and [create new app](https://dashboard.heroku.com/new-app)
- Fill *App name* field with any name and choose appropriate region
- Click on *Create App* button

Get OAuth credentials from GitHub application:

- Visit https://github.com/settings/applications/new to create new application on GitHub
- Fill application name field with any name, it should not be equal to the name of your Heroku application
- Fill *Homepage URL* field with `https://<YOUR-HEROKU-APP-NAME>.herokuapp.com`
- Fill *Authorization callback URL* field with `http://<YOUR-HEROKU-APP-NAME>.herokuapp.com/authorize/callback`
- Save *Client ID* and *Client Secret* as they are needed for the next steps

Set environment variables for your application:

- Open dashboard of your Heroku application
- Go to *Settings* tab
- Click on *Reveal Config Vars* button
- Add `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` keys with OAuth credentials from GitHub application

Login to Heroku CLI:

```
$ heroku login
```

Add a remote to git repository for your Heroku application:

```
$ git remote add heroku https://git.heroku.com/<YOUR-HEROKU-APP-NAME>.git
```

Deploy your master branch to Heroku:

```
$ git push heroku master
```

This command will automatically build and deploy your application.

Go to `https://<YOUR-HEROKU-APP-NAME>.herokuapp.com` to check that you can successfully replicate the repository.
