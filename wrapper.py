def cache(func):
    '''
    实现缓存的装饰器
    '''
    data = {}   #缓存数据，key:func_name-args-kwargs    value: func(*args,**kwargs)
    def wrapper(*args,**kwargs):
        key = f'{func.__name__}-{str(args)}-{str(kwargs)}'  #f'{}'str格式化写法
        print(key)
        if key in data:
            result = data.get(key)
            print('cached')
        else:
            result = func(*args,**kwargs)
            data[key] = result
            print('calculated')
        return result
    return wrapper


@cache
def multiply(x,y):
    return x*y

def test(x,y):
    return x*y



if __name__ == '__main__':
    a = multiply(2,3)
    b = multiply(3,4)
    c = multiply(2,3)
    print(a,b,c)