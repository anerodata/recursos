<template>
  <div class="hello">
    <li> 
      <img class="post-img" :src="commentpost.authorImg" /> 
      <small>{{ commentpost.author }}</small>
      <p class="post-comment">"{{ commentpost.text }}"</p>
    </li>
  </div>
</template>

<script>
export default {
  name: 'MessageItem',
  props: ["commentpost"]
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
li {
  list-style: none outside none;
  text-align: left;
  padding: 10px 0;
  border-bottom: 1px solid #555;
}
.post-img {
  border: 3px solid white;
  float: left;
  margin: 0 15px 0 -2px;
  transition: 0.3s all ease;
}
.post-comment {
  margin: 0 0 5px 0;
}
</style>
