class CollegeUser:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def getdetails(self):
        return 'Name:{0}\nGender:{1}'.format(self.name, self.gender)
