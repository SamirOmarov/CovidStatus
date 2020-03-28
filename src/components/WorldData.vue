<template>
  <div>
    <div class="mt-6">
      <!-- <h5 class="mb-2">Theme Mode</h5> -->
    </div>

    <h2 class="mb-5 title">{{ $t("WorldStatus") }}</h2>

    <!-- <p>{{ mapData }}</p> -->
    <!-- <p>{{ ip.country_code }}</p> -->

    <!-- <div v-for="country in info" :key="country.name">
      <p>{{ country.name }}</p>
    </div>-->

    <div class="vx-row">
      <div class="vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4">
        <statistics-card-line
          hideChart
          class="mb-base"
          icon="EyeIcon"
          :statistic="info.confirmed"
          :statisticTitle="$t('TotalInfected')"
        />
      </div>

      <div class="vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4">
        <statistics-card-line
          hideChart
          class="mb-base"
          icon="SmileIcon"
          :statisticTitle="$t('Recovered')"
          :statistic="info.cured"
          color="success"
        />
      </div>

      <div class="vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4">
        <statistics-card-line
          hideChart
          class="mb-base"
          icon="XIcon"
          :statistic="info.death"
          :statisticTitle="$t('Deaths')"
          color="warning"
        />
      </div>

      <div class="vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4">
        <statistics-card-line
          hideChart
          class="mb-base"
          icon="PercentIcon"
          :statistic="(info.death/info.confirmed*100).toFixed(2)"
          :statisticTitle="$t('Lethality')"
          color="danger"
        />
      </div>
    </div>

    <GChart
      type="GeoChart"
      v-if="themeMode=='dark'"
      :settings="{packages: ['geochart'], mapsApiKey: myMapsApiKey}"
      :data="mapData"
      :options="mapOptionsDark"
    />
    <GChart
      type="GeoChart"
      v-if="themeMode=='light'"
      :settings="{packages: ['geochart'], mapsApiKey: myMapsApiKey}"
      :data="mapData"
      :options="mapOptionLight"
    />

    <h4 class="mt-4 data">Sources: WHO, CDC, ECDC, NHC, DXY, Reuters</h4>
  </div>
</template>

<script>
import StatisticsCardLine from "@/components/statistics-cards/StatisticsCardLine.vue";
import I18n from "@/components/I18n.vue";

import axios from "axios";
// import WorldMap from "vue-world-map";
// import MapData from "./MapData.js"
import { GChart } from "vue-google-charts";

var myMapsApiKey = ""; // API key from Google

export default {
  components: {
    StatisticsCardLine,
    GChart,
    I18n
    // WorldMap
  },
  data() {
    return {
      info: {
        confirmed: 0,
        cured: 0,
        death: 0,
        serious: 0
      },
      map: [],
      ip: [],

      mapData: [["Country", "Confirmed"]],
      mapOptionsDark: {
        colorAxis: {
          values: [9, 99, 999, 9999, 1e4, 1e5],
          colors: ['#f4a3a3', '#f08080', '#ea4b4b', '#e62828', '#bd1616', '#1f0404']
         
        },
        // colorAxis: { colors: [ '#f4a3a3',"#f08080", '#300606'] },
        // colorAxis: { colors: [ "#f4a3a3", "#f29292","#f08080","#ee6e6e","#ec5d5d","#ea4b4b","#e83a3a","#e62828", "#e01a1a" ,"#ce1818","#bd1616","#ab1414","#9a1212", "#881010" ,"#770e0e","#650c0c","#540a0a","#540a0a","#540a0a","#540a0a","#540a0a","#420808", "#300606", "#300606", "#300606", "#300606", "#300606", "#300606", "#300606"] },
        backgroundColor: "#262c49"
      },
      mapOptionLight: {
        colorAxis: { colors: ["#e31b23", "#cc191e", "#b5161b", "#710e11"] }
      },
      myMapsApiKey: myMapsApiKey,
      locale: this.$i18n.locale
    };
  },
  watch: {
    locale(val) {
      this.$i18n.locale = val;
    }
  },
  created() {
    let self = this;

    axios
      .get("http://api.covidstatus.com/cases/all", {})
      .then(response => (this.info = response.data));

    axios.get("http://api.covidstatus.com/cases", {}).then(response => {
      this.map = response.data;
      response.data.forEach(element => {
        if (element.confirmed != 0)
          self.mapData.push([element.country_name, element.confirmed]);
      });
    });
  },

  mounted() {
    //  let self =this ;
    //  setInterval(function(){ console.log(self.$i18n.locale) }, 3000);
    //  console.log(self.$i18n.locale)
  },
  computed: {
    themeMode: {
      get() {
        return this.$store.state.theme;
      }
    }
  }
};
</script>

