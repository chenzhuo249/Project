
def inside(**in_kwargs):
    def my_decor(func):
        def wrapper(*args, **kwargs):
            print("装饰器执行啦")
            n1 = in_kwargs["num1"]
            n2 = in_kwargs["num2"]
            kwargs["a"] = n1 + n2
            return func(*args, **kwargs)
        return wrapper
    return my_decor

@inside(num1=2, num2=3)
def my_print(a):
    a += 1
    return a

print(my_print(a=1))