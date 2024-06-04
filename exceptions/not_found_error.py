class NotFoundError(Exception):
    def __init__(self, entity):
        self.message = f"Error: {entity} not found."
        super().__init__(self.message)