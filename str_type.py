
import re
import time


def capitalize_first(str):
    list_str=re.split(r" |,|!|:|\?",str)
    print(list_str)
    new_str=''
    new_list=[]
    for i in list_str:
        I=i.capitalize()
        new_list.append(I)
        '''1、join的参数不要反了2、list\tuple的值都可以用join连接起来'''
    # return ' '.join(new_list)
    '''#str类型才有title方法'''
    return str.title()

def reverse_str(str):
    '''切片
    [i:j:step]
    i:开始index 空值默认0
    j:结束的index  空值默认最大长度
    '''
    return str[::-1]


def time_print():
    '''time.time() 获取的是时间戳'''
    '''time.localtime() 本地时间'''
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

def strip_blank(str):
    return str.strip()

def code_change(str):
    str.encode("gbk").decode(encoding='utf-8')
    return str





if __name__=="__main__":
    str = ' hello?world:susan ao,welcome to china!nice to c u '
    new_str=code_change(str)
    print(new_str)
