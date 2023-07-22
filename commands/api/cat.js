const { SlashCommandBuilder } = require('discord.js');
const axios = require('axios')
const cat_url = 'https://api.thecatapi.com/v1/images/search';

module.exports = {
	data: new SlashCommandBuilder()
		.setName('cat')
		.setDescription('Get a random picture of a cat.'),
	async execute(interaction) {
		await interaction.reply((await axios.get(cat_url)).data[0].url);
	},
}
			