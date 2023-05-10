import pytest

from instabot.post import Post
from instabot.scheduler import Scheduler
from datetime import datetime, timedelta

def test_schedule_a_valid_post():
    # Given.
    scheduler = Scheduler(":memory:")
    post = Post("../img/valid_test_img.png", "This is a test description.", (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S"))
    count = scheduler.get_quantity_of_posts()

    # When.
    scheduler.schedule_post(post)

    # Then.
    result = scheduler.get_quantity_of_posts()
    scheduler.connection.close()
    assert result == count + 1

def test_view_all_scheduled_posts():
    # Given.
    scheduler = Scheduler(":memory:")
    number_of_posts = 10
    for index in range(number_of_posts):
        post = Post("../img/valid_test_img.png", f"This is a test description number: {index}.", (datetime.now() + timedelta(days=index)).strftime("%d/%m/%Y, %H:%M:%S"))
        scheduler.schedule_post(post)

    # When.
    all_posts = scheduler.get_all_posts()
    scheduler.connection.close()

    # Then.
    assert len(all_posts) == number_of_posts

def test_view_single_scheduled_post():
    # Given.
    scheduler = Scheduler(":memory:")
    post = Post("../img/valid_test_img.png", "This is a test description.", (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S"))
    scheduler.schedule_post(post)

    # When.
    result = scheduler.get_single_post(1)
    scheduler.connection.close()

    # Then.
    assert type(result) == Post

def test_view_non_existent_single_scheduled_post():
    # Given.
    scheduler = Scheduler(":memory:")

    # When and Then
    with pytest.raises(ValueError):
        scheduler.get_single_post(1)

    scheduler.connection.close()

def test_update_description_single_scheduled_post():
    # Given.
    scheduler = Scheduler(":memory:")
    post = Post("../img/valid_test_img.png", "This is a test description.", (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S"))
    scheduler.schedule_post(post)

    # When.
    new_post = scheduler.get_single_post(1)
    new_post.description = "This is a new description."
    result = scheduler.update_post(Post)
    scheduler.connection.close()

    # Then.
    assert type(result) == Post

def test_update_date_single_scheduled_post():
    # Given.
    scheduler = Scheduler(":memory:")
    post = Post("../img/valid_test_img.png", "This is a test description.", (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S"))
    scheduler.schedule_post(post)

    # When.
    new_post = scheduler.get_single_post(1)
    new_post.scheduled_time = (datetime.now() + timedelta(days=2)).strftime("%d/%m/%Y, %H:%M:%S")
    result = scheduler.update_post(Post)
    scheduler.connection.close()

    # Then.
    assert type(result) == Post

def test_update_file_single_scheduled_post():
    # Given.
    scheduler = Scheduler(":memory:")
    post = Post("../img/valid_test_img.png", "This is a test description.", (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S"))
    scheduler.schedule_post(post)

    # When.
    new_post = scheduler.get_single_post(1)
    new_post.filepath = "../img/valid_test_img2.png"
    result = scheduler.update_post(Post)
    scheduler.connection.close()

    # Then.
    assert type(result) == Post


def test_delete_existing_scheduled_post():
    # Given.
    scheduler = Scheduler(":memory:")
    post = Post("../img/valid_test_img.png", "This is a test description.", (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S"))
    scheduler.schedule_post(post)

    # When.
    result = scheduler.delete_post(1)
    scheduler.connection.close()

    # Then.
    assert type(result) == Post

def test_delete_non_existing_scheduled_post():
    # Given.
    scheduler = Scheduler(":memory:")

    # When and Then
    with pytest.raises(ValueError):
        scheduler.delete_post(1)

    scheduler.connection.close()