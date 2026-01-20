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
