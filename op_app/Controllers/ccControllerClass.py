#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    总控制器
'''

from show.Model.projectModelClass import *
from show.Model.systemModelClass import *
from show.Model.appModelClass import *
from show.Model.hostModelClass import *
from show.Model.databaseModelClass import *
from show.Model.userModelClass import *

# from show.Model.navModelClass import *


class CcControllerClass(object):

    # def getNavPageInfo(self, request):
    #     m_project = ProjectModelClass()
    #     data = m_project.getProjectInfo()
    #     m_system = SystemModelClass()
    #     m_app = AppModelClass()
    #     m_db = databaseModeClass()
    #     u_md = UserModelClass()
    #     user = request.session.get('user')
    #     uid=u_md.getUid(user)
    #     for i in range(len(data)):
    #         print 'ab',i
    #
    #         data[i]['children'] = []
    #         data[i]['children'] = m_system.getSystemInfo(data[i]['id'])  # 获取项目对应的系统信息
    #         if len(data[i]['children']) == 0:
    #             data[i].clear()
    #             continue
    #         for j in range(len(data[i]['children'])):
    #             data[i]['children'][j]['children'] = []
    #             data[i]['children'][j]['children'] = m_app.getAppInfo(data[i]['children'][j]['id'])
    #             if len(data[i]['children'][j]['children']) == 0:
    #                 # del data[i]['children']
    #                 # del data[i]['text']
    #                 # del data[i]['id']
    #                 data[i]['children'][j].clear()
    #                 continue
    #             for k in range(len(data[i]['children'][j]['children'])):
    #                 data[i]['children'][j]['children'][k]['children'] = []
    #                 data[i]['children'][j]['children'][k]['children'] = \
    #                     m_db.getDbInfo(data[i]['children'][j]['children'][k]['id'],uid)
    #                 if len(data[i]['children'][j]['children'][k]['children'])==0:
    #                     data[i]['children'][j]['children'][k].clear()
    #                     continue
    #                 pass
    #             pass
    #         pass
    #     print data
    #
    #     retlist = []
    #     for item in data:
    #         if item:
    #             retlist.append(item)
    #         else:
    #             continue
    #
    #     # retdata = []
    #     # for item in data:
    #     #     for ite in item['children']:
    #     #         for it in ite['children']:
    #     #             if len(it['children']) == 0:
    #     #                  it.pop('children')
    #     #                  ite.pop('children')
    #     #                  item.pop('children')
    #     #             retdata.append(item)
    #
    #     print retlist
    #     return retlist

    def getNavPageInfo(self, request):
        m_project = ProjectModelClass()
        data = m_project.getProjectInfo()
        m_system = SystemModelClass()
        m_app = AppModelClass()
        m_db = databaseModeClass()
        m_host = HostModelClass()
        u_md = UserModelClass()
        user = request.session.get('user')
        uid = u_md.getUid(user)
        for i in range(len(data)):
            data[i]['children'] = []
            data[i]['children'] = m_system.getSystemInfo(data[i]['id'])  # 获取项目对应的系统信息
            print data[i]['children']
            for j in range(len(data[i]['children'])):
                data[i]['children'][j]['children'] = []
                data[i]['children'][j]['children'] = m_app.getAppInfo(data[i]['children'][j]['id'])
                for k in range(len(data[i]['children'][j]['children'])):
                    data[i]['children'][j]['children'][k]['children'] = []
                    data[i]['children'][j]['children'][k]['children'] = \
                        m_db.getDbInfo(data[i]['children'][j]['children'][k]['id'],uid) + \
                        m_host.getHostInfo(data[i]['children'][j]['children'][k]['id'],uid)
                    pass
                pass
            pass
        print "alldata:", data
        # return data

        for i in range(len(data)):
            if data[i].has_key('children'):  # 一层
                if len(data[i]['children']) == 0:
                    data[i].clear()
                else:
                    for j in range(len(data[i]['children'])):
                        if data[i]['children'][j].has_key('children'):
                            if len(data[i]['children'][j]['children']) == 0:  # 二层
                                data[i]['children'][j].clear()
                            else:
                                for k in range(len(data[i]['children'][j]['children'])):
                                    if data[i]['children'][j]['children'][k].has_key('children'):
                                        if len(data[i]['children'][j]['children'][k]['children']) == 0:  # 三层
                                            data[i]['children'][j]['children'][k].clear()
                                        else:
                                            for l in range(len(data[i]['children'][j]['children'][k]['children'])):
                                                if data[i]['children'][j]['children'][k]['children'][l].has_key(
                                                        'children'):
                                                    if len(data[i]['children'][j]['children'][k]['children'][l][
                                                               'children']) == 0:  # 四层
                                                        data[i]['children'][j]['children'][k]['children'][
                                                            l].clear()  # 清除数据
                                            for l_2 in range(
                                                    len(data[i]['children'][j]['children'][k]['children'])):  # 循环清除了的数据
                                                if data[i]['children'][j]['children'][k]['children'][l_2].has_key(
                                                        'children'):
                                                    flag_1 = 0
                                                    for e_data in \
                                                    data[i]['children'][j]['children'][k]['children'][l_2]['children']:
                                                        if e_data != {}:
                                                            flag_1 = 1
                                                            break
                                                    if flag_1 == 0:
                                                        data[i]['children'][j]['children'][k]['children'] = []
                                                    else:
                                                        data[i]['children'][j]['children'][k]['children'][l_2][
                                                            'children'] = self.clearNullDicInList(data[i]['children'][j]['children'][k]['children'][l_2]['children'])
                                for k_2 in range(len(data[i]['children'][j]['children'])):
                                    if len(data[i]['children'][j]['children']) !=0:
                                        if data[i]['children'][j]['children'][k_2].has_key('children'):
                                            flag_2 = 0
                                            for e_data in data[i]['children'][j]['children'][k_2]['children']:
                                                if e_data != {}:
                                                    flag_2 = 1
                                                    break
                                            if flag_2 == 0:
                                                data[i]['children'][j]['children'] = []
                                            else:
                                                data[i]['children'][j]['children'][k_2]['children'] = self.clearNullDicInList(data[i]['children'][j]['children'][k_2]['children'])
                    # print 'dddd',data
                    for j_2 in range(len(data[i]['children'])):
                        if len(data[i]['children']) !=0:
                            if data[i]['children'][j_2].has_key('children'):
                                flag_3 = 0
                                for e_data in data[i]['children'][j_2]['children']:
                                    if e_data != {}:
                                        flag_3 = 1
                                        break
                                if flag_3 == 0:
                                    data[i]['children'][j_2]['children'] = []
                                else:
                                    data[i]['children'][j_2]['children'] = self.clearNullDicInList(
                                        data[i]['children'][j_2]['children'])
        for i_2 in range(len(data)):
            if data[i_2].has_key('children'):
                flag_4 = 0
                for e_data in data[i_2]['children']:
                    print 'eee:',data[i_2]['children']
                    # print 'edata',e_data
                    if e_data.has_key('children'):
                        if e_data['children'] != []:
                            flag_4 = 1
                            break
                if flag_4 == 0:
                    data[i_2] = []
                else:
                    data[i_2]['children'] = self.clearNullDicInList(
                        data[i_2]['children'])
        new_data = []
        for e_last_data in data:
            # print 'e_last_data',e_last_data
            if len(e_last_data) != 0:
                new_data.append(e_last_data)
        for i in range(len(new_data)):
            if new_data[i].has_key('children'):
                list = []
                for i_1 in range(len(new_data[i]['children'])):
                    # print 'i_1',i_1
                    if len(new_data[i]['children']) != 0:
                        if new_data[i]['children'][i_1].has_key('children'):
                            if len(new_data[i]['children'][i_1]['children']) == 0:
                                new_data[i]['children'][i_1]=[]
                            if len(new_data[i]['children'][i_1])!=0:
                                list.append(new_data[i]['children'][i_1])
                new_data[i]['children']=list


        print "new_data: ", new_data
        return new_data

    def clearNullDicInList(self, data):
        '''
        :param data: [{},{'a':'1','b':'2','c':'3'}, ...]
        :return: [{'a':'1','b':'2','c':'3'}]
        '''
        t_data = data
        r_data = []
        for e_data in t_data:
            if e_data != {}:
                r_data.append(e_data)
        return r_data




    # 前端打开端口后端处理
    # def openWindow(self, request):
    #     id = request.GET.get('id', '')
    #     type = request.GET.get('wztype', '')
    #     print "id is :", id
    #     print "type is :", type
    #     return '123'


















