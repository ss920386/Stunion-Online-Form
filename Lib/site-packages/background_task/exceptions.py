
class BackgroundTaskError(Exception):
    def __init__(self, message, errors=None):
        super(Exception, self).__init__(message)
        self.errors = errors