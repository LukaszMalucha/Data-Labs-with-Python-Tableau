<template>
<div id="page-index">
  <RowHeaderComponent/>

    <div class="dashboard-cards">
      <br>
      <div class="row">
        <div class="col-data-left">
          <div class="section-left text-left" id="dataScienceLeft">
              <div class="box">
                <h5>DATA SCIENCE IN BIG 5 - SEPTEMBER 2018</h5>
              </div>
              <p>What is the ultimate toolbox for Data Science? Let's find out by analyzing LinkedIn profiles of Data
                  Scientists in most prominent IT Companies - Amazon, Apple, Facebook, Google and Microsoft. Then
                  test your own LinkedIn profile skillset against skillsets of top tier Data Scientists. </p>
              <p>Data Source: <a target="_blank" href="https://www.linkedin.com/"> Linkedin</a></p>
          </div>
        </div>
        <div class="col-data-center">
            <div class="section-viz">
              <div id="divDataScienceViz">
              </div>
            </div>
        </div>
        <div class="col-data-right">
          <div class="section-right text-left" id="dataScienceRight"></div>
        </div>
      </div>
    </div>
</div>
</template>


<script>
import RowHeaderComponent from "@/components/RowHeader.vue";

export default {
  name: "DataScience",
  components: {
        RowHeaderComponent
  },
  data() {
    return {
      divElement: null,
      DataScienceViz: null,
      vizContainer: null,

    }
  },
  methods: {
    getViz() {
        this.vizElementDS = document.getElementById('dataScience');
        if (this.vizElementDS) {
          this.DataScienceVizDS = this.vizElementDS.cloneNode(true);
          this.DataScienceVizDS.id = "VizDS";
          this.DataScienceVizDS.style.height = '740px';
          document.getElementById('divDataScienceViz').appendChild(
            this.DataScienceVizDS
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

