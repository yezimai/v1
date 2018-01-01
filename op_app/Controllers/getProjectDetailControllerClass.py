#!/usr/bin/env python
# -*- coding: utf-8 -*-

from op_app.Model.getProjectDetailModelClass import GetProjectDetailModelClass

class GetProjectDetailControllerClass(object):

    # 检测是否有session 构造函数
    def __init__(self, request):
        self.request = request

    def getProject(self): #获取对应的项目
        user_id = self.request.user.id
        nav_id = self.request.GET.get('node_id')
        #print('nav_id----->',nav_id)
        #print '------>',user.username,type(user),type(user.username)
        i_class = GetProjectDetailModelClass(nav_id,user_id)

        data = i_class.getProjectInfo()
        return data





