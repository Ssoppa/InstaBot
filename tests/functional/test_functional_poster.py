import os

from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from time import sleep

from instabot.post import Post
from instabot.poster import Poster

def test_functional_login():
    # Given.
    poster = Poster(username=os.getenv('TEST_INSTAGRAM_USERNAME'), password=os.getenv('TEST_INSTAGRAM_PASSWORD'), account_name=os.getenv('TEST_INSTAGRAM_ACCOUNT_NAME'))

    # When.
    poster._login()

    # Then.
    profile_link = poster._driver.find_element(By.XPATH, f"//a[contains(@href, '{poster._username}')]").get_attribute('href')
    poster._driver.quit()
    assert profile_link == f"https://www.instagram.com/{poster._username}/"
    
def test_functional_delete_post():
    # Given.
    poster = Poster(username=os.getenv('TEST_INSTAGRAM_USERNAME'), password=os.getenv('TEST_INSTAGRAM_PASSWORD'), account_name=os.getenv('TEST_INSTAGRAM_ACCOUNT_NAME'))
    post = Post(filepath=os.getcwd() + '/tests/img/valid_test_img.png', description="This is a test description.", scheduled_time=(datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y %H:%M:%S"))
    url = poster.post(post)
    default_message = "Sorry, this page isn't available."

    # When.
    poster._delete_post(url)

    # Then.
    poster._driver.get(url)
    sleep(2)
    poster._driver.get(url)
    sleep(2)
    received_message = poster._driver.find_element(By.XPATH, f"//span[contains(text(), 'Sorry, this page')]").text
    poster._driver.quit()
    assert received_message == default_message

def test_functional_post_file():
    # Given.
    poster = Poster(username=os.getenv('TEST_INSTAGRAM_USERNAME'), password=os.getenv('TEST_INSTAGRAM_PASSWORD'), account_name=os.getenv('TEST_INSTAGRAM_ACCOUNT_NAME'))
    post = Post(filepath=os.getcwd() + '/tests/img/valid_test_img.png', description="This is a test description.", scheduled_time=(datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y %H:%M:%S"))
    
    # When.
    url = poster.post(post)

    # Then.
    poster._driver.get(url)
    sleep(2)
    post_description = poster._driver.find_element(By.XPATH, f"//h1[contains(text(), '{post.description}')]").text
    formatted_date = datetime.now().strftime("%b %d, %Y")
    post_image_information = poster._driver.find_element(By.XPATH, f"//img[contains(@alt, '{formatted_date}')]").get_attribute("alt")
    
    assert post_description == post.description
    assert post_image_information == f"Photo by {poster._account_name} on {formatted_date}."
    
    poster._delete_post(url)
    poster._driver.quit()