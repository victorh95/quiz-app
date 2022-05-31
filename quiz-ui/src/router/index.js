import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import AdminPage from '../views/AdminPage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsManager from '../views/QuestionsManager.vue'
import ScorePage from '../views/ScorePage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/admin',
      name: 'AdminPage',
      component: AdminPage
    },
    {
      path: '/new-quiz',
      name: 'NewQuizPage',
      component: NewQuizPage
    },
    {
      path: '/questions',
      name: 'QuestionsManager',
      component: QuestionsManager
    },
    {
      path: '/score',
      name: 'ScorePage',
      component: ScorePage
    }
  ]
})

export default router
