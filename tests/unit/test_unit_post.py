import pytest

from instabot.post import Post
from datetime import datetime, timedelta

def test_unit_create_a_valid_post():
    # Given.
    filepath = "../img/valid_test_img.png"
    description = "This is a test description."
    scheduled_time = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S")

    # When.
    post = Post(filepath, description, scheduled_time)

    # Then.
    assert post.filepath == filepath
    assert post.description == description
    assert post.scheduled_time == scheduled_time

def test_unit_create_a_post_with_a_invalid_file_format():
    # Given.
    filepath = "../img/invalid_test_img.pdf"
    description = "This is a test description."
    scheduled_time = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S")

    # When and then.
    with pytest.raises(ValueError):
        post = Post(filepath, description, scheduled_time)

def test_unit_create_a_post_without_a_file():
    # Given.
    filepath = ""
    description = "This is a test description."
    scheduled_time = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S")

    # When and then.
    with pytest.raises(ValueError):
        post = Post(filepath, description, scheduled_time)

def test_unit_create_a_post_with_invalid_file_type():
    # Given.
    filepath = 123
    description = "This is a test description."
    scheduled_time = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S")

    # When and then.
    with pytest.raises(TypeError):
        post = Post(filepath, description, scheduled_time)

def test_unit_create_a_post_with_invalid_description_type():
    # Given.
    filepath = "../img/valid_test_img.png"
    description = 123
    scheduled_time = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S")

    # When and then.
    with pytest.raises(TypeError):
        post = Post(filepath, description, scheduled_time)

def test_unit_create_a_post_with_invalid_scheduled_time_type():
    # Given.
    filepath = "../img/valid_test_img.png"
    description = "This is a test description."
    scheduled_time = 123

    # When and then.
    with pytest.raises(TypeError):
        post = Post(filepath, description, scheduled_time)

def test_unit_create_a_post_with_a_past_date():
    # Given.
    filepath = "../img/valid_test_img.png"
    description = "This is a test description."
    scheduled_time = (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S")

    # When and then.
    with pytest.raises(ValueError):
        post = Post(filepath, description, scheduled_time)
