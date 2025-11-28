def get_grades():
    try:
        grades = input('Add grades separated by a comma: ')
        grades_list = [int(grd) for grd in grades.split(',')]

    except ValueError:
        print('please add comma separated grades')

    else:
        print(grades_list)

# get_grades()

def read_file():
    try:
        with open('data_set.txt', 'r') as data:
            print(data.read())

    except FileNotFoundError:
        print('File does not exist')

read_file()