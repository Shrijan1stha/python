import json
filename = "students.json"

def delete(student_id):
    with open(filename, "r+") as fp:
        data = json.load(fp)
        if student_id == 'a':
            data.clear()
        else:
            for student in data:
                if student['id'] == student_id:
                    # print(student)
                    data.remove(student)
                    print(f"Student deleted successfully!")
                    break
            else:
                print("Invalid Student id")
        fp.seek(0)
        fp.truncate()
        json.dump(data, fp, indent=2)
    choice = input("Wish to continue (y/n)? ")
    return True if choice == 'y' else False
