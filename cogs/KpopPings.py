import discord, random
from discord.ext import commands

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

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

    @commands.command(aliases = ['s.e.s'])
    async def ses(self, ctx):
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'''S.E.S was a three member group under SM Ent. that debuted in 1996 with the album I\'m Your Girl, and lead single with the same title, making them part of the first generation. They had a fairy concept, and won mulitple bonsangs due to their unique concept. S.E.S disbanded in 2002, only 5 years after debut. In 2016-2017, they briefly reunited for their 20th anniversary, releasing a song on SM Station (Love [Story]), which is a remake of their debut song "I'm Your Girl" and lead single from their third album, "Love", and their 7th Studio album, Remember - S.E.S 20th Anniversary Special.\n{random.choice(self.bot.ses_mv)}''')

    

    

def setup(client):
    client.add_cog(KpopPings(client))