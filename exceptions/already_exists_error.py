class AlreadyExistsError(Exception):
    def __init__(self, entity):
        self.message = f"Error: {entity} already exists."
        super().__init__(self.message)
