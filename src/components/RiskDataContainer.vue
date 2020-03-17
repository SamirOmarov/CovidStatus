<template>
  <div class="container">
    <RiskChart
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import RiskChart from "@/components/charts/RiskData.vue";


export default {
  name: 'RiskChartContainer',
  components: { RiskChart },
 data: () => ({
    // loaded: false,
    // chartdata: null,
    chartdata: {
      labels: ["0-9", "0-19","20-29", "30-39","40-49", "50-59","60-69", "70-79", "80+"],
      datasets: [
        {
          label: "%",
          backgroundColor: ["#26b1fe", "#26b1fe", "#26b1fe","#26b1fe", "#df480c","#c7400b","#c7400b","#c7400b","#af380a",],
          data: [0, 0.2, 0.2, 0.2, 0.4, 1.3, 3.6, 8, 14.8]
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
  // created() {
  //   this.chartdata.labels = [
  //     this.$t("Cardiovascular"),
  //     this.$t("Diabetes"),
  //     this.$t("Chronic"),
  //     this.$t("Blood"),
  //     this.$t("Cancer"),
  //     this.$t("NoIllness")
  //   ];
  // }
}

</script>