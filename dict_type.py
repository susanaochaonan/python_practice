from itertools import islice
import json
from datetime import datetime
from datetime import timedelta
from datetime import date
def dict_hebing(a,b):
    a.update(b)
    print({**a,**b})
    return a

def create_dict(t1,t2):
    print(dict(zip(t1,t2)))

#交换键值对
def exchange_kv(dic):
    # print({v:k for k,v in dic.items()})
    print(dict(zip(dic.keys(),dic.values())))

#生成器类的对象实现切片
def slice_iter():
    gen = iter(range(10))
    for i in islice(gen, 0, 4):
        print(i)


class DateToJson(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def datetime_delay(n):
    now=datetime.now()
    new_time=now+timedelta(n)
    new_time=format(new_time,'%Y-%m-%d %H:%M:%S')
    print(new_time )

def mul_operate(num):
    def operate(a):
        return num*a
    return operate

def deco(f):
    def wrapper(*args):
        print(args)
        print(args * 2)
        return f(*args)

    return wrapper



if __name__=="__main__":
    a = {"A": 1, "B": 2}
    b = {"C": 3, "D": 4}
    t1=(1,2,3,4)
    t2=('a','b','c','d')
    s = {"A": 1, "B": 2}
    d = {'name': 'cxa', 'date': datetime.now()}
    # print(json.dumps(d,cls=DateToJson))
    # print(json.dumps("中国"))
    # print(json.dumps("中国",ensure_ascii=False))
    datetime_delay(2)

print((mul_operate(5))(2))

