# WAP to read the students csv and creata a new csv file where student age is greater tha 25.
import csv

# filename = "student.csv"
# filename1 = "new_student.csv"
# with open(filename, "r") as cr:
#     csv_read = csv.DictReader(cr)
#     # print(csv_read)
#     # field_names = filename1[0].keys()
#     # csv_write = csv.DictWriter(cr, fieldnames=field_names)
#     # csv_write.writeheader()
#     # for data in csv_read:
#     #     if data["age"] > 25:
#     #         csv_write.writerow(data)
#
# with open(filename1, "w") as cw:
#     # field_names = dict(filename1[0]).keys()
#     field_names = dict(filename1[0]).keys()
#     csv_write = csv.DictWriter(cw, fieldnames=field_names)
#     csv_write.writeheader()
#     for data in csv_read:
#         print(data)
#         # if data["age"] > 25:
        #     csv_write.writerow(data)


with open("student.csv", "r") as cr:
    csv_reader = csv.DictReader(cr)
    # fieldnames = csv_reader[0]

    with open("new_students.csv", "w") as cw:
        field_names = ["id", "name", "age"]
        csv_writer = csv.DictWriter(cw, fieldnames=field_names)
        csv_writer.writeheader()
        for each_line in csv_reader:
            if each_line["age"] > "25":
                csv_writer.writerow(each_line)