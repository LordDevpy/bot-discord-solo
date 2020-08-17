const Discord = require('discord.js')
require('dotenv/config')
/*
Instale com npm i dotenv
Crie um arquivo .env e dentro dele coloque TOKEN=seutoken
Nomei as constantes lá tudo em maiúsculo, é um pattern da comunidade
*/

const bot = new Discord.Client()

bot.on('ready',  () => {
    console.log('O bot está online!')
})

const flag = '!safadensa'

bot.on('message', msg => {
    const command = msg.content
      .replace(/\s{2,}/g, ' ') // troca isso (pode ser maior) '     '  por isso ' '
      .split(' ')

    if (command[0] !== flag || msg.channel.type === 'dm' || msg.author.bot) {
      return
    }
    
    switch (command[1]) {
      case 'cardapio':
        msg.channel.send('```BEM-VINDO A MAIOR LOJA DE SAFADENSA DO BRASIL!\n\ Aqui estão suas escolhas:\n\ 1- Porn\n\ 2- Hentai(Novos lançamentos! E latência de server alta)\n\ 3- Furry (Acesso somente para o Zarakiando)\n\  AVISO! Não nos responsabilizamos pelo seu pedido!```')

        bot.on('message', resp => {
          if (resp.channel.id === msg.channel.id && resp.author.id !== msg.author.id) { // se o chat for o mesmo e o autor também, então ele executa
            switch (resp.content) {
              case '1':
                msg.channel.send('**Em manutenção!')
                break

              case '2':
                msg.channel.send('```:scroll: ESCOLHA SEU HENTAO! :scroll:\n\ Aqui estão suas escolhas:\n\ 1- Mikasa\n\ 2- Zero Two\n\ 3- Sakura\n\ 4- Jojo reference(Fora de estoque)\n\ 5- Rakudai kishi no cavalery(só os old lembra porra)\n\ 6- Ichigo\n\ 7- Kokoro ```')
                break

              case '3':
                msg.channel.send('**Cara, tu é doente, vai se tratar!!! :rage:**')
                breal

              default:
                msg.channel.send('Comando inválido!!!\nhttps://i.pinimg.com/600x315/2c/c0/c9/2cc0c9c19f0ee720f8aee7d8185e55e1.jpg')
            }
          }
        })
        break

      case 'kamekameha':
        msg.channel.send('https://i.pinimg.com/originals/a0/93/d1/a093d193fc2bf97db4e5da6ddda19668.gif') 
        break

      case 'bom-dia':
        msg.channel.send('Bom dia delícia!!!')
        break

      default:
        msg.channel.send('Comando inválido!!!\nhttps://i.pinimg.com/600x315/2c/c0/c9/2cc0c9c19f0ee720f8aee7d8185e55e1.jpg')
    }
})   

bot.login(process.env.TOKEN) // process.env.ALGUMACOISA isso pega as contantes que você declarou dentro do arquivo .env
