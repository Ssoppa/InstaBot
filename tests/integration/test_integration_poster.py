import os

from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from time import sleep

from instabot.post import Post
from instabot.poster import Poster

def test_integration_post_multiple_times():
    # Given.
    poster = Poster(username=os.getenv('TEST_INSTAGRAM_USERNAME'), password=os.getenv('TEST_INSTAGRAM_PASSWORD'), account_name=os.getenv('TEST_INSTAGRAM_ACCOUNT_NAME'))
    post1 = Post(filepath=os.getcwd() + '/tests/img/valid_test_img.png', description="This is a test description.", scheduled_time=datetime.now() + timedelta(days=1))
    post2 = Post(filepath=os.getcwd() + '/tests/img/valid_test_img.png', description="This is a test description.", scheduled_time=datetime.now() + timedelta(days=2))

    # When.
    url1 = poster.post(post1)
    url2 = poster.post(post2)

    # Then.
    poster._driver.get(url1)
    sleep(2)
    post_description1 = poster._driver.find_element(By.XPATH, f"//h1[contains(text(), '{post1.description}')]").text
    post_image_information1 = poster._driver.find_element(By.XPATH, f"//img[contains(@alt, '{datetime.now().strftime('%b %d, %Y')}')]").get_attribute("alt")
    
    poster._driver.get(url2)
    sleep(2)
    post_description2 = poster._driver.find_element(By.XPATH, f"//h1[contains(text(), '{post1.description}')]").text
    post_image_information2 = poster._driver.find_element(By.XPATH, f"//img[contains(@alt, '{datetime.now().strftime('%b %d, %Y')}')]").get_attribute("alt")

    poster._delete_post(url1)
    poster._delete_post(url2)
    poster._driver.quit()

    assert post_description1 == post1.description
    assert post_image_information1 == f"Photo by {poster._account_name} on {datetime.now().strftime('%b %d, %Y')}."
    assert post_description2 == post2.description
    assert post_image_information2 == f"Photo by {poster._account_name} on {datetime.now().strftime('%b %d, %Y')}."