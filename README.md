# Django+vuejs 学习过程

## 前后端交互配置

### 学习资料

[Django与vuejs共同开发 设置](https://zhuanlan.zhihu.com/p/25080236)
[Router Get Start](https://router.vuejs.org/zh-cn/essentials/getting-started.html)
[Django跨域问题](https://stackoverflow.com/questions/35881201/django-rest-framework-csrf-and-vue-js)
[Django-webpack-loader](https://stackoverflow.com/questions/37479554/vue-js-with-django-webpack-loader)

### token问题  CORS

怎么同步权限

### webpack设置问题

现在不能实时更新django的静态资源

[Django-VueJS](https://zhuanlan.zhihu.com/p/25080236)

## 前端

### 安装工具

```lang=shell
npm install -g webpack
```

### phantomjs-prebuilt 安装失败

使用cnpm的源
一般在 ~/.npmrc下编辑如下内容即可

```rc

registry=http://registry.cnpmjs.org$                                           ```   

```

```shell

npm install phantomjs-prebuilt@2.1.14 --ignore-scripts

```

### vuejs

Vue-Router

```js
      <router-link to="/hello">跳转到你好页</router-link>
```

### 页面骨架开发
### 项目编译打包

## 后端

### Python替换pip源

```shell

vi ~/.pip/pip.conf

增加trusted-host
  1 [global]$
  2 index-url = http://pypi.douban.com/simple$
  3 trusted-host=pypi.douban.com$

```

### VSCode 环境配置

```json
{
    "python.linting.pylintArgs": ["--load-plugins", "pylint_django"],
    "python.envFile": "${workspaceRoot}/.python-version",
    "python.venvPath": "/usr/local/var/pyenv",
    "python.linting.pylintEnabled": false
}
```

[VSCode Python 的设置](https://donjayamanne.github.io/pythonVSCodeDocs/docs/python-path/)

Python有DjangoDebug模板的配置, 可以只留下两个Django 改名为Django-Debug, 再复制一个Django-Run并删除Debug参数

## Django端

### DRF问题集合
Cannot apply DjangoModelPermissions on a view that does not set `.queryset` or have a `.get_queryset()` method.
[DRF API权限问题](https://stackoverflow.com/questions/31335736/cannot-apply-djangomodelpermissions-on-a-view-that-does-not-have-queryset-pro)

[JSON 返回 去除null字段](https://stackoverflow.com/questions/27015931/remove-null-fields-from-django-rest-framework-response)

[API 注册/管理](https://stackoverflow.com/questions/20825029/registering-api-in-apps)


