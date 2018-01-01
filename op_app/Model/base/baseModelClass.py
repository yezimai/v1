#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from django.db import connections, connection


class BaseDbModelClass(object):

    def __init__(self, db=None):
        self.cursor = connection.cursor() if db == None else connections[db].cursor()

    def _cursorQuery(self, sql, parlist):
        try:
            self.cursor.execute(sql, parlist)
            return self.cursor.fetchall()
        except Exception as e:
            print("[ERROR] Query error, Catch exception:[ %s ], file: [ %s ], line: [ %s ],sql:[ %s ]"\
                  % (e, __file__, sys._getframe().f_lineno,sql))


    ## 插入接口  ##
    def _cursorInsert(self, sql, parlist):
        try:
            self.cursor.execute(sql, parlist)
            return 1
        except Exception as e:
            print("[ERROR] Insert error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]" % (e, __file__, sys._getframe().f_lineno))
            return -1

    ## 更新接口  ##
    def _cursorUpdate(self, sql, parlist):
        try:
            self.cursor.execute(sql, parlist)
            return 1
        except Exception as e:
            print("[ERROR] Update error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]" % (
            e, __file__, sys._getframe().f_lineno))
            return -1

    ## 删除接口  ##
    def _cursorDelete(self, sql, parlist):
        try:
            self.cursor.execute(sql, parlist)
            return 1
        except Exception as e:
            print("[ERROR] Delete error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]" % (
                e, __file__, sys._getframe().f_lineno))
            return -1

# if __name__ == '__main__':
#     m_db = DbBaseModelClass()
#     sql = 'select * from book_info limit 1'
#     ret = m_db._cursorQuery(sql, [])
#     print('ret:', ret)