import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            print(func)
            return func(*args, **kw)
        return wrapper
    return decorator

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

@log('execute')
def now():
    print('2015-3-25')


def main():
    now()
    print(now.__name__)
    print(now)
    print(log('execute'))
    print(log('execute')(now))

    pass

if __name__ == '__main__':
    main()