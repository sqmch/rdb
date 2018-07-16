<template>
  <div>
    <!-- SUBREDDIT SEARCH INPUT -->
    <div class="md-layout">
      <div class="md-size-25">
        <md-field>
          <label>Enter subreddit name...</label>
          <md-input v-model="type"></md-input>

        </md-field>
      </div>
      <md-button v-on:click="getSubs()" class="md-raised md-primary">Search</md-button>
    </div>
      <div class="md-layout">
        <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio">Top</md-radio></div>
        <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio1">Hot</md-radio></div>
        <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio2">New</md-radio></div>
        <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio3">Rising</md-radio></div>
        <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio4">Controversial</md-radio></div>
      </div>
    <!-- DROPDOWNS -->

    <!-- /DROPDOWNS -->
    <!-- DATA TABLE -->
    <div class="md-layout-item">

      <md-table v-model="submissiondata" md-card @md-selected="onSelect">
        <md-table-toolbar>
          <h1 class="md-title">Submissions</h1>
        </md-table-toolbar>

        <md-table-toolbar slot="md-table-alternate-header" slot-scope="{ count }">
          <div class="md-toolbar-section-start">{{ getAlternateLabel(count) }}</div>

          <div class="md-toolbar-section-end">
            <md-button class="md-icon-button">
              <md-icon>delete</md-icon>
            </md-button>
          </div>
        </md-table-toolbar>
        {{ selected }}
        <md-table-row slot="md-table-row" slot-scope="{ item }" md-selectable="multiple" md-auto-select>
          <md-table-cell md-label="Submission" md-sort-by="email">{{ item.title }}</md-table-cell>
        </md-table-row>
      </md-table>
    </div>
  </div>
</template>

<style lang="scss" scoped>
small {
	display: block;
}
.md-radio {
	display: flex;
}
.searchfield {
	//max-width: 300px;
}
.md-app {
	border: 1px solid rgba(#000, 0.12);
}

.md-table + .md-table {
	margin-top: 16px;
}
</style>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data: () => ({
    radio: true,
    submissiondata: {},
    selected: {},
    selectedCountry: null,
    selectedEmployee: null
  }),
  methods: {
    onSelect (item) {
      this.selected = item
    },
    getSubs () {
      const path = 'http://localhost:5000/api/submissions'
      axios
        .get(path)
        .then(response => {
          var dataobj = JSON.parse(response.data)
          this.submissiondata = dataobj
          console.log(dataobj)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}

</script>
