<template>
  <div>
    <div class="md-layout md-gutter">
      <div class="md-layout-item">
        <div class="md-layout-item">
          <!-- 1/3 card -->
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

    <!-- DATA TABLE -->
    <div class="md-layout md-gutter">
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

      <div class="md-layout-item md-size-20">
        <md-card>
          <md-card-content>
            <div v-for="i in commentdata">
              {{ i }}
            </div>
          </md-card-content>
          <md-card-actions>
          </md-card-actions>
        </md-card>
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

export default {
  name: 'Home',
  data: () => ({
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
    selObjects: {}
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
      const path = 'http://localhost:5000/api/process_selections'
      var selctd = this.selected.map(entry => entry.id)
      console.log('selO - ' + this.selO)
      console.log('selected = ' + this.selected)
      console.log('slctd = ' + selctd)

      axios
        .get(path, {
          params: selctd

        })
        .then(response => {
          console.log('START processSelection .then(response...')
          var selobj = JSON.parse(response.data)
          this.commentdata = selobj
          console.log('FINISH processSelection .then(response...')
        })
        .catch((error) => {
        // eslint-disable-next-line
          console.log("this following error happened in processSelection ()")
          console.log(error)
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
