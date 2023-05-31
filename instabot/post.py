import os
import mimetypes

from datetime import datetime


class Post:
    def __init__(self, *args, **kwargs) -> None:
        self.id = kwargs.get('id', None)
        self.filepath = kwargs.get('filepath', None)
        self.description = kwargs.get('description', None)
        self.scheduled_time = kwargs.get('scheduled_time', None)
        self.already_scheduled = kwargs.get('already_scheduled', False)

        self._validate_data()

    def _validate_data(self) -> None:
        if self.already_scheduled:
            return

        # Check the file
        if type(self.filepath) is not str:
            raise TypeError("filepath argument must be a string!")
        if not os.path.isfile(self.filepath):
            raise ValueError("filepath argument must be a file!")
        mimestart = mimetypes.guess_type(self.filepath)[0]

        if mimestart != None:
            mimestart = mimestart.split('/')[0]

            if mimestart not in ['video', 'image']:
                raise ValueError("filepath argument must be an image file!")
        else:
            raise ValueError("filepath argument must be an image file!")
        if not self.filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.mp4', '.mov', '.3gp', '.aac', '.avi', '.mp2')):
            raise ValueError("Accepted formats are: png, jpg, jpeg, bmpg, gif, mp4, mov, 3gp, aac, avi, and mp2. ")
        
        # Check the description
        if type(self.description) is not str:
            raise TypeError("description argument must be a string!")

        # Check the scheduled date
        if type(self.scheduled_time) is not datetime:
            try:
                self.scheduled_time = datetime.strptime(self.scheduled_time, '%Y-%m-%d %H:%M:%S')
            except:
                raise TypeError("scheduled_time argument must be a datetime.datetime!")
        if self.scheduled_time < datetime.now():
            raise ValueError("scheduled_time argument must be in at least in the present.")
        self.already_scheduled = True

    def __str__(self) -> str:
        return f"ID: {self.id}. Filepath: {self.filepath}. Description: {self.description}. Scheduled time: {self.scheduled_time}"