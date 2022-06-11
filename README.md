# rbotp
Twitch bot for personal use

## Installation

### Step 1

```pip install pipenv```

```pipenv --python 3.10```

```pipenv install twitchio```

[Twitchio documentation](https://twitchio.dev/en/latest/)

### Step 2
Create a .env file in your working directory, that looks like this:

```
TMI_TOKEN=
BOT_PREFIX=!
CHANNEL=
```

and fill it in using your specific credentials. More info on how to get your token and registering your app can be found [here.](https://dev.twitch.tv/docs/authentication/register-app)

## How to run

```pipenv run python main.py```