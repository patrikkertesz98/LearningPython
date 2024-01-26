try:
    print(variable)
except NameError:
    print("Exception occured(Name Error), variable not defined")
except: 
    print("Unknown error")

try: 
    f = open('nonexistent file')
except FileNotFoundError:
    print('The file doesn\'t exist')
except:
    print('Bro IDK')
###############################
attempts = 0

while True:
    try:
        input_var = input("Please enter a number: ")
        input_var = int(input_var)
        break
    except ValueError:
        attempts += 1

        if attempts < 3:
            print("How many times do you have to fail this simple task?")
        else:
            print("Ok then string it is....")
            input_var = str(input_var)
            break
###################################
try: 
    a = str(5)
    b = str('Hello')
    c = int('World')
    d = a + b + c
except TypeError:
    print('TypeError was thrown')
except NameError:
    print('NameError was thrown')
except ValueError:
    print('ValueError was thrown')
###################################

# number = int(input("Enter a number: "))

# if number > 5:
#     raise Exception('The number should not exceed 5. Your input is: {}'.format(number))

###################################
def printing(string):
    print(string)

number = int(input("Enter a number: "))


try:
    if number > 5:
        raise Exception('The number should not exceed 5. Your input is: {}'.format(number))
except Exception as error:
    printing('caught this error: ' + repr(error))
