<template>
  <div class="container">
    <!-- <p>{{ chartdata.datasets.data}}</p> -->
    <PercChart :chartdata="chartdata" :options="options" />
  </div>
</template>

<script>
import PercChart from "@/components/charts/Percentage.vue";
// import axios from "axios";

export default {
  name: "PercChartContainer",
  components: { PercChart },
  data: () => ({
    // loaded: false,
    // chartdata: null,
    chartdata: {
      labels: [ 'Severe', 'Critical'],
      datasets: [
        {
          label: 'Data One',
          backgroundColor: ["#3e95cd", "#8e5ea2", "#e8c3b9"],
          data: [45.7, 50.7, 3.9]
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: "13:03:2020"
      }
    }
  }),
  created(){
    this.chartdata.labels=[this.$t('Active'), this.$t('Recovered'),this.$t('Deaths'),]
  }
};
</script>