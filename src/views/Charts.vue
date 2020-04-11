<template>
  <div>
    <div class="vx-row " style="padding: 0 12px">
      <vs-select
        autocomplete
        multiple
        :placeholder="$t('selectCountriesToCompare')"
        class="selectExample mb-2"
        v-model="countrySelected"
        max-selected="5"
        v-on:change="addNewCountry"
        width="300px"
      >
        <vs-select-item :key="index" :value="item.value" :text="item.text" v-for="(item,index) in countries"/>
      </vs-select>
      <!--      <vs-checkbox style="margin-left: 5px;margin-bottom: 10px" v-model="predict" v-on:change="prediction">-->
      <!--        {{$t('predict')}}-->
      <!--      </vs-checkbox>-->
    </div>
    <div class="vx-row">
      <div class="md:w-1/2 w-full mb-base vx-col">
        <vx-card :title="$t('TotalInfected')">
          <canvas id="confirmedChart"></canvas>
        </vx-card>
      </div>
      <div class="md:w-1/2 w-full mb-base vx-col">
        <vx-card :title="$t('TotalInfectedByDay')">
          <canvas id="confirmedChartByDay"></canvas>
        </vx-card>
      </div>

      <div class="md:w-1/2 w-full mb-base vx-col">
        <vx-card :title="$t('TotalInfectedByPopulationConfirmed')">
          <canvas id="confirmedChartByPopulationConfirmed"></canvas>
        </vx-card>
      </div>
      <div class="md:w-1/2 w-full mb-base vx-col">
        <vx-card :title="$t('TotalDeathByPopulation')">
          <canvas id="DeathChartByPopulation"></canvas>
        </vx-card>
      </div>

      <div class="md:w-1/2 w-full mb-base vx-col">
        <vx-card :title="$t('Symptoms')">
          <symptoms/>
        </vx-card>
      </div>

      <div class="md:w-1/2 w-full mb-base vx-col">
        <vx-card :title="$t('WorldWidePercentage')">
          <percentage/>
        </vx-card>
      </div>

      <div class="md:w-1/2 w-full mb-base vx-col">
        <vx-card :title="$t('Preconditions')">
          <risk/>
        </vx-card>
      </div>

      <div class="md:w-1/2 w-full mb-base vx-col">
        <vx-card :title="$t('RiskGroup')">
          <illness/>
        </vx-card>
      </div>

    </div>
  </div>
</template>

<script>
  import symptoms from "@/components/SymptomsContainer.vue";
  import percentage from "@/components/PercentageContainer.vue";
  import illness from "@/components/RiskDataContainer.vue";
  import risk from "@/components/IlnessDataContainer.vue";
  import Chart from 'chart.js';
  import axios from "../axios";

  function addDays(date, days) {
    var result = new Date(date);
    result.setDate(result.getDate() + days);
    return result;
  }

  export default {
    components: {
      symptoms,
      percentage,
      illness,
      risk
    },
    data() {
      return {
        planetChartData: {},
        countrySelected: [],
        country: this.$store.state.country,
        countries: [],
        selectedCountries: {},
        confirmedChart: null,
        confirmedChartByDay: null,
        predict: false
      }
    },
    async mounted() {
      await this.getCountries()
      if (this.country) {
        this.initCharts()
      } else {
        const getIpResponse = await axios.get(
          "https://api.covidstatus.com/info_about_country"
        );
        this.country = getIpResponse.data;
        this.initCharts()
      }

    },
    methods: {
      createChart(chartId, chartData) {
        if (this[chartId]) {
          this[chartId].destroy()
        }
        const ctx = document.getElementById(chartId);
        this[chartId] = new Chart(ctx, {
          type: chartData.type,
          data: chartData.data,
          options: chartData.options,
        });
      },
      prediction() {
        this.initCharts()

      },
      async addNewCountry(codes) {
        this.selectedCountries = []
        for (let code in codes) {
          let country = await axios.get("https://api.covidstatus.com/cases/" + codes[code].toLowerCase(), {})
          this.selectedCountries[codes[code]] = country.data
        }
        this.initCharts()
      },
      async getCountries() {
        let self = this
        let countries = await axios.get("https://api.covidstatus.com/cases", {})
        countries.data.forEach(element => {
          self.countries.push({
            value: element.country_code,
            text: element.country_name,
          })
        });
      },
      async initCharts() {
        let response = await axios.get("https://api.covidstatus.com/cases/" + this.country.code.toLowerCase(), {})
        let from = Date.parse("2020-03-05");

        let dates = []
        let countryData = {
          confirmed: [],
          death: []
        }
        let countryDataByDay = {
          confirmed: [],
        }
        response.data.timeline.forEach(element => {
          if (from < Date.parse(element.date)) {
            dates.push(element.date)
            countryData.confirmed.push(element.total_cases)
            countryData.death.push(element.total_deaths)
            countryDataByDay.confirmed.push(element.new_daily_cases)
          }
        });
        if (this.predict) {
          let diff = null

          if (countryData.confirmed[countryData.confirmed.length - 1] == response.data.confirmed) {
            diff = countryDataByDay.confirmed[countryDataByDay.confirmed.length - 1] / countryDataByDay.confirmed[countryDataByDay.confirmed.length - 2]
          } else {
            diff = response.data.new_confirmed / countryDataByDay.confirmed[countryDataByDay.confirmed.length - 1]
          }
          for (let i = 1; i <= 7; i++) {
            let date = dates[dates.length - 1]
            let someDate = new Date(date);
            let numberOfDaysToAdd = 1;
            someDate.setDate(someDate.getDate() + numberOfDaysToAdd);
            let dd = someDate.getDate();
            let mm = someDate.getMonth() + 1;
            let y = someDate.getFullYear();
            let someFormattedDate = y + '-' + mm + '-' + dd;
            dates.push(someFormattedDate)
            countryDataByDay.confirmed.push(Math.round(countryDataByDay.confirmed[countryDataByDay.confirmed.length - 1] * diff))
            countryData.confirmed.push(Math.round(countryData.confirmed[countryData.confirmed.length - 1] + countryDataByDay.confirmed[countryDataByDay.confirmed.length - 1]))
          }
        }
        let countryDataByPopulation = {
          confirmed: [],
          death: []
        }
        for (let i = 0; i < countryData.confirmed.length; i++) {
          let confirmed = countryData.confirmed[i]
          let death = countryData.death[i]
          countryDataByPopulation.confirmed.push((confirmed * 100 / response.data.population).toFixed(5))
          countryDataByPopulation.death.push((death * 100 / response.data.population).toFixed(5))
        }

        let datasets = [{
          fill: false,
          label: this.country.code,
          data: countryData.confirmed,
          borderColor: '#fe8b36',
          backgroundColor: '#fe8b36',
          display: true
        }]
        let datasetsByPopulaionConfirmed = [{
          fill: false,
          label: this.country.code,
          data: countryDataByPopulation.confirmed,
          borderColor: '#fe8b36',
          backgroundColor: '#fe8b36',
          display: true
        }]
        let datasetsByPopulaionDeath = [{
          fill: false,
          label: this.country.code,
          data: countryDataByPopulation.death,
          borderColor: '#fe8b36',
          backgroundColor: '#fe8b36',
          display: true
        }]
        let datasetsByDay = [{
          fill: false,
          label: this.country.code,
          data: countryDataByDay.confirmed,
          borderColor: '#fe8b36',
          backgroundColor: '#fe8b36',
          display: true
        }]
        let colors = ['blue', 'red', 'green', 'yellow', 'white']
        let colorsTurn = 0
        for (const property in this.selectedCountries) {
          countryData[property] = []
          countryDataByDay[property] = []
          countryDataByPopulation[property + 'Confirmed'] = []
          countryDataByPopulation[property + 'Death'] = []
          this.selectedCountries[property].timeline.forEach(element => {
            if (from < Date.parse(element.date)) {
              countryData[property].push(element.total_cases)
              let percentageByPopulationConfirmed = (parseFloat(element.total_cases) * 100 / parseFloat(this.selectedCountries[property].population)).toFixed(5)
              let percentageByPopulationDeath = (parseFloat(element.total_deaths) * 100 / parseFloat(this.selectedCountries[property].population)).toFixed(5)
              countryDataByPopulation[property + 'Confirmed'].push(percentageByPopulationConfirmed)
              countryDataByPopulation[property + 'Death'].push(percentageByPopulationDeath)
              countryDataByDay[property].push(element.new_daily_cases)
            }
          });
          if (this.predict) {
            let diff = 1
            if (countryData[property][countryData[property].length - 1] == this.selectedCountries[property].confirmed) {
              diff = countryDataByDay[property][countryDataByDay[property].length - 1] / countryDataByDay[property][countryDataByDay[property].length - 2]
            } else {
              diff = this.selectedCountries[property].new_confirmed / countryDataByDay[property][countryDataByDay[property].length - 1]
            }


            for (let i = 1; i <= 7; i++) {
              countryDataByDay[property].push(Math.round(countryDataByDay[property][countryData[property].length - 1] * diff))
              countryData[property].push(Math.round(countryData[property][countryData[property].length - 1] + countryDataByDay[property][countryDataByDay[property].length - 1]))
            }
          }

          datasets.push({
            fill: false,
            label: property,
            data: countryData[property],
            borderColor: colors[colorsTurn],
            backgroundColor: colors[colorsTurn],
            display: true
          })
          datasetsByPopulaionConfirmed.push({
            fill: false,
            label: property,
            data: countryDataByPopulation[property + 'Confirmed'],
            borderColor: colors[colorsTurn],
            backgroundColor: colors[colorsTurn],
            display: true
          })
          datasetsByPopulaionDeath.push({
            fill: false,
            label: property,
            data: countryDataByPopulation[property + 'Death'],
            borderColor: colors[colorsTurn],
            backgroundColor: colors[colorsTurn],
            display: true
          })
          datasetsByDay.push({
            fill: false,
            label: property,
            data: countryDataByDay[property],
            borderColor: colors[colorsTurn],
            backgroundColor: colors[colorsTurn],
            display: true
          })
          colorsTurn++
        }


        let dataDate = {
          labels: dates,
          datasets: datasets,
        }
        let dataDateByPopulationConfirmed = {
          labels: dates,
          datasets: datasetsByPopulaionConfirmed,
        }
        let dataDateByPopulationDeath = {
          labels: dates,
          datasets: datasetsByPopulaionDeath,
        }
        let dataDateByDay = {
          labels: dates,
          datasets: datasetsByDay,
        }
        let options = {
          fill: false,
          responsive: true,
          scales: {
            xAxes: [{
              type: 'time',
              display: true,
              distribution: 'series'
            }],
            yAxes: [{
              ticks: {
                beginAtZero: true,
              },
              display: true,
            }]
          }
        }
        let chart = {
          type: 'line',
          data: dataDate,
          options: options

        };
        let chartByDay = {
          type: 'line',
          data: dataDateByDay,
          options: options
        };
        let chartByPopulationConfirmed = {
          type: 'line',
          data: dataDateByPopulationConfirmed,
          options: options
        };
        let chartByPopulationDeath = {
          type: 'line',
          data: dataDateByPopulationDeath,
          options: options
        };
        this.createChart('confirmedChart', chart);
        this.createChart('confirmedChartByDay', chartByDay);
        this.createChart('confirmedChartByPopulationConfirmed', chartByPopulationConfirmed);
        this.createChart('DeathChartByPopulation', chartByPopulationDeath);


      }
    },
    computed: {}
    ,
  }
  ;
</script>
