# RoBoPug-Twitch
Twitch bot for personal use

## Proposed functionality
- General information commands:
  - [x] Discord
  - [x] Help
  - [x] Uptime
  - [ ] User info
  - [ ] ...
- Spotify
  - [x] Now playing
  - [x] Song request
- Games
  - [ ] Chance games
  - [ ] Prediction points
  - [ ] Fights between users
    - Strength based on followage/prediction_points/...
    - Collection system
    - Experience points, level system
    - Character leveling
    - ...
- ~~Modding commands~~: ***These are built-in in twitch now***
  - [ ] ~~Predictions~~
  - [ ] ~~(Un)ban~~
  - [ ] ~~(Un)timeout~~
  - [ ] ~~(Un)mod~~
  - [ ] ~~(Un)follower mode~~
  - [ ] ~~(Un)subscriber mode~~
  - [ ] ...


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
Get your oauth token [here.](https://twitchapps.com/tmi/)

## How to run

```pipenv run python main.py```

![RoBoPug](/data/images/RoBoPug.png)

<font size="1">[Source](https://www.deviantart.com/bamshackle/art/Mech-Pug-Bot-514793864)</font> 
