<template>
  <div>
    <div class="md-layout md-gutter">
      <div class="md-layout-item">
        <div class="md-layout-item">
          <md-card>
            <md-card-content>
              <!-- SUBREDDIT SEARCH INPUT -->
              <md-field :class="messageClass">
                <label>Enter subreddit name...</label>
                <md-input required v-model="searchphrase"></md-input>
                <span class="md-error">Enter subreddit name</span>
              </md-field>
              <!-- SORT MODE RADIO BUTTONS -->
              <div class="md-layout md-medium-size-33 md-small-size-50 md-xsmall-size-100">
                <md-radio v-model="radio" id="rtop" value="top">Top</md-radio>
                <md-radio v-model="radio" id="rhot" value="hot">Hot</md-radio>
                <md-radio v-model="radio" id="rnew" value="new">New</md-radio>
                <md-radio v-model="radio" id="rgilded" value="rising">Gilded</md-radio>
                <md-radio v-model="radio" id="rcontroversial" value="controversial">Controversial</md-radio>
              </div>
            </md-card-content>
            <!-- SEARCH BUTTON -->
            <md-card-actions md-alignment="left">
              <div class="searchbut">
                <md-button v-on:click="getSubs()"
                           class="md-raised md-primary"
                           :disabled="this.radio == true || this.searchphrase.length <= 0">
                           <md-icon md-alignment-top-center>search</md-icon>
                           Search
                </md-button>
              </div>
            </md-card-actions>
          </md-card>
          <!--{{ selected }} -->
        </div>
      </div>
    </div>
    <!-- PROGRESS BAR -->
    <div class="md-layout-item prbar">
      <md-progress-bar v-visible="isLoading" md-mode="query"></md-progress-bar>
    </div>

    <div class="md-layout md-gutter">
      <!-- DATA TABLE -->
      <div class="md-layout-item">
        <md-table md-card v-model="submissiondata" @md-selected="onSelect">
          <md-table-empty-state md-label="No submissions found"
                                md-description="Please search for a valid subreddit above."
                                md-icon="mood_bad">
          </md-table-empty-state>

          <!-- TITLE TOGGLE -->
          <md-table-toolbar>
            <transition name="fade"><h2 v-if="titleVisible" class="md-title">Submissions</h2>
            </transition>
          </md-table-toolbar>

          <!-- SELECTED ITEM COUNTER BARS -->
          <md-table-toolbar slot="md-table-alternate-header" slot-scope="{ count }">
            <div class="md-toolbar-section-start">
              <md-button class="md-raised md-primary"
                         v-on:click="processSelection()">
                <md-icon md-alignment-top-center md-size-2x>library_add</md-icon>
                Grab data
              </md-button>
            <div class="tete md-toolbar-section-beginning">{{ getAlternateLabel(count) }}</div>

            </div>
          </md-table-toolbar>

          <!-- TABLE ROWS -->
          <md-table-row class="tabrow" slot="md-table-row" slot-scope="{ item }" md-selectable="multiple" md-auto-select>
            <md-table-cell md-label="All">{{ item.title }}</md-table-cell>
          </md-table-row>
        </md-table>
      </div>

      <!-- RESULTS TABLE-->
      <div class="md-layout-item md-size-66">
        <div class="md-layout-item">
          <md-table md-card v-model="commentdata">
            <md-table-empty-state md-label="Let's get started!"
                                  md-description="Select submissions and grab data."
                                  md-icon="library_books">
            </md-table-empty-state>

            <!-- TITLE TOGGLE -->
            <md-table-toolbar>
              <transition name="fade"><h2 v-if="titleVisible" class="md-title">Results</h2>
              </transition>
            </md-table-toolbar>

            <!-- TABLE ROWS -->
            <md-table-row class="tabrow" slot="md-table-row" slot-scope="{ item }">
              <md-table-cell md-label="ID">{{ item.id }}</md-table-cell>
              <md-table-cell md-label="Title">{{ item.title }}</md-table-cell>
              <md-table-cell md-label="Title Polarity">{{ item.title_polarity }}</md-table-cell>
              <md-table-cell md-label="Title Subjectivity">{{ item.title_subjectivity }}</md-table-cell>
              <md-table-cell md-label="Comment Amount">{{ item.cmnt_amt }}</md-table-cell>
              <md-table-cell md-label="Score">{{ item.score }}</md-table-cell>
            </md-table-row>
          </md-table>
          <chartjs-line :data='polaritydata' :labels='polaritydatalabels' :bind='true'></chartjs-line>
          <chartjs-bar :data='polaritydata' :labels='polaritydatalabels' :bind='true'></chartjs-bar>
          <chartjs-radar :data='polaritydata' :labels='polaritydatalabels' :bind='true'></chartjs-radar>
          </md-card>
        </div>
      </div>

    </div>
  </div>
</template>

<style lang="scss" scoped>
.tete {
	text-align: left;
}
.prbar {
	margin-top: 12px;
	margin-bottom: 12px;
}
.searchbut {
	text-align: left;
}
.tabrow {
	text-align: left;
}
.fade-enter-active,
.fade-leave-active {
	transition: opacity 1.5s ease-out;
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
	margin-top: 8px;
}

// Demo purposes only
.md-drawer {
	width: 230px;
	max-width: calc(100vw - 125px);
}
</style>

<script>
import axios from 'axios'
import {Bar} from 'vue-chartjs'

export default {
  extends: Bar,
  name: 'Home',
  data: () => ({
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    dataset: [1511, 59, 2323, 8981, 56, -5585, -5566.5],
    searchphrase: '',
    sortmode: 'top',
    required: null,
    isLoading: false,
    titleVisible: false,
    radio: true,
    commentdata: [],
    submissiondata: {},
    selected: {},
    menuVisible: false,
    hasMessages: false,
    selObjects: {},
    polaritydata: [],
    polaritydatalabels: []
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
    onDatagrab () {
      this.processSelection()
    },
    getSubs () {
      this.selected.length = 0
      this.submissiondata.length = 0
      this.isLoading = true
      const path = 'http://localhost:5000/api/submissions'
      axios
        .get(path, {
          params: {
            sphrase: this.searchphrase,
            sortmode: this.radio
          }
        })
        .then(response => {
          var dataobj = JSON.parse(response.data)
          this.submissiondata = dataobj
          this.isLoading = false
          this.titleVisible = true
        })
        .catch(error => {
          console.log(error)
          this.isLoading = false
          this.titleVisible = true
        })
    },
    processSelection () {
      this.isLoading = true
      const path = 'http://localhost:5000/api/process_selections'
      var selctd = this.selected.map(entry => entry.id)

      axios
        .get(path, {
          params: selctd

        })
        .then(response => {
          var selobj = JSON.parse(response.data)
          this.commentdata = selobj
          this.polaritydatalabels = this.commentdata.map(a => a.id)
          this.polaritydata = this.commentdata.map(a => a.title_polarity)
          this.addData()
          this.isLoading = false
          console.log('polaritydata =' + this.polaritydata)
          console.log('polaritydatalabels =' + this.polaritydatalabels)
        })
        .catch((error) => {
        // eslint-disable-next-line
          console.log(error)
          this.isLoading = false
        })
    },
    getSubsOnLoad () {
      this.selected.length = 0
      this.submissiondata.length = 0
      this.isLoading = true
      const path = 'http://localhost:5000/api/submissions'
      axios
        .get(path)
        .then(response => {
          var dataobj = JSON.parse(response.data)
          this.submissiondata = dataobj
          this.isLoading = false
          this.titleVisible = true
        })
        .catch(error => {
          console.log(error)
          this.isLoading = false
          this.titleVisible = true
        })
    },
    addData () {
      this.polaritydata.push(this.commentdata.map(a => a.title_polarity))
    }
  },
  computed: {
    messageClass () {
      return {
        'md-invalid': this.hasMessages
      }
    }
  },
  created: function () {
    this.getSubsOnLoad()
  }
}

</script>
