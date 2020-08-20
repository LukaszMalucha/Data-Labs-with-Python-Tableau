<template>
  <div class="row header">
      <div class="row top-menu">
        <div class="col-sm-2 col-md-1  col-lg-1 plain-element col-logo">
          <router-link :to="{name: 'home'}">
            <img src="@/assets/tableau.png"
                 class="img responsive tableau" alt="Tableau logo"/>
          </router-link>
        </div>
        <div class="col-sm-12 col-md-11 col-lg-11 plain-element">
          <ul>
            <li>
              <router-link :to="{name: 'data-science'}">Data Science in Big 5</router-link>
            </li>
            <li>
              <router-link :to="{name: 'daft-analytics'}">Daft.ie Analytics</router-link>
            </li>
            <li>
              <router-link :to="{name: 'github-activity'}">GitHub Activity</router-link>
            </li>
            <li>
              <router-link :to="{name: 'life-expectancy'}">World Life Expectancy</router-link>
            </li>
            <li class="link-extras"><a target="_blank" href="https://public.tableau.com/profile/lukaszmaluchadataviz#!/vizhome/SeismicAwakening/EarthquakesVulcanoes">Seismic Awakening</a></li>
            <li class="link-extras"><a target="_blank" href="https://public.tableau.com/profile/lukaszmaluchadataviz#!/vizhome/WorldDemographic1960-2013/WorldDemographics">Demographics 1960 -2013</a></li>
            <li class="link-extras"><a target="_blank" href="https://public.tableau.com/profile/lukaszmaluchadataviz#!/vizhome/TheRushHour/TheRushHour">Taxi Rush Hour</a></li>
          </ul>
        </div>
      </div>
    </div>
</template>

<script>
export default {
    name: "RowHeaderComponent"
}

</script>