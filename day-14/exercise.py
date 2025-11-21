f = open("hello_world.txt", "w")
f.write("Hello, World!")
f.close()

with open("hello_world.txt", "w") as write_file:
    write_file.write("Hello, World!")

with open("hello_world.txt", "a") as append_file:
    append_file.append("/n")