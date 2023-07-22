const { SlashCommandBuilder } = require('discord.js');
const dog_url = 'https://dog.ceo/api/breeds/image/random';

module.exports = {
	data: new SlashCommandBuilder()
		.setName('dog')
		.setDescription('Get a random picture of a dog.'),
	async execute(interaction) {
		fetch(dog_url)
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