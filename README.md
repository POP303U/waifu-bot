# waifu-bot
A Discord bot for scraping images from the waifu.pics api.

## How to set up the Bot?

**Step 1:** Create the bot

Go to the Discord Developer Portal (https://discord.com/developers/applications).
Create a new application and give it a name.
Navigate to the "Bot" section and click on "Add Bot" to create a bot user.
Enable the "Presence Intent" and "Server Members Intent" under the "Privileged Gateway Intents" section.
Copy the bot token for later use.

**Step 2:** Install necessary dependencies:

Install the discord library by running ```pip install discord```

**Step 3:** Use your bot token 

Replace the string in the function bot.run() with the actual bot token you obtained earlier.

**Step 4:** Add the bot to your server

Go to the Discord Developer Portal and click on your application.
Navigate to the "OAuth2" section and then to "Url Generator".
Check the box "bot" and then in the new window below "Administrator".
Use the url that has been generated to add the bot to your server.

**Step 5:** Run the Programm

After you verified that your bot has all permissions and the bot token is correct,
run the programm and test it out in a server with the bot running by typing: 
!waifu

