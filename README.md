# 学习

## 学习资料

[Django与vuejs共同开发 设置](https://zhuanlan.zhihu.com/p/25080236)
[Router Get Start](https://router.vuejs.org/zh-cn/essentials/getting-started.html)
[Django跨域问题](https://stackoverflow.com/questions/35881201/django-rest-framework-csrf-and-vue-js)
[Django-webpack-loader](https://stackoverflow.com/questions/37479554/vue-js-with-django-webpack-loader)

## token问题

怎么同步权限

## webpack设置问题

现在不能实时更新


## 安装工具

```lang=shell
npm install -g webpack
```


## Python替换pip源
```
vi ~/.pip/pip.conf

增加trusted-host 
  1 [global]$
  2 index-url = http://pypi.douban.com/simple$
  3 trusted-host=pypi.douban.com$

```


## phantomjs-prebuilt 安装失败
```
npm install phantomjs-prebuilt@2.1.14 --ignore-scripts
```