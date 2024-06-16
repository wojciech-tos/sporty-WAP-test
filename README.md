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

| Step | Verification |
| ------ | ------ |
| close_cookies_consent_if_visible | check if cookies popup exists and if yes click accept |
| close_privacy_info_popup_if_visible | check if privacy info popup exists and click close |
| click_search_button | find search button and click |
| input_text_into_search_bar | find search bar, input text |
| click_first_search_suggestion_link | find first suggestion on the list, click |
| click_show_all_link | find show all channels, click |
| wait_for_channels_list_to_load | check if searched channels elements are displayed |
| scroll_down | just scroll down |
| choose_channel | check for visible channels and click first, wait for channel to load |
| save_screenshot | save screenshot |

Every find element is a validation by itself, as it waits implicit wait and checks if element exist on a page.
Every find elements is verified with len, as a verification if it exists or does not exist.

File structure:
Test file is in tests main folder. I used Page Object Pattern and created page files for search and cookies elements. There is also utils folder with utilities used in test like webdriver instance or UI operations like scroll and saving screenshot.

INFO:
There is a bug with closing cookies popup on twitch website. I implemented a workaround. Video record with this bug is in folder **misc/twitch_bugs**.
There is a problem with Chrome and webdriver ActionChains scroll page functionality. I implemented a workaround for that too.
