const { SlashCommandBuilder } = require('discord.js');
const axios = require('axios')
const cat_url = 'https://api.thecatapi.com/v1/images/search';

module.exports = {
	data: new SlashCommandBuilder()
		.setName('cat')
		.setDescription('Get a random picture of a cat.'),
	async execute(interaction) {
		const res = await axios.get(cat_url);
		console.log(res);
		const imageUrl = res.data[0].url;
		return await interaction.reply(imageUrl);
	},
};