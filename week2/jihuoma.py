# -*- coding:utf-8 -*-

import uuid
def jihuoma(num):
    jhm_list = []
    for i in range(num):
        jhm_list.append(str(uuid.uuid1()))
    print(jhm_list)

if __name__ == '__main__':
    jihuoma(10)
