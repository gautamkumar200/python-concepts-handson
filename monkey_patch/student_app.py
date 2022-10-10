from student import *


def monkey_func(self):
    print(" monkey function called")
    return 20


if __name__ == "__main__":
    Student.get_roll = monkey_func
    student = Student()
    print(student.get_roll())
