<template>
  <div class="container">
    <div class="content">
      <img src="./assets/sochan.jpeg" alt="jeremy">
      <h1 style="color: white;">Jeremy Sochan's last five games</h1>
      <table v-if="gameData.length > 0">
        <thead>
          <tr>
            <th>DATE</th>
            <th>GAME</th>
            <th>RESULT</th>
            <th>MIN</th>
            <th>PTS</th>
            <th>FGM</th>
            <th>FGA</th>
            <th>REB</th>
            <th>AST</th>
            <th>STL</th>
            <th>BLK</th>
            <th>TOV</th>
            <th>+/-</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="game in gameData" :key="game.GAME_DATE">
            <td>{{ game.GAME_DATE }}</td>
            <td>{{ game.MATCHUP }}</td>
            <td>{{ game.WL }}</td>
            <td>{{ game.MIN }}</td>
            <td>{{ game.PTS }}</td>
            <td>{{ game.FGM }}</td>
            <td>{{ game.FGA }}</td>
            <td>{{ game.REB }}</td>
            <td>{{ game.AST }}</td>
            <td>{{ game.STL }}</td>
            <td>{{ game.BLK }}</td>
            <td>{{ game.TOV }}</td>
            <td>{{ game.PLUS_MINUS }}</td>
          </tr>
        </tbody>
      </table>
      <div v-else>
        Loading...
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      gameData: []
    };
  },
  created() {
    axios.get(process.env.VUE_APP_ST_API_URL + '/get_last_games')
      .then(response => {
        this.gameData = response.data;
      })
      .catch(error => {
        console.error('Error fetching game data:', error);
      });
  }
}
</script>

<style>
.container {
  background-color: black;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.content {
  text-align: center;
}

img {
  width: 40%;
  margin-bottom: 20px;
}

table {
  margin-left: auto;
  margin-right: auto;
  border-collapse: collapse;
  width: 80%;
}

th, td {
  border: 1px solid white;
  padding: 8px;
  color: white;
}

th {
  background-color: #333;
}

tr:nth-child(even) {
  background-color: #555;
}

tr:hover {
  background-color: #777;
}

body {
    overflow: hidden;
    height: 100vh;
}
</style>
