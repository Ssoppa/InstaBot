import os

from instabot.instabot import Instabot
from instabot.scheduler import Scheduler
from instabot.post import Post
from instabot.poster import Poster

from datetime import datetime, timedelta


def test_functional_instabot_bot_with_one_post():
    # Given.
    scheduler = Scheduler(":memory:")
    post = Post(filepath=os.getcwd() + '/tests/img/valid_test_img.png', description=f"This is a test description number: 1.", scheduled_time=datetime.now())
    scheduler.schedule_post(post)

    # When.
    instabot = Instabot(":memory:")

    for url in instabot._lists_of_url:
        instabot._poster._delete_post(url)

    # Then.
    remaining_posts = instabot._scheduler.get_quantity_of_posts()
    assert remaining_posts == 0

def test_functional_instabot_bot_with_two_posts():
    # Given.
    scheduler = Scheduler(":memory:")
    for index in range(2):
        post = Post(filepath=os.getcwd() + '/tests/img/valid_test_img.png', description=f"This is a test description number: {index + 1}.", scheduled_time=datetime.now())
        scheduler.schedule_post(post)

    # When.
    instabot = Instabot(":memory:")

    for url in instabot._lists_of_url:
        instabot._poster._delete_post(url)

    # Then.
    remaining_posts = instabot._scheduler.get_quantity_of_posts()
    assert remaining_posts == 0

def test_functional_instabot_bot_with_multiple_posts_and_one_remaining():
    # Given.
    scheduler = Scheduler(":memory:")
    for index in range(2):
        post = Post(filepath=os.getcwd() + '/tests/img/valid_test_img.png', description=f"This is a test description number: {index + 1}.", scheduled_time=datetime.now())
        scheduler.schedule_post(post)
    post = Post(filepath=os.getcwd() + '/tests/img/valid_test_img.png', description=f"This is a test description number: {index + 1}.", scheduled_time=datetime.now() + timedelta(days=1))
    scheduler.schedule_post(post)

    # When.
    instabot = Instabot(":memory:")

    for url in instabot._lists_of_url:
        instabot._poster._delete_post(url)

    # Then.
    remaining_posts = instabot._scheduler.get_quantity_of_posts()
    assert remaining_posts == 1

