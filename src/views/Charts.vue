<template>
  <div>
    <div class="vx-row " style="padding: 0 12px">
      <vs-select
        autocomplete
        multiple
        :placeholder="$t('selectCountriesToCompare')"
        class="selectExample mb-2"
        v-model="countrySelected"
        v-on:change="addNewCountry"
        width="300px"
      >
        <vs-select-item :key="index" :value="item.value" :text="item.text" v-for="(item,index) in countries"/>
      </vs-select>
      <vs-checkbox style="margin-left: 5px;margin-bottom: 10px" v-model="predict" v-on:change="prediction">
        Predict
      </vs-checkbox>
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
        console.log(this.predict)
        this.initCharts()

      },
      async addNewCountry(codes) {
        console.log(codes)
        this.selectedCountries = []
        for (let code in codes) {
          console.log(codes[code])
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
        let ar = await axios.get("https://api.covidstatus.com/cases/ar", {})
        let from = Date.parse("2020-03-05");

        let countryData = {
          dates: [],
          confirmed: [],
        }
        let countryDataByDay = {
          dates: [],
          confirmed: [],
        }
        response.data.timeline.forEach(element => {
          if (from < Date.parse(element.date)) {
            countryData.dates.push(element.date)
            countryDataByDay.dates.push(element.date)
            countryData.confirmed.push(element.total_cases)
            countryDataByDay.confirmed.push(element.new_daily_cases)
          }
        });
        if (this.predict) {
          let diff = countryData.confirmed[countryData.confirmed.length - 1] / countryData.confirmed[countryData.confirmed.length - 2]
          for (let i = 1; i <= 7; i++) {
            let date = countryData.dates[countryData.dates.length - 1]
            let someDate = new Date(date);
            let numberOfDaysToAdd = 1; // add 6 days
            someDate.setDate(someDate.getDate() + numberOfDaysToAdd);
            let dd = someDate.getDate();
            let mm = someDate.getMonth() + 1;
            let y = someDate.getFullYear();
            let someFormattedDate = y + '-' + mm + '-' + dd;
            countryData.dates.push(someFormattedDate)
            countryDataByDay.dates.push(someFormattedDate)
            countryData.confirmed.push(Math.floor(countryData.confirmed[countryData.confirmed.length - 1] * diff))
            countryDataByDay.confirmed.push(Math.floor(countryDataByDay.confirmed[countryDataByDay.confirmed.length - 1] * diff))
          }
        }
        let datasets = [{
          fill: false,
          label: this.country.code,
          data: countryData.confirmed,
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
          this.selectedCountries[property].timeline.forEach(element => {
            if (from < Date.parse(element.date)) {
              countryData[property].push(element.total_cases)
              countryDataByDay[property].push(element.new_daily_cases)
            }
          });
          if (this.predict) {
            let diff = countryData[property][countryData[property].length - 1] / countryData[property][countryData[property].length - 2]
            for (let i = 1; i <= 7; i++) {
              countryData[property].push(Math.floor(countryData[property][countryData[property].length - 1] * diff))
              countryDataByDay[property].push(Math.floor(countryDataByDay[property][countryDataByDay[property].length - 1] * diff))
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
          labels: countryData.dates,
          datasets: datasets,
        }
        let dataDateByDay = {
          labels: countryDataByDay.dates,
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
              scaleLabel: {
                display: true,
                labelString: this.$t('TotalInfected'),
              }
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
        this.createChart('confirmedChart', chart);
        this.createChart('confirmedChartByDay', chartByDay);

      }
    },
    computed: {}
    ,
  }
  ;
</script>
