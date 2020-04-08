<template>
  <div class="container">
    <IllChart :chartdata="chartdata" :options="options"/>
  </div>
</template>

<script>
  import IllChart from "@/components/charts/IlnessData.vue";

  export default {
    name: "PercChartContainer",
    components: {IllChart},
    data: () => ({
      // loaded: false,
      // chartdata: null,
      chartdata: {
        labels: ["Severe", "Critical"],
        datasets: [
          {
            label: "%",
            backgroundColor: ["#af380a", "#c7400b", "#df480c", "#f25213", "#f57543", "#26b1fe"],
            data: [10.5, 7.3, 6.3, 6, 5.6, 0.9]
          }
        ]
      },
      options: {
        title: {
          display: true,
          text: "N = 44,672"
        },
        maintainAspectRatio: false,

      },

    }),
    created() {
      this.chartdata.labels = [
        this.$t("Cardiovascular"),
        this.$t("Diabetes"),
        this.$t("Chronic"),
        this.$t("Blood"),
        this.$t("Cancer"),
        this.$t("NoIllness")
      ];
    }
  };
</script>
