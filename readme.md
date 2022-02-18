## Springboard Analytics

#### [Visit the App](https://springboardanalytics.herokuapp.com/)

<br>

![5](https://user-images.githubusercontent.com/26208598/97291419-cd39f300-1841-11eb-8a3a-f004697925be.PNG)

<br>

## App Description

Django App that allows user to:

1. Scrape and clean course data from Springboardcourses.ie - manually or with scheduled task
2. Load course data to postgres db.
2. Interact with data through Vue.js fronted or directly through Django REST backend.


## App Views

#### Main Dashboard
##### `/`

Main App Navigation

<br>

![1](https://user-images.githubusercontent.com/26208598/97290937-25242a00-1841-11eb-9e28-5da7dac98fa2.PNG)

<br>

-----------------


#### User Handling
##### `/user/`

 User Handling views - register, login, forgot password

<br>

![2](https://user-images.githubusercontent.com/26208598/97290932-23f2fd00-1841-11eb-8a8d-3040970071ad.PNG)

<br>

-----------------

#### Springboard Statistics
##### `/course-statistics`

 Statistical data with Chart.js.

<br>

![3](https://user-images.githubusercontent.com/26208598/97290934-248b9380-1841-11eb-8cb7-9d8360135738.PNG)

-----------------

## Django REST Endpoints

#### User
##### `/api/`

 User handling via RESTFUL Api with Token Authorization.

<br>

![7](https://user-images.githubusercontent.com/26208598/53902106-5fbbcc00-4038-11e9-9ed0-848d3e11c1da.png)

<br>

-----------------

#### Courses Data
##### `/api/courses`

 Springboard.ie courses data via RESTFul Api.

<br>

![4](https://user-images.githubusercontent.com/26208598/97290935-25242a00-1841-11eb-9ed5-46b43c420351.PNG)

<br>

-----------------

### App Testing:

##### `/api/tests/`
##### `/core/tests/` 
##### `/user/tests/`

-----------------

## TOOLS, MODULES & TECHNIQUES

##### Backend Development:
Django RESTful

##### Data Analysis
pandas | numpy | sklearn | scipy

##### Frontend Development
Vue.js | Vuex | Materialize | Chart.js

##### Deployment
Docker | Heroku | Travis CI | AWS S3

##### Web Scraping:
beautifulsoup4

##### Testing
django.test | coverage

#### NPM

npm install --save axios loadash qs vue-router

npm install --save vuex 

npm install --save-dev webpack-bundle-tracker@0.4.3    

npm install --save vue-chartjs chart.js  
