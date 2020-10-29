average_grade = int(input("average_grade:"))
recommended_by_tutor = bool(input("recommended tutor?"))
finished_course = bool(input("finished course?"))
introductory_couse = int(input("introdutory_course:"))

enroll_student = ((average_grade >= 40 and recommended_by_tutor) or (finished_course and introductory_couse > 85))

print(enroll_student)
