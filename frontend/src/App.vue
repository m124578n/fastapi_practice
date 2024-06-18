<!-- App.vue -->
<template>
  <div id="app">
    <h1>用户管理系统</h1>
    <form @submit.prevent="addUser">
      <label for="name">姓名：</label>
      <input type="text" id="name" v-model="newUser.name" required>
      <button type="submit">添加用户</button>
    </form>
    <ul>
      <li v-for="user in users" :key="user.id">{{ user.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      users: [],
      newUser: {
        name: ''
      }
    }
  },
  async mounted() {
    await this.getUsers();
  },
  methods: {
    async getUsers() {
      try {
        const response = await axios.get('http://localhost:8000/users/');
        this.users = response.data;
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    },
    async addUser() {
      try {
        console.log(this)
        const response = await axios.post('http://localhost:8000/users/', this.newUser);
        this.users.push(response.data);
        this.newUser.name = ''; // 清空输入框
      } catch (error) {
        console.error('Error adding user:', error);
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Arial, Helvetica, sans-serif;
  margin: 2rem;
}

form {
  margin-bottom: 1rem;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 0.5rem;
}
</style>
