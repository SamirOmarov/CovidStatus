<template>
  <div>
    <div class="mt-4">
      <h5 class="mb-2">Theme Mode</h5>
      <div>
        <vs-radio v-model="themeMode" vs-value="light" class="mr-4" vs-name="theme-mode-light">Light</vs-radio>
        <vs-radio v-model="themeMode" vs-value="dark" class="mr-4" vs-name="theme-mode-dark">Dark</vs-radio>
      </div>
    </div>

    <h2 class="mb-5 title">World Status</h2>
    <!-- <p>{{ info }}</p> -->

    <!-- <div v-for="country in info" :key="country.name">
      <p>{{ country.name }}</p>
    </div>-->

    <div class="vx-row">
      <div class="vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4">
        <statistics-card-line
          hideChart
          class="mb-base"
          icon="EyeIcon"
          statistic="129583"
          statisticTitle="Total Infected"
        />
      </div>

      <div class="vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4">
        <statistics-card-line
          hideChart
          class="mb-base"
          icon="SmileIcon"
          statisticTitle="Recovered"
          statistic="68667"
          color="success"
        />
      </div>

      <div class="vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4">
        <statistics-card-line
          hideChart
          class="mb-base"
          icon="XIcon"
          statistic="4749"
          statisticTitle="Deaths"
          color="warning"
        />
      </div>

      <div class="vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4">
        <statistics-card-line
          hideChart
          class="mb-base"
          icon="PercentIcon"
          statistic="3.6%"
          statisticTitle="Lethality"
          color="danger"
        />
      </div>
    </div>

    <!-- <WorldMap :countydata="MapData"></WorldMap> -->


    <GChart
      type="GeoChart"
      :settings="{packages: ['geochart'], mapsApiKey: myMapsApiKey}"
      :data="mapData"
      :options="mapOptionsDark"
    />

  </div>
</template>

<script>
import StatisticsCardLine from "@/components/statistics-cards/StatisticsCardLine.vue";
import axios from "axios";
// import WorldMap from "vue-world-map";
// import MapData from "./MapData.js"
import { GChart } from "vue-google-charts";

var myMapsApiKey = ""; // API key from Google

export default {
  components: {
    StatisticsCardLine,
    GChart
    // WorldMap
  },
  data() {
    return {
      info: [],
      mapData: [
        ["Country", "Infected"],
        ["Germany", 2200],
        ["United States", 300],
        ["Brazil", 400],
        ["Canada", 500],
        ["France", 600],
        ["China", 88600],
        ["Azerbaijan", 11],
        ["Turkey", 1],
        ["Russia", 700]
      ],
      mapOptionsDark: {
        colorAxis: { colors: ["#e31b23", "#cc191e", "#b5161b", "#710e11"] },
        backgroundColor: '#262c49',
      },
      mapOptionLight: {
        colorAxis: { colors: ["#e31b23", "#cc191e", "#b5161b", "#710e11"] },
        
      },
      myMapsApiKey: myMapsApiKey
    };
  },
  mounted() {
    axios
      .get("https://restcountries.eu/rest/v2/all", {})
      .then(response => (this.info = response.data));
  },
  computed: {
    themeMode: {
      get() {
        return this.$store.state.theme;
      },
      set(val) {
        this.$store.dispatch("updateTheme", val);
      }
    }
  }
};
</script>

