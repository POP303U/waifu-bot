const { SlashCommandBuilder } = require('discord.js');
const axios = require('axios')
const dog_url = 'https://dog.ceo/api/breeds/image/random';

module.exports = {
	data: new SlashCommandBuilder()
		.setName('dog')
		.setDescription('Get a random picture of a dog.'),
	async execute(interaction) {
		await interaction.reply((await axios.get(dog_url)).data.message)
	},
};