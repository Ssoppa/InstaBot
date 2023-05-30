import os

from instabot.scheduler import Scheduler
from instabot.post import Post

class CLI:
    def __init__(self) -> None:
        self.database_configuration()

    def database_configuration(self):
        db_path = input("Enter the database path: ")
        if not os.path.isfile(db_path):
            try:
                open(db_path, "x")
            except:
                print("Invalid path! Try again with a valid path.")
                exit()

        self.scheduler = Scheduler(db_path=db_path)
        self.print_main_menu()

    def print_main_menu(self):
        print("\nSelect the desired option.")
        menu = "1 - Schedule a post.\n2 - View scheduled posts.\n3 - Update a scheduled post.\n4 - Delete a scheduled post.\n9 - Exit program."
        choices = ["1", "2", "3", "4", "9"]
        paths = [self.create_post, self.view_posts, self.update_post, self.delete_post, self.exit_program]
        print(menu)
        choice = input()

        while choice not in choices:
            print("\nOption not available, try again.")
            print(menu)
            choice = input()

        paths[choices.index(choice)]()

    def create_post(self):
        filepath = input('Filepath: ')
        description = input('Description: ')
        scheduled_time = input('Time to post (%Y-%m-%d %H:%M:%S): ')

        try:
            post = Post(filepath=filepath, description=description, scheduled_time=scheduled_time)
            self.scheduler.schedule_post(post)
            print("Post scheduled!")
        except Exception as e:
            print(e)
            self.create_post()
            return

        self.print_main_menu()

    def view_posts(self):
        all_posts = self.scheduler.get_all_posts()
        for post in all_posts:
            print(post)

        self.print_main_menu()

    def update_post(self):
        post_id = input('Post id: ')

        try:
            post_id = int(post_id)
            selected_post = self.scheduler.get_single_post(post_id)
            print(selected_post)
        except Exception as e:
            print(e)
            self.update_post()
            return
        
        filepath = input('Filepath: ')
        description = input('Description: ')
        scheduled_time = input('Time to post (%Y-%m-%d %H:%M:%S): ')

        try:
            updated_post = Post(id=selected_post.id, filepath=filepath, description=description, scheduled_time=scheduled_time)
            self.scheduler.update_post(updated_post)
            print("Post updated!")
        except Exception as e:
            print(e)
            self.update_post()
            return

        self.print_main_menu()

    def delete_post(self):
        post_id = input('Post id: ')

        try:
            post_id = int(post_id)
            deleted_post = self.scheduler.delete_post(post_id)
            print("Deleted the following post: ", deleted_post)
        except Exception as e:
            print(e)
            self.delete_post()
            return

        self.print_main_menu()

    def exit_program(self):
        print("See you next time.")
        exit()

CLI()