import { createStore } from 'vuex'

export default createStore({
  state: {
    comments: [
      {
        text: 'Looks great Julianne!',
        author: 'Robin Rendle',
        authorImg: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/28963/v-coffee.jpg'
      },
      {
        text: 'I love the Sea',
        author: 'Miriam Suzanne',
        authorImg: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/28963/v-miriam.jpg'
      },
      {
        text: 'Where are you?',
        author: 'Geoff Graham',
        authorImg: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/28963/v-geoff.jpg'
      }
    ]
  },
  getters: {
  },
  mutations: {
    addComment(state, newComment) {
      const newCommentObj = {
        text: newComment,
        author: 'Magoo',
        authorImg: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/28963/v-skull.jpg'
      };
      state.comments.push(newCommentObj);
    }
  },
  actions: {
  },
  modules: {
  }
})
