from collegeuser import CollegeUser
from student_oop import Student

class PhotoSession:

    def takephoto(collegeuser):
        # collegeuser parameter passed is an instance of CollegeUser
        # Student
        # Professor
        # Librarian or any sub class of CollegeUser in the future
        if isinstance(collegeuser, CollegeUser):
            if isinstance(collegeuser, Student):
                print('Photo taken of {0} with roll {1}'.format(collegeuser.name, collegeuser.roll))
            else:
                print('Photo taken of {0}'.format(collegeuser.name))
        else:
            print('Please pass in someone who is a college user')
