const { SlashCommandBuilder } = require('discord.js');
const axios = require('axios')
const dog_url = 'https://dog.ceo/api/breeds/image/random';

module.exports = {
	data: new SlashCommandBuilder()
		.setName('dog')
		.setDescription('Get a random picture of a dog.'),
	async execute(interaction) {
		const res = await axios.get(dog_url);
		const imageUrl = res.data.message;
		return await interaction.reply(imageUrl);
	},
};