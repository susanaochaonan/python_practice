
def json_travel(data,arry=None,text=1,num=1):
    """
       完成json数据的倍数操作
       :param data: 要修改的内容
       :param array: 列表的修改规则，为None默认不修改
       :param text: 字符串的修改规则，为1默认不修改
       :param num: 整数或者浮点数的修改规则，为1默认不修改
       :return: data_new
       """
    #返回的数据
    data_new=None

    if isinstance(data,int) or isinstance(data,float):
        data_new=num*data

    elif isinstance(data,str):
        data_new=data*text

    elif isinstance(data,list):
        data_new=[]
        for i in data:
            item_new=json_travel(i,arry,text,num)
            if arry is None:
                data_new.append(item_new)
            else:
                if isinstance(arry,int) and arry>=0:
                    for i in range(int):
                        data_new.append(item_new)
                else:
                    data_new=data
    elif isinstance(data,dict):
        data_new=dict()
        for k,v in data.items():
            data_new[k]=json_travel(v,arry,text,num)
            # data[k]=data_new
    else:
        data_new=data
    return data_new