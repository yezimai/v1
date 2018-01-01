#!/usr/bin/python
# -*- coding: UTF-8 -*-
from op_app.Model.base.baseModelClass import BaseDbModelClass

class DefaultDbModelClass(BaseDbModelClass):

    def __init__(self):
        self.db = 'default'
        super(DefaultDbModelClass, self).__init__(self.db)



