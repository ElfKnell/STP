<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div>
      <TodoNew />
      <TodoList />
    </div>

  </div>
</template>

<script>
import TodoNew from '@/components/TodoNew.vue';
import TodoList from '@/components/TodoList.vue';


export default {
  components: {
    TodoNew,
    TodoList
  }
}
</script>