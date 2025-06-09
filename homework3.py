##################
# Program Name : Grade Management Program (Database Version)
# 소프트웨어학부 / 2024042027 / 오주노
# 작성일 : 2025-06-09
#
# 프로그램 설명:
# - 학생 정보 입력, 저장, 처리 기능 제공
# - 총점, 평균, 학점, 등수 계산
# - 학생 삽입, 삭제, 탐색(학번/이름), 총점 기준 정렬
# - 평균 80점 이상 학생 수 카운트 기능 포함
##################

class Student:
    def __init__(self, student_id, name, english, c_prog, python):
        self.student_id = student_id
        self.name = name
        self.english = english
        self.c_prog = c_prog
        self.python = python

        self.total = self.calculate_total()
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()
        self.rank = 0

    def calculate_total(self):
        return self.english + self.c_prog + self.python

    def calculate_average(self):
        return self.total / 3

    def calculate_grade(self):
        avg = self.average
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B+"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"

    def __str__(self):
        return f"{self.student_id}\t{self.name}\t{self.english}\t{self.c_prog}\t{self.python}\t{self.total}\t{self.average:.2f}\t{self.grade}\t{self.rank}"


# 등수 계산 함수
def assign_ranks(students):
    sorted_students = sorted(students, key=lambda x: x.total, reverse=True)
    for idx, student in enumerate(sorted_students):
        student.rank = idx + 1


# 삽입 함수
def insert_student(students):
    student_id = input("Student ID: ")
    name = input("Name: ")
    english = int(input("English Score: "))
    c_prog = int(input("C Programming Score: "))
    python = int(input("Python Score: "))
    students.append(Student(student_id, name, english, c_prog, python))


# 삭제 함수
def delete_student(students):
    student_id = input("Enter Student ID to delete: ")
    for s in students:
        if s.student_id == student_id:
            students.remove(s)
            print("Student deleted successfully.")
            return
    print("Student not found.")


# 탐색 함수 (학번 또는 이름)
def search_student(students):
    key = input("Enter student ID or Name to search: ")
    found = False
    for s in students:
        if s.student_id == key or s.name == key:
            print("Found:", s)
            found = True
    if not found:
        print("No matching student found.")


# 정렬 함수 (총점 기준 내림차순)
def sort_by_total(students):
    students.sort(key=lambda x: x.total, reverse=True)
    print("Sorted by total score.")


# 평균 80점 이상 학생 수 카운트 함수
def count_high_achievers(students):
    count = sum(1 for s in students if s.average >= 80)
    print(f"Number of students with average >= 80: {count}")


# 출력 함수
def print_all(students):
    print("\nGrade Management System")
    print("=" * 80)
    print("ID\tName\tEnglish\tC\tPython\tTotal\tAvg\tGrade\tRank")
    print("=" * 80)
    for student in students:
        print(student)


# 메인 함수
def main():
    students = []
    while True:
        print("\n==== Menu ====")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Search Student")
        print("4. Sort by Total")
        print("5. Count >= 80 Avg")
        print("6. Show All")
        print("0. Exit")
        choice = input("Select menu: ")

        if choice == '1':
            insert_student(students)
        elif choice == '2':
            delete_student(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            sort_by_total(students)
        elif choice == '5':
            count_high_achievers(students)
        elif choice == '6':
            assign_ranks(students)
            print_all(students)
        elif choice == '0':
            print("Bye~")
            break
        else:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main()
