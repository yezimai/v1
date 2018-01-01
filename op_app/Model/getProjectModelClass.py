#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from op_app.Model.base.baseModelClass import BaseDbModelClass
from op_app.logger.log import dblog
import json

class GetProjectModelClass(BaseDbModelClass):

    def __init__(self, user):
        super(GetProjectModelClass, self).__init__()
        self.user = user

    def getProjectInfo(self):
        '''# 1.先根据用户-组-权限-机器-应用-菜单来获取系统的菜单表，具体是先获取服务器的类型1为物理机，2为虚拟机
        2.在根据用户-组-权限-菜单来获取菜单，然后将2个获取的菜单合并展示出最后的菜单表
        3.根据菜单表来获取对应的nav导航
        :return:返回的格式是一个字典 {}
        '''
        dblog.info("Enter getProjectInfo successed,file: [ %s ], line: [ %s ]" % (
                            __file__, sys._getframe().f_lineno))
        r_list = []
        r_list_final = []
        id = self.user.id
        sql = '''
            select DISTINCT cd.server_type,cd.physical_server_id,cd.virtual_server_id 
            from auth_user a,op_app_group_user ab,op_app_group b,
                  op_app_permission c,op_app_group_permission bc ,op_app_permission_server cd 
            where a.id = %s and a.id =ab.user_id and ab.group_id=b.id 
                  and ab.group_id=bc.group_id and c.id=cd.permission_id 
                  and c.id = cd.permission_id '''
        try:
            data = self._cursorQuery(sql, [id])
            print('<------>\033[32;1m%s\033[0m' %len(data))
            dblog.info('data is: %s, file: [ %s ], line: [ %s ]' % (data, __file__, sys._getframe().f_lineno))
            if not len(data):
                dblog.error('data is None , file: [ %s ], line: [ %s ]' % (__file__, sys._getframe().f_lineno))
                return []
            for v in data:
                if int(v[0]) == 2:  # 虚拟机
                    sql = '''select f.code from auth_user a,op_app_group_user ab,
                            op_app_group b,op_app_permission c,op_app_group_permission bc ,
                            cmdb_virtual_server d,op_app_permission_server cd,
                            cmdb_server_app de,cmdb_app e,cmdb_project f
                            where a.id = %s and a.id =ab.user_id and ab.group_id=b.id and ab.group_id=bc.group_id 
                            and c.id=cd.permission_id and cd.virtual_server_id=d.id and d.id=de.virtual_server_id 
                            and de.app_id=e.id and e.project_id=f.id'''
                    try:
                        data = self._cursorQuery(sql, [id])

                        dblog.info(
                            'data2 is: %s, file: [ %s ], line: [ %s ]' % (data, __file__, sys._getframe().f_lineno))
                    except Exception as e:
                        dblog.error("[ERROR] Query error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]" % (
                            e, __file__, sys._getframe().f_lineno))
                    else:
                        for i in data:
                            # dic1 = dict()
                            # dic1['id'] = data[i][0]
                            # dic1['text'] = data[i][1]
                            # dic1['code'] = data[i][2]
                            # print data[i][1]
                            # if dic1 not in r_list:
                            r_list.append(i[0])
                        # print('<------>\033[32;1m%s\033[0m' %r_list)
                else:
                    sql = '''
                          select f.code 
                          from auth_user a,op_app_group_user ab,op_app_group b,
                                   op_app_permission c,op_app_group_permission bc,cmdb_physical_server d,
                                   op_app_permission_server cd,cmdb_server_app de,cmdb_app e,cmdb_project f
                          where a.id=%s and ab.user_id=a.id and b.id=bc.group_id 
                                and c.id=bc.permission_id=cd.permission_id and cd.physical_server_id=d.id=de.physical_server_id
                                and de.app_id=e.id and e.project_id=f.id'''
                    try:
                        data = self._cursorQuery(sql, [id])
                        print('-----9999', data)
                        dblog.info('data1 is: %s, file: [ %s ], line: [ %s ]' \
                                   % (data, __file__, sys._getframe().f_lineno))
                    except Exception as e:
                        dblog.error("[ERROR] Query error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]"\
                                    %(e, __file__, sys._getframe().f_lineno))
                    else:
                        if len(data) > 0:
                            for i in data:
                                # dic2 = dict()
                                # dic2['id'] = data[i][0]
                                # dic2['text'] = data[i][1]
                                # dic2['code'] = data[i][2]
                                # if dic2 not in r_list:
                                r_list.append(i[0])

        except Exception as e:
            dblog.error("[ERROR] Query error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]" % (e, __file__, sys._getframe().f_lineno))

        # for i in r_list:  # 对查找的系统进行去重
        #     if i not in r_list_final:
        #         r_list_final.append(i)
        # dblog.info("r_list last: %s,file: [ %s ], line: [ %s ]" % (
        #     json.dumps(r_list_final, indent=4), __file__, sys._getframe().f_lineno))
        # dblog.info("Exit getProjectInfo with successed, file: [ %s ], line: [ %s ]" % (
        #     __file__, sys._getframe().f_lineno))

        #通过user-组-权限-机器-应用-系统来获取对应的系统列表
        m_list=[]
        sql = '''select DISTINCT f.code from auth_user a ,op_app_group g,op_app_group_user ag,op_app_permission c,
                        op_app_group_permission cg,op_app_nav f ,op_app_permission_nav cf
                  where a.id = %s and a.id=ag.user_id and ag.group_id=g.id=cg.group_id 
                        and cg.permission_id=c.id=cf.permission_id and cf.nav_id=f.id and f.pid=0'''

        try:
            data = self._cursorQuery(sql, [id])

        except Exception as e:
            dblog.error("[ERROR] Query error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]" % (
                e, __file__, sys._getframe().f_lineno))
        else:
            if len(data) < 0:
                dblog.info('data is None , file: [ %s ], line: [ %s ]' % (__file__, sys._getframe().f_lineno))
                return []
            for v in data:
                m_list.append(v[0])
        #对2个获取的项目code进行求交集,然后去找对应的导航
        r_set = set(r_list)
        m_set = set(m_list)
        final_set = r_set.intersection(m_set)    # final_set = set([u'CAP'])
        print('<r_set------>\033[34;1m%s\033[0m' % r_set)
        print('<m_set------>\033[34;1m%s\033[0m' % m_set)
        print('<final_set------>\033[34;1m%s\033[0m' % final_set)
        final_list = list(final_set)
        print('<final_list------>\033[34;1m%s\033[0m' % final_list)
        #final_list = ",".join(["'%s'"%x for x in final_list])
        #final_list = '('+final_list+')'
        print('<final_list------>\033[34;1m%s\033[0m' % final_list)

        #args = tuple(final_list)
        #print('<final_tuple------>\033[34;1m%s\033[0m' % args)
        if len(final_list) == 0:
            print('no intersection--')
            return []
        for i in final_list:
            sql = '''select p.id,p.name,p.code from cmdb_project p where p.code = %s'''
            try:
                data = self._cursorQuery(sql, [i])
                dblog.info(
                    'datajiaoji is: %s, file: [ %s ], line: [ %s ]' % (data, __file__, sys._getframe().f_lineno))
            except Exception as e:
                dblog.error("[ERROR] Query error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]" % (
                    e, __file__, sys._getframe().f_lineno))
                return []
            else:
                if data is None :
                    dblog.error('data is None , file: [ %s ], line: [ %s ]' % (__file__, sys._getframe().f_lineno))
                    return []
                for j in data:
                    dic = dict()
                    dic['id'] = j[0]
                    dic['text'] = j[1]
                    dic['code'] = j[2]
                    # if dic2 not in r_list:
                    r_list_final.append(dic)

        return r_list_final

