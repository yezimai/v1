#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from django.db import connections, connection
from op_app.Model.base.baseModelClass import BaseDbModelClass

class GetHostInfoModelClass(object):

    def __init__(self,request):
        self.request = request

    def getHostInfo(self):
        '''# 先获取服务器的类型1为物理机，2为虚拟机
        :return:返回的格式是一个字典
        '''
        user_id =self.request.user.id
        env_id = self.request.GET.get('env_id','0') #环境类型id
        app_id = self.request.GET.get('app_id','0') #应用id
        print('userid,env_id,app_id',user_id,env_id,app_id)
        sql = '''SELECT ab.server_type from cmdb_app a, cmdb_server_app ab \
              where a.id=%s and a.id=ab.app_id'''
        i_calss = BaseDbModelClass()
        data = i_calss._cursorQuery(sql,[app_id])
        print '!!!!!',data
        r_list = []
        for v in data:
            if int(v[0]) == 2:#虚拟机,获取虚拟机的ip，责任人信息
                sql = '''SELECT ip.sys_ip,u.user_name \
                    from cmdb_app a, cmdb_server_app ad,cmdb_virtual_server d,cmdb_env e,\
                    cmdb_env_server de,cmdb_ip ip,cmdb_project f ,cmdb_user_info u,auth_user au,op_app_group g,\
                    op_app_group_user ag,op_app_permission c,op_app_group_permission cg,op_app_permission_server cd \
                    where a.id=%s and a.id=ad.app_id and d.id = ad.virtual_server_id and e.env_type=%s \
                    and de.server_type='2' and de.env_id=e.id and d.ip_id=ip.id and a.project_id=f.id \
                    and f.project_manager=u.only_id and au.id=%s and au.id=ag.user_id and ag.group_id=g.id=cg.group_id \
                    and cg.permission_id=c.id=cd.permission_id and cd.virtual_server_id=d.id and g.type=%s'''

                i_calss = BaseDbModelClass()
                data = i_calss._cursorQuery(sql,[app_id,env_id,user_id,env_id])

                for i in range(len(data)):
                    dic1 = {}
                    dic1['ip']=data[i][0]
                    dic1['manager'] = data[i][1]
                    dic1['env_info'] = env_id #
                    #print data[i][1]
                    r_list.append(dic1)
                print('<------>\033[32;1m%s\033[0m' %r_list)
            else:
                sql = '''select ip.sys_ip,u.user_name \
                      from cmdb_app e,cmdb_physical_server d,cmdb_server_app de,cmdb_env H,\
                            cmdb_env_server hd,cmdb_ip ip,cmdb_user_info u,cmdb_project p\
                      where e.id=11 and e.id=de.app_id and de.physical_server_id=d.id  \
                      and H.id=hd.env_id and hd.physical_server_id=d.id \
                      and H.env_type=1=hd.env_id and d.ip_id=ip.id and e.project_id=p.id \
                      and p.project_manager=u.only_id'''
                i_calss = BaseDbModelClass()
                data = i_calss._cursorQuery(sql,[id])
                for i in range(len(data)):
                    dic2 = {}
                    dic2['ip']=data[i][0]
                    dic2['manager'] = data[i][1]
                    dic2['env_info'] = env_id #
                    r_list.append(dic2)
        print('rlist<------>\033[32;1m%s\033[0m' % r_list)
        return r_list