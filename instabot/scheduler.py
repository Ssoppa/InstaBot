import sqlite3

from post import Post

class Scheduler:
    def __init__(self, db_path : str) -> None:
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

        command = "CREATE TABLE posts (pk_postid integer primary key autoincrement, filepath TEXT, description TEXT, scheduled_time TEXT)"
        self.cursor.execute(command)

        self.connection.commit()
        
    def schedule_post(self, post : Post) -> Post:
        self.cursor.execute("INSERT INTO posts (filepath, description, scheduled_time) VALUES (?, ?, ?)"
                            " RETURNING *", 
                            (post.filepath, post.description, post.scheduled_time))
        row = self.cursor.fetchone()
        
        self.connection.commit()

        new_post = Post(id=row[0], filepath=row[1], description=row[2], scheduled_time=row[3])

        return new_post

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