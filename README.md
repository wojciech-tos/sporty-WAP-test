# Sporty.com task

## How to run Twitch test:

- Clone this repository locally
- Enter main folder **sporty_WAP_task**
- Install, create and activate virtual environment
> pip install virtualenv

> virtualenv venv

> source venv/Scripts/activate
- Install requirements
> pip install -r requirements.txt
- Run
> pytest --html=report.html

After test succeeds a screenshot and report will be generated in main folder (**screenshot.png** and **report.html**)

INFO:
There is a bug with closing cookies popup on twitch website. I implemented a workaround. Video record with this bug is in folder **misc/twitch_bugs**.
There is a problem with Chrome and webdriver ActionChains scroll page functionality. I implemented a workaround for that too.
