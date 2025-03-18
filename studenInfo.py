class StudentInfo:
    def __init__(self, first_name, age, quiz_1_score):
        self.first_name = first_name
        self.age = age
        self.quiz_1_score = quiz_1_score
        self.quiz_status = None

    def update_quiz_status(self):
        if self.quiz_1_score is None:
            self.quiz_status = None
        elif self.quiz_1_score >= 5:
            self.quiz_status = True
        else:
            self.quiz_status = False

    def display_info(self):
        print("―" * 20)
        print(f"First Name: {self.first_name}")
        print(f"Age: {self.age}")
        print(f"Quiz 1 Score: {self.quiz_1_score}")
        if self.quiz_status is None:
            print("Quiz Status: None (Not taken)")
        elif self.quiz_status:
            print("Quiz Status: Passed")
        else:
            print("Quiz Status: Failed")
        print("―" * 20)

QUIZ_PASSING_SCORE = 5

first_name = "Jacob Go"
age = 21
quiz_1_score = None

student = StudentInfo(first_name, age, quiz_1_score)
student.display_info()

quiz_1_score = 3  # Integer value
student.quiz_1_score = quiz_1_score
student.update_quiz_status()
student.display_info()

quiz_1_score = 10  # Integer value
student.quiz_1_score = quiz_1_score
student.update_quiz_status()
student.display_info()

quiz_1_score = 9.5  # Float value
student.quiz_1_score = quiz_1_score
student.update_quiz_status()
student.display_info()