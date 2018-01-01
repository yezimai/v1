#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, render_to_response
from Controllers.loginControllerClass import LoginControllerClass
from op_app.Controllers import (getNavControllerClass, getProjectNavControllerClass,
                                getProjectDetailControllerClass,getHostInfoControllerClass)
def login(request):
    c_login = LoginControllerClass(request)
    return c_login.login()
# 退出
def logout(request):
    c_login = LoginControllerClass(request)
    return c_login.logout()
# 密码更改
def password_change(request):
    c_login = LoginControllerClass(request)
    return c_login.password_change()
# 密码更改完成
def password_change_done(request):
    return render(request, 'login/password_change_done.html')
# 首页
def index(request):
    c_login = LoginControllerClass(request)
    return c_login.index()




####### code begin ##############
#print('<------>\033[32;1m%s\033[0m' %r_list)
def getNav(request):
    '''
    导航数据获取
    :param request:
    :return:
    '''
    # data = [
    #     {
    #         'text': u'蜂巢系统',
    #         'id': 23L,
    #         'children': [
    #             {
    #                 'text': u'管理',
    #                 'id': 40L,
    #                 # 'children': []
    #             }, {
    #                 'text': u'统计',
    #                 'id': 50L,
    #                 # 'children': []
    #             }
    #         ]
    #      },{
    #         'text': u'信审系统',
    #         'id': 27L,
    #         'children': [
    #             {
    #                 'text': u'管理',
    #                 'id': 40L,
    #                 # 'children': []
    #             }, {
    #                 'text': u'统计',
    #                 'id': 50L,
    #                 # 'children': []
    #             }
    #         ]
    #     }
    # ]
    # 获取用户有权限的项目
    i_pro_class = getProjectNavControllerClass.GetProjectNavControllerClass(request)
    data = i_pro_class.getProject()
    #获取导航
    i_nav_class = getNavControllerClass.GetNavControllerClass(request, data)
    data = i_nav_class.getNav()


    return JsonResponse(data, safe=False)


def manage(request):
    '''
    管理页面获取
    :param request:
    :return:
    '''
    data = {
        'project_name': '蜂巢系统',
        'project_code': 'HCS',
        'project_id': 1,
        'envs': [
            {
                'id': 1,
                'name': 'DEV',
                'selected': 0
            },{
                'id': 2,
                'name': 'SIT',
                'selected': 0
            },{
                'id': 3,
                'name': 'UAT',
                'selected': 1
            },{
                'id': 4,
                'name': 'PRE',
                'selected': 0
            },{
                'id': 5,
                'name': 'PRD',
                'selected': 0
            }
        ],
        'apps': [
            {
                'id': 10,
                'name': 'beehive',
            },{
                'id': 11,
                'name': 'LoginSYS',
            },{
                'id': 12,
                'name': 'fileupload',
            }
        ]
    }
    i_class = getProjectDetailControllerClass.GetProjectDetailControllerClass(request)
    data = i_class.getProject()
    return render(request, 'manage/index.html', {'data': data})

def release(request):
    '''
    发布页面获取
    :return:
    '''
    return render(request, 'release/release.html', {'data': 'test release'})

def statistics(request):
    '''
    统计页面获取
    :return:
    '''
    return render(request, 'statistics/statistics.html', {'data': 'test statistics'})


def hostInfo(request):
    '''
    获取主机信息，返回给前端管理页面
    :param request: GET 传参，  project_id、 env_type、 select_app
    :return:
    '''
    project_id, env_id, app_id = request.GET.get('project_id', '0'), request.GET.get('env_id', '0'), request.GET.get('app_id', '0')
    print('project_id:', project_id, ' env_id:', env_id, ' select_app:', app_id)

    data = {
        "data": [
            {
                "ip": "10.0.0.2",
                "env_name": "sit1",
                "manager": "刘国华"
            },
            {
                "ip": "10.0.0.3",
                "env_name": "sit3",
                "manager": "李华"
            },
            {
                "ip": "10.0.0.4",
                "env_name": "sit4",
                "manager": "游昌永"
            },
            {
                "ip": "10.0.0.5",
                "env_name": "sit5",
                "manager": "游昌永"
            },
            {
                "ip": "10.0.0.6",
                "env_name": "sit1",
                "manager": "李智军"
            },
            {
                "ip": "10.0.0.7",
                "env_name": "sit1",
                "manager": "游昌永"
            },
            {
                "ip": "10.0.0.8",
                "env_name": "sit7",
                "manager": "刘国华"
            },
            {
                "ip": "10.0.0.9",
                "env_name": "sit1",
                "manager": "李智军"
            },
            {
                "ip": "10.0.0.10",
                "env_name": "sit1",
                "manager": "刘国华"
            },
            {
                "ip": "10.0.0.11",
                "env_name": "sit1",
                "manager": "游昌永"
            },
            {
                "ip": "10.0.0.12",
                "env_name": "sit1",
                "manager": "刘国华"
            },
            {
                "ip": "10.0.0.13",
                "env_name": "sit1",
                "manager": "李智军"
            },
        ]
    }
    i_class = getHostInfoControllerClass.GetHostInfoControllerClass(request)
    data = i_class.getHostInfo()
    return JsonResponse(data, safe=False)

def doServiceManageAction(request):
    '''
    用户操作页面， 如启动、停止、等等执行运行远程命令的操作
    :param request:
    :return:
    '''
    project_id = request.POST.get('project_id', '0')
    env_id = request.POST.get('env_id', '')
    app_id = request.POST.get('app_id', '')
    ip = request.POST.get('ip', '')
    action = request.POST.get('action', '')
    '''根据项目、环境、应用、ip对对应的部署在此机器上的应用进行操作,
        1、确定要操作的机器，找出应用部署的用户名、端口、密码，部署路径等详细信息；
        2、同步本地脚本到远程端；
           假如有个应用 LoginSYS，部署在 10.0.0.3 机器，部署用户为 beehive用户，那么：
           2.1 在tasks 下创建一个
             service_manage/10.0.0.3/LoginSYS/scripts/
                - bin/ 这个是从 scripts/client/service_manage/bin/* 拷贝过来的；
                - conf/ 这个下面有个配置文件：app_config.conf 文件实时生成；
                配置文件参考

            # 写入配置文件
            f = open(scriptdir + '/conf/app_config.conf', 'w') # 开始写入配置文件
            f.write('pkgfile={0}'.format(REMOTE_BASE_DIR + dir_name + '/'  + appname + '/pkg/' + dic['pkgname']) + '\n')
            f.write('appnumber={0}'.format('1') + '\n')
            f.write('projectname={0}'.format(data[1]) + '\n')
            f.write('ip={0}'.format(ip) + '\n')
            f.write('user[1]={0}'.format(dic['name']) + '\n')
            f.write('upgradetype[1]=full' + '\n')
            f.write('apptype[1]=tomcat' + '\n')
            f.write('backupdir[1]={0}'.format(REMOTE_BASE_DIR + dir_name + '/' + appname + '/backup') + '\n')
            f.write('appdir[1]={0}'.format(dic['appdir']) + '\n')
            f.write('appwarname[1]={0}'.format(dic['pkgname']) + '\n')
            f.write('startuptime[1]=1000' + '\n')
            f.write('port[1]=8080' + '\n')
            f.close() # 写入配置文件完成

           2.2 将 service_manage/10.0.0.3/ 目录下的内容 rsync 同步到远程目录固定目录： ${HOME}/service_manage/ 下，
           2.3 远程调用 10.0.0.3 机器下  ${HOME}/service_manage/bin/startapp.sh 或者 stopapp.sh, 成功返回成功，失败返回失败

    '''
    import time
    time.sleep(5)
    return JsonResponse('ok', safe=False)


def doFunctionPage(request):
    '''
    单独的页面进行操作如：日志查看、任务管理、命令执行、机器详情页面
    :param request:
    :return:
    '''
    project_id = request.GET.get('project_id', '0')
    env_id = request.GET.get('env_id', '')
    app_id = request.GET.get('app_id', '')
    ip = request.GET.get('ip', '')
    action = request.GET.get('action', '')
    if action == 'log_show': # 日志查看
        return render(request, 'manage/log_show.html', {'data': 'test log_show'})
    elif action == 'task_manage': # 任务管理
        return render(request, 'manage/task_manage.html', {'data': 'test task_manage'})
    elif action == 'run_command': # 命令执行
        return render(request, 'manage/run_command.html', {'data': 'test run_command'})
    elif action == 'machine_detail': # 机器详情
        return render(request, 'manage/machine_detail.html', {'data': 'test machine_detail'})
    else:
        return render(request, '404.html', {'data': 'test 404'})

def getLogDetail(request):
    '''
    在执行命令的时候，获取实时的日志输出，主要针对 action是启动、停止、重启
    远程执行命令获取日志信息返回，
    :param request:
    :return:
    '''
    project_id = request.GET.get('project_id', '0')
    env_id = request.GET.get('env_id', '')
    app_id = request.GET.get('app_id', '')
    ip = request.GET.get('ip', '')
    action = request.GET.get('action', '')
    data = {
        'data': 'this is log ...... ....safdasdfasdfasdfasdf',
        'title': '运维平台-日志查看-日志详情'
    }
    return render(request, 'manage/logdetail.html', {'data': data})










### 测试代码 #####
def test(request):
    # m_data = CmdbModelClass()
    return JsonResponse('123', safe=False)


### 测试代码 #####
def test2(request):
    # m_data = CmdbModelClass()
    return JsonResponse('123', safe=False)








