"""
处理url, 封装get和post方法，头信息，登陆
"""
from setting import BASE_URL,Login_info
import requests
from loguru import logger
from cacheout import Cache  #Cache 是个类

cache = Cache()

class Base():
    def get_url(self,path,params=None):
        if params:
            full_path = BASE_URL + path + params
            return full_path
        return BASE_URL + path

    def get(self,url):
        result = None
        response = requests.get(url,headers=self.get_heaaders())
        try:
            result = response.json()
            logger.success("请求URL：{}，返回结果：{}".format(url,result))
            return result
        except Exception as e:
            logger.error("请求get方法异常，返回数据为{}".format(result))

    def post(self,url,data):
        result = None
        response = requests.post(url,json=data,headers=self.get_heaaders())
        try:
            result = response.json()
            logger.success("请求URL：{}，请求参数：{},返回结果：{}".format(url,data,result))
            return result
        except Exception as e:
            logger.error("请求post方法异常，返回数据为{}".format(result))

    def get_heaaders(self):
        headers = {'Content-Type':'appkucation/json'}
        token = cache.get('token')
        #如果不是None的话执行if语句
        if token:
            headers.update({'X-Litemall-Admin-Token':token})
            return headers
        return headers

    def login(self):
        login_path = '/admin/auth/login'
        login_url = self.get_url(login_path)
        result = self.post(login_url,Login_info)
        try:
            if 0 == result.get('errno'):
                logger.info("请求登陆接口成功")
                token = result.get('data').get('token')
                cache.set('token',token)
            else:
                logger.error("登陆失败：{}".format(result))
                return None
        except Exception as e:
            logger.error("请求登陆接口返回异常，异常数据：{}".format(result))
            logger.error("报错信息：{}".format(e))

# main回车
if __name__ == '__main__':
    base=Base()
    login_url = base.get_url('/admin/auth/login')
    login_data = {"username":"admin123","password":"admin123"}
    print(base.post(login_url,login_data))
