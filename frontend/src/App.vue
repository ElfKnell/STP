<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/sections">Sections</router-link> |
    <router-link v-if="authen" to="/login">Login</router-link> 
    <a class="router-link router-link-exact" v-if="!authen" @click="logout" >Log out</a>
  </div>
  <router-view/>
</template>


<script>
import { ref } from 'vue'

export default {
  name: 'app',
  setup() {
    let authen = localStorage.authen ? ref(false) : ref(true)

    const logout = async () => {
      if (localStorage.authen) { 
        localStorage.authen = "";
        location.replace("#/login");
        location.reload();
        //authen.value = false;
        
      }
    }
     
    return {
      authen, logout
    } 
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
