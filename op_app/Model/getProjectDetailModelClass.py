#!/usr/bin/python
# -*- coding: UTF-8 -*-


from op_app.Model.base.baseModelClass import BaseDbModelClass

class GetProjectDetailModelClass(object):

    def __init__(self,nav_id,user_id):
        self.nav_id = nav_id
        self.user_id = user_id

    def getProjectInfo(self):
        '''#
        :return:返回的格式是一个字典
        '''
       #先查找出项目和应用的相关信息
        sql = '''select b.name,b.code,b.id ,c.`name`,c.id  from cmdb_project b,cmdb_app c 
              where c.project_id= b.id and b.name=
              (select aa.navname from op_app_nav aa where aa.id=
              (SELECT a.pid from op_app_nav a where a.id=%s))'''
        # sql = '''SELECT a.navname from op_app_nav a where a.id=%s'''
        i_calss = BaseDbModelClass()
        data = i_calss._cursorQuery(sql,[self.nav_id])
        print '!!!!!data :', data
        res_dic = {}
        r_list=[]

        app_list=[]
        for v in data:
            r_dic = {}
            res_dic['project_name'] = v[0]
            res_dic['project_code'] = v[1]
            res_dic['project_id'] = v[2]
            r_dic['name']=v[3]
            r_dic['id']=v[4]
            r_list.append(r_dic)
            res_dic['apps']=r_list
            #app_list.append(v[4])
        print('rdic<------>\033[32;1m%s\033[0m' % res_dic)
        #print('app_list<------>\033[32;1m%s\033[0m' % app_list)
        #2.找到权限对应环境相关信息
        #
        sql = '''SELECT b.type from auth_user a,op_app_group b,op_app_group_user ab \
                  WHERE a.id=%s and a.id=ab.user_id and ab.group_id=b.id'''
        i_calss = BaseDbModelClass()
        data = i_calss._cursorQuery(sql,[self.user_id])
        env_list = []
        print('envtpye999999',data)
        if data:
            env_type_choices={
                1:'dev',
                2:'sit',
                3:'uat',
                4:'pre',
                5:'prd',
            }
            for i in data:  #data=((2,), (1,))
                env_dic={}
                print('pppp',i)
                index=i[0]
                if index in  env_type_choices:
                    #env_type_name = env_type_choices[i]
                    env_dic['id'] = index
                    env_dic['name']=env_type_choices[index]
                    env_dic['selected']=0
                    env_list.append(env_dic)
                    print('@@@@@@------',env_list)
        res_dic['envs'] = env_list
        #env_data_list = []

        # for i in app_list:#根据app来找server类型
        # # for i in res_dic:
        #     sql = '''select ab.server_type, ab.physical_server_id,ab.virtual_server_id
        #           from cmdb_app a,cmdb_server_app ab
        #           where a.id=%s and ab.app_id=a.id'''
        #     i_calss = BaseDbModelClass()
        #     data = i_calss._cursorQuery(sql, [i])
        #     print('!!!!!---server_type',data)
        #     if len(data):
        #         env_data_dic = {}
        #         for j in data:
        #
        #             if j[0] == '2':#2为虚拟机
        #                 sql = '''SELECT e.name,e.id from cmdb_virtual_server d,cmdb_env e,cmdb_env_server de
        #                     where d.id=%s and d.id= de.virtual_server_id and e.id=de.env_id'''
        #                 i_calss = BaseDbModelClass()
        #                 data = i_calss._cursorQuery(sql, [j[2]])
        #                 # for env_data in data:
        #                 #     env_data_dic['name'] = env_data[0]
        #                 #     env_data_dic['id'] = env_data[1]
        #                 #     env_data_dic['selected'] = 0
        #                 #     env_data_list.append(env_data_dic)
        #                 #     print('single_env_data000000',env_data_list)
        #
        # # res_dic['envs']=env_data_list
        # # print('resdic<------>\033[34;1m%s\033[0m' % res_dic)
        #
        #             elif j[0] == '1':#物理机
        #                 sql = '''SELECT e.name,e.id from cmdb_physical_server d,cmdb_env e,cmdb_env_server de \
        #                       where d.id=%s and d.id= de.physical_server_id and e.id=de.env_id'''
        #                 i_calss = BaseDbModelClass()
        #                 data = i_calss._cursorQuery(sql, [j[1]])
        #             for env_data in data:
        #                 env_data_dic['name'] = env_data[0]
        #                 env_data_dic['id'] = env_data[1]
        #                 env_data_dic['selected'] = 0
        #             env_data_list.append(env_data_dic)
        #             print('single_env_data000000',env_data_list)
        #res_dic['envs']=env_data_list
        print('resdic<------>\033[34;1m%s\033[0m' % res_dic)
        return res_dic
        #return r_list