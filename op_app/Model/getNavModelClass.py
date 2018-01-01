#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from django.db import connections, connection
from op_app.Model.base.baseModelClass import BaseDbModelClass
from op_app.logger.log import dblog
import json
class GetNavModelClass(BaseDbModelClass):

    def __init__(self, user, data):
        super(GetNavModelClass, self).__init__()
        self.user = user
        self.data = data

    def getNavInfo(self):
        # 通过用户id,系统id来获取导航
        id = self.user.id

        for j in self.data:
            code = j['code']
            print '2222222',code
            r_list = []
            sql = '''select DISTINCT d.id,d.navname,d.url from auth_user a,op_app_group_user ab,op_app_group b,
                                      op_app_group_permission bc,op_app_permission c,op_app_nav d ,
                                      op_app_permission_nav cd
                      where a.id=%s and a.id=ab.user_id and ab.group_id=b.id=bc.group_id 
                            and bc.permission_id=c.id=cd.permission_id and cd.nav_id=d.id 
                            and d.pid = (select dd.id from op_app_nav dd where dd.code=%s)'''
            try:
                res = self._cursorQuery(sql, [id, code])
                print 'navinfo!!!!!',res
                if len(res) < 0:
                    dblog.error('navinfo is None , file: [ %s ], line: [ %s ]' % (__file__, sys._getframe().f_lineno))
                    return []
            except Exception as e:
                dblog.error("[ERROR] Query error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]" % (
                    e, __file__, sys._getframe().f_lineno))
                return []
            else:
                for i in range(len(res)):

                    dic = dict()
                    dic['id']=res[i][0]
                    dic['text'] = res[i][1]
                    dic['url'] = res[i][2]
                    r_list.append(dic)
                    j['children']=r_list
                print('<------>\033[32;1m%s\033[0m' %r_list)

        # dblog.info("nav_data last: %s,file: [ %s ], line: [ %s ]" % (
        #     json.dumps(self.data, indent=4), __file__, sys._getframe().f_lineno))
        #print('navinfo------>\033[32;1m%s\033[0m' %self.data)
        return self.data
# if __name__ == '__main__':
#     m_db = DbBaseModelClass()
#     sql = 'select * from book_info limit 1'
#     ret = m_db._cursorQuery(sql, [])
#     print('ret:', ret)