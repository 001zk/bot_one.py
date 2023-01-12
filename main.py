from http import client
from mailbox import linesep
import discord 
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '!regras':
                           await message.channel.send(f"**ola,{message.author.mention}as regras do server sao:**{os.linesep} 1º Spam e Flood são   completamente proibidos, não polua o chat com mensagens que não fazem sentido {os.linesep} {os.linesep} 2º Qualquer tipo de preconceito é também proibido, respeite os outros, sem xingamentos direcionados, assédio, bullyng, etc {os.linesep} {os.linesep} 3º Não divulgue link de nenhum servidor sem a permissão de um administrador{os.linesep} {os.linesep} 4º Mantenha o respeito <a:bluetick:985187193796575293> {os.linesep} {os.linesep} 5º Caso você queira ajuda, ou queira fazer alguma denuncia faça um ticket no canal <#979022261057118238> (qualquer denuncia ou sugestao no privado dos adms sera ignorada) {os.linesep} {os.linesep} 6º Sem divulgação no chat ou no privado de membros do servidor. {os.linesep} {os.linesep} **Essas regras podem mudar com o passar do tempo, então mantenha esses obrigações acima para  melhor ambiente no servidor ** {os.linesep} {os.linesep}_envie sugestao de coisas interessantes para a melhoria do server no canal de suporte._")
                           
                           
                           
async def enviarembed(ctx):
    embed = discord.embed(
        title = 'regras',
        colour = discord.colour.red(),
        description = 'await message.channel.send(f"**ola,{message.author.mention}as regras do server sao:**{os.linesep} 1º Spam e Flood são   completamente proibidos, não polua o chat com mensagens que não fazem sentido {os.linesep} {os.linesep} 2º Qualquer tipo de preconceito é também proibido, respeite os outros, sem xingamentos direcionados, assédio, bullyng, etc {os.linesep} {os.linesep} 3º Não divulgue link de nenhum servidor sem a permissão de um administrador{os.linesep} {os.linesep} 4º Mantenha o respeito <a:bluetick:985187193796575293> {os.linesep} {os.linesep} 5º Caso você queira ajuda, ou queira fazer alguma denuncia faça um ticket no canal <#979022261057118238> (qualquer denuncia ou sugestao no privado dos adms sera ignorada) {os.linesep} {os.linesep} 6º Sem divulgação no chat ou no privado de membros do servidor. {os.linesep} {os.linesep} 7° caso digite algo proibido ou quebra alguma regra você tera apenas mais oportunidades, o banimento sera imediato após os 3 avisos, qualquer erro ou engano contate os moderadores {os.linesep} **Essas regras podem mudar com o passar do tempo, então mantenha esses obrigações acima para  melhor ambiente no servidor ** {os.linesep} {os.linesep}_envie sugestao de coisas interessantes para a melhoria do server no canal de suporte._")',
    )

    await ctx.send(embed = embed)

                                                         
client = MyClient()
client.run('') #token do seu bot do discord
