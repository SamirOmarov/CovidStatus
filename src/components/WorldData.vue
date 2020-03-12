<template>
  <div>

    <h2 class="mb-5 Title">World Status</h2>
    <!-- <p>{{ info }}</p> -->
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
  </div>
</template>

<script>
import StatisticsCardLine from "@/components/statistics-cards/StatisticsCardLine.vue";
import axios from "axios";



export default {
  
  data () {
    return {
      info: []
    }
  },
  mounted () {
    axios
      .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .then(response => (this.info = response.data))
  },

  components: {
    StatisticsCardLine
  }
};


</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Montserrat&display=swap");

.Title {
  font-family: "Montserrat", sans-serif;
  font-size: 36px;
  letter-spacing: 10px;
}
</style> 