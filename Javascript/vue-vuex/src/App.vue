<template>
  <div id="app">
    <div class="container">
      <AddTodo/>
      <FilterTodos/>
      <Todos/>
    </div>
  </div>
</template>

<script>
import Todos from './components/Todos.vue'
import AddTodo from './components/AddTodo.vue'
import FilterTodos from './components/FilterTodo.vue'

export default {
  name: 'App',
  components: {
    Todos,
    AddTodo,
    FilterTodos
  }
}
</script>

<style>

</style>
