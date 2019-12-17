import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import NotFound from "./views/NotFound.vue";
import LifeExpectancy from "./views/LifeExpectancy.vue";
import GithubActivity from "./views/GithubActivity.vue";
import DataScience from "./views/DataScience.vue";
import DaftAnalytics from "./views/DaftAnalytics.vue";

Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/life-expectancy",
      name: "life-expectancy",
      component: LifeExpectancy
    },
    {
      path: "/github-activity",
      name: "github-activity",
      component: GithubActivity
    },
    {
      path: "/data-science",
      name: "data-science",
      component: DataScience
    },
    {
      path: "/daft-analytics",
      name: "daft-analytics",
      component: DaftAnalytics
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound,
    },
  ]
})
