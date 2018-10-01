from collegeuser import CollegeUser
class Professor(CollegeUser):

    def __init__(self, name, gender, subjects):
        super().__init__(name, gender)
        self.subjects = subjects
