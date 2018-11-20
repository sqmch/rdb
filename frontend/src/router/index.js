import Vue from 'vue'
import Router from 'vue-router'
import VueMaterial from 'vue-material'
import VueVisible from 'vue-visible'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default-dark.css'
import VueCharts from 'hchs-vue-charts'

Vue.use(Router)
Vue.use(VueMaterial)
Vue.use(VueVisible)
Vue.use(VueCharts)

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
  component: 'Histstats'
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
