import csv

class Student:
    def __init__(self, student_id, name, math, english, science):
        self.id = student_id
        self.name = name
        self.math = int(math)
        self.english = int(english)
        self.science = int(science)
        self.total = self.math + self.english + self.science
        self.average = round(self.total / 3, 2)
        self.rank = None

class StudentManager:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.students = []

    def load_data(self):
        with open(self.input_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                student = Student(row['ID'], row['Name'], row['Math'], row['English'], row['Science'])
                self.students.append(student)

    def assign_ranks(self):
        sorted_students = sorted(self.students, key=lambda s: s.total, reverse=True)
        rank = 1
        for student in sorted_students:
            student.rank = rank
            rank += 1

    def export_data(self):
        fieldnames = ['ID', 'Name', 'Math', 'English', 'Science', 'Total', 'Average', 'Rank']
        with open(self.output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for s in self.students:
                writer.writerow({
                    'ID': s.id,
                    'Name': s.name,
                    'Math': s.math,
                    'English': s.english,
                    'Science': s.science,
                    'Total': s.total,
                    'Average': s.average,
                    'Rank': s.rank
                })

    def filter_by_average(self, threshold):
        return [s for s in self.students if s.average >= threshold]

if __name__ == "__main__":
    manager = StudentManager("../data/students.csv", "../data/students_processed.csv")
    manager.load_data()
    manager.assign_ranks()
    manager.export_data()
    print("Processing complete! Output saved to students_processed.csv")


    high_avg_students = manager.filter_by_average(8)
    print("Students with average >= 8:")
    for s in high_avg_students:
        print(f"{s.name} - Average: {s.average}")
