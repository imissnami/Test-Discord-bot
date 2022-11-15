from discord.ext import commands
import discord

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=".", help_command= None, intents = intents)

@bot.event
async def on_ready():
    print("this bot in now online")

@bot.command()
async def say(ctx):
    embed=discord.Embed(title="Mazza", description="description", color=0xff0000)
    embed.set_footer(text="Power By Mazza")
    await ctx.send(embed=embed)

@bot.command()
async def test(ctx):
    await ctx.send("Mazza")

#bot.event
#sync def on_message(message):
#   Blacklisted = [".com", "https://", "http://", "www.", "discord.gg", ".gif"]
#   report_logs = bot.get_channel(1041550283471343686)
#   for m in Blacklisted: 
#       if m in message.content or m.lower() in message.content: 
#           await report_logs.send(f"{message.author.mention} has tried to use blacklisted word.")
#           await message.delete()
#           await message.channel.send(f"You can not send this message {message.author.mention}.")

bot.run("Token")
