class Post:
    def __init__(self, *args, **kwargs) -> None:
        self.id = kwargs.get('id', None)
        self.filepath = kwargs.get('filepath', None)
        self.description = kwargs.get('description', None)
        self.scheduled_time = kwargs.get('scheduled_time', None)

    def _validate_data():
        pass