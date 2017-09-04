import Vue from 'vue';
import Router from 'vue-router';
import Hello from '@/components/Hello';
import Foo from '@/components/Foo';
import Login from '@/components/Login';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello,
    },

    {
      path: '/foo',
      name: 'foo',
      component: Foo,
    },

    {
      path: '/login',
      name: 'login',
      component: Login,
    },

  ],
});
