class MarksException(Exception):
    pass

class Student():
    def __init__(self, name,rollnum,standard,marks,gpa):
        self.name=name
        self.roll_num=rollnum
        self.std=standard
        self.marks=marks
        self.pointer=gpa
        print(f"\nHere's Your Details {self.name},{self.roll_num},{self.std},{self.marks},{self.pointer}")

    def get_marks(self):
        print(f"\n{self.name} your marks is displayed here: {self.marks}")

    def marks_increment(self,increment):
        