#!/usr/bin/env python
# -*- coding: utf-8 -*-

from op_app.Model.getProjectModelClass import GetProjectModelClass
from op_app.logger.log import runlog

class GetProjectNavControllerClass(object):

    # 检测是否有session 构造函数
    def __init__(self, request):
        self.request = request

    def getProject(self): #获取对应的项目
        user = self.request.user
        #print '------>',user.username,type(user),type(user.username)
        i_class = GetProjectModelClass(user)
        data = i_class.getProjectInfo()
        import json
        runlog.info('getProjectInfo data: %s' % (json.dumps(data, indent=4)))
        return data





