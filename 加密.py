# -*- coding:utf-8 _*-
""" 
#   author : YOYO
#   time :  2019/7/31 10:53
#   email : youyou.xu@enesource.com
#   project_name :  python-study
#   file_name :  加密
#   function： 
"""

import hashlib

def jm_sha256( value):
    '''
    sha256加密
    return:加密结果转成16进制字符串形式
    '''
    hsobj = hashlib.sha256()
    hsobj.update(value.encode("utf-8"))
    return hsobj.hexdigest()



m = jm_sha256('aaaa1234')
print(m)
