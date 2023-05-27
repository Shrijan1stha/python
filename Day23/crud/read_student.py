import json
filename = "students.json"


def read(student_id):
    with open(filename, "r") as fp:
        # data = fp.read()
        # data = json.loads(data)
        data = json.load(fp)

    student = list(filter(lambda x: x['id'] == student_id, data))
    if student:
        print(student[0])
    else:
        print("Invalid student id")
    choice = input("Wish to continue (y/n)? ")
    return True if choice == 'y' else False

    # for student in data:
    #     if student['id'] == student_id:
    #         print(student)
    #         break
