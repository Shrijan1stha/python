import json
filename = "students.json"


def update(student_id, to_change, changed_value):
    with open(filename, "r+") as fp:
        data = json.load(fp)
        for student in data:
            if student['id'] == student_id:
                student[to_change] = changed_value
                break
        fp.seek(0)
        fp.write(json.dumps(data, indent=2))

        # json.dump(data, fp, indent=2)
    print("Student Updated Successfully !!")
    choice = input("Wish to continue (y/n)? ")
    return True if choice == 'y' else False

