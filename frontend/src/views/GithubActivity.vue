<template>
<div id="page-index">
  <RowHeaderComponent/>

    <div class="dashboard-cards">
      <div class="row">
        <div class="col-md-2 col-left">
          <div class="section-left text-left" id="textGithub">
          <h5>GITHUB ACTIVITY A.D. 2018</h5>
            <p>2018 was very busy year so far. Over 900 contributions and still three months to go... I did some
                data mining on my own Selenium-scraped repository<br> to find out
                which days are the best to schedule some social activities. I also found out great use for this
                beautiful Radial Bar Chart vizualization. </p>
            <p>Data Source: <a target="_blank" href="https://lukaszmalucha.github.io/portfolio/"> Github</a></p>
          </div>
        </div>
        <div class="col-md-10 col-center">
            <div class="section-viz" >
              <div id="divGithubActivityViz">

              </div>
            </div>
        </div>
      </div>
    </div>
</div>
</template>


<script>
import RowHeaderComponent from "@/components/RowHeader.vue";

export default {
  name: "GithubActivity",
  components: {
        RowHeaderComponent
  },
  data() {
    return {
      divElement: null,
      githubActivityViz: null,
      vizContainer: null,

    }
  },
  methods: {
    getViz() {
        this.vizElementGA = document.getElementById('githubActivity');
        if (this.vizElementGA) {
          this.githubActivityVizGA = this.vizElementGA.cloneNode(true);
          this.githubActivityVizGA.id = "VizGA";
          this.githubActivityVizGA.style.height = '740px';
          document.getElementById('divGithubActivityViz').appendChild(
            this.githubActivityVizGA
          );
        }
    },

  },
  mounted() {
      this.getViz()
  },
  created() {
    document.title = "Github Activity";
  }
}


</script>

