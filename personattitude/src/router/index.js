import Vue from 'vue'
import Router from 'vue-router'
import video from './../components/video'
import photo from './../components/photo'
Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // }
    {
      path: '/video',
      name: 'video',
      component: video
    },
    {
      path: '/',
      name: 'photo',
      component: photo
    }
  ]
})
