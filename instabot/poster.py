import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from dotenv import load_dotenv

from instabot.post import Post


class Poster:
    def __init__(self, *args, **kwargs) -> None:
        self._username = kwargs.get('username', None)
        self._account_name = kwargs.get('account_name', None)
        self._password = kwargs.get('password', None)
        self._logged = False

        if self._username is None:
            raise ValueError("username argument is required!")
        if self._account_name is None:
            raise ValueError("account_name argument is required!")
        if self._password is None:
            raise ValueError("password argument is required!")
        if type(self._username) is not str:
            raise TypeError("username argument must be a string!")
        if type(self._account_name) is not str:
            raise TypeError("account_name argument must be a string!")
        if type(self._password) is not str:
            raise TypeError("password argument must be a string!")

        self._config_driver()

    def _config_driver(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("test-type")
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--enable-precise-memory-info")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-default-apps")
        chrome_options.add_argument("test-type=browser")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone 12 Pro"})

        self._driver = webdriver.Chrome(ChromeDriverManager().install(),
                            options=chrome_options)

    def _login(self) -> None:
        try:
            self._driver.get("https://www.instagram.com/")

            sleep(2)
            self._driver.find_element(By.XPATH, "//div[contains(text(), 'Log in')]").click()
            self._driver.find_element(By.XPATH, "//input[@name=\"username\"]").send_keys(self._username)
            self._driver.find_element(By.XPATH, "//input[@name=\"password\"]").send_keys(os.getenv('TEST_INSTAGRAM_PASSWORD'))
            self._driver.find_element(By.XPATH, '//button[@type="submit"]').click()
            sleep(5)
            try:
                self._driver.find_element(By.XPATH, "//div[contains(text(), 'Not Now')]").click()
                sleep(5)
            except:
                pass
            try:
                self._driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
                sleep(2)
            except:
                pass

            self._logged = True
        except Exception as e:
            raise Exception(e)

    def _delete_post(self, url : str) -> None:
        self._driver.get(url)
        sleep(2)
        self._driver.find_element(By.XPATH, "//*[name()='svg' and @aria-label='More options']").find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "..").click()
        sleep(1)
        self._driver.find_element(By.XPATH, '//button[contains(text(), "Delete")]').click()
        sleep(1)
        self._driver.find_element(By.XPATH, '//button[contains(text(), "Delete")]').click()

    def post(self, post : Post) -> str:
        if not self._logged:
            self._login()
        else:
            self._driver.get("https://www.instagram.com/")
            sleep(2)

        self._driver.find_element(By.XPATH, "//a[contains(@href, '#')]").click()
        sleep(2)
        self._driver.find_element(By.XPATH, "//div[@class='x1exxlbk']/div").click()
        # self._driver.find_element(By.XPATH, "//span[contains(text(), 'Post')]").click()
        # post_element = self._driver.find_element(By.XPATH, "//span[contains(text(), 'Post')]").find_element(By.XPATH, "..").find_element(By.XPATH, "..")
        # self._driver.execute_script("arguments[0].scrollIntoView();", post_element)
        # self._driver.execute_script("arguments[0].click();", post_element)
        sleep(2)
        self._driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(post.filepath)
        sleep(10)
        try:
            self._driver.find_element(By.XPATH, '//span[contains(text(), "Expand")]').click()
            sleep(2)
        except:
            pass
        self._driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]").click()
        sleep(5)
        self._driver.find_element(By.XPATH, "//textarea[@aria-label='Write a caption…']").click()
        sleep(1)
        self._driver.find_element(By.XPATH, "//textarea[@aria-label='Write a caption…']").send_keys(post.description)
        sleep(1)
        self._driver.find_element(By.XPATH, "//button[contains(text(), 'Share')]").click()
        sleep(5)
        self._driver.find_element(By.XPATH, "//*[name()='svg' and @aria-label='More options']").find_element(By.XPATH, "..").find_element(By.XPATH, "..").find_element(By.XPATH, "..").click()
        sleep(2)
        url = self._driver.find_element(By.XPATH, "//button[contains(text(), 'Delete')]/following-sibling::button/a").get_attribute('href')
        return url