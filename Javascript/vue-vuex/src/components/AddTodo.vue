<template>
  <div>
    <h3>Add Todo</h3>
    <div class="add">
      <form @submit="onSubmit">
        <input type="text" v-model="title" placeholder="Add todo">
        <input type="submit" value="Enviar">
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'AddTodo',
  data() {
    return {
      title: ''
    }
  },
  methods: {
    ...mapActions(['addTodo']),
    onSubmit(e) {
      e.preventDefault();
      this.addTodo(this.title)
    }
  }
}
</script>

<style scoped>
  form {
    display: flex;
  }

  form input[type="text"] {
    flex: 10;
    padding: 10px;
  }

  form input[type="submit"] {
    flex: 2;
    border: 1px;
    background-color: lightblue;
  }
</style>
