# -*- coding:utf-8 -*- 
"""
    author comger@gmail.com
    migrant 前端展示公共页面
"""
from kpages import url
from utility import BaseHandler

@url(r'/?')
class Index(BaseHandler):
    def get(self):
        self.render('action/index.html')

@url(r'/login?')
class Login(BaseHandler):
    def get(self):
        self.render('action/login.html')


@url(r'/profile?')
class Profile(BaseHandler):
    def get(self):
        self.render('action/profile.html')

@url(r'/setpwd?')
class SetPwd(BaseHandler):
    def get(self):
        print self.request.uri
        self.render('action/setpwd.html')
