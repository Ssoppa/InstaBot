import os

from instabot.instabot import Instabot
from instabot.post import Post

from datetime import datetime, timedelta
from time import sleep


def test_functional_instabot_bot_with_one_post():
    # Given.
    instabot = Instabot(":memory:")
    post = Post(filepath=os.getcwd() + '/tests/img/valid_test_img.png', description=f"This is a test description number: 1.", scheduled_time=datetime.now() + timedelta(seconds=1))
    instabot._scheduler.schedule_post(post)
    sleep(2)

    # When.
    instabot._check_and_post()

    for url in instabot._lists_of_url:
        instabot._poster._delete_post(url)

    # Then.
    remaining_posts = instabot._scheduler.get_quantity_of_posts()
    assert remaining_posts == 0

def test_functional_instabot_bot_with_two_posts():
    # Given.
    instabot = Instabot(":memory:")
    for index in range(2):
        post = Post(filepath=os.getcwd() + '/tests/img/valid_test_img.png', description=f"This is a test description number: {index + 1}.", scheduled_time=datetime.now() + timedelta(seconds=1))
        instabot._scheduler.schedule_post(post)
    sleep(2)

    # When.
    instabot._check_and_post()

    for url in instabot._lists_of_url:
        instabot._poster._delete_post(url)

    # Then.
    remaining_posts = instabot._scheduler.get_quantity_of_posts()
    assert remaining_posts == 0

def test_functional_instabot_bot_with_multiple_posts_and_one_remaining():
    # Given.
    instabot = Instabot(":memory:")
    for index in range(2):
        post = Post(filepath=os.getcwd() + '/tests/img/valid_test_img.png', description=f"This is a test description number: {index + 1}.", scheduled_time=datetime.now() + timedelta(seconds=1))
        instabot._scheduler.schedule_post(post)
    post = Post(filepath=os.getcwd() + '/tests/img/valid_test_img.png', description=f"This is a test description number: {index + 1}.", scheduled_time=datetime.now() + timedelta(days=1))
    instabot._scheduler.schedule_post(post)
    sleep(2)

    # When.
    instabot._check_and_post()

    for url in instabot._lists_of_url:
        instabot._poster._delete_post(url)

    # Then.
    remaining_posts = instabot._scheduler.get_quantity_of_posts()
    assert remaining_posts == 1

