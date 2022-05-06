<template>
  <div class="place">
    <img :src="location.img"/>
    <header>
      <slot name="header"></slot>
      <h2>{{location.name}}</h2>
    </header>
    <p>{{location.desc}}</p>
  </div>
</template>
<script>
export default {
  name: "LocationItem",
  props: ["location"],
}
</script>
<style>
.place {
  display: flex;
  flex-direction: column;
  width: 280px;
  justify-content: center;
  background: white;
  border: 1px solid #ddd;
  padding: 20px 20px;
  margin: 10px;
  h2 {
    margin: 0;
    text-align: center;
  }
  img {
    margin: 10px;
    align-self: center;
  }
}
</style>
