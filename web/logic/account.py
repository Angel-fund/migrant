# -*- coding:utf-8 -*- 
"""
    account logic (curd)
    author comger@gmail.com
"""
from kpages import not_empty,get_context,mongo_conv
from kpages.model import *
from utility import m_update,m_del,m_page,m_exists,m_info,BaseModel

TName = 'account'
Tb = lambda :get_context().get_mongo()[TName]

INIT, ACTIVATED, IDENTIFIED = range(3)

class AccountModel(BaseModel):
    username = CharField(required=True)
    password = CharField(required=True)
    city = CharField()


def add(username, password, city=None, **kwargs):
    try:
        not_empty(username, password)
        r = m_exists(TName, username=username)
        if not r:
            val = dict(username=username, password=password, city=city)
            val.update(kwargs)
            _id = Tb().insert(val, saft=True)
            val['_id'] = str(_id)
            return True, val
        else:
            return False, 'EXISTS'
    except ValueError:
        return False, 'NO_EMPTY'


def reset_pwd(uid, old_password, new_password):
    try:
        not_empty(uid, old_password, new_password)
        _id = ObjectId(uid)
        kwargs = dict(_id=_id, password=old_password)
        valid = m_exists(TName, **kwargs)
        if valid:
            Tb().update(kwargs, {'$set': {'password': new_password}})
            return True, 'OK'
        else:
            return False, 'INVALIDED'
    except ValueError:
        return False, 'NO_EMPTY'


def login(username,password,isadmin = None):
    try:
        not_empty(username,password)
        cond = dict(username=username,password=password)
        if isadmin:
            cond.update(isadmin = isadmin)

        r = m_exists(TName,**cond)
        if r:
            r = mongo_conv(r)
            return True, r
        else:
            return False,None
    except Exception as e:
        return False,e.message


def auth_login(site,otherid,name,**kwargs):
    try:
        not_empty(site,otherid,name)
        r = m_exists(TName,site=site,otherid=otherid,name=name)
        if r:
            r = mongo_conv(r)
            return True,r
        else:
            val = dict(site=site,otherid=otherid,name=name)
            _id = Tb().insert(val,saft=True)
            val['_id'] = str(_id)
            return True,val
    except Exception as e:
        return False,e.message


def page(since,**kwargs):
    return m_page(TName,since=since,**kwargs)

def info(_id):
    return m_info(TName,_id)


def conv_user(obj):
    if isinstance(obj, (list, tuple)):
        for d in obj:
            conv_user(d)

    elif isinstance(obj,dict):
        r,v = info(obj['uid'])
        if r:
            obj['username'] = v['username']
        else:
            obj['username'] = 'deleted user'
