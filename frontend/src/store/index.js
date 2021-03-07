import { createStore } from 'vuex'
import sections from './modules/section'

export default createStore({
    state: () => ({
        todos: []
    }),
    mutations: {
        addTodo(state, item) {
            state.todos.unshift(item);
        }
    },
    getters: {
        getTodos (state) {
            return state.todos;
        },
        todoCount (state) {
            return state.todos.length;
        }
    },
    modules: {
        sections
    }
});
