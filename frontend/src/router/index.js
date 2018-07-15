import Vue from 'vue'
import Router from 'vue-router'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default-dark.css'

Vue.use(Router)
Vue.use(VueMaterial)

const routerOptions = [{
  path: '/',
  component: 'Home'
},
{
  path: '/misc',
  component: 'Misc'
},
{
  path: '/stats',
  component: 'Stats'
}
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () =>
      import(`@/components/${route.component}.vue`)
  }
})

export default new Router({
  routes,
  mode: 'history'
})
