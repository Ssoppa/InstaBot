import sqlite3

from instabot.post import Post


class Scheduler:
    def __init__(self, db_path : str) -> None:
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

        command = "CREATE TABLE IF NOT EXISTS posts (pk_postid integer primary key autoincrement, filepath TEXT, description TEXT, scheduled_time timestamp)"
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
        self.cursor.execute("SELECT * FROM posts")
        result = self.cursor.fetchall()
        all_posts = []

        for post in result:
            single_post = Post(id=post[0], filepath=post[1], description=post[2], scheduled_time=post[3], already_scheduled = True)
            all_posts.append(single_post)

        return all_posts
    
    def get_all_posts_to_publish(self) -> list:
        self.cursor.execute("SELECT * FROM posts WHERE scheduled_time < DATETIME('now')")
        result = self.cursor.fetchall()
        all_posts = []

        for post in result:
            single_post = Post(id=post[0], filepath=post[1], description=post[2], scheduled_time=post[3], already_scheduled = True)
            all_posts.append(single_post)

        return all_posts

    def get_single_post(self, id : int) -> Post:
        self.cursor.execute("SELECT * FROM posts WHERE pk_postid = ?", (id,))
        result = self.cursor.fetchone()

        if result == None:
            raise ValueError("A post with the provided id was not found!")
        
        single_post = Post(id=result[0], filepath=result[1], description=result[2], scheduled_time=result[3])
        
        return single_post

    def get_quantity_of_posts(self) -> int:
        self.cursor.execute("SELECT COUNT(*) FROM posts")
        count = self.cursor.fetchone()[0]
        
        return count

    def update_post(self, updated_post : Post) -> Post:
        self.cursor.execute("UPDATE posts SET filepath = ?, description = ?, scheduled_time = ? WHERE pk_postid = ?"
                            " RETURNING *", 
                            (updated_post.filepath, updated_post.description, updated_post.scheduled_time, updated_post.id))
        row = self.cursor.fetchone()
        
        self.connection.commit()

        new_post = Post(id=row[0], filepath=row[1], description=row[2], scheduled_time=row[3], already_scheduled = True)

        return new_post

    def delete_post(self, id : int) -> Post:
        self.cursor.execute("DELETE FROM posts WHERE pk_postid = ? RETURNING *", (id,))
        result = self.cursor.fetchone()
        
        self.connection.commit()

        if result == None:
            raise ValueError("A post with the provided id was not found!")

        deleted_post = Post(id=result[0], filepath=result[1], description=result[2], scheduled_time=result[3], already_scheduled = True)

        return deleted_post