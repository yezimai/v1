#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.conf.urls import url
from views import *


urlpatterns = [
    ##### login ####
    url(r'^$', index, name='index'),
    url(r'^index/$',  index, name='index'),
    url(r'^login/$',  login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^password_change/$', password_change,name='password_change'),
    url(r'^password_change_done/$', password_change_done, name='password_change_done'),
    ##### login end ####

    ## 导航 ##
    url(r'^getNav/$', getNav, name='getNav'),

    ## 管理 ###
    url(r'^manage/$', manage, name='manage'),
    url(r'^hostInfo/$', hostInfo, name='hostInfo'),
    url(r'^doServiceManageAction/$', doServiceManageAction, name='doServiceManageAction'),
    url(r'^getLogDetail/$', getLogDetail, name='getLogDetail'),
    url(r'^doFunctionPage/$', doFunctionPage, name='doFunctionPage'),


    ### 发布 ###
    url(r'^release/$', release, name='release'),

    ### 统计 ###
    url(r'^statistics/$', statistics, name='statistics'),



    url(r'^test/$', test, name='test'),

]