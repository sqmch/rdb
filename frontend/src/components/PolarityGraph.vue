<template>
  <div class="md-layout-item">
    <chartjs-line :data='polaritydata' :labels='polaritydatalabels'></chartjs-line>
    <chartjs-bar :data='polaritydata' :labels='polaritydatalabels'></chartjs-bar>
    <chartjs-radar :data='polaritydata' :labels='polaritydatalabels'></chartjs-radar>
  </div>
</template>

<script>
export default {
  name: 'Misc'
}
</script>
