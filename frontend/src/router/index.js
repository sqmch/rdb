import Vue from 'vue'
import Router from 'vue-router'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default-dark.css'

Vue.use(VueMaterial)

const routerOptions = [{
  path: '/',
  component: 'Home'
},
{
  path: '/about',
  component: 'About'
}
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () =>
      import(`@/components/${route.component}.vue`)
  }
})
Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
