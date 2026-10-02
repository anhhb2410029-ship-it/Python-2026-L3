class Person:
    def __init__(self, pid, name, dob):
        self._id = pid
        self._name = name
        self._dob = dob

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name