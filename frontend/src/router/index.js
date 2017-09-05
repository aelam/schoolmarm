import Vue from 'vue';
import Router from 'vue-router';
import Hello from '@/components/Hello';
import Foo from '@/components/Foo';
import Login from '@/components/Login';
import TopNavi from '@/components/TopNavi';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/hello',
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

    {
      path: '/navi',
      name: 'Top Navigations',
      component: TopNavi,
    },
  ],
});
