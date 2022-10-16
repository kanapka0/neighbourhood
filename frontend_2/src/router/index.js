import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NeededPage from "@/components/NeededPage";
import PetitionPage from "@/components/PetitionPage";
import ComunicatsPage from "@/components/ComunicatsPage";
import ContactPage from "@/components/ContactPage";
import HelpPage from "@/components/HelpPage";
import MapPage from "@/components/MapPage";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/needed',
    name: 'needed',
    component: NeededPage
  },
  {
    path: '/petition',
    name: 'petition',
    component: PetitionPage
  },
  {
    path: '/comunicats',
    name: 'comunicats',
    component: ComunicatsPage
  },
  {
    path: '/contacts',
    name: 'contacts',
    component: ContactPage
  },
  {
    path: '/help',
    name: 'help',
    component: HelpPage
  },
  {
    path: '/map',
    name: 'map',
    component: MapPage
  },

]

const router = new VueRouter({
  routes
})

export default router
