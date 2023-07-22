const { SlashCommandBuilder } = require('discord.js');
const axios = require('axios');
const waifu_url = 'https://api.waifu.pics/';

module.exports = {
	data: new SlashCommandBuilder()
		.setName('waifu')
		.setDescription('Get a random picture of a waifu.')
        .addStringOption(option =>
            option.setName('type')
                .setDescription('Choose the type of images')
                .setRequired(true)
                .addChoices(
                    { name: "sfw", value: 'sfw'},
                    { name: 'nsfw', value: 'nsfw'},
                ))
        .addStringOption(option =>
            option.setName('category')
                .setDescription('Choose the category of images')
                .setRequired(true)
                .addChoices(
                    { name: 'waifu', value: 'waifu'},
                    { name: 'neko', value: 'neko'},
                    { name: 'shinobu', value: 'shinobu'},
                    { name: 'megumin', value: 'megumin'},
                    { name: 'bully', value: 'bully'},
                    { name: 'cuddle', value: 'cuddle'},
                    { name: 'cry', value: 'cry'},
                    { name: 'hug', value: 'hug'},
                    { name: 'awoo', value: 'awoo'},
                    { name: 'kiss', value: 'kiss'},
                    { name: 'lick', value: 'lick'},
                    { name: 'pat', value: 'pat'},
                    { name: 'smug', value: 'smug'},
                    { name: 'bonk', value: 'bonk'},
                    { name: 'yeet', value: 'yeet'},
                    { name: 'blush', value: 'blush'},
                    { name: 'smile', value: 'smile'},
                    { name: 'wave', value: 'wave'},
                    { name: 'highfive', value: 'highfive'},
                    { name: 'handhold', value: 'handhold'},
                    { name: 'nom', value: 'nom'},
                    { name: 'bite', value: 'bite'},
                    { name: 'glomp', value: 'glomp'},
                    { name: 'slap', value: 'slap'},
                )),
	async execute(interaction) {
        const arg1 = interaction.options.getString('type');
        const arg2 = interaction.options.getString('category');
        const response = await axios.get(waifu_url + arg1 + '/' + arg2);
        const imageUrl = response.data.url;
        return await interaction.reply(imageUrl);
	},
};