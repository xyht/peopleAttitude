// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueResource from 'vue-resource'

import Vant from 'vant'
import 'vant/lib/vant-css/index.css'

Vue.config.productionTip = false

/* eslint-disable no-new */
Vue.use(Vant)
Vue.use(VueResource)
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
