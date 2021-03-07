<template>
    <div id="sections" >
        <form class="row g-3" v-if="prop">
        <div class="col-md-6">
            <label for="id_name_section" class="form-label">Name section</label>
            <input
                v-model="form.name_section"
                type="text"
                class="form-control"
                placeholder="Name section"
                autofocus="autofocus"
                maxlength="100"
                id="id_name_section">
        </div>
        <div class="col-md-6">
            <label for="id_color" class="form-label">Color</label>
            <input
                v-model="form.color"
                class="form-control"
                type="text"
                placeholder="Color"
                id="id_color">
        </div>
        <div class="col-12">
            <label for="id_description" class="form-label">Description</label>
            <input
                v-model="form.description"
                type="text"
                class="form-control"
                placeholder="description"
                id="id_description">
        </div>
        <div class="col-md-6">
          <button 
              @click="save"             
              class="btn btn-primary"
              type="submit">save</button>
        </div>
        <div class="col-md-6">
          <button 
              @click="clean"             
              class="btn btn-danger"
              type="submit">clean</button>
        </div>
    </form>
        <table class="table">
            <thead>
                <th>Name</th>
                <th>Color</th>
                <th>Description</th>
            </thead>
            <tbody>
                <tr v-for="section in sections" :key="section.id">
                    <td>{{ section.name_section }}</td>
                    <td>{{ section.color }}</td>
                    <td>{{ section.description }}</td>
                    <td><button 
                            @click="edit_form(section)"             
                            class="btn btn-primary"
                            type="submit">edit</button>
                    </td>
                    <td><button 
                            @click="delete_section(section.id)"             
                            class="btn btn-danger"
                            type="submit">delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import { reactive } from 'vue';

export default {
  setup() {
        const form = reactive({
            name_section: '',
            color: '',
            description: ''
        })
        
        const prop = localStorage.authen
        console.log(prop)

        const url = 'http://127.0.0.1:8000/api/v1/sections/section/create/'

        const url_d = 'http://127.0.0.1:8000/api/v1/sections/section/detail/'
        
        const add_section = async () => {            
            
            const data = {
                name_section: form.name_section,
                color: form.color,
                description: form.description
            }

            try {
                const response = await fetch(url, {
                method: 'POST', // или 'PUT'
                body: JSON.stringify(data), // данные могут быть 'строкой' или {объектом}!
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': localStorage.authen
                    }
                })
                if (response.ok) {
                    const json = await response.json();
                    console.log('Успех:', JSON.stringify(json));
                
                    location.reload();
                }              
                             
            } catch (error) {
                console.error('Ошибка:', error);
            }   
            
        }

        const delete_section = async (id) => {            
            
            
            const url_del = url_d + id;
            
            try {
                const response = await fetch(url_del, {
                method: 'DELETE',                
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': localStorage.authen
                    }
                })
                if (response.ok) {
                    
                    console.log('Успех:');                
                    location.reload();
                }               
                             
            } catch (error) {
                console.error('Ошибка:', error);
            }  
        }

        const edit_section = async() => {
            const url_edit = url_d + localStorage.id;

            const data = {
                name_section: form.name_section,
                color: form.color,
                description: form.description
            }

            try {
                const response = await fetch(url_edit, {
                method: 'PUT', // или 'PUT'
                body: JSON.stringify(data), // данные могут быть 'строкой' или {объектом}!
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': localStorage.authen
                    }
                })
                if (response.ok) {
                    const json = await response.json();
                    console.log('Успех:', JSON.stringify(json));
                
                    location.reload();
                }              
                             
            } catch (error) {
                console.error('Ошибка:', error);
            }
        }

        const edit_form = async(section) => {
            
            localStorage.id = section.id;
            
            console.log(section.id, section.name_section);
            form.name_section = section.name_section;
            form.color = section.color;
            form.description = section.description;

        }

        const save = async() => {
            
            const x = localStorage.id;
            console.log('xxxxx=', x);
            if (x != 'null') {                
                edit_section();
                console.log('xxxxx=', x);
            } else {
                console.log(localStorage.id);
                add_section();
            }
        }
        const clean = async() => {
            localStorage.id = null;     
            form.name_section = '';
            form.color = '';
            form.description = '';
        }
        
        return {
            form, save, delete_section, edit_form, clean, prop
        }
    },  
  
  computed: {
    sections() {
      return this.$store.getters.allSections;
    }
  },
  async created() {
    this.$store.dispatch('fetchSection');
    localStorage.id = null    
  }

}
</script>