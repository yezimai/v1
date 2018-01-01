#!/usr/bin/python
# coding:utf-8

import os
import yaml

current_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(current_dir, 'config.yaml')


def load_db_config():
    with open(config_file, 'r') as f:
        obj_ymal = yaml.load(f)
        return { x['name']: {
                    'ENGINE': x['ENGINE'],
                    'HOST': x['HOST'],
                    'PORT': x['PORT'],
                    'USER': x['USER'],
                    'PASSWORD': x['PASSWORD'],
                    'NAME': x['DB_NAME'],
                  } for x in obj_ymal['db'] }


def get_other_parameters():
    with open(config_file, 'r') as f:
        obj = yaml.load(f)
        return [{
            'name': x['name'],
            'txt_base_dir': x['txt_base_dir'],
        } for x in obj['other'] ]



if __name__ == '__main__':
    import json
    ret = load_db_config()
    print(json.dumps(ret, indent=4))
#     print('ret:', ret)