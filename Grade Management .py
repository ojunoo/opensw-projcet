  ##################

  # Program Name : Grade Management Program

  # 소프트웨어학부 / 2024042027 / 오주노

  # 작성일 : 2025-04-10

  # 프로그램 설명: 
  # 1. 학생 클래스(Student) 정의
  # 2. 총점, 평균, 학점 계산
  # 3. 입력 (main함수) - 5명의 학생 정보를 입력받고 객체 생성 후 리스트에 저장
  # 4. 등수 계산 (assign_ranks 함수) - 총점이 높은 학생부터 내림차순으로 정렬
  # 5. 표 형태로 출력

  ###################

# Student class to store and calculate student information
class Student:
    def __init__(self, student_id, name, english, c_prog, python):
        self.student_id = student_id  # ID
        self.name = name              # Name
        self.english = english        # English score
        self.c_prog = c_prog          # C Programming score
        self.python = python          # Python score

        self.total = self.calculate_total()      # Total score
        self.average = self.calculate_average()  # Average score
        self.grade = self.calculate_grade()      # Grade (A, B+, etc.)
        self.rank = 0                            # Rank (set later)

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

    # Format for printing student info
    def __str__(self):
        return f"{self.student_id}\t{self.name}\t{self.english}\t{self.c_prog}\t{self.python}\t{self.total}\t{self.average:.2f}\t{self.grade}\t{self.rank}"


# Set rank based on total scores
def assign_ranks(students):
    sorted_students = sorted(students, key=lambda x: x.total, reverse=True)
    for idx, student in enumerate(sorted_students):
        student.rank = idx + 1


# Main function to run the program
def main():
    students = []

    # Input 5 students
    for _ in range(5):
        student_id = input("Student ID: ")
        name = input("Name: ")
        english = int(input("English Score: "))
        c_prog = int(input("C Programming Score: "))
        python = int(input("Python Score: "))
        students.append(Student(student_id, name, english, c_prog, python))
    
    assign_ranks(students)

    # Print results
    print("\nGrade Management System")
    print("=" * 70)
    print("ID\tName\tEnglish\tC\tPython\tTotal\tAvg\tGrade\tRank")
    print("=" * 70)
    for student in students:
        print(student)

# Start the program
if __name__ == "__main__":
    main()
