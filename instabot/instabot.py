import sqlite3

class Post:
    def __init__(self, filepath, description, scheduled_time) -> None:
        self.filepath = filepath
        self.description = description
        self.scheduled_time = scheduled_time


class Scheduler:
    def __init__(self, db_path : str) -> None:
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

        command = "CREATE TABLE posts (filepath TEXT, description TEXT, scheduled_time TEXT)"
        self.cursor.execute(command)

        self.connection.commit()

    def schedule_post(self, post : Post) -> Post:
        self.cursor.execute("INSERT INTO posts VALUES (?, ?, ?)", (post.filepath, post.description, post.scheduled_time))

        self.connection.commit()

    def get_all_posts(self) -> list:
        pass

    def get_single_post(self, id : int) -> Post:
        pass

    def get_quantity_of_posts(self) -> int:
        pass

    def update_post(self) -> Post:
        pass

    def delete_post(self, id : int) -> Post:
        pass


class Poster:
    def __init__(self) -> None:
        pass


class Verifier:
    def __init__(self) -> None:
        pass