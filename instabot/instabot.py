import os

from instabot.scheduler import Scheduler
from instabot.poster import Poster


class Instabot:
    def __init__(self, db_path : str) -> None:
        self._lists_of_url = []
        self._scheduler = Scheduler(db_path)
        self._poster = Poster(username=os.getenv('TEST_INSTAGRAM_USERNAME'), password=os.getenv('TEST_INSTAGRAM_PASSWORD'), account_name=os.getenv('TEST_INSTAGRAM_ACCOUNT_NAME'))
        self._check_and_post()

    def _check_and_post(self) -> None:
        list_of_posts = self._scheduler.get_all_posts_to_publish()
        
        for post in list_of_posts:
            url = self._poster.post(post)
            self._lists_of_url.append(url)
            self._scheduler.delete_post(post.id)


