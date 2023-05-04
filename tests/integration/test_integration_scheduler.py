import sqlite3

from instabot.instabot import Scheduler, Post

def test_schedule_a_valid_post():
    # Given.
    scheduler = Scheduler(":memory:")
    scheduler.cursor.execute("SELECT COUNT(*) from posts")
    count = scheduler.cursor.fetchone()[0]

    # When.
    post = Post("", "", "")
    scheduler.schedule_post(post)

    # Then.
    scheduler.cursor.execute("SELECT COUNT(*) from posts")
    result = scheduler.cursor.fetchone()[0]
    scheduler.connection.close()
    assert result == count + 1

def test_view_all_scheduled_posts():
    # Given.
    # When.
    # Then.
    pass

def test_view_single_scheduled_post():
    # Given.
    # When.
    # Then.
    pass

def test_view_non_existent_single_scheduled_post():
    # Given.
    # When.
    # Then.
    pass

def test_update_description_single_scheduled_post():
    # Given.
    # When.
    # Then.
    pass

def test_update_date_single_scheduled_post():
    # Given.
    # When.
    # Then.
    pass

def test_update_file_single_scheduled_post():
    # Given.
    # When.
    # Then.
    pass


def test_delete_existing_scheduled_post():
    # Given.
    # When.
    # Then.
    pass

def test_delete_non_existing_scheduled_post():
    # Given.
    # When.
    # Then.
    pass