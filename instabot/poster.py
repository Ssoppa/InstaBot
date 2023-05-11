import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from dotenv import load_dotenv

from instabot.post import Post


class Poster:
    def __init__(self) -> None:
        self._config_driver()

    def _config_driver(self) -> None:
        pass

    def _login(self) -> None:
        pass

    def _delete_post(self, post : Post) -> None:
        pass

    def post(post : Post) -> str:
        pass