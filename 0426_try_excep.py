x = 10
#if x > 5:
#    raise Exception('x should not exceed 5. The value of x was {}'.format(x))

assert x >= 5, "x should not exceed 5. The value of x was {}".format(x)

def modify_x():
    assert x <= 5, "x should not exceed 5.The value of x was {}".format(x)
    print('x is being modified')
    print(x)

try:
    x = 50
    modify_x()
except AssertionError as error:
    print(error)
    print('modify_x() function was not successfully executed')
else:
    print("everything looking good")
finally:
    print("We did it!")
    
print("Hello World!")

try:
    x = 10
    modify_x()
    f = open('my_file.txt')
except FileNotFoundError as fnf_error:
    print(fnf_error)
    print('file does not exist')
except AssertionError as error:
    print(error)
    print('modify_x() function was not successfully executed')