from instabot.post import Post
from instabot.scheduler import Scheduler

from datetime import datetime, timedelta

def test_schedule_a_valid_post():
    # Given.
    scheduler = Scheduler(":memory:")
    post = Post(filepath="../img/valid_test_img.png", description="This is a test description.", scheduled_time=(datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S"))

    # When.
    result = scheduler.schedule_post(post)
    scheduler.connection.close()

    # Then.
    assert result.filepath == post.filepath
    assert result.description == post.description
    assert result.scheduled_time == post.scheduled_time

def test_view_all_scheduled_posts():
    # Given.
    scheduler = Scheduler(":memory:")
    number_of_posts = 10
    test_posts = []
    for index in range(number_of_posts):
        post = Post("../img/valid_test_img.png", f"This is a test description number: {index}.", (datetime.now() + timedelta(days=index)).strftime("%d/%m/%Y, %H:%M:%S"))
        test_posts.append(post)
        scheduler.schedule_post(post)

    # When.
    all_posts = scheduler.get_all_posts()
    scheduler.connection.close()

    # Then.
    for index, post in enumerate(all_posts):
        assert post.filepath == test_posts[index].filepath
        assert post.description == test_posts[index].description
        assert post.scheduled_time == test_posts[index].scheduled_time

def test_view_single_scheduled_post():
    # Given.
    scheduler = Scheduler(":memory:")
    post = Post("../img/valid_test_img.png", "This is a test description.", (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S"))
    scheduler.schedule_post(post)

    # When.
    result = scheduler.get_single_post(1)
    scheduler.connection.close()

    # Then.
    assert result.filepath == post.filepath
    assert result.description == post.description
    assert result.scheduled_time == post.scheduled_time

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
    assert result.filepath == new_post.filepath
    assert result.description == new_post.description
    assert result.scheduled_time == new_post.scheduled_time

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
    assert result.filepath == new_post.filepath
    assert result.description == new_post.description
    assert result.scheduled_time == new_post.scheduled_time

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
    assert result.filepath == new_post.filepath
    assert result.description == new_post.description
    assert result.scheduled_time == new_post.scheduled_time


def test_delete_existing_scheduled_post():
    # Given.
    scheduler = Scheduler(":memory:")
    post = Post("../img/valid_test_img.png", "This is a test description.", (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S"))
    scheduler.schedule_post(post)

    # When.
    result = scheduler.delete_post(1)
    scheduler.connection.close()

    # Then.
    assert result.filepath == post.filepath
    assert result.description == post.description
    assert result.scheduled_time == post.scheduled_time
