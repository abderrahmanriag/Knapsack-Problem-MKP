class item:
    def __init__(self, resource, value):
        self.resource=resource
        self.value=value

    def show(self):
        print(self.resource, '# ', self.value)
