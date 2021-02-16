import inspect


def exec_func(func_to_exec, *args):
    save_func = func_to_exec
    save_args = args
    return save_func(*save_args)


def my_add(a, b):
    return a+b


print(my_add(2, 3))
print(exec_func(my_add, 2, 3))
print(inspect.isfunction(my_add))

