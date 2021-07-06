import json


def odd_genarate():
    print(list(filter(lambda x: x % 2==0, range(1,101))))
    print(list(filter(lambda x: x % 2, range(1, 101))))
    print(list(range(2, 101, 2)))


def json_translate():
    dic = {'a': 123, 'b': "456", 'c': "liming"}
    json_str = json.dumps(dic)
    print(json_str)
    dic2 = json.loads(json_str)
    print(dic2)

def log_decrate(info):
    def wrapper(func):
        def inner_wrapper(*args,**kwargs):
            try:
                print("level", info)
                func(*args, **kwargs)
            except Exception as e:
                print("name",func.__name__)
        return inner_wrapper
    return wrapper









if __name__=="__main__":


    # @log_decrate("debug")
    # def foo(a, b, c):
    #     s=a + b + c
    #     print(s==10)
    #
    #
    # foo(1, 2, 3)

    json_translate()