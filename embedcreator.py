import discord
from random import choice

title1 = title2 = desc1 = desc2 = embed = None

async def embcreate(msg, message, error):
    verificar = str(message).count('[') == str(message).count(']')
    if verificar is True:
            global title1, title2, desc1, desc2
            title1 = message.find('[')
            title2 = message.find(']', title1)
            desc1 = message.find('[', title2)
            desc2 = message.find(']', desc1)
            embed = discord.Embed(title=message[title1+1:title2],
                                  color=int(choice(['1752220', '3066993', '10181046', '2123412', '15158332', '15105570'])))
            if str(message).count('[') == 2:
                await msg.channel.send(embed=discord.Embed(title=message[title1+1:title2],
                                      color=int(choice(['1752220', '3066993', '10181046', '2123412', '15158332', '15105570'])),
                                      description=message[desc1+1:desc2]))
            else:
                await msg.channel.send(embed=embed)
    else:
        await msg.channel.send(embed=error)
