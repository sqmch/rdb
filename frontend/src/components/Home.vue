<template>
  <div>
    <!-- SUBREDDIT SEARCH INPUT -->
    <div md-scrollbar class="md-layout">
      <div class="md-layout-item md-size-25">
        <md-field>
          <label>Enter subreddit name...</label>
          <md-input v-model="type"></md-input>

        </md-field>
      </div>
      <md-button class="md-raised md-primary">Search</md-button>
    </div>
      <div class="md-layout md-alignment-right">
        <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio">Top</md-radio></div>
        <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio1">Hot</md-radio></div>
        <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio2">New</md-radio></div>
        <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio3">Rising</md-radio></div>
        <div class=" md-medium-size-33 md-small-size-50 md-xsmall-size-100"><md-radio v-model="radio" value="my-radio4">Controversial</md-radio></div>
      </div>
    <!-- DROPDOWNS -->

    <!-- /DROPDOWNS -->
    <!-- DATA TABLE -->
    <md-table md-scrollbar v-model="people" md-card @md-selected="onSelect">
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

      <md-table-row slot="md-table-row" slot-scope="{ item }" :md-disabled="item.name.includes('Stave')" md-selectable="multiple" md-auto-select>
        <md-table-cell md-label="Name" md-sort-by="name">{{ item.name }}</md-table-cell>
        <md-table-cell md-label="Email" md-sort-by="email">{{ item.email }}</md-table-cell>
        <md-table-cell md-label="Gender" md-sort-by="gender">{{ item.gender }}</md-table-cell>
        <md-table-cell md-label="Job Title" md-sort-by="title">{{ item.title }}</md-table-cell>
      </md-table-row>
    </md-table>

    <p>Selected:</p>
    {{ selected }}
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

.md-progress-bar {
	position: absolute;
	top: 0;
	right: 0;
	left: 0;
}
</style>

<script>
export default {
  name: 'Home',
  data: () => ({
    radio: true,
    selected: {},
    selectedCountry: null,
    selectedEmployee: null,
    countries: [
      'Algeria',
      'Argentina',
      'Brazil',
      'Canada',
      'Italy',
      'Japan',
      'United Kingdom',
      'United States'
    ],
    employees: [
      'Jim Halpert',
      'Dwight Schrute',
      'Michael Scott',
      'Pam Beesly',
      'Angela Martin',
      'Kelly Kapoor',
      'Ryan Howard',
      'Kevin Malone',
      'Creed Bratton',
      'Oscar Nunez',
      'Toby Flenderson',
      'Stanley Hudson',
      'Meredith Palmer',
      'Phyllis Lapin-Vance'
    ],
    people: [
      {
        id: 1,
        name: 'Shawna Dubbin',
        email: 'sdubbin0@geocities.com',
        gender: 'Male',
        title: 'Assistant Media Planner'
      },
      {
        id: 2,
        name: 'Odette Demageard',
        email: 'odemageard1@spotify.com',
        gender: 'Female',
        title: 'Account Coordinator'
      },
      {
        id: 3,
        name: 'Lonnie Izkovitz',
        email: 'lizkovitz3@youtu.be',
        gender: 'Female',
        title: 'Operator'
      },
      {
        id: 4,
        name: 'Thatcher Stave',
        email: 'tstave4@reference.com',
        gender: 'Male',
        title: 'Software Test Engineer III'
      },
      {
        id: 5,
        name: 'Clarinda Marieton',
        email: 'cmarietonh@theatlantic.com',
        gender: 'Female',
        title: 'Paralegal'
      },
      {
        id: 1,
        name: 'Shawna Dubbin',
        email: 'sdubbin0@geocities.com',
        gender: 'Male',
        title: 'Assistant Media Planner'
      },
      {
        id: 2,
        name: 'Odette Demageard',
        email: 'odemageard1@spotify.com',
        gender: 'Female',
        title: 'Account Coordinator'
      },
      {
        id: 3,
        name: 'Lonnie Izkovitz',
        email: 'lizkovitz3@youtu.be',
        gender: 'Female',
        title: 'Operator'
      },
      {
        id: 4,
        name: 'Thatcher Stave',
        email: 'tstave4@reference.com',
        gender: 'Male',
        title: 'Software Test Engineer III'
      },
      {
        id: 5,
        name: 'Clarinda Marieton',
        email: 'cmarietonh@theatlantic.com',
        gender: 'Female',
        title: 'Paralegal'
      },
      {
        id: 3,
        name: 'Lonnie Izkovitz',
        email: 'lizkovitz3@youtu.be',
        gender: 'Female',
        title: 'Operator'
      },
      {
        id: 4,
        name: 'Thatcher Stave',
        email: 'tstave4@reference.com',
        gender: 'Male',
        title: 'Software Test Engineer III'
      },
      {
        id: 5,
        name: 'Clarinda Marieton',
        email: 'cmarietonh@theatlantic.com',
        gender: 'Female',
        title: 'Paralegal'
      }
    ]
  }),
  methods: {getClass: ({ id }) => ({
    'md-primary': id === 2,
    'md-accent': id === 3
  }),
  onSelect (item) {
    this.selected = item
  }
  }
}

</script>
