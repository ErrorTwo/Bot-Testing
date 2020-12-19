import discord
import random

from discord.ext import commands

client = commands.Bot(command_prefix='.')
client.remove_command('help')


@client.event
async def Bot():
    print("Bot is Ready")

@client.command(aliases=['gm'])
async def gaymeter(ctx, player):
    color = [
        discord.Colour.blue(),
        discord.Colour.magenta(),
        discord.Colour.purple(),
        discord.Colour.orange(),
        discord.Colour.blurple(),
        discord.Colour.dark_gold(),
        discord.Colour.dark_gray(),
        discord.Colour.dark_blue(),
        discord.Colour.red()
    ]
    await ctx.send(
        embed=discord.Embed(
            title='**Gay Meter**',
            description=f'**:rainbow_flag: {player} is %{random.randint(0, 100)}** :rainbow:',
            colour=random.choice(color)
        )
    )


@client.command(aliases=['wm'])
async def weebmeter(ctx, player):
    await ctx.send(
        embed=discord.Embed(
            title='**Weeb Meter**',
            description=f"""
{player} is %{random.randint(0, 100)} Weeb
            """,
            colour=discord.Colour.green()
        )
    )


@client.command(aliases=['km'])
async def knowledgemeter(ctx, player):
    await ctx.send(
        embed=discord.Embed(
            title='**Knownledge Meter**',
            description=f':brain: {player} is %{random.randint(0, 100)} :brain:',
            colour=discord.Colour.from_rgb(255, 182, 193)
        )
    )


@client.command(aliases=['8ball', 'ft'])
async def _8ball(ctx, *, question):
    responses = ['It is Certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful']
    await ctx.send(
        embed=discord.Embed(
            title='**8Ball**',
            description=f'Question: {question}\n Answer: {random.choice(responses)}',
            colour=discord.Colour.blurple()
        )
    )


@client.command(aliases=['rs'])
async def randomstand(ctx, player):
    response = [
        f"""
**Star Platinum(Jotaro)**
https://cdn.discordapp.com/attachments/773991102071570442/774472193710882847/latest.png
""",
        f"""
**The World(Dio)**
https://cdn.discordapp.com/attachments/773991102071570442/774474087422492692/585925a78e6763ec4e146494a327e3ce.png
""",
        f"""
**Crazy Diamond(Josuke)**
https://cdn.discordapp.com/attachments/773991102071570442/774478730600382464/9k.png
""",
        f"""
**D4C(Strano)**
https://cdn.discordapp.com/attachments/773991102071570442/774479339294556181/maxresdefault.png
""",
        f"""
**Hierophant Green(Noriaki)**
https://cdn.discordapp.com/attachments/773991102071570442/774479808696287242/images.png
""",
        f"""
**The Hand(Okuyasu)**
https://cdn.discordapp.com/attachments/773991102071570442/774480378588168192/2Q.png
""",
        f"""
**Killer Queen(Yoshikage)**
https://cdn.discordapp.com/attachments/773991102071570442/774480876347588648/Z.png
""",
        f"""
**Sliver Chariot(Shiruba)**
https://cdn.discordapp.com/attachments/773991102071570442/774481311670468658/9k.png
"""]
    await ctx.send(
        f"""
{player} your stand is...
{random.choice(response)}
"""
    )

@client.command(aliases=['ac', 'admincmds'])
async def admincommands(ctx):
    embed = discord.Embed(
        title='**Admin Commands**',
        colour=discord.Colour.green()
    )
    embed.set_author(name='A Marvelous Adventure', icon_url='https://i.imgur.com/GuOtREd.png')
    embed.set_thumbnail(url='https://i.imgur.com/GuOtREd.png')
    embed.add_field(name='Clear', value='This command is exclusive to the Clear role and it clears text from a channel in a certain amount.')

    await ctx.send(embed=embed)

@client.command(aliases=['information', 'help'])
async def info(ctx):
    embed = discord.Embed(
        title='**Information/Help**',
        description='The AMA Bot is only for the A Marvelous Adventure Group.',
        colour=discord.Colour.purple()
    )
    embed.set_author(name='A Marvelous Adventure', icon_url='https://i.imgur.com/GuOtREd.png')
    embed.set_image(url='https://i.imgur.com/FJ0jCzt.png')
    embed.set_thumbnail(url='https://i.imgur.com/GuOtREd.png')
    embed.add_field(name='/ac or /admincmd', value='Shows commands for certain role.')
    embed.add_field(name='/rsinfo', value='Shows you all the stands in the /randomstand or /rs.')
    embed.add_field(name='/staffinfo or si or staffinformation', value="This command tells you about the staff username and there ranking.")
    embed.add_field(name='/fc or /funcommans', value='This command shows all the fun command you could use.')
    embed.add_field(name='/gi or /gameinfo or /gameinformation', value='This command tells you about the game and give a little description.')
    embed.set_footer(text='From AMA / A Marvelous Adventure Bot', icon_url='https://i.imgur.com/GuOtREd.png')
    await ctx.send(embed=embed)


@client.command(aliases=['randomstandinformation', 'randomstandinfp'])
async def rsinfo(ctx):
    await ctx.send(
        embed=discord.Embed(
            title='**Random Stand Info**',
            description="""
            
[+] Star Platinum(Jotaro)
[+] The World(Dio)
[+] Crazy Diamond(Josuke)
[+] D4C(Strano)
[+] Hierophant Green(Noriaki)
[+] The Hand(Okuyasu)
[+] Killer Queen(Yoshikage)
[+] Sliver Chariot(Shiruba)
            """
        )
    )

@client.command(aliases=['fc'])
async def funcommands(ctx):
    embed=discord.Embed(
        title='**Fun Commands**',
        colour=discord.Colour.orange()
    )
    embed.set_author(name='A Marvelous Adventure', icon_url='https://i.imgur.com/GuOtREd.png')
    embed.set_thumbnail(url='https://i.imgur.com/GuOtREd.png')
    embed.add_field(name='/randomstand or /rs', value='This command will generate a stand.')
    embed.add_field(name='/weebmeter or /wm', value='This command will generate a random percent.')
    embed.add_field(name='/knowledgemeter or /km', value='This command will generate a random percent.')
    embed.add_field(name='/8ball', value='This command will generate a random response.')
    embed.add_field(name='/gaymeter or /gm', value='This command will generate a random percent.')
    embed.add_field(name='/ping', value='This command shows your Ping / ms.')
    embed.set_footer(text='From AMA / A Marvelous Adventure Bot', icon_url='https://i.imgur.com/GuOtREd.png')
    await ctx.send(embed=embed)

@client.command(aliases=['gi', 'gameinformation'])
async def gameinfo(ctx):
    await ctx.send(
        embed=discord.Embed(
            title='**A Marvelous Adventure**',
            description="""
A Marvelous Adventure is a Roblox game, made from iiamdover(
https://web.roblox.com/users/862332519/profile). The game is based on the popular anime called "Jojo Bizarre Adventure" 
right now the game is still in development. """,
            colour=discord.Colour.red()
        )
    )


@client.command(aliases=['si', 'staffinformation'])
async def staffinfo(ctx):
    await ctx.send(
        embed=discord.Embed(
            title='**Staff (Roblox Username)**',
            description="""
**Owner:**
iiamdover

**Co-Owners:**
TheRelROBO_DYSTORYER
CrispyChris989 or iusemarjuana

**Developers:**
iiamdover
happyangelicus
razbijaclol123 or gruchie
TonyDuy12
VoidedFuture

**Head Admins:**
DeferentPVZ
happyangelicus
TonyDuy12

**Admins:**
Kaydenpro
sirshark8
pencilstastebad or all_ahismyfav
nullakingjabron15

**Mods:**
itchyEversongamer
NiceDullChristian22
Ichka222
StoveZdefe
sherwin8846

**Leader of the testers:**
CrispyChris989 or iusemarjuana
            """
        )
    )

@client.command()
async def ping(ctx):
    await ctx.send(f'Your Ping is {round(client.latency * 1000)}ms')

@client.command()
@commands.has_role('Clear')
async def clear(ctx, *, amount=None):
    await ctx.channel.purge(limit=int(amount))


@client.event
async def on_message(message):
    message.content = message.content.lower()
    await client.process_commands(message)


client.run('Nzc2MTAwODk1NDAyMjI5ODAw.X6v-SA.GaL9N_gts7KfEFeeot-tAIdP2G8')
