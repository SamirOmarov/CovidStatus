<template>
  <div class="container">
    <SympChart :chartdata="chartdata" :options="options" />
  </div>
</template>

<script>
import SympChart from "@/components/charts/Symptoms.vue";

export default {
  name: "SympChartContainer",
  components: { SympChart },
  data: () => ({
    // loaded: false,
    // chartdata: null,
    chartdata: {
      labels: [ 'Severe', 'Critical'],
      datasets: [
        {
          label: 'Data One',
          backgroundColor: ["#3e95cd", "#8e5ea2", "#e8c3b9"],
          data: [81.5, 13.8, 4.7]
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: "N = 44,672"
      }
    }
  }),
  created(){
    this.chartdata.labels=[this.$t('Mild'), this.$t('Severe'),this.$t('Critical'),]
  }


  // async mounted() {
  //   this.loaded = false;
  //   try {
  //     const { datalist } = await fetch(
  //       "http://api.covidstatus.com/symptoms_statistics"
  //     );
  //     this.chartdata = datalist;
  //     console.log(this.chartdata);
  //     this.loaded = true;
  //   } catch (e) {
  //     console.error(e);
  //   }
  // }
};
</script>