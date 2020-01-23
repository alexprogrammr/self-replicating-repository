# Technical Specification

## Overview

1. The user clicks on the *Replicate repository* button on the main application page.
2. The user is redirected to GitHub to allow access to his/her public repositories.
3. Application forks its repository to the user's GitHub account.

## How does it work

Application is created using [Flask](https://github.com/pallets/flask) - a lightweight WSGI web application framework. Authorization to the user's GitHub account is implemented with the [OAuth2](https://oauth.net/2/) protocol using [Authlib](https://authlib.org) framework. Application is hosted on [Heroku](https://heroku.com) - a cloud application platform.

The whole process consists of the next steps:

1. Authorization

    The user is redirected to GitHub authentication [URL](https://github.com/login/oauth/authorize) and is asked to grant permission to public repositories (`public_repo` scope).

2. Authorization Callback

    GitHub redirects the user to the application authorization callback. At this step, the application retrieves the user's access token that is used to make requests to GitHub API.

3. Replication

    Application performs POST request to `/repos/:owner/:repo/forks` endpoint to create a fork for the authenticated user. Finally, the user is redirected to the GitHub page of the forked repository.
