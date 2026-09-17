
class StudentManagement:
    def __init__(self, name, age, course):
        self.name = name
        self.age = int(age)
        self.course = course
        self.__marks = {"English": 0,
                        "Maths": 0,
                        "Science": 0,}

        self.__average = 0

    def english_marks(self, english):
        if english >=0:
            self.__marks["English"] = english
        else:
            print("Negative marks can't be given to students")
        return self.__marks

    def maths_marks(self, maths):
            if maths >=0:
                self.__marks["Maths"] = maths
            else:
                print("Negative marks can't be given to students")
            return self.__marks

    def science_marks(self, science):
            if science >=0:
                self.__marks["Science"] = science
            else:
                print("Negative marks can't be given to students")
            return self.__marks

    def average_marks(self):
        self.__average = (self.__marks["English"] + self.__marks["Maths"] + self.__marks["Science"]) / 3

        return round(self.__average, 2)

    def check_result(self):
         if self.__average >= 40:
              return "(Pass)"
         else:
              return "(Fail)"

    def info(self):
        marks_text = ""
        for subject, score in self.__marks.items():
            marks_text += f"{subject} : {score}\n"

        marks_text = marks_text.rstrip()
        
        return f"""
================================
        {self.name}'s Info
================================
Name: {self.name}
Age: {self.age}
Course: {self.course}

Marks:-
{marks_text}

Average: {self.average_marks()} => {self.check_result()}
"""

# =========================
# TEST CODE
# =========================

# 1st student
student1 = StudentManagement("Utkarsh", 22, "BCA")

student1.english_marks(50)
student1.maths_marks(30)
student1.science_marks(70)

print(student1.info())

# 2nd student
student2 = StudentManagement("Rekzyl", 25, "BCA-NEWOL")

student2.english_marks(70)
student2.maths_marks(65)
student2.science_marks(80)

print(student2.info())