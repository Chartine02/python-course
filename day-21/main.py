import myfile

print(__name__)

try:
    myfile.get_user_age()
except ValueError:
    print("That's not a valid value for your age!")


# If you have a lot of sub folders you can, use . to enter the folder:
# from folder.subfolder.module import something_in_the_module




