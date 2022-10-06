import datetime
import os

print('\n')


def getdate():
    return datetime.datetime.now()


def select_name():

    name = {1: 'Devam', 2: 'Rajesh', 3: 'Dipal'}
    # try:
    #     name = {}
    #     while True:
    #         name.append(str(input("Enter name: ")))
    # except:
    #     print(name)

    for key, value in name.items():
        print("Enter ", key, "for", value, '\n', end='')
    xy = int(input('Type here: '))
    print('\n')

    if xy > 3:
        print("\nWrond input! Program terminating!")
        exit()
    else:
        return xy


def select_file_action():

    action = {1: 'Log', 2: 'Retrieve', 3: 'Delete'}

    for key, value in action.items():
        print("Enter ", key, "for", value, '\n', end='')

    x = int(input('Type here: '))
    print('\n')

    if x > 3:
        print("\nWrond input! Program terminating!")
        exit()
    else:
        return x


def select_action():

    b = {1: 'Food', 2: 'Exercise'}

    for key, value in b.items():
        print("Enter ", key, "for", value, '\n', end='')
    y = int(input('Type here: '))
    print('\n')

    if y > 2:
        print("\nWrond input! Program terminating!")
        exit()
    else:
        return y

# def file_delete():
#     t = {1 : 'Delete', 2 : "Don't Delete"}

#     for key, value in t.items():
#         print("Enter ", key, 'for ', value, '\n', end='')
#     h = str(input('Type here: '))
#     print('\n')

#     if t > 2:
#         print("\nWrond input! Program terminating!")
#         exit()
#     else:
#         return h


def action(n, x, y):

    if n == 1 and x == 1 and y == 1:
        a = input("Enter the food: ")

        with open(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\devamfood.txt', 'a') as devamfood:
            devamfood.write(str([str(getdate())]) + ': ' + a + '\n')
            print('successfully logged')

    elif n == 1 and x == 1 and y == 2:
        b = input("Enter the exercise: ")

        with open(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\devamexercise.txt', 'a') as devamexercise:
            devamexercise.write(str([str(getdate())]) + ': ' + b + '\n')
            print('successfully logged')

    elif n == 1 and x == 2 and y == 1:
        try:
            with open(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\devamfood.txt', 'r') as df:
                z = df.read()
                print(z)
        except Exception as e:
            print('File not found!')
            exit()

    elif n == 1 and x == 2 and y == 2:
        try:
            with open(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\devamexercise.txt', 'r') as de:
                y = de.read()
                print(y)
        except Exception as e:
            print('File not found!')
            exit()

    elif n == 1 and x == 3 and y == 1:
        try:
            if os.path.exists(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\devamfood.txt'):
                os.remove(
                    r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\devamfoo.txt')
                print("File successfully deleted!")
            else:
                print('No such file exists')
        except:
            print('No such file exists')

    elif n == 2 and x == 1 and y == 1:
        c = input("Enter the food: ")

        with open(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\rajeshfood.txt', 'a') as rajeshfood:
            rajeshfood.write(str([str(getdate())]) + ': ' + c + '\n')
            print('successfully logged')

    elif n == 2 and x == 1 and y == 2:
        d = input("Enter the exercise: ")

        with open(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\rajeshexercise.txt', 'a') as rajeshexercise:
            rajeshexercise.write(str([str(getdate())]) + ': ' + d + '\n')
            print('successfully logged')

    elif n == 2 and x == 2 and y == 1:
        try:
            with open(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\rajeshfood.txt', 'r') as rf:
                x = rf.read()
                print(x)
        except Exception as e:
            print('File not found!')
            exit()

    elif n == 2 and x == 2 and y == 2:
        try:
            with open(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\rajeshexercise.txt', 'r') as re:
                w = re.read()
                print(w)
        except Exception as e:
            print('File not found!')
            exit()

    elif n == 2 and x == 3 and y == 1:
        try:
            if os.path.exists(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\rajeshfood.txt'):
                os.remove(
                    r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\rajeshfood.txt')
                print("File successfully deleted!")
            else:
                print('No such file exists')
        except:
            print('No such file exists')

    elif n == 2 and x == 3 and y == 2:
        try:
            if os.path.exists(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\rajeshexercise.txt'):
                os.remove(
                    r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\rajeshexercise.txt')
                print("File successfully deleted!")
            else:
                print('No such file exists')
        except:
            print('No such file exists')

    elif n == 3 and x == 1 and y == 1:
        f = input("Enter the food: ")

        with open(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\dipalfood.txt', 'a') as dipalfood:
            dipalfood.write(str([str(getdate())]) + ': ' + f + '\n')
            print('successfully logged')

    elif n == 3 and x == 1 and y == 2:
        g = input("Enter the exercise: ")

        with open(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\dipalexercise.txt', 'a') as dipalexercise:
            dipalexercise.write(str([str(getdate())]) + ': ' + g + '\n')
            print('successfully logged')

    elif n == 3 and x == 2 and y == 1:
        try:
            with open(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\dipalfood.txt', 'r') as dpf:
                v = dpf.read()
                print(v)
        except Exception as j:
            print('File not found!')
            exit()

    elif n == 3 and x == 2 and y == 2:
        try:
            with open(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\dipalexercise.txt', 'r') as dpe:
                u = dpe.read()
                print(u)
        except Exception as k:
            print('File not found!')
            exit()

    elif n == 3 and x == 3 and y == 1:
        try:
            if os.path.exists(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\dipalfood.txt'):
                os.remove(
                    r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\dipalfood.txt')
                print("File successfully deleted!")
            else:
                print('No such file exists')
        except:
            print('No such file exists')

    elif n == 3 and x == 3 and y == 2:
        try:
            if os.path.exists(r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\dipalexercise.txt'):
                os.remove(
                    r'C:\Users\Rajesh\Desktop\Python\python-scripts\health_manage_sys\exercise.txt')
                print("File successfully deleted!")
            else:
                print('No such file exists')
        except:
            print('No such file exists')

    else:
        print('\nWrond input! Program terminating!')
        exit()


getdate()
p = select_name()
q = select_file_action()
r = select_action()
action(p, q, r)
