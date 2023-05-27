# List Comprehension
# List comprehension is a short and elegant pythonic way to create a list.

a = []
for i in range(10):
    a.append(i)


print(a)

b = [i for i in range(10)]  # This is a list comprehension
print(b)

b = [i for i in range(20) if i % 2 == 0 ]
print(b)



# Dictionary Comprehension
student = [("name", "Jon"), ("age", 45), ("department", "CS")]
# Without dictionary Comprehension

d = {}
for k, v in student:
    d.update({k: v})
print(d)

# With dictionary Comprehension
d = {k: v for k, v in student}
print(d)

d = {k: v for k, v in student if v != "Jon"}
print(d)


# Trello, Slack, Jira
