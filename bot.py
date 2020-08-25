import discord
import dotenv
from random import choice
from picselector import menu
from embedcreator import embcreate

dotenv.load_dotenv()

client = discord.Client()
msg_user = msg = bmsg = pedidouser = pedidoid = None
start = discord.Embed(title='Escolha seu nsfw da zero two! <:zerogun:738732464117121045>: ',
                      description='**1- Imagens\n 2- Gifs\n 3- Imagens realistas\n 4- Ahegao**\n\n AVISO!!! Não nos responsabilizamos pelo seu pedido<:zerotwocrazy:738974003280216194>',
                      color=1752220)
error = discord.Embed(title='<:dissapointment:738974002944409642>Mds tu é burro cara, usa assim:',
                      color=15158332,
                      description='!embed **[título] [descrição]**')

@client.event
async def on_ready():
    print(f'Bot pronto para o uso em {len(client.guilds)} server(s)')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} server(s)"))

@client.event
async def on_message(message):
    args = message.content.lower()

    # argumentos para não: responder outro bot ou si mesmo/ não responder dms
    if message.author == client.user:
        return
    if message.channel.name == 'dm':
        return


    if args == 'bom dia':  # comando bom dia
        await message.channel.send('bom dia delícia! <:zerotwolove:738974003443662918>')

    if args == '!safadensa':
        if message.channel.is_nsfw():
            global bmsg, pedidouser, pedidoid, respostaid, msg
            bmsg = await message.channel.send(embed=start)
            radd = bmsg.add_reaction
            await radd('1️⃣') # tagged
            await radd('2️⃣') # gif
            await radd('3️⃣') # realista
            await radd('4️⃣') # ahegao

            pedidouser = message.author
            pedidoid = message.id
            msg = message
        else:
            await message.channel.send(content='Esse chat NÃO é nsfw! <:dissapointment:738974002944409642>')
    
    if args == 'eduardo':
        await message.channel.send(content="""**E D U A R D O**
https://cdn.discordapp.com/attachments/497062752473317397/736651644468723842/eduardo_1.mp4""")

    if args.startswith('!pergunta ') and len(args) > 11:
        await message.channel.send(choice(['Sim, eu acho!', 'Não, eu não acho.', 'Talvez...']))

    if args.startswith('!embed '):
        await embcreate(message, message.content, error)
        await message.delete()
    if args == '!embed':
        await message.channel.send(embed=error)


@client.event
async def on_reaction_add(reaction, user):

    if user != client.user: # se não for o bot
        if user == pedidouser: # se for o dono do request da msg
            if bmsg.id == reaction.message.id: # se ele reagiu a msg certa
                await menu(reaction.emoji[0], msg)
                await bmsg.delete()


client.run('xxxxxxx')
