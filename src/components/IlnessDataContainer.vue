<template>
  <div class="container">
    <IllChart
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import IllChart from "@/components/charts/Percentage.vue";


export default {
  name: 'PercChartContainer',
  components: { IllChart },
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