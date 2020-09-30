<template>
  <div id="app">
  <Header />
  <AddTodo v-on:add-todo="addTodo"/>
	<Todos v-bind:todos="todos" v-on:del-todo="deleteTodo"/>
  </div>
</template>
	
<script>
import Todos from '../components/Todos.vue'
import AddTodo from '../components/AddTodo.vue'
import axios from 'axios'

export default {
  name: 'Home',
  components: {
    Todos,
	
	AddTodo
  },
  data(){
	return {
		todos:[/*
			{
				id:1,
				title:"Todo one",
				completed:false
			},
			{
				id:2,
				title:"Todo two",
				completed:true
			},
			{
				id:3,
				title:"Todo three",
				completed:false
			},*/
		]
	}
  },
  
  methods:{
		deleteTodo(id){
			axios.delete(`https://jsonplaceholder.typicode.com/todos/${id}`)
				.then(function(){
					
					this.todos = this.todos.filter(todo => todo.id !== id)
				}.bind(this))
				.catch(err => console.log(err))
			
		},
		
		addTodo(newTodo){
			//title and completed from the new todo
			const {title, completed } = newTodo
			axios.post('https://jsonplaceholder.typicode.com/todos', {
				title,
				completed
			})
			//add new todo to the server and then show in the ui
			.then(res => this.todos = [...this.todos, res.data])
			.catch(err => console.log(err))
		}
	},
	
	created(){
			axios.get('https://jsonplaceholder.typicode.com/todos?_limit=5')
				.then(res => this.todos = res.data)
				.catch(err => console.log(err))
		}
}
</script>

<style>

</style>
