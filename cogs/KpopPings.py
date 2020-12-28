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

    def __init__(self, bot):
        self.bot = bot

        self.bot.ses_mv = ["https://www.youtube.com/watch?v=WpmTLDtr4qY", #im your girl
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

        self.bot.cl_gif = ["https://media.discordapp.net/attachments/771238115255255060/785288565273788426/image2.gif",
            "https://media.discordapp.net/attachments/771238115255255060/785288564912160819/image1.gif",
            "https://media.discordapp.net/attachments/771238115255255060/785288541785161758/image0.gif",
            "https://tenor.com/view/cl-hello-bitches-group-show-gif-14566826",
            "https://tenor.com/view/2ne1-cl-chaelin-chaerin-chaelin-lee-gif-7177115",
            "https://tenor.com/view/cl-kpop-performance-singer-gif-14566821",
            "https://tenor.com/view/cl-2ne1-rapper-korean-k-pop-gif-9210983",
            "https://tenor.com/view/2ne1-hello-kpop-hi-gif-14032003",
            "https://tenor.com/view/2ne1-chaelin-cl-chaelin-lee-mocking-gif-7177330"]

    

    @commands.command(aliases = ['s.e.s'])
    async def ses(self, ctx):
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'''S.E.S was a three member group under SM Ent. that debuted in 1996 with the album I\'m Your Girl, and lead single with the same title, making them part of the first generation. They had a fairy concept, and won mulitple bonsangs due to their unique concept. S.E.S disbanded in 2002, only 5 years after debut. In 2016-2017, they briefly reunited for their 20th anniversary, releasing a song on SM Station (Love [Story]), which is a remake of their debut song "I'm Your Girl" and lead single from their third album, "Love", and their 7th Studio album, Remember - S.E.S 20th Anniversary Special.\n{random.choice(self.bot.ses_mv)}''')

    @commands.command()
    async def cl(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{k8}>, <@!{ctx.author.id}> is talking about CL :cherries: ')
                await ctx.send(random.choice(self.bot.cl_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about CL :cherries:')
            await ctx.send(random.choice(self.bot.cl_gif))
            await ctx.message.delete()

    

def setup(client):
    client.add_cog(KpopPings(client))