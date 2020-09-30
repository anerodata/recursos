<template>
	<div>
		<h3>Todos</h3>
		<div class="todos">
			<div @dblclick="onDblClick(todo)" v-for="todo in allTodos" :key="todo.id" class="todo" v-bind:class="{'is-completed':todo.completed}">
				{{todo.title}}
				<span id="delete" @click="deleteTodo(todo.id)">x</span>
			</div>
		</div>
	</div>
</template>

<script type="text/javascript">
	import { mapGetters ,mapActions } from 'vuex'
	export default {
		name: "Todos",
		methods: {
			// ... allows to add more methods
			...mapActions(['fetchTodos', 'deleteTodo', 'updateTodo']),
			onDblClick(todo) {
				const updTodo = {
					id: todo.id,
					title: todo.title,
					completed: !todo.completed
				}
				this.updateTodo(updTodo)
			}
		},
		computed: mapGetters(['allTodos']),
		created() {
			this.fetchTodos()
		}
	}
</script>

<style type="text/css" scoped>
	.todo.is-completed{
		background-color: lightgreen;
	}
	#delete {
		color: white;
		padding: 2px 5px;
		background-color: Crimson;
		cursor: pointer;
	}
	.todos {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		grid-gap: 1rem;
	}
	.todo {
		background-color: lightblue;
		text-align: center;
		padding: 1rem;
	}
</style>