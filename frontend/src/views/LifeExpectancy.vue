<template>
<div id="page-index">
  <RowHeaderComponent/>

    <div class="dashboard-cards">
      <div class="row">
        <div class="col-md-2 col-left">
          <div class="section-left text-left" id="textLife">
          <h5>LIFE EXPECTANCY AT BIRTH, 1960-2015</h5>
            <p>In the early years of previous century, life expectancy started to grow as an effect of ongoing industrialization. But the growth wasn't equal worldwide. Dramatic improvement of living standard in
                    developed countries stood in stark contrast to the poor regions. Over the last decades this tendencies decreased, what is shown in the Tableau Visualization below.</p>
                <p>Data Source: <a target="_blank" href="https://data.worldbank.org/indicator/SP.DYN.LE00.IN"> World Bank</a> </p>
          </div>
        </div>
        <div class="col-md-10 col-center">
            <div class="section-viz">
              <div id="divLifeExpectancyViz">

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
  name: "LifeExpectancy",
  components: {
        RowHeaderComponent
  },
  data() {
    return {
      divElementLE: null,
      lifeExpectancyVizLE: null,
      vizContainerLE: null,

    }
  },
  methods: {
    getViz() {
        this.vizElementLE = document.getElementById('lifeExpectancy');
        if (this.vizElementLE) {
          this.lifeExpectancyVizLE = this.vizElementLE.cloneNode(true);
          this.lifeExpectancyVizLE.id = "Viz";
          this.lifeExpectancyVizLE.style.height = '740px';
          document.getElementById('divLifeExpectancyViz').appendChild(
            this.lifeExpectancyVizLE
          );
        }
    },

  },
  mounted() {
      this.getViz()
  },
  created() {
    document.title = "Life Expectancy";
  }
}


</script>

