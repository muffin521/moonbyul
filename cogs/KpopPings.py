import discord, random
from discord.ext import commands

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

#//people
muffin = 488423352206229505
weakado = 259409277482041344
k8 = 573974040679809044
mae = 492769416610840586
kiwi = 390317665463566336
kate = 382715972722753536

class KpopPings(commands.Cog):

    def __init__(self, client):
        self.client = client

        #7
        self.yiren_gif = ["https://tenor.com/view/yireon-hearts-wishing-wish-produce48-gif-11924127",
            "https://tenor.com/view/love-you-more-wink-side-eye-flirt-smile-gif-16944406",
            "https://tenor.com/view/%E7%8E%8B%E6%80%A1%E4%BA%BAwang-yiren-cute-kpop-smile-gif-16236336",
            "https://tenor.com/view/wang-yiren-everglow-kpop-cute-sad-gif-16526333",
            "https://tenor.com/view/everglow-yiren-wang-yiren-maknae-rapper-gif-15970519",
            "https://tenor.com/view/wang-yiren-everglow-kpop-fierce-gif-15559282",
            "https://tenor.com/view/%E7%8E%8B%E6%80%A1%E4%BA%BAwang-yiren-cute-kpop-smile-gif-16236336"]

        #19
        self.yeeun_gif = ["https://tenor.com/view/yeeun-clc-gif-19116003",
            "https://tenor.com/view/yeeun-clc-gif-19116004",
            "https://tenor.com/view/yeeun-clc-gif-19116007",
            "https://tenor.com/view/yeeun-clc-gif-19116012",
            "https://tenor.com/view/yeeun-clc-bad-girls-jang-gif-13252706",
            "https://tenor.com/view/yeeun-clc-crystal-clear-cute-girl-group-gif-15041212",
            "https://tenor.com/view/clc-yeeun-clc-yeeun-rap-kpop-gif-15340668",
            "https://tenor.com/view/clc-kpop-yeeun-gif-18657579",
            "https://tenor.com/view/yeeun-jang-clc-cute-stare-gif-13329818",
            "https://tenor.com/view/yeeun-jang-yeeun-cute-clc-kpop-gif-17883335",
            "https://tenor.com/view/yeeun-clc-crystal-clear-cute-girl-group-gif-15041189",
            "https://tenor.com/view/yeeun-clc-bad-girls-jang-gif-13252063",
            "https://tenor.com/view/yeeun-jang-clc-flip-hair-gif-13252498",
            "https://tenor.com/view/yeeun-jang-clc-gif-13328477",
            "https://tenor.com/view/jang-ye-eun-selfie-talking-cute-pretty-gif-16653425",
            "https://tenor.com/view/yeeun-jang-yeeun-clc-crystal-clear-girl-group-gif-15041366",
            "https://tenor.com/view/crystal-clear-jang-kpop-yeeun-clc-gif-14859536",
            "https://tenor.com/view/yay-wink-cute-yeeun-clc-gif-14300869",
            "https://tenor.com/view/yeeun-jang-clc-not-yummy-gif-13252749",
            "https://tenor.com/view/crystal-clear-jang-kpop-devil-yeeun-gif-14999392"]

        #11
        self.lucas_gif = ["https://tenor.com/view/lucas-wayv-heart-gif-14723401",
            "https://tenor.com/view/smile-handsome-cute-lucas-nct-gif-15246419",
            "https://tenor.com/view/nct-lucas-nct-lucas-cute-smile-gif-12612522",
            "https://tenor.com/view/nct-lucas-being-extra-hi-gif-14904496",
            "https://tenor.com/view/pout-kiss-handsome-cute-lucas-gif-15246420",
            "https://tenor.com/view/lucas-nct-way-v-gif-13770508",
            "https://tenor.com/view/wong-yukhei-lucas-nct-cute-kpop-gif-16350448",
            "https://tenor.com/view/lucas-nct-wayv-gif-19030351",
            "https://tenor.com/view/lucas-nct-smile-gif-19015832",
            "https://tenor.com/view/lucas-smile-cute-poke-cheek-gif-12719055",
            "https://tenor.com/view/lucas-nct-wong-yukhei-wayv-gif-14579895"]

        #17
        self.ses_mv = ["https://www.youtube.com/watch?v=WpmTLDtr4qY", #im your girl
            "https://www.youtube.com/watch?v=ZpJJIK1gK6I", #oh my love
            "https://www.youtube.com/watch?v=q_yyXw83rt8", #dreams come true 
            "https://www.youtube.com/watch?v=Z3UBcSRxjo0", #i love you
            "https://www.youtube.com/watch?v=1Cjt_2BsnCs", #shy boy
            "https://www.youtube.com/watch?v=T-KJZjHJYjo", #love
            "https://www.youtube.com/watch?v=A_x9_iK1nGA", #twilight zone
            "https://www.youtube.com/watch?v=T7imPmAQhfc", #show me your love
            "https://www.youtube.com/watch?v=geWN7mHXzv4", #be natural
            "https://www.youtube.com/watch?v=Izyclmg2Jp8", #just in love
            "https://www.youtube.com/watch?v=z1Px4wF9dMo", #U
            "https://www.youtube.com/watch?v=8XrnhhmTN9E", #just a feeling
            "https://www.youtube.com/watch?v=-gUU29UCQwQ", #S.II.S (Soul to Soul)
            "https://www.youtube.com/watch?v=M14nT1ZELfM", #love story
            "https://www.youtube.com/watch?v=Rr0kii_IYqU", #remember
            "https://www.youtube.com/watch?v=vAO_OcRz6xQ" #paradise
            ]


    #yiren (everglow) command for weakado
    @commands.command()
    async def yiren(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{weakado}>, <@!{ctx.author.id}> is talking about Yiren :orange_heart:')
                await ctx.send(random.choice(self.yiren_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yiren :orange_heart:')
            await ctx.send(random.choice(self.yiren_gif))
            await ctx.message.delete()
    
    #yeeun (clc) command for me
    @commands.command()
    async def yeeun(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Yeeun :heart:')
                await ctx.send(random.choice(self.yeeun_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yeeun :heart:')
            await ctx.send(random.choice(self.yeeun_gif))
            await ctx.message.delete()

    @commands.command()
    async def lucas(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{kate}>, <@!{ctx.author.id}> is talking about Lucas :heart: ')
                await ctx.send(random.choice(self.lucas_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Lucas :heart:')
            await ctx.send(random.choice(self.lucas_gif))
            await ctx.message.delete()
    
    @commands.command(aliases = ['s.e.s'])
    async def ses(self, ctx):
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'''S.E.S was a three member group under SM Ent. that debuted in 1996 with the album I\'m Your Girl, and lead single with the same title, making them part of the first generation. They had a fairy concept, and won mulitple bonsangs due to their unique concept. S.E.S disbanded in 2002, only 5 years after debut. In 2016-2017, they briefly reunited for their 20th anniversary, releasing a song on SM Station (Love [Story]), which is a remake of their debut song "I'm Your Girl" and lead single from their third album, "Love", and their 7th Studio album, Remember - S.E.S 20th Anniversary Special.\n{random.choice(self.ses_mv)}''')

def setup(client):
    client.add_cog(KpopPings(client))