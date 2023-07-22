const { SlashCommandBuilder } = require('discord.js');
const cat_url = 'https://api.thecatapi.com/v1/images/search';

module.exports = {
	data: new SlashCommandBuilder()
		.setName('cat')
		.setDescription('Get a random picture of a cat.'),
	async execute(interaction) {
		fetch(cat_url)
			.then(response => {
				if (!response.ok) {
					throw new Error("Network response was not ok");
				}
				return response.json();
			})
			.then(data => {
				const imageUrl = data[0].url;
				return interaction.reply(imageUrl);
			})
	},
};