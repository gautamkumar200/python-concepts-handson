# --------------------------- example 1 --------------------------------------
def preprocess_wt_arg_and_return(function):
    def wrapper():
        print("started ..")
        function()
        print("End..")
    return wrapper

# 1. x = preprocess_wt_arg_and_return(wt_arg_and_return)
# 2. x()
# above line 1 can be replaced with below decorator @preprocess_wt_arg_and_return
@preprocess_wt_arg_and_return
def wt_arg_and_return():
    print(" This is without argument and without return function .. ")

# --------------------------- example 1 ends  --------------------------------------


# --------------------------- example 2 --------------------------------------
def pre_process_with_arg_and_wt_return_func(function):
    def wrapper(*param, **named_params):
        print(" preprocessing started ....")
        function(*param, **named_params)
        print("preprocessing ends ..")
    return wrapper

# 1. x = pre_process_with_arg_and_wt_return_func(with_arg_and_wt_return_func)
# 2. x("Krish", 2)
# above line 1 can be replaced with below decorator @pre_process_with_arg_and_wt_return_func
@pre_process_with_arg_and_wt_return_func
def with_arg_and_wt_return_func(a, b):
    print(" This is with argument {a} - {b} and without return function ..".format(a=a, b=b))

# --------------------------- example -2 ends ------------------------


# --------------------------- example 3 --------------------------------------
def pre_process_with_arg_and_and_return_func(function):
    def wrapper(*arg, **kwargs):
        print(" started ....")
        val = function(*arg, **kwargs)
        print(" ends ..")
        return val
    return wrapper

# 1. x = pre_process_with_arg_and_and_return_func(with_arg_and_and_return_func)
# 2. x(3, 2)
# above line 1 can be replaced with below decorator @pre_process_with_arg_and_and_return_func
@pre_process_with_arg_and_and_return_func
def with_arg_and_and_return_func(a, b):
    print(" This is with argument {a} - {b} and with return function ..".format(a=a, b=b))
    return a + b


# --------------------------- example -3 ends ------------------------


if __name__ == "__main__":
    # wt_arg_and_return()
    # with_arg_and_wt_return_func("Krish", 2)
    print("function returned valued " + str(with_arg_and_and_return_func(3, 5)))


