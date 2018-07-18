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
                <span class="md-error">Enter correct subreddit name</span>
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
                <md-button v-on:click="getSubs()" class="md-raised md-primary" :disabled="(radio == true)">Scan</md-button>
              </div>
            </md-card-actions>
          </md-card>
          {{ selected }} {{ radio }}
        </div>
      </div>
    </div>
    <!-- PROGRESS BAR -->
      <div class="md-layout-item prbar">
        <md-progress-bar v-visible="isLoading" md-mode="query"></md-progress-bar>
      </div>

    <!-- DATA TABLE -->
    <div class="md-layout-item">
      <md-table md-card v-model="submissiondata" @md-selected="onSelect">
        <md-table-empty-state md-label="Hello! Let's get started..."
                              md-description="Enter name. Choose sorting type. Hit search." >
        </md-table-empty-state>

        <!-- TITLE TOGGLE -->
        <md-table-toolbar>
          <transition name="fade"><h2 v-if="titleVisible" class="md-title">Submissions</h2>
          </transition>
        </md-table-toolbar>

        <!-- SELECTED ITEM COUNTER BARS -->
        <md-table-toolbar slot="md-table-alternate-header" slot-scope="{ count }">
          <div class="md-toolbar-section-start">{{ getAlternateLabel(count) }}</div>
          <div class="md-toolbar-section-end">
            <md-button class="md-icon-button">
              <md-icon md-alignment-top-center>add</md-icon>
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
    searchphrase: null,
    sortmode: 'top',
    required: null,
    isLoading: false,
    titleVisible: false,
    radio: true,
    submissiondata: {},
    selected: [],
    menuVisible: false,
    hasMessages: false
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
    processSelection (payload) {
      const path = 'http://localhost:5000/api/process_selections'
      axios.post(path, payload)
        .then(() => {
          // pass
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        })
    },
    onProcess (evt) {
      const payload = this.selected
      this.processSelection(payload)
    }
  },
  computed: {
    messageClass () {
      return {
        'md-invalid': this.hasMessages
      }
    }
  }
}

</script>
