class Course:
    def __init__(self, cid, name, credits):
        self._id = cid
        self._name = name
        self._credits = credits

    def get_id(self):
        return self._id
        
    def get_credits(self):
        return self._credits