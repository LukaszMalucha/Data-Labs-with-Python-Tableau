<template>
  <div class="row header">
      <div class="row top-menu">
        <div class="col-sm-2 col-md-1  col-lg-1 plain-element col-logo">
          <a>
            <img src="@/assets/tableau.png"
                 class="img responsive tableau" alt="Tableau logo"/>
          </a>
        </div>
        <div class="col-sm-12 col-md-11 col-lg-11 plain-element">
          <ul>
            <li>
              <a>Data Science in Big 5</a>
            </li>
            <li>
              <a>Daft.ie Analytics</a>
            </li>
            <li>
              <a>GitHub Activity</a>
            </li>
            <li>
              <router-link :to="{name: 'life-expectancy'}">World Life Expectancy</router-link>
            </li>
            <li class="link-extras"><a>Seismic Awakening</a></li>
            <li class="link-extras"><a>World 1960 -2013</a></li>
            <li class="link-extras"><a>Taxi Rush Hour</a></li>
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