import os

from datetime import datetime, timedelta
from selenium.webdriver.common.by import By

from instabot.post import Post
from instabot.poster import Poster

def test_functional_post_file():
    # Given.
    poster = Poster()
    scheduled_time = (datetime.now() + timedelta(days=1))
    post = Post(filepath=os.getcwd() + '/tests/img/valid_test_img.png', description="This is a test description.", scheduled_time=scheduled_time.strftime("%d/%m/%Y %H:%M:%S"))

    # When.
    url = poster.post(post)

    # Then.
    poster._driver.get(url)
    post_description = poster._driver.find_element(By.XPATH, f"//div[contains(text(), '{post.description}')]").text
    formatted_date = scheduled_time.strftime("%d %b, %Y")
    post_image_information = poster._driver.find_element(By.XPATH, f"//img[contains(@alt, '{formatted_date}')]").text
    
    assert post_description == post.description
    assert post_image_information == f"Photo by {poster._account_name} on {formatted_date}."
    
    poster._delete_post(post)

def test_functional_login():
    # Given. When.
    poster = Poster()

    # Then.
    profile_link = poster._driver.find_element(By.XPATH, f"//a[contains(@href, '{poster._username}')]").href
    assert profile_link == f"/{poster._username}/"
    

def test_functional_delete_post():
    # Given.
    poster = Poster()
    post = Post(filepath=os.getcwd() + '/tests/img/valid_test_img.png', description="This is a test description.", scheduled_time=(datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y %H:%M:%S"))
    url = poster.post(post)
    default_message = "The link you followed may be broken, or the page may have been removed."

    # When.
    poster._delete_post(post)

    # Then.
    poster._driver.get(url)
    received_message = poster._driver.find_element(By.XPATH, f"//span[contains(text(), '{default_message}')]").text
    assert received_message == {default_message}