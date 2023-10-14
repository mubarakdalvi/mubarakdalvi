def student_Result():
    n = int(input('Enter Number OF Students: '))
    student_marks = {}
    for _ in range(n):
        student_first_name,student_last_name, *marks = input('Enter Student Name : ').split()
        score= list(map(float,marks))
        full_name = student_first_name + '-' + student_last_name
        print(full_name,score)
        student_marks[(full_name)] = score
    query_full_name = input('Enter Student Name To Get His Avg Score: ').split()
    avg = sum(student_marks[full_name]) / len(student_marks[full_name])
    return query_full_name,'{:.2i}'.format(avg)
print(student_Result())
