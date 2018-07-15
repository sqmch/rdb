<template>
  <div>
    <div>
      <md-field class="searchfield">
        <label>Enter subreddit name...</label>
        <md-input v-model="type"></md-input>
        <md-button class="md-primary md-raised">Search</md-button>
      </md-field>
      <div class="searchbut">

      </div>
    </div>
    <md-table v-model="users" md-sort="name" md-sort-order="asc" md-card>
      <md-table-toolbar>
        <h1 class="md-title">Users</h1>
      </md-table-toolbar>

      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID" md-numeric>{{ item.id }}</md-table-cell>
        <md-table-cell md-label="Name" md-sort-by="name">{{ item.name }}</md-table-cell>
        <md-table-cell md-label="Email" md-sort-by="email">{{ item.email }}</md-table-cell>
        <md-table-cell md-label="Gender" md-sort-by="gender">{{ item.gender }}</md-table-cell>
        <md-table-cell md-label="Job Title" md-sort-by="title">{{ item.title }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<style lang="scss" scoped>
.searchfield {
	max-width: 300px;
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
    users: [
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
      }
    ]
  }),
  methods: {}
}

</script>
