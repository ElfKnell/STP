<template lang="html">
<div>
    <form class="login form">
        <div class="field">
            <label for="id_email">Email</label>
            <input v-model="form.email"
                type="text"
                placeholder="Email"
                autofocus="autofocus"
                maxlength="100"
                id="id_email">
        </div>
        <div class="field">
            <label for="id_password">Password</label>
            <input v-model="form.password"
                type="password"
                placeholder="Password"
                id="id_password">
        </div>
        <button
            @click.prevent="authenticate"
            class="button primary"
            type="submit">Login</button>
    </form>

</div>        
</template>


<script>
import { reactive } from 'vue';
//import router from "@/router";

export default {
    setup() {
        const form = reactive({
            email: '',
            password: ''
        })
        
        const url = 'http://127.0.0.1:8000/api/v1/users/user/obtain_token/'
        
        const authenticate = async () => {            
            
            const data = {
                email: form.email,
                password: form.password
            }

            try {
                const response = await fetch(url, {
                method: 'POST',
                body: JSON.stringify(data),
                headers: {
                'Content-Type': 'application/json'
                    }
                })
                
                
                if (response.ok) {
                    const json = await response.json();
                    console.log('Успех:', JSON.stringify(json));
                    const result = JSON.stringify(json);
                    localStorage.authen =  'JWT ' + result.slice(10, -2);
                    location.replace("#/");  
                    location.reload();
                } else {
                    localStorage.authen = null
                    
                }
                
                              
                } catch (error) {
                console.error('Ошибка:', error);
                }   
            form.email = form.password = ''
        }
        
        return {
            form, authenticate
        }
    }
}
</script>


<style lang="css">

</style>