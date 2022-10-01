import os
import discord
from discord.ext import commands
import random

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix=commands.when_mentioned_or("$"),
                   description='Relatively simply awesome bot.',
                   case_insensitive=True,
                   intents=discord.Intents.all())

snoop_trigger_lazy = list()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if bot.user.mentioned_in(message):
        if message.content in snoop_trigger_lazy:
            await message.channel.send('https://tenor.com/bEpJu.gif')
    await bot.process_commands(message)


@bot.command(name='8ball', description='Let the 8 Ball Predict!\n')
async def eight_ball(ctx, question):
    responses = ['As I see it, yes.',
                 'Yes.',
                 'Positive',
                 'From my point of view, yes',
                 'Convinced.',
                 'Most Likely.',
                 'Chances High',
                 'No.',
                 'Negative.',
                 'Not Convinced.',
                 'Perhaps.',
                 'Not Sure',
                 'Maybe',
                 'Im to lazy to predict.',
                 'I am tired. *proceeds with sleeping*']
    response = random.choice(responses)
    embed = discord.Embed(title="The Magic 8 Ball has Spoken!")
    complete_message = str(ctx.message.content).split('$8ball ')
    embed.add_field(name='Question: ', value=f'{complete_message[1]}', inline=True)
    embed.add_field(name='Answer: ', value=f'{response}', inline=False)
    await ctx.send(embed=embed)


@bot.command(name='guess', description='Guess a number between 0 and 100!\n')
async def guess_the_number(ctx):
    number = random.randint(0, 100)
    await ctx.send('Type your guess:')
    for i in range(0, 5):
        response = await bot.wait_for('message')
        guess = int(response.content)
        if guess > number:
            await ctx.send('Try a smaller number')
        if guess < number:
            await ctx.send('Try a bigger number')
        if guess == number:
            await ctx.send('You found it!')


@bot.command(name='simp', description='Let snoop check how much of a simp you are!\n')
async def simp(ctx):
    simp_lvl = random.randint(0, 100)
    embed = discord.Embed(title="About your Simpness",
                          description=str(ctx.message.author.name) + ", you're a " + str(
                              simp_lvl) + "% simp for Maddie "
                                          "🏳️‍🌈.",
                          color=0x008f37)
    await ctx.send(embed=embed)



bot.run(token=TOKEN)
