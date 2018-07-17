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

    <!-- SORT MODE RADIO BUTTONS -->
    <div class="md-layout">
      <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio">Top</md-radio></div>
      <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio1">Hot</md-radio></div>
      <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio2">New</md-radio></div>
      <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio3">Rising</md-radio></div>
      <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio4">Controversial</md-radio></div>
    </div>

    <!-- PROGRESS BAR -->
    <div class="md-layout-item">
      <md-progress-bar v-visible="isLoading" md-mode="query"></md-progress-bar>
    </div>

    <!-- DATA TABLE -->
    <div class="md-layout-item">
      <md-table md-card v-model="submissiondata" @md-selected="onSelect">
        <md-table-empty-state
          md-label="Hello! Let's get started..."
          :md-description="'Enter a subreddit name, pick your sorting preference and press Search to load submissions.'">
        </md-table-empty-state>

        <!-- TITLE TOGGLE -->
        <md-table-toolbar md-alignment-center>
          <transition name="fade">
            <h2 v-if="titleVisible" class="md-title">Submissions</h2>
          </transition>
        </md-table-toolbar>

        <!-- SELECTED ITEM COUNTER BARS -->
        <md-table-toolbar slot="md-table-alternate-header" slot-scope="{ count }">
          <div class="md-toolbar-section-start">{{ getAlternateLabel(count) }}</div>
          <div class="md-toolbar-section-end">
            <md-button class="md-icon-button">
              <md-icon>delete</md-icon>
            </md-button>
          </div>
        </md-table-toolbar>

        <!-- TABLE ROWS -->

        <md-table-row class="tabrow" slot="md-table-row" slot-scope="{ item }" md-selectable="multiple" md-auto-select>
          <md-table-cell md-label="Title">{{ item.title }}</md-table-cell>
        </md-table-row>
      </md-table>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.tabrow {
	text-align: left;
}
.fade-enter-active,
.fade-leave-active {
	transition: opacity 2.5s ease-out;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
	opacity: 0;
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
.md-app {
	border: 1px solid rgba(#000, 0.12);
}

// Demo purposes only
.md-drawer {
	width: 230px;
	max-width: calc(100vw - 125px);
}
</style>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data: () => ({
    isLoading: false,
    titleVisible: false,
    radio: true,
    submissiondata: {},
    selected: {},
    selectedCountry: null,
    selectedEmployee: null,
    menuVisible: false
  }),
  methods: {
    onSelect (item) {
      this.selected = item
    },
    getAlternateLabel (count) {
      let plural = ''

      if (count > 1) {
        plural = 's'
      }

      return `${count} submission${plural} selected`
    },
    getSubs () {
      this.isLoading = true
      const path = 'http://localhost:5000/api/submissions'
      axios
        .get(path)
        .then(response => {
          var dataobj = JSON.parse(response.data)
          this.submissiondata = dataobj
          console.log(dataobj)
          this.isLoading = false
          this.titleVisible = true
        })
        .catch(error => {
          console.log(error)
          this.isLoading = false
          this.titleVisible = true
        })
    }
  }
}

</script>
