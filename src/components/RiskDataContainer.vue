<template>
  <div class="container">
    <RiskChart
      v-if="loaded"
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
    loaded: false,
    chartdata: null
  }),
  async mounted () {
    this.loaded = false
    try {
      const { datalist } = await fetch('api/datalist/percentage',
      )
      this.chartdata = datalist
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}

</script>