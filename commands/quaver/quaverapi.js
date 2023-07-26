const { SlashCommandBuilder } = require('discord.js');
const axios = require('axios')
const user_url = 'https://api.quavergame.com/v1/users/full/POP303U';

module.exports = {
	data: new SlashCommandBuilder()
		.setName('quaver')
		.setDescription('Log quaver user info'),
	execute(interaction) {
    const data = fetch(user_url)
      .then(re => re.json)
      .then(hi => hi['user']['info']['username'])
		interaction.reply(data);
	},
}
