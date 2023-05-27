folder_path = "C:\\Users\\shres\\OneDrive\\Desktop\\Practice"


######## Creating files ############
# for i in range(1, 6):
#     fp = open(f"{folder_path}\\file{i}.py", "w")
#     fp.close()


import os
import shutil

os.chdir(folder_path)
# print(os.listdir())


########## Renaming files ##########
# for count, file in enumerate(os.listdir(), start=1):
#     name, ext = os.path.splitext(file)
#     new_name = f"test{count},{ext}"
#     os.rename(file, new_name)


########### Creating a folder ###########
if not os.path.exists("data"):
    os.mkdir("data")


########## Move and copy files ########
# for file in os.listdir():
#     if file == "data":
#         continue
#     # shutil.move(file, "data")
#     shutil.copy(file, "data")


# os.remove("test1,.py")
# os.rmdir("test")
shutil.rmtree("data")  # It recursively deletes the files inside a folder including the folder itself.


