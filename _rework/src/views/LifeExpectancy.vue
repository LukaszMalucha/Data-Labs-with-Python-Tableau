<template>
<div id="page-index">

  <div class="row row-banner">
    <div class="col-md-12 text-center col-banner plain-element">
      <h4>LIFE EXPECTANCY AT BIRTH, 1960-2015</h4>
    </div>
  </div>
    <div class="dashboard-cards">
      <div class="row">
        <div class="col-md-12">
            <div class="section-center">
            <div class="card tableau_card" id="tableauViz">

            </div>
            </div>
        </div>
      </div>
    </div>
</div>
</template>


<script>


export default {
  name: "LifeExpectancy",
  components: {

  },
  data() {
    return {
      divElement: null,
      lifeExpectancyViz: null,
      vizContainer: null,

    }
  },
  methods: {
    getViz() {
        this.vizElement = document.getElementById('lifeExpectancy');
        if (this.vizElement) {
          this.lifeExpectancyViz = this.vizElement.cloneNode(true);
          this.lifeExpectancyViz.id = "Viz";
          this.lifeExpectancyViz.style.height = '800px';
          document.getElementById('tableauViz').appendChild(
            this.lifeExpectancyViz
          );
        }
    },

  },
  mounted() {
      this.getViz()
  },
  created() {
  }
}


</script>

