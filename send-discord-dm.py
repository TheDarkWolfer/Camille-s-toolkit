import discord
from discord.ext import commands

# Your bot's token
bot_token = 'YOUR_BOT_TOKEN'

# Initialize a bot instance
bot = commands.Bot(command_prefix='!')

# Event handler when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to send a message to a specific user
@bot.command()
async def send_message(ctx, user_id: int, *, message: str):
    try:
        # Fetch the user based on their ID
        user = bot.get_user(user_id)

        if user:
            # Send a direct message to the user
            await user.send(message)
            await ctx.send(f'Message sent to {user.name}: {message}')
        else:
            await ctx.send('User not found.')

    except Exception as e:
        await ctx.send(f'Error sending message: {str(e)}')

# Start the bot
bot.run(bot_token)
