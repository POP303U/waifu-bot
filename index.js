const { Client, GatewayIntentBits } = require("discord.js")
const Discord = require("discord.js"); 
const bot = new Discord.Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.DirectMessages, GatewayIntentBits.MessageContent], partials: ["CHANNEL"]})

const waifu_url = 'https://waifu.pics/api/'
const dog_url = 'https://dog.ceo/api/breeds/image/random'
const cat_url = 'https://api.thecatapi.com/v1/images/search'
const duck_url = 'https://random-d.uk/api/v2'

bot.on("ready", () => { 
  console.log(`Logged in as ${bot.user.tag}!`) 
}) 

bot.on('messageCreate', async message => {
  if (message.content === "!waifu") {
    console.log(`Received Message: ` + message.content)
    message.reply("pong");
  }

});

bot.login('');
