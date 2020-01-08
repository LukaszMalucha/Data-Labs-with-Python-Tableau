<template>
<div id="page-index">
  <RowHeaderComponent/>

    <div class="dashboard-cards">
      <div class="row">
        <div class="col-md-12 col-left">
          <div class="section-viz">
               <div class="row summary text-left">
                  <div class="box">
                      <h5>DAFT PROPERTY PRICES - AUGUST 2018 </h5>
                      <a target="_blank" href="http://www.quantproperties.com/" class="btn-algorithm">Estimate Property</a>
                  </div>
                  <p>This visualization was created to show current property market situation in four major cities of
                      Ireland - Cork, Dublin, Galway & Limerick. Magic quadrant-style data display allows to determine most
                      attractive investments based on price & energy rating (BER). Additionally, user is in control of
                      specifying his current budget, number of bedrooms required and city area. Data Source:
                      <a target="_blank" href="https://www.daft.ie/"> Daft.ie</a></p>

              </div>
              <div id="divDaftAnalyticsViz">

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
  name: "DaftAnalytics",
  components: {
        RowHeaderComponent
  },
  data() {
    return {
      divElement: null,
      daftAnalyticsViz: null,
      vizContainer: null,

    }
  },
  methods: {
    getViz() {
        this.vizElementDA = document.getElementById('daftAnalytics');
        if (this.vizElementDA) {
          this.daftAnalyticsVizDA = this.vizElementDA.cloneNode(true);
          this.daftAnalyticsVizDA.id = "VizDA";
          this.daftAnalyticsVizDA.style.height = '950px';
          document.getElementById('divDaftAnalyticsViz').appendChild(
            this.daftAnalyticsVizDA
          );
        }
    },

  },
  mounted() {
      this.getViz()
  },
  created() {
    document.title = "Daft Analytics";
  }
}


</script>

