<template>
  <div class="container">
    <!-- <p>{{ chartdata.datasets.data}}</p> -->
    <PercChart :chartdata="chartdata" :options="options"/>
  </div>
</template>

<script>
  import PercChart from "@/components/charts/Percentage.vue";
  // import axios from "axios";

  export default {
    name: "PercChartContainer",
    components: {PercChart},
    data: () => ({
      // loaded: false,
      // chartdata: null,
      chartdata: {
        labels: ['Severe', 'Critical'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: ["#3e95cd", "#8e5ea2", "#e8c3b9"],
            data: [73.05, 21.2, 5.75]
          }
        ]
      },
      options: {
        title: {
          display: true,
          text: "08.04.2020"
        },
        maintainAspectRatio: false,

      }
    }),
    created() {
      this.chartdata.labels = [this.$t('Active'), this.$t('Recovered'), this.$t('Deaths'),]
    }
  };
</script>
