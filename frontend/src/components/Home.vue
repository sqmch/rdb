<template>
  <div class="page-container">
    <md-app md-waterfall md-mode="fixed-last">
      <md-app-toolbar class="md-large md-dense md-primary">
        <div class="md-toolbar-row">
          <div class="md-toolbar-section-start">
            <md-button class="md-icon-button" @click="menuVisible = !menuVisible">
              <md-icon>menu</md-icon>
            </md-button>

            <span class="md-title">Tristan Evert</span>
          </div>

          <div class="md-toolbar-section-end">
            <md-button class="md-icon-button">
              <md-icon>more_vert</md-icon>
            </md-button>
          </div>
        </div>

        <div class="md-toolbar-row">
          <md-tabs class="md-primary">
            <md-tab id="tab-home" md-label="Projects"></md-tab>
            <md-tab id="tab-pages" md-label="Who?"></md-tab>
          </md-tabs>
        </div>
      </md-app-toolbar>

      <md-app-drawer :md-active.sync="menuVisible">
        <md-toolbar class="md-transparent" md-elevation="0">Navigation</md-toolbar>

        <md-list>
          <md-list-item>
            <md-icon>move_to_inbox</md-icon>
            <span class="md-list-item-text">Inbox</span>
          </md-list-item>

          <md-list-item>
            <md-icon>send</md-icon>
            <span class="md-list-item-text">Sent Mail</span>
          </md-list-item>

          <md-list-item>
            <md-icon>delete</md-icon>
            <span class="md-list-item-text">Trash</span>
          </md-list-item>

          <md-list-item>
            <md-icon>error</md-icon>
            <span class="md-list-item-text">Spam</span>
          </md-list-item>
        </md-list>
      </md-app-drawer>

      <md-app-content>
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">MYMANI</div>
              <div class="md-subhead">It also have a ripple</div>
            </md-card-header>

            <md-card-content>
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio. Dolores, sed accusantium quasi non.
            </md-card-content>

            <md-card-actions>
              <md-button>GITHUB</md-button>
              <md-button>DEMO</md-button>
              <md-button>DETAILS</md-button>
            </md-card-actions>
          </md-ripple>
        </md-card>
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">rcdbot</div>
              <div class="md-subhead">It also have a ripple</div>
            </md-card-header>

            <md-card-content>
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio. Dolores, sed accusantium quasi non.
            </md-card-content>

            <md-card-actions>
              <md-button>GITHUB</md-button>
              <md-button>DEMO</md-button>
              <md-button>DETAILS</md-button>
            </md-card-actions>
          </md-ripple>
        </md-card>
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">rcdbot</div>
              <div class="md-subhead">It also have a ripple</div>
            </md-card-header>

            <md-card-content>
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio. Dolores, sed accusantium quasi non.
            </md-card-content>

            <md-card-actions>
              <md-button>GITHUB</md-button>
              <md-button>DEMO</md-button>
              <md-button>DETAILS</md-button>
            </md-card-actions>
          </md-ripple>
        </md-card>
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">Card with hover effect</div>
              <div class="md-subhead">It also have a ripple</div>
            </md-card-header>

            <md-card-content>
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio. Dolores, sed accusantium quasi non.
            </md-card-content>

            <md-card-actions>
              <md-button>GITHUBBBB</md-button>
              <md-button>DEMO</md-button>
              <md-button>DETAILS</md-button>
            </md-card-actions>
          </md-ripple>
        </md-card>
      </md-app-content>
    </md-app>
  </div>
</template>

<style lang="scss" scoped>
.md-app {
	max-height: 400px;
	border: 1px solid rgba(#000, 0.12);
}
.md-card {
	width: 320px;
	margin: 4px;
	display: inline-block;
	vertical-align: top;
}
// Demo purposes only
.md-drawer {
	width: 230px;
	max-width: calc(100vw - 125px);
}
</style>

<script>
export default {
  name: 'LastRowFixed',
  data: () => ({
    menuVisible: false
  })
}
</script>
