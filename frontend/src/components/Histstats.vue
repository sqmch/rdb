<template>
  <div>
    <div class="md-layout-item">
      <md-tabs class="md-primary" md-alignment="centered">
        <!-- HSTORIC DATA TAB -->
        <md-tab md-icon="show_chart">
          <div class="md-gutter">
            <chartjs-line
              bordercolor="rgba(144,202,249,1)"
              backgroundcolor="rgba(144,202,249,1)"
              :data="hpolaritydata"
              :labels="hlabels"
              :bind="true"
              :height="50"
              :linetension="0"
              :datalabel="'Average Polarity'"
            ></chartjs-line>
            <chartjs-line
              bordercolor="rgba(144,202,249,1)"
              backgroundcolor="rgba(144,202,249,1)"
              :data="hsubjectivitydata"
              :labels="hlabels"
              :bind="true"
              :height="50"
              :linetension="0"
              :datalabel="'Average Subjectivity'"
            ></chartjs-line>
          </div>
        </md-tab>
        <md-tab md-icon="table_chart">
          <div class="md-layout-item md-gutter">
            <md-table md-card v-model="historic_data">
              <md-table-empty-state
                md-label="No data to load..."
                md-description="Please try again later."
                md-icon="library_books"
              ></md-table-empty-state>

              <!-- TITLE TOGGLE -->
              <md-table-toolbar>
                <md-button :disabled="this.historic_data.length <= 0" class="md-primary">
                  <md-icon>save_alt</md-icon>
                  <download-csv :data="historic_data" name="historicData.csv">CSV</download-csv>
                </md-button>
              </md-table-toolbar>

              <!-- TABLE ROWS -->
              <md-table-row class="tabrow" slot="md-table-row" slot-scope="{ item }">
                <md-table-cell md-label="Date">{{ item.fulldate }}</md-table-cell>
                <md-table-cell md-label="Average polarity ">{{ item.avg_title_polarity }}</md-table-cell>
                <md-table-cell md-label="Average subjectivity">{{ item.avg_title_subjectivity }}</md-table-cell>
              </md-table-row>
            </md-table>
          </div>
        </md-tab>
      </md-tabs>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { Bar } from 'vue-chartjs';

export default {
  extends: Bar,
  name: 'Histstats',
  data: () => ({
    historic_data: [],
    hlabels: [],
    hpolaritydata: [],
    hsubjectivitydata: []
  }),
  methods: {
    historicData () {
      const path = 'http://localhost:5000/api/historic_data';
      axios
        .get(path)
        .then(response => {
          var dataobj = JSON.parse(response.data)
          this.historic_data = dataobj
          this.hlabels = this.historic_data.map(a => a.fulldate)
          this.hpolaritydata = this.historic_data.map(
            a => a.avg_title_polarity
          )
          this.hsubjectivitydata = this.historic_data.map(
            a => a.avg_title_subjectivity
          )
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
        })
    }
  },
  created: function () {
    this.historicData()
  }
}
</script>

<style lang="scss" scoped>
.md-list {
  max-width: 100%;
  display: inline-block;
  vertical-align: top;
  border: 1px solid rgba(#000, 0.12);
}
</style>
