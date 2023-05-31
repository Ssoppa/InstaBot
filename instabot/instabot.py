import os

from instabot.scheduler import Scheduler
from instabot.poster import Poster


class Instabot:
    def __init__(self, *args, **kwargs) -> None:
        self._db_path = kwargs.get('db_path', None)
        self._username = kwargs.get('username', None)
        self._account_name = kwargs.get('account_name', None)
        self._password = kwargs.get('password', None)

        self._validade_data()

        self._lists_of_url = []
        self._scheduler = Scheduler(self._db_path)
        self._poster = Poster(username=self._username, password=self._password, account_name=self._account_name)
        self._check_and_post()

    def _validade_data(self):
        if self._db_path is None:
            raise ValueError("database path argument is required!")
        if self._username is None:
            raise ValueError("username argument is required!")
        if self._account_name is None:
            raise ValueError("account_name argument is required!")
        if self._password is None:
            raise ValueError("password argument is required!")
        
        if type(self._db_path) is not str:
            raise TypeError("database path argument must be a string!")
        if type(self._username) is not str:
            raise TypeError("username argument must be a string!")
        if type(self._account_name) is not str:
            raise TypeError("account_name argument must be a string!")
        if type(self._password) is not str:
            raise TypeError("password argument must be a string!")
        
        if not os.path.isfile(self._db_path):
            raise ValueError("database argument must be a file!")

    def _check_and_post(self) -> None:
        list_of_posts = self._scheduler.get_all_posts_to_publish()
        
        for post in list_of_posts:
            url = self._poster.post(post)
            self._lists_of_url.append(url)
            self._scheduler.delete_post(post.id)


