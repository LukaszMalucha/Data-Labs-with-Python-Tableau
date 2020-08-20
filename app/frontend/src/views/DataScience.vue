<template>
<div id="page-index">
  <RowHeaderComponent/>

    <div class="dashboard-cards">
      <br>
      <div class="row">
        <div class="col-data-left">
          <div class="section-left text-left" id="dataScienceLeft">
              <div class="row plain-element">
                <h5>DATA SCIENCE IN BIG 5 - SEPTEMBER 2018</h5>
                <p>What's the ultimate Data Science toolbox? Let us find out by analyzing LinkedIn profiles of Data
                    Scientists in 5 prominent IT Companies - Amazon, Apple, Facebook, Google and Microsoft.
                    Source: <a target="_blank" href="https://www.linkedin.com/"> Linkedin</a></p>

              </div>

              <div class="row plain-element">
                <h5>DO YOU HAVE WHAT IT TAKES?</h5>
                <p> To test your own LinkedIn profile skillset against skillsets of top tier Data Scientists, list your skills separated by comma below: </p>
                <form form @submit.prevent="onSubmit" class="col s12">
                  <div class="row plain-element">
                     <div class="form-group">
                      <textarea class="form-control" rows="3" v-model="skillset" placeholder="List your skills..."></textarea>
                     </div>
                  </div>
                  <div class="row plain-element">
                    <button type="submit" class="btn-enter"><span>Evaluate My Skillset
                                <i class="far fa-arrow-alt-circle-right"></i></span>
                    </button>
                  </div>
                </form>
              <div v-if="error" class="row row-error text-center">
                <div class="row"></div>
                <h5  class="muted error-message">{{ error }}</h5>
              </div>
              </div>
              <div class="row plain-element">
              <div id="foundChart">
                  <h5>DATA SCIENTISTS LIST:</h5>
                  <found-chart  :chart-data="foundChartData" :styles="chartStyles"></found-chart>
              </div>
              </div>
          </div>
        </div>
        <div class="col-data-center">
            <div class="section-viz">
              <div id="divDataScienceViz">
              </div>
            </div>
        </div>
        <div class="col-data-right">
          <div class="section-right text-left" id="dataScienceRight">
            <div class="row plain-element">
              <div id="missingChart">
                  <h5>SKILLS YOU ARE MISSING:</h5>
                  <missing-chart  :chart-data="missingChartData" :styles="chartStyles"></missing-chart>
              </div>
              </div>
          </div>
        </div>
      </div>
    </div>
</div>
</template>


<script>
import { apiService } from "@/common/api.service.js";
import RowHeaderComponent from "@/components/RowHeader.vue";
import FoundChart from "@/common/FoundChart.js"
import MissingChart from "@/common/MissingChart.js"

export default {
  name: "DataScience",
  components: {
        RowHeaderComponent,
        FoundChart,
        MissingChart,
  },
  data() {
    return {
      divElement: null,
      DataScienceViz: null,
      vizContainer: null,
      skillset: "",
      error: "",
      found: {},
      missing: {},
      foundChartData: {},
      missingChartData: {},
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
    onSubmit() {
      if (this.skillset == "") {
        this.error = "You have to list some skills.";
        document.getElementById("foundChart").style.display = "none"
        document.getElementById("missingChart").style.display = "none"
      } else {
        let endpoint = "/api/test-profile/";
        let method = "POST";
        apiService(endpoint, method, { skills: this.skillset })
        .then(data => {
          this.error = "";
          this.found = data.found;
          this.missing = data.missing;
          document.getElementById("foundChart").style.display = "block"
          document.getElementById("missingChart").style.display = "block"
          this.fillFoundChart();
          this.fillMissingChart();
        })
      }
    },
    fillFoundChart() {
      var dataset = this.found
      var dataLabels = Object.keys(dataset)
      var dataValues = Object.values(dataset)
      this.foundChartData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#2b5b89","#356899", "#5789b6", "#7bb0d5",
                              "#89bddc", "#90c3df", "#98c8e2", "#9ccae3", "#9ccae3"],
            data: dataValues
          }
        ]
      }
    },
    fillMissingChart() {
      var dataset = this.missing
      var dataLabels = Object.keys(dataset)
      var dataValues = Object.values(dataset)
      this.missingChartData = {
        labels: dataLabels,
        datasets: [
          {
            backgroundColor: ["#2b5b89","#2b5b89","#356899", "#356899","#5789b6", "#5789b6","#7bb0d5","#7bb0d5",
                             "#89bddc", "#89bddc","#90c3df", "#90c3df", "#98c8e2", "#9ccae3", "#9ccae3",
                             "#9ccae3", "#9ccae3", "#9ccae3", "#9ccae3","#9ccae3", "#9ccae3"],
            data: dataValues
          }
        ]
      }
    },

  },
  computed: {
    chartStyles () {
      return {
        height: `100%`,
        position: "relative"
      }
    }
  },
  mounted() {
      this.getViz()
  },
  created() {
    document.title = "Data Science in Big 5";
  }
}


</script>

