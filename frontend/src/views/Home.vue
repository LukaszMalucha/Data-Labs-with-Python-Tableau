<template>
<div id="page-index">
  <RowHeaderComponent/>
  <RowBannerComponent/>
  <div class="dashboard-cards">
      <div class="row">
        <div class="col-md-2 col-left">
          <div class="section-left">
            <div class="section-heading text-left">
              New Projects
            </div>
            <div class="single-project">
              <div class="col-md-3 text-left plain-element">
                <img src="https://lm-data-labs.s3-eu-west-1.amazonaws.com/static/img/projects/thompson.jpg" class="img responsive single-project-img"
                     alt="project img"/>
              </div>
              <div class="col-md-9 text-left col-project-content">
                <div class="row plain-element">
                  <a target="_blank" href="http://www.thompsonsampling.com/" class="single-project-title">Thompson Sampling</a>
                </div>
                <div class="row plain-element">
                  <a target="_blank" href="http://www.thompsonsampling.com/" class="btn subscribe-btn"> Visit Project</a>
                </div>
              </div>
            </div>
            <div class="single-project">
              <div class="col-md-3 text-left plain-element">
                <img src="https://lm-data-labs.s3-eu-west-1.amazonaws.com/static/img/projects/blockchain.jpg" class="img responsive single-project-img"
                     alt="project img"/>
              </div>
              <div class="col-md-9 text-left col-project-content">
                <div class="row plain-element">
                  <a target="_blank" href="http://www.minerstartup.com" class="single-project-title">Blockchain Example</a>
                </div>
                <div class="row plain-element">
                  <a target="_blank" href="http://www.minerstartup.com" class="btn subscribe-btn"> Visit Project</a>
                </div>
              </div>
            </div>
            <div class="single-project">
              <div class="col-md-3 text-left plain-element">
                <img src="https://lm-data-labs.s3-eu-west-1.amazonaws.com/static/img/projects/quant.jpg" class="img responsive single-project-img"
                     alt="project img"/>
              </div>
              <div class="col-md-9 text-left col-project-content">
                <div class="row plain-element">
                  <a target="_blank" href="http://www.quantproperties.com/" class="single-project-title">Quant Properties</a>
                </div>
                <div class="row plain-element">
                  <a target="_blank" href="http://www.quantproperties.com/" class="btn subscribe-btn"> Visit Project</a>
                </div>
              </div>
            </div>
            <div class="single-project">
              <div class="col-md-3 text-left plain-element">
                <img src="https://lm-data-labs.s3-eu-west-1.amazonaws.com/static/img/projects/unflasking.jpg" class="img responsive single-project-img"
                     alt="project img"/>
              </div>
              <div class="col-md-9 text-left col-project-content">
                <div class="row plain-element">
                  <a target="_blank" href="http://www.unflasked.com/" class="single-project-title">Unflasking AI</a>
                </div>
                <div class="row plain-element">
                  <a target="_blank" href="http://www.unflasked.com/" class="btn subscribe-btn"> Visit Project</a>
                </div>
              </div>
            </div>
            <div class="single-project">
              <div class="col-md-3 text-left plain-element">
                <img src="https://lm-data-labs.s3-eu-west-1.amazonaws.com/static/img/projects/cat_dog.jpg" class="img responsive single-project-img"
                     alt="project img"/>
              </div>
              <div class="col-md-9 text-left col-project-content">
                <div class="row plain-element">
                  <a target="_blank" href="http://www.septellar.com/" class="single-project-title">Cat Dog Classifier</a>
                </div>
                <div class="row plain-element">
                  <a target="_blank" href="http://www.septellar.com/" class="btn subscribe-btn"> Visit Project</a>
                </div>
              </div>
            </div>
            <div class="single-project">
              <div class="col-md-3 text-left plain-element">
                <img src="https://lm-data-labs.s3-eu-west-1.amazonaws.com/static/img/projects/twitter.jpg" class="img responsive single-project-img"
                     alt="project img"/>
              </div>
              <div class="col-md-9 text-left col-project-content">
                <div class="row plain-element">
                  <a target="_blank" href="http://www.tweetever.com/" class="single-project-title">Top 10 US Trends</a>
                </div>
                <div class="row plain-element">
                  <a target="_blank" href="http://www.tweetever.com/" class="btn subscribe-btn"> Visit Project</a>
                </div>
              </div>
            </div>
            <div class="single-project">
              <div class="col-md-3 text-left plain-element">
                <img src="https://lm-data-labs.s3-eu-west-1.amazonaws.com/static/img/projects/yahoo.png" class="img responsive single-project-img"
                     alt="project img"/>
              </div>
              <div class="col-md-9 text-left col-project-content">
                <div class="row plain-element">
                  <a target="_blank" href="http://www.findmecity.com/" class="single-project-title">Yahoo WOEID Search</a>
                </div>
                <div class="row plain-element">
                  <a target="_blank" href="http://www.findmecity.com/" class="btn subscribe-btn"> Visit Project</a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-8 col-center">
          <div class="section-center">
            <div class="section-heading text-left">
              Most popular
            </div>
            <div class="row plain-element row-medium-projects">
              <div class="col-xs-4 col-sm-4 col-md-4 col-lg-4 col-project-left">
                <div class="single-project-left">
                  <img src="https://lm-data-labs.s3-eu-west-1.amazonaws.com/static/img/daft_analytics.png"
                       class="img responsive img-project-medium" alt="Tableau Public"/>
                </div>
                <div class="single-project-content content-side text-left">
                <router-link :to="{name: 'daft-analytics'}"><span>Daft.ie Analytics</span><br>
                    Daft.ie property market analysis.</router-link>
                </div>
              </div>
              <div class="col-xs-4 col-sm-4 col-md-4 col-lg-4 plain-element col-project-center">
                <div class="single-project-center">
                  <img src="https://lm-data-labs.s3-eu-west-1.amazonaws.com/static/img/git_activity.png"
                       class="img responsive img-project-medium" alt="Tableau Public"/>
                </div>
                <div class="single-project-content content-center text-left">
                  <router-link :to="{name: 'github-activity'}"><span>Github Activity</span><br>
                    My GitHub Activity on Radial Bar Chart.</router-link>
                </div>
              </div>
              <div class="col-xs-4 col-sm-4 col-md-4 col-lg-4 plain-element col-project-right">
                <div class="single-project-right">
                  <img src="https://lm-data-labs.s3-eu-west-1.amazonaws.com/static/img/life_expectancy.png"
                       class="img responsive img-project-medium" alt="Tableau Public"/>
                </div>
                <div class="single-project-content content-side text-left">
                  <router-link :to="{name: 'life-expectancy'}"><span>World Life Expectancy</span><br>
                    Visualizing increase in world life expectancy.</router-link>
                </div>
              </div>
            </div>
            <div class="section-heading text-left">
              Data Scientists in Big 5
            </div>
            <div class="row plain-element">
              <div class="col-xs-4 col-sm-4 col-md-4 col-lg-4 plain-element col-img-lg">
                <img src="https://lm-data-labs.s3-eu-west-1.amazonaws.com/static/img/data_science.png"
                     class="img responsive img-section img-project-lg" alt="Tableau Public"/>
              </div>
              <div class="col-xs-8 col-sm-8 col-md-8 col-lg-8">
                <div class="row plain-element text-left">
                  <router-link :to="{name: 'data-science'}" class="link-date">MAY 21, 2019 / Data Science</router-link>
                </div>
                <div class="row plain-element text-left">
                  <h5>What is the ultimate toolbox for Data Science?</h5>
                </div>
                <div class="section-text text-left">
                  What is the ultimate toolbox for Data Science? Let's find out by analyzing LinkedIn profiles of Data
                  Scientists in most prominent IT Companies
                  - Amazon, Apple, Facebook, Google and Microsoft. Then test your own LinkedIn profile skillset against
                  skillsets of top tier Data Scientists.
                </div>
                <div class="row plain-element text-left">
                <router-link :to="{name: 'data-science'}" class="link-visit-lg">Visit Dashboard</router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-2 col-right">
          <div class="section-right">
            <div class="section-heading text-left">
              Tableau Public
            </div>
            <div class="section-text text-center">
              To get more live interaction with data dashboards please visit my Tableau Public:
            </div>
            <div class="section-image">
              <img src="https://lm-data-labs.s3-eu-west-1.amazonaws.com/static/img/public.png"
                   class="img responsive img-section" alt="Public"/>
            </div>
            <div class="row plain-element">
              <button type="submit" class="btn btn-visit"
                onclick="window.open('https://public.tableau.com/profile/lukaszmaluchadataviz#!/')">Tableau Public</button>
            </div>
            <br>
            <div class="section-heading text-left">
              Coding Portfolio
            </div>
            <div class="section-text text-center">
              My python portfolio including Django & Flask REST applications,
              AI and data analysis concepts:
            </div>
            <div class="section-image">
              <img src="https://lm-data-labs.s3-eu-west-1.amazonaws.com/static/img/portfolio.png"
                   class="img responsive img-section" alt="Public"/>
            </div>
            <div class="row plain-element">
            <button type="submit" class="btn btn-visit"
                onclick="window.open('https://www.lukaszmalucha.com/')">Code Portfolio</button>
            </div>
          </div>
        </div>
      </div>
    </div>
</div>
</template>





<script>
import RowHeaderComponent from "@/components/RowHeader.vue";
import RowBannerComponent from "@/components/RowBanner.vue";

export default {
  name: 'home',
  components: {
    RowHeaderComponent,
    RowBannerComponent
  },
  created() {
    document.title = "Data Labs";
  }
};

</script>