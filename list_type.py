'''一行代码循环读取'''
import random


def read_list(list):
    x=[j for i in list for j in i]
    return x

def get_differ(l1,l2):
    differ=(set(l1)^set(l2))
    return differ

def get_same(l1,l2):
    same = (set(l1) & set(l2))
    return same

def extend_list(l1,l2):
    # l1.extend(l2)
    l1=l1+l2
    return l1


def disorder_list(l):
    random.shuffle(l)
    print(l)

def order_list(list):
    print(sorted(i['age'] for i in list))
    print(sorted(list,key=lambda x:x['age']))












if __name__=="__main__":
    l1=[[1, 2], [3, 4], [5, 6],[0,1]]
    l2=[3,1,2,9,4,5,6]
    d1 = [
        {'name': 'alice', 'age': 38},
        {'name': 'bob', 'age': 18},
        {'name': 'Carl', 'age': 28},
    ]
print(sorted(list,key=lambda x:x['age']))
order_list(d1)