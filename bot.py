#!/usr/bin/python3.5
import discord
from discord.ext import commands
import random

description = 'a'
bot = commands.Bot(command_prefix='#', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def cowboy():
   
#    cowboy='''
#Вы арестованы:cowboy:
#　　　　　:100::100::100:
#　　　　:100: 　:100:　:100:
#　　　:point_down::skin-tone-3:　  :100::100:　:point_down::skin-tone-3:
#　　　　　:100:　  :100:
#　　　　　:100:　　:100:
#　　　　　 :boot:　　:boot:
#'''
    cowboy='''
Я арестован    :tired_face:
　　　　　:100::100::100:
　　　　:100: 　:100:　:100:
　　　:point_down::skin-tone-3:　  :100::100:　:point_down::skin-tone-3:
　　　　　:100:　  :100:
　　　　　:100:　　:100:
　　　　　 :boot:　　:boot:
'''
    await bot.say(cowboy)


@bot.command()
async def test_pic():
    await bot.say("http://windowsnotes.ru/wp-content/uploads/2013/10/cmdvsps9.png")


@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command()
async def pidor():
    await bot.say("sam pidor")

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')



bot.run('MzM2Nzc5NjE4MzIzNTI5NzI4.DE9j0g.RUCtxv1lg7NjZStI6ZY4-Ac5g8c')
