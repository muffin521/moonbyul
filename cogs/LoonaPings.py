import discord, random
from discord.ext import commands

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

class LoonaPings(commands.Cog):

    def __init__(self, client):
        self.client = client

        #10
        self.heejin_gif = ["https://tenor.com/view/%EC%9D%B4%EB%8B%AC%EC%9D%98%EC%86%8C%EB%85%80-%ED%9D%AC%EC%A7%84-loona-heejin-dancing-gif-15500748",
            "https://tenor.com/view/heejin-waving-hi-hello-smile-gif-16980677",
            "https://tenor.com/view/heejin-loona-gif-18855977",
            "https://tenor.com/view/heejin-loona-gif-18630598",
            "https://tenor.com/view/heejin-loona-gif-18892027",
            "https://tenor.com/view/loona-hee-jin-hello-smile-gif-14824756",
            "https://tenor.com/view/loona-heejin-cute-gif-8365491",
            "https://tenor.com/view/heejin-loona-nodding-sad-nodding-yeah-gif-16288849",
            "https://tenor.com/view/heejin-loona-gif-18855987",
            "https://tenor.com/view/heejin-loona-gif-18855973"]

        #16
        self.hyunjin_gif = ["https://cdn.discordapp.com/attachments/771238115255255060/771239029291221022/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239029982101534/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239030301786132/image2.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239030984933376/image3.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239031534649344/image4.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239032360271872/image5.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239033023496202/image6.gif",
            "https://tenor.com/view/hyunjin-hyunjin-cute-loona-hyunjin-loona-kpop-girl-gif-15567551",
            "https://cdn.discordapp.com/attachments/771238115255255060/771478311045955584/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771478314715447316/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771478316427378748/image2.gif",
            "https://tenor.com/view/k-im-hyunjin-loona-got-you-cute-pretty-gif-16467662",
            "https://tenor.com/view/loona-loona-hyunjin-hyunjin-kim-hyunjin-loona-aeong-gif-18902504",
            "https://cdn.discordapp.com/attachments/771238115255255060/777819042685779978/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/777819043649683476/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/777819045034065920/image2.gif"]

        #13
        self.kimlip_gif = ["https://thumbs.gfycat.com/CaringAlertHellbender-max-1mb.gif",
            "https://64.media.tumblr.com/632b50fcf95204b79d978049034e2f9f/tumblr_pe89snEig71x29wuzo4_250.gif",
            "https://i.pinimg.com/originals/b8/22/88/b82288fdc234bd0a50be07ae1ec212ef.gif",
            "https://thumbs.gfycat.com/WeeSillyAngelfish-max-1mb.gif",
            "https://media1.tenor.com/images/8cdb11b9b4a58c517215531156cc1812/tenor.gif?itemid=13802828",
            "https://i2.wp.com/66.media.tumblr.com/935a3a56a302380eeb10be67640a880a/b3f428ad85343842-de/s400x600/b31d01f30df1a8ac781460c8460f697e87c2e57d.gif?w=817&ssl=1",
            "https://64.media.tumblr.com/496da05c77ed58eac63f37cdd4bc7e9b/abfaa74408006212-71/s400x600/df7abdfe16b17d71598cab49b1202362b5ca4e61.gif",
            "https://i.pinimg.com/originals/15/41/f8/1541f83313271d2e8eb76220cbf43f24.gif",
            "https://data.whicdn.com/images/290426395/original.gif",
            "https://64.media.tumblr.com/151136f17e11dd8f80fe626d7fe685e4/tumblr_pdue0gd2P81somnmfo2_400.gif",
            "https://i.pinimg.com/originals/b6/26/68/b62668ab9b50797aa7418e16074de809.gif",
            "https://64.media.tumblr.com/0072acb65c1a86773f842628f748faaa/tumblr_pul162PtSc1xpl3u9o1_r1_250.gif",
            "https://64.media.tumblr.com/40ad336b08f95aa5490afeedf10df5c6/tumblr_p92066rl3z1w5jkuno5_r1_500.gif"]

        #7
        self.choerry_gif = ["https://tenor.com/view/choerry-loona-gif-18740424",
            "https://tenor.com/view/loona-choerry-kpop-cute-wave-gif-16635613",
            "https://tenor.com/view/choi-yerim-choerry-kpop-paper-loona-gif-17213985",
            "https://cdn.discordapp.com/attachments/747275528993636424/775111507486310450/4ab7d195-ce65-423a-a177-cb1f6a6a7648.gif",
            "https://media.discordapp.net/attachments/704248706269970488/775111463579942952/image0.gif",
            "https://cdn.discordapp.com/attachments/747275528993636424/775112055244980264/2010061.gif",
            "https://cdn.discordapp.com/attachments/747275528993636424/775112225965867048/2002192.gif"]

    #heejin command for mae and aeong
    @commands.command()
    async def heejin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@492769416610840586>, <@542342961392779264>, <@!{ctx.author.id}> is talking about Heejin :rabbit:')
                await ctx.send(random.choice(self.heejin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Heejin :rabbit:')
            await ctx.send(random.choice(self.heejin_gif))
            await ctx.message.delete()

    #hyunjin command for k8 and aeong
    @commands.command()
    async def hyunjin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@573974040679809044>, <@542342961392779264>, <@!{ctx.author.id}> is talking about Hyunjin :rabbit:')
                await ctx.send(random.choice(self.hyunjin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Hyunjin :rabbit:')
            await ctx.send(random.choice(self.hyunjin_gif))
            await ctx.message.delete()

    #kim lip command for stanley
    @commands.command(aliases=['kim', 'lip', 'lippington', 'kimlip'])
    async def lippie(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@727312020717830264>, <@!{ctx.author.id}> is talking about Kim Lip :owl:')
                await ctx.send(random.choice(self.kimlip_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=6)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Kim Lip :owl:')
            await ctx.send(random.choice(self.kimlip_gif))
            await ctx.message.delete()


    #choerry command for rith and ple
    @commands.command()
    async def choerry(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@346724857725059075>, <@416903886968979466>, <@!{ctx.author.id}> is talking about Choerry :bat:')
                await ctx.send(random.choice(self.choerry_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()            
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Choerry :bat:')
            await ctx.send(random.choice(self.choerry_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(LoonaPings(client))