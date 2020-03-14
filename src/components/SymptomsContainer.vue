<template>
  <div class="container">
    <SympChart
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import SympChart from "@/components/charts/Symptoms.vue";


export default {
  name: 'SympChartContainer',
  components: { SympChart },
  data: () => ({
    loaded: false,
    chartdata: null
  }),
  async mounted () {
    this.loaded = false
    try {
      const { datalist } = await fetch('api/datalist/symptoms',
      )
      this.chartdata = datalist
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}

</script>