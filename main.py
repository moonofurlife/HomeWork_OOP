class Student:
    students = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.students.append(self)
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {__averagerating__(self.grades)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return __averagerating__(self.grades) < __averagerating__(other.grades)
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
                
class Lecturer(Mentor):
    lectors = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.lectors.append(self)
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {__averagerating__(self.grades)}'
        return res
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Character!')
            return
        return __averagerating__(self.grades) < __averagerating__(other.grades)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
def __averagerating__(grades):
    for i in grades.values():
        res = sum(i)/len(i)
    return res     
#Создаю два экземпляра класса студента
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ["Git", "Введение"]
student_anna = Student('Anna', "Kulan", "f")
student_anna.courses_in_progress += ["Python", "OOP"]
student_anna.finished_courses += ["Git", "Введение"]
#Создаю два экземпляра класса ревьюера
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'OOP']
some_mentor = Reviewer('Pillipp', 'Krakov')
some_mentor.courses_attached += ['Python']
#Создаю два экземпляра класса лектора
cool_lector = Lecturer('Oleg', 'Some')
cool_lector.courses_attached += ['Python']
some_lector = Lecturer('Katerina', 'Pupkina')
some_lector.courses_attached += ['Python', 'OOP']
#Оценивание лекторов
best_student.rate_hw(cool_lector, 'Python', 10)
best_student.rate_hw(cool_lector, 'Python', 10)
student_anna.rate_hw(some_lector, 'Python', 8)
student_anna.rate_hw(some_lector, 'OOP', 9)
student_anna.rate_hw(some_lector, 'OOP', 10)
#Оценивание студентов
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(student_anna, 'Python', 10)
cool_mentor.rate_hw(student_anna, 'OOP', 15)
cool_mentor.rate_hw(student_anna, 'OOP', 15)

#Вывод ревьюера,лектора и студента
print(cool_mentor)
print()
print(cool_lector)
print()
print(student_anna)
print()
#Сравнивание студентов и лекторов
print(best_student > student_anna)
print(some_lector < cool_lector)
#Функция для нахождения среднего балла по курсу среди студентов
def count_students(user, course):
    a  =[]
    for i in user:
        if course in i.courses_in_progress:
            for g in i.grades.get(course) :
                a.append(g)
    a = sum(a)/len(a)
    return a    

#Функция для нахождения среднего балла по курсу среди лекторов
def count_lectors(user, course):
    a  =[]
    for i in user:
        if course in i.courses_attached:
            for g in i.grades.get(course) :
                a.append(g)
    a = sum(a)/len(a)
    return a  
#Проверка
print(count_students(Student.students, "OOP"))
print(count_lectors(Lecturer.lectors, "Python"))