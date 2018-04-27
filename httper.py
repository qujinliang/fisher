"""
 Created by qujl on 2018-04-27
"""
__author__ = 'qujl'
import requests

class HTTP:
    @staticmethod
    # 低级错误静态方法 不需要加self
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     pass
