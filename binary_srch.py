class Student:
    def __init__(self, first_name, last_name, student_code):
        self.first_name = first_name
        self.last_name = last_name
        self.student_code = student_code


def binary_search(students, target_code):
    low = 0
    high = len(students) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_student = students[mid]

        if mid_student.student_code == target_code:
            return mid_student
        elif mid_student.student_code < target_code:
            low = mid + 1
        else:
            high = mid - 1

    return None


def main():
    students = []
    num_stu = int(input('enter num of student--> '))
    for _ in range(num_stu):
        first_name = input("Enter the first name of the student: ")
        last_name = input("Enter the last name of the student: ")
        student_code = int(input("Enter the student code: "))
        print('-------------------------------')
        student = Student(first_name, last_name, student_code)
        students.append(student)

    students.sort(key=lambda s: s.student_code)

    print("Sorted Students:")
    for student in students:
        print(f"First Name: {student.first_name}, Last Name: {student.last_name}, Student Code: {student.student_code}")
        print('-------------------------------------------')

    target_code = int(input("Enter the student code to search: "))
    found_student = binary_search(students, target_code)

    if found_student:
        print(f"Student found - First Name: {found_student.first_name}, Last Name: {found_student.last_name}, Student Code: {found_student.student_code}")
        print('-------------------------')
    else:
        print("Student not found.")


if __name__ == "__main__":
    main()
