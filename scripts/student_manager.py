import csv

class Student:
    def __init__(self, student_id, name, math, english, science):
        self.id = student_id
        self.name = name
        self.math = int(math)
        self.english = int(english)
        self.science = int(science)

class StudentManager:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.students = []

if __name__ == "__main__":
    manager = StudentManager("../data/students.csv", "../data/students_processed.csv")
def load_data(self):
    with open(self.input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student = Student(row['ID'], row['Name'], row['Math'], row['English'], row['Science'])
            student.total = student.math + student.english + student.science
            student.average = round(student.total / 3, 2)
            self.students.append(student)
