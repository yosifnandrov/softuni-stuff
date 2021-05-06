class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.__students_two = []
        self.__grades_two = []

    def add_student_two(self, nick, grade):
        self.nick = nick
        self.grade = grade
        if len(self.__students_two) < self.__students_count:
            self.__students_two.append(self.nick)
            self.__grades_two.append(self.grade)
    def get_average_grade(self):
        result = sum(self.__grades_two) / len(self.__grades_two)
        return f"{result:.2f}"

    def __repr__(self):
        self.students_as_str = ", ".join(self.__students_two)
        return f"The students in {self.name}: {self.students_as_str}. Average grade: {self.get_average_grade()}"


a_class = Class("11B")
a_class.add_student_two("Peter", 4.80)
a_class.add_student_two("George", 6.00)
a_class.add_student_two("Amy", 3.50)
d_class = Class("12D")
d_class.add_student_two("yosif", 2.00)
d_class.add_student_two("stoqn", 2.20)
d_class.add_student_two("boqn", 5.30)
d_class.add_student_two("gosho", 4.49)

print(Class.__repr__(a_class))
print(Class.__repr__(d_class))


