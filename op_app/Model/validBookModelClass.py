#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
     valid_book model
'''

import sys
from op_app.Model.base.defaultDbModelClass import DefaultDbModelClass
from op_app.logger.log import dblog


class ValidBookModelClass(DefaultDbModelClass):

    def getBookId(self, id):
        sql = 'select book_id from valid_book where book_id=%s'
        try:
            ret = self._cursorQuery(sql, [id])
            if len(ret) == 0:
                return '-1'
            else:
                return ret[0][0]
        except Exception as e:
            dblog.error("[ERROR] Query error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]" % (e, __file__, sys._getframe().f_lineno))
            return '-1'

    def addBookId(self, id):
        sql = '''insert into valid_book(`book_id`) values (%s)'''
        try:
            ret = self._cursorInsert(sql, [id])
            return '1'
        except Exception as e:
            print("[ERROR] Query error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]" % (
            e, __file__, sys._getframe().f_lineno))
            return '-1'

    def updateBook(self, id, pindao, title, book_type, is_free, valid):
        sql = '''update valid_book set pindao=%s, title=%s, book_type=%s, is_free=%s, valid=%s where book_id=%s'''
        try:
            ret = self._cursorUpdate(sql, [pindao, title, book_type, is_free, valid, id])
            return '1'
        except Exception as e:
            print("[ERROR] Update error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]" % (
                e, __file__, sys._getframe().f_lineno))
            return '-1'

    def updateScrapyedStatus(self, book_id, result='SUCCESSED'):
        if result == 'SUCCESSED':
            val = 1
        elif result == 'FAILED':
            val = 3
        elif result == 'RUNNING':
            val = 2
        else:
            val = 4
        sql = '''update valid_book set scrapyed=%s where book_id=%s'''
        try:
            ret = self._cursorUpdate(sql, [val, book_id])
            return '1'
        except Exception as e:
            print("[ERROR] Update error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]" % (
                e, __file__, sys._getframe().f_lineno))
            return '-1'

    def getUnCrapyedBookId(self):  #返回一个未爬取的书本ID
        sql = '''select book_id from valid_book where is_free=1 and valid=1 and scrapyed=0 order by book_id limit 1'''
        try:
            ret = self._cursorQuery(sql, [])
            if len(ret) == 0:
                return ''
            else:
                return ret[0][0]
        except Exception as e:
            print("[ERROR] Query error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]" % (
            e, __file__, sys._getframe().f_lineno))
            return '-1'

    def getFailedAndUnknowStatusBookId(self): # 得到一个状态未知或者爬取失败的书本ID
        sql = '''select book_id from valid_book where is_free=1 and valid=1 and (scrapyed=3 or scrapyed=4) order by book_id limit 1'''
        try:
            ret = self._cursorQuery(sql, [])
            if len(ret) == 0:
                return ''
            else:
                return ret[0][0]
        except Exception as e:
            print("[ERROR] Query error, Catch exception:[ %s ], file: [ %s ], line: [ %s ]" % (
                e, __file__, sys._getframe().f_lineno))
            return '-1'

