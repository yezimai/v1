#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from op_app.Model.getNavModelClass import GetNavModelClass

class GetNavControllerClass(object):

    # 检测是否有session 构造函数
    def __init__(self, request,data):
        self.request = request
        self.data = data

    def getNav(self):
        user = self.request.user
        print 'user------>',user.username,type(user),type(user.username)
        i_class = GetNavModelClass(user,self.data)
        data = i_class.getNavInfo()
        return data


    ##### 根据ID 获取 有效菜单所有信息  #######
    # def getSystemInfo(self, user):
    #     sql = 'select id,name from show_system where project_id=%s'
    #     try:
    #         data = self.__cursorQuery(sql, [project_id])
    #         ret_list = []
    #         for i in range(len(data)):
    #             dic = {}
    #             dic['id'] = data[i][0]
    #             dic['text'] = data[i][1]
    #             ret_list.append(dic)
    #         return ret_list
    #     except:
    #         return ''
    #
    #
    # # 检测是否有session
    # def is_logined(self):
    #     if self.request.session.get('user') is None:
    #         return False
    #     else:
    #         return True
    #
    # # 登录到首页
    # def index(self):
    #     if self.is_logined() == True:
    #         return render(self.request, 'index.html')
    #     else:
    #         return self.login()
    # # 退出
    # def logout(self):
    #     auth.logout(self.request)
    #     return self.login()
    #
    # # 密码更改
    # def password_change(self):
    #     if self.request.method == 'POST':
    #         form = PasswordChangeForm(user=self.request.user, data=self.request.POST)
    #         if form.is_valid():
    #             form.save()
    #             update_session_auth_hash(self.request, form.user)
    #             return HttpResponseRedirect(reverse('show:password_change_done'))
    #     else:
    #         form = PasswordChangeForm(user=self.request.user)
    #     return render(self.request, 'password_change.html', {'form':form})
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #



