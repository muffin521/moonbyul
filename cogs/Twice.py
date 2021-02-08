import discord, random, os
from discord.ext import commands
from datetime import datetime

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

#//people
gareth = 389897179701182465

class gamerPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.mina_gif = ["https://tenor.com/NUon.gif",
            "https://tenor.com/4vrC.gif",
            "https://tenor.com/HydV.gif",
            "https://tenor.com/brQ1g.gif",
            "https://media.giphy.com/media/qzuGfHYC152dG/giphy.gif",
            "https://64.media.tumblr.com/6180c42fe314efaa840ab99c1f461550/c8dd9ab35553aa4d-7e/s540x810/e377c67b5af8309e2c9120f2ce95bfd1c44c4452.gif",
            "https://64.media.tumblr.com/567ebdddcad6bd8cd8bc1936b6e965ee/2617704d59173453-4d/s400x600/8039fbc724642a74527ffabd09d4df4b5edb7ae6.gif",
            "https://64.media.tumblr.com/ba76b980d2cd735420cf0827881fc091/b8fef663de1f7a99-1d/s400x600/9fd70725b5d8d1326247604dcfdecd420151df1c.gif",
            "https://64.media.tumblr.com/b9baab82f79bf54ae9d55dfeeae404f7/c2c0d737ddf77bee-31/s400x600/21a1e7283aef69779b6e964e07522ed17fe686b1.gif",
            "https://64.media.tumblr.com/7f447af2c8af7859490e4ad1be7fd08c/7378d62a6b5e080d-7b/s400x600/3c087510487f48bd494604058246679ec819841d.gif",
            "https://64.media.tumblr.com/e247fe8c9fe7e8c56731e5fe1131a7c5/d6d42f274ab81eb9-ed/s540x810/9d022e647bfc39663d2884d252594e522271345f.gif",
            "https://64.media.tumblr.com/9f60506b39f318fbd864ba46c5d04cf6/ea259c1353ae60d4-20/s400x600/1e8426d4f812ca6f890086991969290af5828cfd.gif",
            "https://64.media.tumblr.com/692e8b5944bf0c03651a4bfb9475fe9c/fbddd6465e73e5be-88/s540x810/cccb18e6439e1d483e1a2c030ce6c35491a1b488.gif",
            "https://64.media.tumblr.com/1962f8fb8b35e6202ce1968408b790d4/ac86dbbe396b04a5-0e/s540x810/71f05ff7c39623e7f31ae3a22b5aed063758c690.gif",
            "https://64.media.tumblr.com/26e9c4978b68f728f098f1dd7abcc666/e330829990f571a5-66/s540x810/e26e99166689f2c7373af3de241ce397954f2a39.gif",
            "https://64.media.tumblr.com/6dd8a524c52d9b56a10e7feb12301589/928dd6e3d0ee7a5a-5c/s540x810/d79eb5c8a29713e1181e888fad2efd1c927bc7de.gif",
            "https://64.media.tumblr.com/79ca43dcddbaef5afdbb82995926ce41/ccab6d71ba02df9b-91/s400x600/42a73d54093d796237cff9b42dee10aefa1cad27.gif",
            "https://64.media.tumblr.com/54bd81a8abe22d7c9b7785dde77fdf3b/2cc21bec233193aa-a9/s400x600/6b7a549b558548b7f92ea3d273b8457b88cc1a68.gif",
            "https://64.media.tumblr.com/28474864d922eef6bbeeeb71d7fbde92/7e7e6dc3eceb02ab-a3/s400x600/7b53db3b6cb0a391c28c69468861ec70805f5aec.gif",
            "https://64.media.tumblr.com/06f2790f48516cee780817da28afb7f3/26be919e22fb6fcd-52/s540x810/ad419450ee94866247d66717305065273d79c11c.gif",
            "https://64.media.tumblr.com/c3a71d0061e4647ebcc082374708b700/35a57a49f126c5fe-53/s400x600/52dd4cd2f9fffce9e8320d5298cd995920d544d7.gif",
            "https://64.media.tumblr.com/3629e5aed89ff2a1aa94a51a9ac0396d/ba269b895e46fb77-2d/s400x600/766afd4caedc073d6001eb909116fe2c0fea4c4d.gif",
            "https://64.media.tumblr.com/bd6ea2f34657fe54fcd9c301af147f3e/35c4ee5e1bee21b0-ba/s400x600/7afe24c361153f19344dc45a7c4bdb36724279d0.gif",
            "https://64.media.tumblr.com/143de6013efe79c8827fa2a08d5a6ed1/68d13c07c1735b1e-f2/s540x810/f3180f3bc9fd9405c567594ddde716b403320fb9.gif",
            "https://64.media.tumblr.com/e98884d5a77fd0c585230441b97ba15f/603cdb5ab920c1df-ad/s400x600/7c2900a8441076d1bc0651d51361da4b04812aaf.gif",
            "https://64.media.tumblr.com/18df16ccae26f9adc3a6a9dedb05e97a/74bc82b9e06f35e0-0e/s400x600/1531b95fa5f28f04c50a246eb4b9021614187ec2.gif",
            "https://64.media.tumblr.com/d752fc4aae4b78cf40a03d493a2bf396/7732225bb8893b18-5f/s400x600/1c1c17145470b9bbf7e7aa57e26c76ca59509483.gif",
            "https://data.whicdn.com/images/289498109/original.gif",
            "https://64.media.tumblr.com/86545621ad6214b8aff2f5e1a6a4fcfc/186cb8bbcfab3654-60/s400x600/e700ef010b40ecd240cd486b069bd85adfefac96.gif",
            "https://64.media.tumblr.com/6755b1038a238e0e3493f88272c4f5ee/2089d1a9445d705c-38/s400x600/5aac1b865a3ffd271e427ceaa37ba897fdcc3c81.gif",
            "https://64.media.tumblr.com/5b6753dff1d79eb4695ac7e1fdee4521/3306e196c47c89f3-c8/s400x600/64f8a5acfa378951ad6f6a2d6031d330069186fc.gif",
            "https://64.media.tumblr.com/b4ad4f3a9ee5d520abb0f023ab98fcf0/043e143bf9aca2c2-99/s540x810/4449fd38ebd0b6d77daa47b37b76f99a28913685.gif",
            "https://64.media.tumblr.com/f8d1608c175164332e7135573855155d/tumblr_p7gvk50xIt1wi7204o1_540.gif",
            "https://64.media.tumblr.com/569bc66343344560422e7d3446b9b704/tumblr_pir6g7HSqA1wj9n4bo1_400.gif",
            "https://64.media.tumblr.com/54b47b0162ad83cfda6e2b158416dbc5/46daa3353e78681b-34/s540x810/5a706736355154b290cec474d6d5265a6e90d9e9.gif",
            "https://64.media.tumblr.com/1c61bec91ad3a8bc617ba65afea6e2d5/46daa3353e78681b-c2/s540x810/948d07e92aed7b5d03dd130d8f9002f918dfdae7.gif",
            "https://64.media.tumblr.com/058f2c58a8b5faee4b63b8ee5aa3b20c/a74ec8775c4e199d-c1/s400x600/b6a3f545f11bf6052ad4ef7d3995572ec48e606c.gif",
            "https://64.media.tumblr.com/828531bb96a302009c3bcfb1adfd9cc3/df9785efa4b7ac82-54/s400x600/91b19825d1d091a589d29db0d5c8dccd57859b85.gif",
            "https://64.media.tumblr.com/162a741e154557e2c3c5c5703a8a1689/tumblr_inline_o8xq6duwiN1rifr4k_540.gif",
            "https://data.whicdn.com/images/324201333/original.gif"]

        self.bot.sana_gif = ["https://tenor.com/view/sana-twice-kitty-dance-kpop-gif-17314571",
            "https://media.giphy.com/media/xUySTXXuWvIVDggisg/giphy.gif",
            "https://tenor.com/view/sana-sana-twice-twice-sana-minatozaki-sana-gif-18564320",
            "https://tenor.com/view/sana-twice-heart-minatozaki-jpop-gif-10758695",
            "https://tenor.com/view/twice-shyshyshy-sana-dance-cute-gif-9784878",
            "https://tenor.com/view/sanapinkhair-sana-twice-sana-gif-18677676",
            "https://tenor.com/view/samichae-sana-twice-serious-gif-15019560",
            "https://tenor.com/view/fancy-twice-sana-gif-14010342",
            "https://tenor.com/view/twice-minatozaki-sana-fix-hair-gif-12344636",
            "https://tenor.com/view/fancy-twice-you-sana-gif-14137521",
            "https://tenor.com/view/sana-minatozaki-sana-twice-jyp-jyp-entertainment-gif-18654791",
            "https://tenor.com/view/performance-stage-music-dance-dance-performance-gif-15855577",
            "https://tenor.com/view/twice-sana-fancy-dance-gif-14035182",
            "https://tenor.com/view/performance-stage-music-dance-dance-performance-gif-15855648",
            "https://tenor.com/view/sana-fancy-dance-cute-fancy-gif-15434915",
            "https://tenor.com/view/sana-minatozaki-sana-twice-fancy-jyp-gif-18654790",
            "https://tenor.com/view/fancy-twice-cutie-sana-sexy-gif-13983688",
            "https://tenor.com/view/sana-ohyo-ohyo-ohyo-sana-fancy-fancy-sana-twice-gif-13983779",
            "https://tenor.com/view/twice-sana-fancy-stare-gif-14017602",
            "https://tenor.com/view/sana-twice-sana-more-more-sana-cute-sana-clumsy-gif-18766260",
            "https://tenor.com/view/sana-twice-wondering-thinking-bored-gif-6184780",
            "https://tenor.com/view/welcome-twice-sana-minatozaki-sana-vocalist-gif-17907768",
            "https://tenor.com/view/sana-twice-heart-point-gif-18331546",
            "https://tenor.com/view/sana-cute-face-gif-10623438",
            "https://tenor.com/view/twice-cheerup-sana-shyshyshy-gif-6325860",
            "https://tenor.com/view/sana-twice-kpop-gif-5328449",
            "https://tenor.com/view/kpop-twice-sana-gif-5677495",
            "https://tenor.com/view/sana-sad-crying-twice-twice-sana-gif-16875037",
            "https://tenor.com/view/twice-feel-special-twice-feel-special-kpop-gif-19924880",
            "https://tenor.com/view/twice-kiss-sana-cute-flying-kiss-gif-14041423",
            "https://tenor.com/view/sana-sana-twice-minatozaki-sana-twice-sana-twice-gif-14011183",
            "https://tenor.com/view/twice-sana-cheese-kimbap-gimbap-bros-gif-11163723",
            "https://tenor.com/view/sana-momo-sana-twice-momo-twice-twice-gif-13983819",
            "https://tenor.com/view/sana-sana-twice-minatozaki-sana-gif-18815585",
            "https://tenor.com/view/sana-sana-twice-twice-sana-twice-minatozaki-sana-gif-13495040",
            "https://64.media.tumblr.com/c45f65595b9843ea92dde971eb32b00c/ab666d001db0126c-57/s540x810/ce7be132787345b2639177b16960e72ba3127126.gif",
            "https://64.media.tumblr.com/9677e14efb1733e32c5f662fd9d57ff3/tumblr_pyynpfUc7G1vp9gyko1_540.gif",
            "https://64.media.tumblr.com/40de841f0442df520520265fabe8fa16/4a119414513c0464-79/s540x810/2ae18f0131c07088b53e4ea528f8860f804f6738.gif",
            "https://64.media.tumblr.com/d4dd3b4391f7af7fa512a6d21e9f5388/da8528a756c146b5-88/s540x810/99e38a3529ba48c702b46c51518d5a0cda9e3744.gif",
            "https://64.media.tumblr.com/2f063543ee74fb543c3a8387c1771f41/tumblr_pb79uxjM4C1vp9gyko1_540.gif",
            "https://64.media.tumblr.com/c16874d4fd41225344a087939dad90e1/tumblr_pqu0p3Cydf1s2vcg0o1_540.gif",
            "https://64.media.tumblr.com/259be50125fceab70de6a7011c5dc167/e4fbc57b43f7f1f8-08/s540x810/576364e58af4d04f63c7e19ff33f3f8532879db9.gif",
            "https://64.media.tumblr.com/01dc22661fc58f007523e3953bdb0bb6/19228f63c0e446b2-ac/s500x750/a3f18386c896f64058edc82f7ccf05ee25d14981.gif"]

        #5
        self.bot.momo_gif = ["https://tenor.com/UZ2D.gif",
            "https://tenor.com/boSu5.gif",
            "https://tenor.com/brfIg.gif",
            "https://media.giphy.com/media/LOQdYUQeQ1EXUP9loM/giphy.gif",
            "https://media.giphy.com/media/emLsFpAymOfaDgQ7qm/giphy.gif"]

        #5
        self.bot.jeongyeon_gif = ["https://tenor.com/bgvYS.gif",
            "https://tenor.com/bm9Bh.gif",
            "https://media.giphy.com/media/QxYGmXN0vs2W6oHAO2/giphy.gif",
            "https://media.giphy.com/media/Pm3E3SsR3TSeT0eI6p/giphy.gif",
            "https://media.giphy.com/media/jOyCT02EvfnMc7trkh/giphy.gif"]
        
        #5
        self.bot.tzuyu_gif = ["https://media.giphy.com/media/sKdL5e5zah0gE/giphy.gif",
            "https://media.giphy.com/media/jmphxHznc7wBmsuaW1/giphy.gif",
            "https://tenor.com/5MSV.gif",
            "https://tenor.com/Fguv.gif",
            "https://tenor.com/bsSaJ.gif"]

        #9
        self.bot.nayeon_gif = ["https://tenor.com/9b5w.gif",
            "https://tenor.com/YChI.gif",
            "https://tenor.com/bs6Qy.gif",
            "https://media.giphy.com/media/gg3XU0ggfN7B0tlHnw/giphy.gif",
            "https://media.giphy.com/media/URvyQpZe0uoCT6jHo8/giphy.gif",
            "https://media.giphy.com/media/h7dxG65XwW00aBVkBc/giphy.gif",
            "https://tenor.com/view/mood-twice-nayeon-i-dont-know-gif-14052273",
            "https://tenor.com/view/pop-hair-twice-mouth-kpop-gif-16633600",
            "https://tenor.com/view/twice-nayeon-kpop-cute-gif-15007259"]

        #5
        self.bot.dahyun_gif = ["https://tenor.com/zEfV.gif",
            "https://tenor.com/ZKRA.gif",
            "https://tenor.com/brQ06.gif",
            "https://media.giphy.com/media/gLcbZ01uqIOZIsBWlC/giphy.gif",
            "https://tenor.com/bd1b8.gif"]

        #5
        self.bot.jihyo_gif = ["https://media.giphy.com/media/Ph6A5WjBAI3981PAsf/giphy.gif",
            "https://tenor.com/bnZ6r.gif",
            "https://tenor.com/bbKLS.gif",
            "https://tenor.com/brGhA.gif",
            "https://tenor.com/brT8L.gif"]

        #6
        self.bot.chaeyoung_gif = ["https://tenor.com/view/chaeyoung-twice-kpop-jyp-jypnation-gif-14436666",
            "https://media.giphy.com/media/xUySTt5f5AmRUBgdUI/giphy.gif",
            "https://media.giphy.com/media/lptOHczNAFD1G79Ofq/giphy.gif",
            "https://media.giphy.com/media/Qy2WthVCTLkeT1gZLS/giphy.gif",
            "https://tenor.com/XiHw.gif",
            "https://tenor.com/bn9Lf.gif"]

    @commands.command()
    async def twice(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Twice | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "mina":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Mina :heart:')
                    await ctx.send(random.choice(self.bot.mina_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mina :heart:')
                await ctx.send(random.choice(self.bot.mina_gif))
                await ctx.message.delete()
        elif arg == "sana":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Sana :heart:')
                    await ctx.send(random.choice(self.bot.sana_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sana :heart:')
                await ctx.send(random.choice(self.bot.sana_gif))
                await ctx.message.delete()
        elif arg == "momo":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Momo :heart:')
                    await ctx.send(random.choice(self.bot.momo_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Momo :heart:')
                await ctx.send(random.choice(self.bot.momo_gif))
                await ctx.message.delete()
        elif arg == "jeongyeon":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Jeongyeon :heart:')
                    await ctx.send(random.choice(self.bot.jeongyeon_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jeongyeon :heart:')
                await ctx.send(random.choice(self.bot.jeongyeon_gif))
                await ctx.message.delete()
        elif arg == "tzuyu":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Tzuyu :heart:')
                    await ctx.send(random.choice(self.bot.tzuyu_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Tzuyu :heart:')
                await ctx.send(random.choice(self.bot.tzuyu_gif))
                await ctx.message.delete()
        elif arg == "nayeon":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Nayeon :heart:')
                    await ctx.send(random.choice(self.bot.nayeon_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Nayeon :heart:')
                await ctx.send(random.choice(self.bot.nayeon_gif))
                await ctx.message.delete()
        elif arg == "dahyun" or arg == "dubu":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Dahyun :heart:')
                    await ctx.send(random.choice(self.bot.dahyun_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Dahyun :heart:')
                await ctx.send(random.choice(self.bot.dahyun_gif))
                await ctx.message.delete()
        elif arg == "jihyo":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Jihyo :heart:')
                    await ctx.send(random.choice(self.bot.jihyo_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jihyo :heart:')
                await ctx.send(random.choice(self.bot.jihyo_gif))
                await ctx.message.delete()
        elif arg == "chaeyoung":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Chaeyoung :heart:')
                    await ctx.send(random.choice(self.bot.chaeyoung_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chaeyoung :heart:')
                await ctx.send(random.choice(self.bot.chaeyoung_gif))
                await ctx.message.delete()


   
def setup(client):
    client.add_cog(gamerPings(client))