from time import strftime, localtime, time


def finish_date(func):
    # You have to code here!!
    def wrapper(*args, **kwargs):
        print( strftime(f" inicio function {func.__name__} %d/%m/%Y %H:%M:%S", localtime(time())))
        func(*args, **kwargs)
        print( strftime(f" finalizo la funcion {func.__name__} %d/%m/%Y %H:%M:%S", localtime(time())))
    return wrapper

@finish_date
def palindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


@finish_date
def long_function():
    for _ in range(1000000000):
        pass


def run():
    palindrome('Ana')
    long_function()


if __name__ == '__main__':
    run()
