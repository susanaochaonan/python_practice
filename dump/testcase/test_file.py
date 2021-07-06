import json
import pytest

from testcase.json_traval import json_travel


def test_file():
    # f=open(r"F:\a.json",'r',encoding='utf-8')
    # data=f.read()
    data ={'data':{'items':[{'market':{"status_id": 7},'quote':{'name':'卡点'}},{'market':{"status_id": 7},'quote':{'name':'卡点'}}]}}
    new_json=json_travel(data,num=2,text=2)
    print(new_json)

