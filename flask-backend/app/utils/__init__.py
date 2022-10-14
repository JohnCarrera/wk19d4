class ValidationError(Exception):

    def __init__(self, title, message='Validation Error', status=422):
        Exception.__init__(self)
        self.title = title
        self.message = message
        self.status = status

    def to_dict(self):
        rv = dict()
        rv['title'] = self.title
        rv['message'] = self.message
        rv['status'] = self.status
        return rv
