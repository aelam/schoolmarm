<template>
 <div class="log-email">
  <input type="text" placeholder="用户名" :class="'log-input' + (account==''?' log-input-empty':'')" v-model="account">
  <input type="password" placeholder="密码" :class="'log-input' + (password==''?' log-input-empty':'')" v-model="password">
  <a href="javascript:;" rel="external nofollow" class="log-btn" @click="login">Login</a>
 </div>
</template>

<script>
  export default {
    name: 'Login',
    data() {
      return {
        msg: '登录',
        account: '',
        password: '',
        isLoging: false,
      };
    },

    methods: {
      login() {
        console.log('login click');
      },
    },
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
