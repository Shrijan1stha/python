from Day15.decorators import decorate_me, to_upper, exec_time, login_required
# @decorate_me
# def message():
#     print("Hello World")
#
# # nested_function_of_decorator = decorate_me(message)
# message()
#
# @to_upper
# def next_message():
#     return "Python is awosome"
# next_message()


# @exec_time
# def test_fxn():
#     for i in range(100000000):
#         pass
#     return "Done !!"
#
# print(test_fxn())


@login_required
def get_message():
    return "Learning at broadway !"

print(get_message())