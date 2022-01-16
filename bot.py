import discord
import asyncio
import datetime
from discord.utils import get
from asyncio import sleep
from discord.ext import tasks
from discord.ext import commands

TOKEN = "OTMxOTg0MDMxNDg5MzUxNzAx.YeMXxA.RaYTBu6QLyY9cdVbsYZQj9HJ6OE"

bot = commands.Bot(command_prefix=('f!'))
bot.remove_command( 'help' )

@bot.event
async def on_ready():
    print("Я запущен!") 
	
@bot.command()
async def server(ctx):
	 await ctx.send("Идет подсчет данных серверов котырые используют нашего бота")
	 await asyncio.sleep(5)
	 await ctx.send(len(bot.guilds))
	 await asyncio.sleep(1)
	 await ctx.send("Подсчет окончен by LoveHUB_BOT")
	
@bot.command()
async def info(ctx):
    await ctx.send('**Привет я уникальный бот**\n:wilted_rose:**FlowerLand**:wilted_rose:\n \nмоддерируй свой сервер\nподробнее f!help ')
	
@bot.command()
async def help(ctx):
    await ctx.send('**ПОМОЩЬ**\n:wilted_rose:**FlowerLand**:wilted_rose:\n \n Команды для модерирование сервера\n \n f!ban - Банит участника\n f!kick - Кикает участника\n f!unban - разбанивает\n f!clean n - очищяет чат (место n колличество сообщений) \n f!server - показывает кольчество серверов которые используют нашего бота \n \n Игровые команды \n \n :red_circle: f!popit - мини попыт 5 на 5 ')

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx,member:discord.Member,*,reason=None):
	await member.kick(reason=reason)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, amount = 500):
	await ctx.channel.purge(limit = amount)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx,member:discord.Member,*,reason=None):
	await member.ban(reason=reason)
	await ctx.message.delete()
	await ctx.send("вы успешно выдали бан")
	await asyncio.sleep(5)
	await ctx.message.delete()
	
@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
	bannedUsers = await ctx.guild.bans()
	name, discriminator = member.split('#')
	
	for ban in bannedUsers:
		user = ban.user
		
		if(user.name, user.discriminator) == (name, discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f"{user.mention} разбанен")
			return

@bot.command()
async def popit(ctx):
	await ctx.send('||:red_square:||||:purple_square:||||:blue_square:||||:yellow_square:||||:green_square:||\n||:red_square:||||:purple_square:||||:blue_square:||||:yellow_square:||||:green_square:||\n||:red_square:||||:purple_square:||||:blue_square:||||:yellow_square:||||:green_square:||\n||:red_square:||||:purple_square:||||:blue_square:||||:yellow_square:||||:green_square:||\n||:red_square:||||:purple_square:||||:blue_square:||||:yellow_square:||||:green_square:||\n')


bot.run(TOKEN)			
