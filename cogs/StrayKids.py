import discord, random
from discord.ext import commands
from datetime import datetime

#//servers
luminary = 758468592957521972

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

class StrayPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
        self.bot.bangchan_gif = ["https://tenor.com/view/bang-chan-stray-kids-skz-wave-gif-15490742",
            "https://tenor.com/view/bang-chan-stray-kids-kpop-hanger-funny-gif-15229014",
            "https://tenor.com/view/stray-kids-dingo-bang-chan-hey-kpop-gif-14230381",
            "https://tenor.com/view/bang-chan-gif-18200044",
            "https://tenor.com/view/bang-chan-gif-18199694",
            "https://tenor.com/view/bang-chan-stray-kids-cb97-shaking-head-gif-10984556",
            "https://tenor.com/view/bang-chan-bang-cb97-gif-11237020",
            "https://tenor.com/view/bang-chan-bang-cb97-gif-11237019",
            "https://tenor.com/view/bangchan-stray-kids-stray-kids-bang-chan-skz-skz-chan-gif-19987791",
            "https://tenor.com/view/bang-chan-stray-kids-skz-kpop-cute-gif-16034273",
            "https://tenor.com/view/stray-kids-stray-kids-bang-chan-bang-chan-stray-kids-chan-chan-gif-20118369",
            "https://tenor.com/view/stray-kids-stray-kids-bang-chan-bang-chan-stray-kids-chan-chan-gif-20118507",
            "https://tenor.com/view/bangchan-chris-bang-stray-kids-skz-blueprint-gif-19048445",
            "https://tenor.com/view/bang-chan-gif-19701233",
            "https://tenor.com/view/bang-chan-chan-skz-stray-kids-gif-20114031",
            "https://tenor.com/view/skz-chan-bangchan-kiss-mwah-gif-19118140",
            "https://tenor.com/view/stray-kids-stray-kids-bang-chan-bang-chan-stray-kids-chan-chan-gif-19985645",
            "https://tenor.com/view/stray-kids-stray-kids-bang-chan-bang-chan-stray-kids-chan-chan-gif-19985641",
            "https://tenor.com/view/stray-kids-stray-kids-bang-chan-bang-chan-chan-get-cool-gif-19811722",
            "https://tenor.com/view/stray-kids-stray-kids-bang-chan-bang-chan-chan-awkward-silence-gif-19770578",
            "https://tenor.com/view/stray-kids-stray-kids-bang-chan-bang-chan-chan-awkward-silence-gif-19768876",
            "https://tenor.com/view/stray-kids-stray-kids-bang-chan-bang-chan-chan-awkward-silence-gif-19768877",
            "https://tenor.com/view/stray-kids-hellevator-bang-chan-chan-stray-kids-bang-chan-gif-19633511",
            "https://tenor.com/view/bang-chan-stray-kids-backdoor-straykids-gif-19640555",
            "https://tenor.com/view/stray-kids-bang-chan-kpop-skz-christopher-bang-gif-20284292",
            "https://tenor.com/view/stray-kids-stray-kids-bang-chan-bang-chan-chan-grow-up-gif-19724693",
            "https://tenor.com/view/stray-kids-stray-kids-bang-chan-bang-chan-chan-grow-up-gif-19724836",
            "https://tenor.com/view/stray-kids-stray-kids-bang-chan-bang-chan-chan-grow-up-gif-19724643",
            "https://tenor.com/view/stray-kids-stray-kids-bang-chan-bang-chan-chan-grow-up-gif-19724600",
            "https://tenor.com/view/stray-kids-bang-chan-stray-kids-bang-chan-chandler-stray-kids-chan-gif-19512178",
            "https://tenor.com/view/stray-kids-stray-kids-bang-chan-bang-chan-chan-stray-kids-chan-gif-19512187",
            "https://tenor.com/view/best-leader-christopher-bang-stray-kids-bang-chan-smile-gif-15654617",
            "https://tenor.com/view/bang-chan-skz-christopher-bang-stray-kids-cute-gif-15747908",
            "https://tenor.com/view/stray-kids-chris-bang-chan-crispy-bang-chan-bangchan-finger-heart-gif-14481431",
            "https://tenor.com/view/stray-kids-skz-bang-chan-christopher-bang-kpop-gif-17214481",
            "https://tenor.com/view/bottom-bang-chan-dance-kpop-stray-kids-gif-14035145",
            "https://tenor.com/view/bang-chan-stray-kids-chrisbang-bang-byung-chan-byung-chan-gif-10984538",
            "https://tenor.com/view/bang-chan-stray-kids-chris-bang-byung-chan-cb97-gif-10984541",
            "https://tenor.com/view/bang-chan-bang-cb97-gif-11237027",
            "https://tenor.com/view/bangchan-stray-kids-chris-bang-byung-chan-cb97-gif-10984549",
            "https://gfycat.com/waryuncommonelver-stray-kids-bang-chan-seuteurei-kijeu-skz-gimujin",
            "https://giphy.com/gifs/straykids-k-pop-stray-kids-bang-chan-hTavYkyL9ZI8XiyZnC",
            "https://64.media.tumblr.com/c8f0aa1076494945fc929a757e27a462/8e24266a8cc2cf21-55/s400x600/07ee236ddbe962992b240e3dcc0d1e320e99435e.gif",
            "https://64.media.tumblr.com/6fac355664f4ee517e742b4348918b60/509220339df7560c-ee/s400x600/66498dbfa605a90c7a072b21389ff86a82e85585.gif",
            "https://64.media.tumblr.com/e70a691d79a05f36779291900d82fa06/509220339df7560c-72/s400x600/0f9dd79160a620795cfb9af49296a41926b849d6.gif",
            "https://64.media.tumblr.com/75a2afde681ebb6681643344432e042d/509220339df7560c-50/s400x600/d9c7f51abd49efed12c4f257777d26943b1d14fb.gif",
            "https://64.media.tumblr.com/dca95c72eaf62fa7074dff3304ac57da/509220339df7560c-85/s400x600/bce87e31123db38ef47cc0495bea97131c2b4c00.gif"]

        self.bot.felix_gif = ["https://tenor.com/view/felix-lee-yongbok-dog-puppy-gif-16974825",
            "https://tenor.com/view/stray-kids-felix-lee-lee-felix-cute-gif-13005382",
            "https://tenor.com/view/cute-felix-gif-16008442",
            "https://tenor.com/view/felix-stray-kids-kpop-stare-cute-gif-17660812",
            "https://tenor.com/view/stray-kids-lee-felix-fly-kiss-gif-14222407",
            "https://cdn.discordapp.com/attachments/802983833204162670/802986872878923786/image0.gif",
            "https://cdn.discordapp.com/attachments/802983833204162670/802986873449742356/image1.gif",
            "https://cdn.discordapp.com/attachments/802983833204162670/802987069186113616/image0.gif",
            "https://cdn.discordapp.com/attachments/802983833204162670/802987069726785556/image1.gif",
            "https://tenor.com/view/felix-lee-cute-stray-kids-gif-18617656",
            "https://tenor.com/view/stray-kids-felix-lee-felix-lee-yongbok-lead-dancer-gif-17580819",
            "https://tenor.com/view/felix-stray-kids-smile-gif-10510975",
            "https://tenor.com/view/felix-felix-bite-hear-b_yonglix-yongbok-lee-yongbok-gif-19316192",
            "https://tenor.com/view/lee-felix-yongbok-stray-kids-felix-skz-felix-skz-hi-gif-18570889",
            "https://tenor.com/view/stray-kids-stray-kids-felix-felix-miroh-gif-19908540",
            "https://tenor.com/view/felix-felix-pretty-pretty-prettyfelix-aesthetic-felix-gif-20149238",
            "https://tenor.com/view/stray-kids-skz-felix-felix-skz-felix-stray-kids-skz-gif-20305046",
            "https://tenor.com/view/stray-kids-stray-kids-felix-felix-skz-code-gif-20118377",
            "https://gfycat.com/badhandybilby-dance-k-pop-live-mnet-mpd-raibeu-aidol-empidi-kpab",
            "https://gfycat.com/favoritescentedbooby-dance-practice-gods-menu-stray-kids-felix-du-du",
            "https://gfycat.com/completefixedbaldeagle-lee-yongbok-stray-kids-lee-felix-adorable-kpop",
            "https://tenor.com/view/stray-kids-pout-sigh-gif-12932111",
            "https://tenor.com/view/stray-kids-stray-kids-felix-felix-get-cool-gif-19812247",
            "https://tenor.com/view/stray-kids-stray-kids-felix-felix-get-cool-gif-19812175",
            "https://tenor.com/view/stray-kids-stray-kids-felix-felix-get-cool-gif-19812131",
            "https://tenor.com/view/stray-kids-felix-stray-kids-felix-blueprint-gif-19512201",
            "https://tenor.com/view/stray-kids-felix-stray-kids-felix-blueprint-gif-19512191",
            "https://tenor.com/view/stray-kids-stray-kids-felix-felix-victory-song-gif-19985703",
            "https://tenor.com/view/stray-kids-stray-kids-felix-felix-victory-song-gif-19985866",
            "https://tenor.com/view/felix-skz-stray-kids-lee-yongbok-gif-16974414",
            "https://tenor.com/view/stray-kids-felix-lee-felix-lee-yongbok-lead-dancer-gif-17807471",
            "https://tenor.com/view/stray-kids-stray-kids-felix-felix-grow-up-gif-19724815",
            "https://tenor.com/view/stray-kids-stray-kids-felix-felix-grow-up-gif-19724641",
            "https://tenor.com/view/stray-kids-stray-kids-felix-felix-chronosaurus-gif-20185279",
            "https://tenor.com/view/stray-kids-stray-kids-felix-felix-chronosaurus-gif-20185844",
            "https://tenor.com/view/stray-kids-stray-kids-felix-felix-my-pace-gif-19747531",
            "https://tenor.com/view/stray-kids-stray-kids-felix-felix-awkward-silence-gif-19768869",
            "https://giphy.com/gifs/straykids-k-pop-stray-kids-gods-menu-mECxedRUVIukjLHPhP",
            "https://i.pinimg.com/originals/50/56/5e/50565e0753df535384d408c22b2a06ca.gif",
            "https://data.whicdn.com/images/343320397/original.gif",
            "https://64.media.tumblr.com/53a01cbe2b1988b21949c4397f6caacd/c0342fb32cc40623-8c/s540x810/a5d81c4245457b5a49927992b4c2401e24526d20.gif",
            "https://i.pinimg.com/originals/72/e1/35/72e135351154f508b4885a62afbe1cab.gif",
            "https://i.pinimg.com/originals/66/25/cd/6625cdbf68b53893dc900badda4472a1.gif",
            "https://pa1.narvii.com/7661/e4cadf6c468042f868da2a696826fea8c03bed49r1-540-379_hq.gif",
            "https://64.media.tumblr.com/ecf128157e4a6d771dcdccef2d3ca7c0/81c4d0eb0825ff04-d4/s540x810/3c1e4af0e71333dd0b848aa6ec57174940c896c9.gif",
            "https://i.pinimg.com/originals/19/6c/ef/196cef0c292f7a75825194603cb72c0e.gif",
            "https://data.whicdn.com/images/320858012/original.gif",
            "https://i.pinimg.com/originals/7f/79/35/7f79359a28a6a7ded0850370148d99f4.gif",
            "https://pa1.narvii.com/6886/30a3c14c3787821821adae135c3d0f1dab9defe1r1-582-327_hq.gif",
            "https://64.media.tumblr.com/5a5a50907b28215b350328b0a05186df/tumblr_ozc02zXf061whqlfzo1_500.gif",
            "https://i.pinimg.com/originals/ec/14/8e/ec148e6592181ff6908954c39c1c5b85.gif",
            "https://i.pinimg.com/originals/5a/b6/6c/5ab66c4e8d4607b8a34a272bafdf80f7.gif",
            "http://pa1.narvii.com/6886/212001cede2039af977b0b1c2ecb633dd180e3b5r1-480-480_00.gif",
            "https://i.pinimg.com/originals/bb/8c/6d/bb8c6d21a7d38817662eb3f20bae351f.gif",
            "https://64.media.tumblr.com/a6783764e0bd92cf534868ab750449dd/00c14831ed564ab2-e2/s400x600/6534b5ba1b4f3f60e787dd70f56d16825ccf6061.gif",
            "https://i.pinimg.com/originals/70/43/9d/70439d4b8ec88ef1f748cd4e5f776baf.gif",
            "https://data.whicdn.com/images/321959313/original.gif",
            "https://64.media.tumblr.com/6748875b39ee534a8650db0f2eaeef92/a8ea39bcd1945fa9-48/s2048x3072_c0,0,100000,80752/e5f24e579b314bfbd86e5dbd2869b053aa69e693.gif",
            "https://data.whicdn.com/images/338042189/original.gif",
            "https://pa1.narvii.com/6818/cf23490347d718bb122ebe7e66fa3a68f2c46e5c_hq.gif",
            "https://data.whicdn.com/images/346211070/original.gif",
            "https://data.whicdn.com/images/345531425/original.gif",
            "https://thumbs.gfycat.com/DearestEasygoingAfricanharrierhawk-size_restricted.gif",
            "https://data.whicdn.com/images/348362470/original.gif",
            "https://i.pinimg.com/originals/c7/0a/c5/c70ac56225ef4dd2f7781e71b6f1befd.gif"]

        self.bot.shyunjin_gif = ["https://tenor.com/view/funny-jyp-cute-hyunjincute-hyunjin-gif-13417088",
            "https://tenor.com/view/hyunjin-hyunjin-skz-anyways-skz-stray-kids-gif-18096876",
            "https://tenor.com/view/hyunjin-hwang-gif-18553566",
            "https://tenor.com/view/straykids-hyunjin-rapper-hair-f-ix-head-shake-gif-17468856",
            "https://tenor.com/view/hwang-hyunjin-kpop-gif-14009678",
            "https://cdn.discordapp.com/attachments/802983894273359942/802987219883130880/image0.gif",
            "https://tenor.com/view/stray-kids-stray-kids-hyunjin-gif-18127666",
            "https://tenor.com/view/hyunjin-hwang-hyungin-stare-look-hot-gif-18901080",
            "https://tenor.com/view/hwang-hyunjin-hyunjin-love-kiss-cute-gif-19104982",
            "https://tenor.com/view/hyunjin-kpop-stray-kids-skz-gif-18126493",
            "https://tenor.com/view/hyunjin-stray-kids-double-knot-kpop-stray-kids-double-knot-gif-20140905",
            "https://tenor.com/view/hyunjin-hyunjin-skz-skz-code-hyunjin-laugh-laugh-gif-20300405",
            "https://tenor.com/view/stray-kids-stray-kids-hyunjin-hyunjin-skz-code-gif-20118380",
            "https://tenor.com/view/stray-kids-stray-kids-hyunjin-hyunjin-get-cool-gif-19812264",
            "https://tenor.com/view/stray-kids-stray-kids-hyunjin-hyunjin-get-cool-gif-19811138",
            "https://tenor.com/view/stray-kids-stray-kids-hyunjin-hyunjin-my-pace-gif-19747628",
            "https://tenor.com/view/stray-kids-stray-kids-hyunjin-hyunjin-my-pace-gif-19747564",
            "https://tenor.com/view/stray-kids-stray-kids-hyunjin-hyunjin-my-pace-gif-19747462",
            "https://tenor.com/view/stray-kids-stray-kids-hyunjin-hyunjin-blueprint-gif-19525245",
            "https://tenor.com/view/stray-kids-hyunjin-stray-kids-hyunjin-blueprint-gif-19512234",
            "https://gfycat.com/flatimmaterialfoxterrier-jyp-entertainment-stray-kids-bang-chan",
            "https://gfycat.com/acidicmeaslyalbertosaurus",
            "https://giphy.com/gifs/straykids-k-pop-stray-kids-gods-menu-StFBbLOY1NHThdLWRA",
            "https://giphy.com/gifs/straykids-k-pop-stray-kids-kEzzTrBtbR2J1uAPA7",
            "https://i.pinimg.com/originals/b4/45/85/b445856ec0321d443ba26174f86b4946.gif",
            "https://media1.tenor.com/images/6555ba2816aab984c17e0cfbe1a67c58/tenor.gif?itemid=18122357",
            "https://i.pinimg.com/originals/b8/81/85/b88185eee6d76b88d6a9cff94163d8b1.gif",
            "https://i.pinimg.com/originals/37/c4/95/37c495a24a789f0f8a926cd5aeb80f8b.gif",
            "https://p.favim.com/orig/2018/10/17/stray-kids-hyunjin-i-Favim.com-6470613.gif",
            "https://i.pinimg.com/originals/ba/44/fa/ba44fabb0883900b7f6faf14d60b64b9.gif",
            "https://image.kpopmap.com/2020/09/hyunjin-stray-kids-long-hair-article.gif",
            "https://thumbs.gfycat.com/EdibleVillainousGraysquirrel-size_restricted.gif",
            "http://pa1.narvii.com/7666/1576112d4f7fcb45e01759781485225be32561b9r1-268-350_00.gif",
            "https://78.media.tumblr.com/48087b09588862e2ca1005e8ee3b4bab/tumblr_pdvq6nOFgB1xe473mo1_500.gif",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQlSLOMW821iy_Fm4ra_YrMy_oJf22eW1UAA&usqp=CAU",
            "https://i.pinimg.com/originals/6a/8b/dd/6a8bdd2abdaf2815ee4d6b9069193e1f.gif",
            "https://64.media.tumblr.com/5407e16f25f6532d563830648aa5cbc9/6c72380129d691f5-75/s400x600/785b519f712ff5c95bbad487d8d5d4b701336aa1.gif",
            "https://64.media.tumblr.com/57616d728d08422efd2c3cf71f74d9cf/808a6b4b1e87db7c-5c/s500x750/9206caad81c08e926928a187339451c3798a5f57.gif",
            "https://s12.favim.com/gif_previews/6/635/6350/63509/6350964.gif",
            "https://data.whicdn.com/images/319976227/original.gif",
            "https://p.favim.com/orig/2018/08/24/hwang-hyunjin-gif-hyunjin-Favim.com-6235741.gif",
            "https://data.whicdn.com/images/319081662/original.gif",
            "https://data.whicdn.com/images/317784754/original.gif",
            "https://64.media.tumblr.com/ded5dad4af25b54bc1e7dcf99e312a77/6fe2f0fa4f045613-9d/s500x750/6cf9afa7426d61440037795d21bf8e9b208d78d5.gif",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSML47eqVgSaa96m9-hE6gLq7wCC4AOqoQ2hQ&usqp=CAU",
            "https://64.media.tumblr.com/4c1796c32146b4109a39e8664e517d6f/e8276cab24640499-34/s500x750/b756010531258049e6b5d47fdd37a79f2d9fca92.gif",
            "https://pa1.narvii.com/6700/de2f3fd7bd31d06f52b703f0b182cec7628fb46e_hq.gif",
            "https://i.pinimg.com/originals/f0/24/73/f024734fe2bb15f1777138966d337a97.gif",
            "http://images6.fanpop.com/image/photos/42900000/Hyunjin-stray-kids-F0-9F-8C-BA-42985895-540-235.gif",
            "https://p.favim.com/orig/2018/08/24/gif-hwang-hyunjin-stray-kids-Favim.com-6221246.gif",
            "https://data.whicdn.com/images/318077681/original.gif",
            "https://p.favim.com/orig/2018/11/06/i-181104-gif-Favim.com-6523878.gif",
            "https://64.media.tumblr.com/5d4f122e36f4b7ded3c49578e6b56ad7/56bfb7d495c9430a-ea/s500x750/d7417e82b3f011078df4f0e323d3336ac75ab009.gif",
            "https://static-storychat.pstatic.net/217026_13672994/86hna09d64eic2.gif",
            "https://i.pinimg.com/originals/a3/38/9b/a3389b2132c991083dbdc9862ccf2e31.gif",
            "https://i.pinimg.com/originals/41/61/98/4161980b83d1d7d6dc0ba87e36ea677a.gif",
            "https://media1.tenor.com/images/b999ea289d6301d54cb91af898ac0885/tenor.gif?itemid=13515177",
            "https://78.media.tumblr.com/5463e9d1d2efc26d05aba2a9090651b2/tumblr_pdbc5tm4xf1whz8b5o1_400.gif",
            "https://p.favim.com/orig/2018/11/21/gif-musicbank-hwang-hyunjin-Favim.com-6577113.gif",
            "https://data.whicdn.com/images/329834745/original.gif",
            "https://images6.fanpop.com/image/photos/43000000/Hyunjin-stray-kids-F0-9F-8C-BA-43049965-250-299.gif",
            "https://64.media.tumblr.com/c023f6a925ed80d7e948fbd57cd9bef9/a9a02b06f546a626-91/s400x600/296dfd15b15e338e1fcff7e00c0699c6d06e5001.gif",
            "https://data.whicdn.com/images/320557174/original.gif",
            "https://media1.tenor.com/images/56a0a409380f0481d3e0e621e01e50f3/tenor.gif?itemid=10765235",
            "https://66.media.tumblr.com/5e0e2b1d61adec993c64b2fbcd025796/b1fa64aa90977db2-ab/s500x750/b158824d01a49c77919c8061074858df947ece43.gif",
            "https://images6.fanpop.com/image/photos/43000000/Hyunjin-stray-kids-F0-9F-8C-BA-43013523-500-250.gif",
            "https://64.media.tumblr.com/349f8fb0b3c199f511b12e96b2659a86/2f9bf47341104a63-80/s250x400/6949993374be5dee80fa854f0c6298c40e099cef.gif",
            "https://64.media.tumblr.com/e3d766873bc55cef259a0695ab4087a2/59bec0fda5b77c2c-c1/s400x600/f58b9245e11e48e2a08acdca5eb1791d24f6e3c0.gif"]

        self.bot.leeknow_gif = ["https://tenor.com/view/lee-know-straykids-lee-minho-leeknow-straykids-leeminho-straykids-gif-14398192",
            "https://tenor.com/view/stray-kids-lee-know-minho-lee-lee-minho-gif-13005374",
            "https://tenor.com/view/lee-know-lee-minho-stray-kids-shocked-kpop-gif-14968607",
            "https://tenor.com/view/stray-kids-lee-know-lee-know-stray-kids-stray-kids-lee-know-minho-gif-18109448",
            "https://tenor.com/view/hanniefelix-stray-kids-lee-know-minho-gif-18122290",
            "https://tenor.com/view/lee-know-lino-minho-lee-minho-stray-kids-gif-18658916",
            "https://tenor.com/view/lee-know-minho-straykids-fan-gif-17295403",
            "https://tenor.com/view/minho-gif-18871629",
            "https://tenor.com/view/minho-stray-kids-kpop-gif-14976277",
            "https://tenor.com/view/minho-gif-18199692",
            "https://tenor.com/view/lee-know-lee-minho-minho-stray-kids-stray-kids-minho-gif-18175614",
            "https://tenor.com/view/stray-kids-stray-kids-lee-know-lee-know-stray-kids-minho-minho-gif-20118376",
            "https://tenor.com/view/stray-kids-stray-kids-lee-know-lee-know-minho-get-cool-gif-19812206",
            "https://tenor.com/view/stray-kids-stray-kids-lee-know-lee-know-minho-get-cool-gif-19811249",
            "https://tenor.com/view/stray-kids-stray-kids-lee-know-lee-know-minho-get-cool-gif-19812245",
            "https://tenor.com/view/stray-kids-stray-kids-lee-know-stray-kids-minho-lee-know-minho-gif-19525226",
            "https://tenor.com/view/stray-kids-stary-kids-minho-stray-kids-lee-know-lee-know-minho-gif-19525215",
            "https://tenor.com/view/stray-kids-minho-stray-kids-minho-stray-kids-lee-know-lee-know-gif-19512248",
            "https://tenor.com/view/stray-kids-minho-stray-kids-minho-stray-kids-lee-know-lee-know-gif-19512255",
            "https://tenor.com/view/stray-kids-minho-stray-kids-minho-stray-kids-lee-know-lee-know-gif-19512248",
            "https://tenor.com/view/leeknow-lee-minho-lino-straykids-skz-gif-19016266",
            "https://tenor.com/view/stray-kids-stray-kids-lee-know-lee-minho-gif-15263545",
            "https://tenor.com/view/stray-kids-lee-know-lee-minho-double-knot-dance-gif-15263515",
            "https://gfycat.com/celebratedgraciousflatcoatretriever-hwanghyunjin-seochangbin-stray-kids",
            "https://tenor.com/view/lee-know-lee-minho-skz-stray-kids-lee-kno-gif-20017429",
            "https://tenor.com/view/lee-know-stray-kids-lee-know-smile-gif-19453330",
            "https://tenor.com/view/lee-know-stray-kids-pose-gif-14375828",
            "https://tenor.com/view/lee-know-straykids-lee-minho-leeknow-straykids-leeminho-straykids-gif-14398192",
            "https://tenor.com/view/stray-kids-stray-kids-lee-know-stray-kids-minho-minho-lee-know-gif-19534907",
            "https://tenor.com/view/lee-know-stray-kids-pose-gif-14375826",
            "https://tenor.com/view/stray-kids-skiz-skz-minho-lee-minho-gif-12100439",
            "https://tenor.com/view/stray-kids-lee-know-lee-minho-main-dancer-vocalist-gif-17356838",
            "https://tenor.com/view/stray-kids-leeknow-sexy-smile-gif-15998976",
            "https://tenor.com/view/stray-kids-lee-know-lee-minho-stray-kids-lee-min-ho-peace-gif-14375804",
            "https://tenor.com/view/lee-know-lee-minho-stray-kids-stray-kids-lee-know-jyp-entertainment-gif-17279807",
            "https://64.media.tumblr.com/0e7c6c6405ef6b37c3896b287dd16e41/tumblr_inline_pqx8v0JFaw1wc9fqa_500.gif",
            "https://data.whicdn.com/images/329014773/original.gif",
            "https://i.makeagif.com/media/4-03-2019/vdp7ib.gif",
            "https://66.media.tumblr.com/6bb7cb8785011edbad2b1c8dfa0a6ddf/tumblr_pwc27x1Mme1wi1gnho1_540.gif",
            "https://s11.favim.com/orig/7/766/7660/76609/stray-kids-lee-know-minho-Favim.com-7660904.gif",
            "https://64.media.tumblr.com/c14cc8f8fff0006658da3adf5cf631df/f7dba0716159096d-02/s540x810/f09f3221335675430ec309e5ae322799a8af1480.gif",
            "https://p.favim.com/orig/2018/09/05/k-pop-lee-know-jeongin-Favim.com-6247492.gif",
            "https://64.media.tumblr.com/6d661c69a93cbf9cfbb0a8a88d667cee/d92a3259af60a1ed-75/s640x960/478c78712986ce1292e95ee7010cbf453ccfb61a.gif",
            "https://images6.fanpop.com/image/photos/42800000/Tmt-stray-kids-F0-9F-8C-BA-42888538-540-220.gif",
            "https://64.media.tumblr.com/51a2aaf41e12a81f09735560746d676b/bfe05c63ef166057-93/s500x750/5708fb4179b026170db3b29d6575675b128e3523.gif",
            "https://64.media.tumblr.com/41827e637b086ce363807e6b9785672f/bfe05c63ef166057-25/s500x750/effa73c7eb820645fb4a1b8436901f0ed212c84d.gif",
            "https://64.media.tumblr.com/8f8238ca696f2c70e75a5ca1be01d3b1/5273795cc85cc6e1-3a/s540x810/51c910a6b83c2210e709a52fffcc1bc46db0cc02.gif",
            "https://66.media.tumblr.com/ccbb40944bacd252fdd4dfd4b0468fec/tumblr_pwyhat4xsI1yp01sno2_500.gif",
            "https://data.whicdn.com/images/340871907/original.gif",
            "https://i.pinimg.com/originals/6b/17/92/6b1792f42bdce0ed08accb30cdbb0498.gif",
            "https://i.pinimg.com/originals/06/85/e0/0685e00a49fda5f25fbe515a7be491aa.gif",
            "https://i.pinimg.com/originals/73/bf/f8/73bff8713295c9afc7f32c3c04f1538e.gif",
            "https://media1.tenor.com/images/c8981f80e22a6739ed3deda0146c0e63/tenor.gif?itemid=17243966",
            "https://pa1.narvii.com/6856/eba61a2d47b8b3456c0d65cb610b4a7fabaf1b7b_hq.gif",
            "https://thumbs.gfycat.com/PopularTenseFrenchbulldog-size_restricted.gif",
            "https://64.media.tumblr.com/7c3b4e45fe3d2f53a09afcfc258c5a67/ce1b371d8a49cf3f-78/s500x750/e6edb14504b1239e00cfe88837d83cbb6029b8ea.gif",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6_moO2H3gXnGSldfesRy2SzfJNaB7NnmQIg&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXTm6inughJqdbh_dj3Wi6JlbYQeWzutDmFw&usqp=CAU",
            "https://64.media.tumblr.com/3128e261412eaff3f4fea4c5dbe7cd91/ebc0f040de698391-67/s540x810/94dc20dfeea3f1667c720a7e71fac599c4fd97a3.gif",
            "https://64.media.tumblr.com/eee91b6c43e8b97c9e4e2ca35af049e2/7116970746616103-08/s400x600/14a13dd99e05787e8675a238017903d6212ac76a.gif",
            "https://i.pinimg.com/originals/8b/f3/13/8bf31328d78a77d310ba2f514a98d2f8.gif",
            "https://pa1.narvii.com/6909/37c7caa2511d57a23551bdd31ece83c4b220b331r1-540-200_hq.gif",
            "https://64.media.tumblr.com/c8a7fa64d13bddb3fc0b1a99b295cb74/0b3bb89273f58b4a-c8/s500x750/b9a86a2413c3a5eb0494eab76e4eb69bc3585849.gif",
            "https://64.media.tumblr.com/f9a08dbe9ca828dd36bea35ceb0c8d88/e783b56e2d6d3a65-25/s500x750/53cd2fc0cba629e1c24260f49f9544006b0b3ec0.gif",
            "https://64.media.tumblr.com/7db99b353250afa99f6ae0935f99a3c0/6a03370b70301187-22/s400x600/fe8d473872cb17844ad2cfa19e158deb9fbaee35.gif",
            "https://64.media.tumblr.com/ebef8f34053d85bddd589dfd389dbff8/tumblr_paj85xr7uy1wdfx9jo1_500.gif",
            "https://pa1.narvii.com/6992/e6f9afc6336c622cfa9e1e66b63bd980ed84e47cr1-540-270_hq.gif",
            "https://images6.fanpop.com/image/photos/42800000/Lee-Know-stray-kids-F0-9F-8C-BA-42880355-500-279.gif",
            "https://i.pinimg.com/originals/e8/74/eb/e874eb21cb5776421d5266168a077743.gif",
            "https://i.pinimg.com/originals/a7/da/58/a7da583703a138e0a7fdc51793b786fc.gif",
            "https://cdn140.picsart.com/313779271198201.gif?to=min&r=640",
            "https://i.pinimg.com/originals/96/ff/ed/96ffed8401cb31f67499115cc54001b7.gif",
            "https://64.media.tumblr.com/8c23d1a15d19da369a087ae69711b0c3/97f837717df12850-32/s500x750/f7196d8f8bd1a8b41d010298e5c527fac402b2d4.gif",
            "https://64.media.tumblr.com/1b05093baa10b4e22379cea5b43348bd/tumblr_pww6caeWPI1y9ycogo3_400.gif",
            "https://64.media.tumblr.com/bffccf2087aa1735a8d6840b12a5b279/tumblr_pww6caeWPI1y9ycogo2_400.gif",
            "https://i.pinimg.com/originals/b2/39/ed/b239ed39f1e672b4663aa7de56e6c170.gif",
            "https://pa1.narvii.com/7593/49c5cd4952028a7a3bde32f5005c9fde9ee8f25er1-540-250_hq.gif",
            "https://i.pinimg.com/originals/40/f2/03/40f2031e420a2717d7fde5b372102a32.gif",
            "https://64.media.tumblr.com/35412a701508f52f533917dffec82f15/31c27b96c1c243c8-f2/s540x810/0f087d0e6b78754edc77869a1d0bfac5037247b2.gif",
            "https://64.media.tumblr.com/fd447627b4ee9b1c60af346b65b3ec54/cf0434f56c84b3ba-4d/s400x600/bfcc632899b26e3fd0dc823f82a1e682b4434dba.gif",
            "https://64.media.tumblr.com/a2dfbb6e4c77b81611cbb0fadef796c6/619fd8b202a71e64-71/s500x750/a8f0ef5f83050db63d7876e3f45ab5cda13340d8.gif",
            "https://64.media.tumblr.com/a1f878d08585a539b1fbfc261fcc9a0b/5273795cc85cc6e1-f8/s540x810/a8c5ec7ab844c2198a0ec9cbe16bccb29955059f.gif",
            "https://64.media.tumblr.com/280ad4a20820f99e072f30142681597e/7b2328f702ee99ad-50/s400x600/43a3877319962008c3d51824d5a68f82a344ac50.gif",
            "https://64.media.tumblr.com/71871b2ae6aa691b06e4454babe9b7e2/tumblr_inline_pcec2nMGfU1w1d8bm_500.gif",
            "https://64.media.tumblr.com/8f8238ca696f2c70e75a5ca1be01d3b1/5273795cc85cc6e1-3a/s540x810/51c910a6b83c2210e709a52fffcc1bc46db0cc02.gif",
            "https://i.pinimg.com/originals/0c/82/8b/0c828b4608ebd4fbedbf547679f9bd1d.gif",
            "https://i.pinimg.com/originals/cb/96/67/cb96677b0622e4a7b05c39f0ddf0ea2f.gif",
            "https://64.media.tumblr.com/58f1ca2637c3b617db39baf60822087f/tumblr_ptcbpxVPpZ1x1z9lzo2_540.gif",
            "https://i.pinimg.com/originals/68/b4/75/68b4759ce0f23b603120a73834af434e.gif",
            "https://64.media.tumblr.com/6e8ad31d441d8e28e8b68fd051ff7400/9541757193045d2c-e6/s540x810/4dbc1817fae5518e32dae4b8fa5ee6010f65528d.gif"]

        self.bot.changbin_gif = ["https://tenor.com/view/seo-changbin-changbin-stray-kids-cute-kpop-gif-16229714",
            "https://tenor.com/view/stray-kids-skx-changbin-seo-changbin-lip-bite-gif-16669575",
            "https://tenor.com/view/stray-kids-skz-changbin-seo-changbin-handsome-gif-16669535",
            "https://tenor.com/view/stray-kids-changbin-seo-kpop-smile-handsome-gif-16275076",
            "https://tenor.com/view/stray-kids-skz-changbin-seo-changbin-gif-16669559",
            "https://tenor.com/view/changbin-wink-gif-18980336",
            "https://tenor.com/view/stray-kids-stray-kids-changbin-changbin-gif-19534821",
            "https://tenor.com/view/seo-changbin-changbin-stray-kids-skz-singing-gif-16669494",
            "https://tenor.com/view/stray-kids-stray-kids-changbin-changbin-skz-code-gif-20118498",
            "https://tenor.com/view/seo-changbin-gif-14380241",
            "https://tenor.com/view/seo-changbin-stray-kids-cute-gif-16276145",
            "https://tenor.com/view/stray-kids-skz-kpop-ccg-ccg1-gif-18642520",
            "https://tenor.com/view/changbin-stray-kids-skz-seo-changbin-cute-gif-16669474",
            "https://tenor.com/view/changbin-skz-skz-meme-stray-kids-kpop-gif-18503523",
            "https://tenor.com/view/stray-kids-changbin-seo-changbin-skz-spear-b-gif-16669212",
            "https://tenor.com/view/stray-kids-stray-kids-changbin-changbin-victory-song-gif-19986042",
            "https://tenor.com/view/stray-kids-stray-kids-changbin-changbin-victory-song-gif-19985801",
            "https://tenor.com/view/cute-changbin-stray-kids-rock-music-video-gif-12052823",
            "https://tenor.com/view/stray-kids-stray-kids-changbin-changbin-get-cool-gif-19812127",
            "https://tenor.com/view/stray-kids-changbin-stray-kids-changbin-blueprint-gif-19512276",
            "https://tenor.com/view/changbin-stray-kids-drink-gif-16243463",
            "https://tenor.com/view/seo-changbin-happy-stray-kids-kpop-gif-14682153",
            "https://tenor.com/view/seo-changbin-changbin-stray-kids-skz-singing-gif-16669497",
            "https://tenor.com/view/stray-kids-changbin-seo-changbin-main-rapper-vocalist-gif-17214557",
            "https://tenor.com/view/stray-kids-skz-seo-changbin-gif-19979913",
            "https://tenor.com/view/seo-changbin-changbin-stray-kids-cute-kpop-gif-16229969",
            "https://tenor.com/view/changbin-seo-gif-19653935",
            "https://tenor.com/view/seo-changbin-changbin-stray-kids-cute-kpop-gif-16229713",
            "https://tenor.com/view/stray-kids-changbin-stray-kids-cute-stray-kids-changbin-cute-stray-kids-funny-skz-gif-19590943",
            "https://tenor.com/view/seo-changbin-changbin-stray-kids-cute-kpop-gif-16463943",
            "https://tenor.com/view/stray-kids-changbin-seo-changbin-fairy-halloween-gif-12778793",
            "https://tenor.com/view/seo-changbin-changbin-stray-kids-cute-kpop-gif-16229762",
            "https://tenor.com/view/stray-kids-changbin-seo-changbin-skz-spear-b-gif-16669227",
            "https://tenor.com/view/seo-changbin-changbin-stray-kids-cute-kpop-gif-16463918",
            "https://tenor.com/view/seo-changbin-changbin-stray-kids-cute-kpop-gif-16463907",
            "https://tenor.com/view/stray-kids-stray-kids-x-clio-stray-kids-changbin-changbin-gif-20310970"]

        self.bot.han_gif = ["https://tenor.com/view/skz-stray-kidz-stray-kids-han-jisung-kpop-gif-16958093",
            "https://tenor.com/view/han-jisung-han-gif-17974604",
            "https://tenor.com/view/han-flip-hair-gif-13165511",
            "https://tenor.com/view/han-jisung-stray-kids-gif-14185103",
            "https://tenor.com/view/han-jisung-happy-dance-shake-it-stray-kids-gif-15409399",
            "https://tenor.com/view/stray-kids-han-jisung-heart-gif-13072732",
            "https://tenor.com/view/rude-hot-boy-jisung-sexy-gif-14072971",
            "https://tenor.com/view/han-gif-13343941",
            "https://tenor.com/view/stray-kids-jisung-sing-gif-14697863",
            "https://tenor.com/view/stray-kids-stray-kids-han-han-stray-kids-jisung-jisung-gif-20118370",
            "https://tenor.com/view/stray-kids-stray-kids-han-han-stray-kids-jisung-jisung-gif-20118501",
            "https://tenor.com/view/han-jisung-han-jisung-hjs-stray-kids-han-gif-18807991",
            "https://tenor.com/view/stray-kids-stray-kids-han-han-jisung-get-cool-gif-19812044",
            "https://tenor.com/view/stray-kids-stray-kids-han-han-jisung-stray-kids-jisung-gif-19512211",
            "https://tenor.com/view/stray-kids-han-stray-kids-han-jisung-stray-kids-jisung-gif-19512219",
            "https://gfycat.com/crispcommonindianpalmsquirrel-stray-kids-bang-chan-seuteurei-kijeu-skz-gimujin",
            "https://64.media.tumblr.com/98c5b13375fb7cfaeb8c9d12fa87d4d7/tumblr_pkwqnpxqkd1xq20zeo1_400.gif",
            "https://i.pinimg.com/originals/6b/06/bc/6b06bcbe1aaf22231ab7948d63c94923.gif",
            "https://i.pinimg.com/originals/19/20/75/192075cfa1a408d85e4fbdcc09c179df.gif",
            "https://64.media.tumblr.com/7b3248116a857053604cde879ec79011/tumblr_inline_ppfiv8EgmY1w6oz1r_400.gif",
            "https://data.whicdn.com/images/346885078/original.gif",
            "https://thumbs.gfycat.com/SkinnyInsistentDore-max-1mb.gif",
            "https://data.whicdn.com/images/329460843/original.gif",
            "https://s11.favim.com/orig/7/712/7120/71206/han-jisung-stray-kids-gif-Favim.com-7120630.gif",
            "https://data.whicdn.com/images/337657552/original.gif",
            "https://64.media.tumblr.com/85b03c9e9dcb2539863e13957da396ce/125daa0f990bc9c7-8d/s500x750/4cdd24eacd08c8689153c3df63e9a2ea34f9b214.gif",
            "https://pa1.narvii.com/7122/5d9890d020e8099d46bf7e7680f5104c99ce1525r1-540-220_hq.gif",
            "https://i.pinimg.com/originals/36/8a/2b/368a2bedba6184d052219ec73f776e32.gif",
            "https://data.whicdn.com/images/346495260/original.gif",
            "https://data.whicdn.com/images/343981771/original.gif",
            "https://i.pinimg.com/originals/a5/d6/4f/a5d64f811e4cde7e023b988cf41b0f6d.gif",
            "https://p.favim.com/orig/2019/01/08/stray-kids-slu-gif-Favim.com-6752698.gif",
            "https://p.favim.com/orig/2018/12/09/ig-jone-i-Favim.com-6642193.gif",
            "https://cdn130.picsart.com/299125546139201.gif",
            "https://i.pinimg.com/originals/e2/63/37/e26337d814ded2056eef377e91d77563.gif",
            "https://data.whicdn.com/images/338867782/original.gif",
            "https://static-storychat.pstatic.net/2113523_30842777/eaek4hn65knhg0.gif",
            "https://i.pinimg.com/originals/03/c7/56/03c75687867ac98511811fc1821a44b9.gif",
            "https://i.pinimg.com/originals/59/07/f7/5907f7469f8c9e4971f374de5186c4a7.gif",
            "https://i.pinimg.com/originals/63/23/8e/63238e677874e1ef46a088e9975850e4.gif",
            "https://v-phinf.pstatic.net//20201215_168/1608013319666jbpIQ_GIF/image.gif?type=w1000",
            "https://v-phinf.pstatic.net/20201122_61/1606057044392j1aY2_GIF/tenor_%282%29.gif?type=w1000",
            "https://i.pinimg.com/originals/aa/3d/0c/aa3d0c5870caea93b41d2c561e3615fd.gif",
            "https://64.media.tumblr.com/48eafd019aed968274a2c409d91e07e6/50e79e7e855cde99-4c/s540x810/c13ec9c9dbc5431bce270fd3b759af45c7279b37.gif",
            "https://64.media.tumblr.com/8faca9ce1f1e24bfa299c6f9f611f355/cf26e40fe572b3ba-c0/s540x810/3ebd52ae840c7d050ce555ad38a022c06a28a29e.gif",
            "https://cdn140.picsart.com/302990742327201.gif",
            "https://64.media.tumblr.com/aa19dc5ece81e1a6a7ee5939571e22e4/3aa88773cc2ca21e-ea/s540x810/234d8e8e0d4b127322ccdee740bfe342398f9f0c.gif",
            "https://thumbs.gfycat.com/RichHelpfulHydra-size_restricted.gif",
            "https://data.whicdn.com/images/345677281/original.gif",
            "https://64.media.tumblr.com/29610ea59a69399c371553e244d4bed3/d9549d139f52cc78-97/s540x810/bfa985ed3761e855558211a9c07499b448bc9a26.gif",
            "https://64.media.tumblr.com/903e848229f5e0be7b41ad3d5fc96e23/85bd919e4a536e8c-e0/s540x810/793007fd338d87fa832460bbfa5b782a204fb29c.gif",
            "https://64.media.tumblr.com/9cd823eba706e95e1e6ee89cd3eac4d6/85bd919e4a536e8c-2f/s500x750/80bb526646bd2a5f22edb08558e6bdee5ce29fff.gif",
            "https://images6.fanpop.com/image/photos/41300000/Jisung-stray-kids-F0-9F-8C-BA-41322116-540-240.gif",
            "https://64.media.tumblr.com/b10563a4f84df9a51bf986bb1d37c502/318d2a1a47ec2405-2e/s500x750/67462cb206b927d6d73c02b67cdd39174271f3ae.gif",
            "https://64.media.tumblr.com/7bb0c3048562bb5104c2f774e0bad82f/c0f48a807ad51cf7-01/s500x750/687d76a02b53899eae1cf4912a928d8dd723091d.gif",
            "https://64.media.tumblr.com/1415e77fdcf30d40829d2c1f87a07164/7a8bbccdfda4551a-ea/s500x750/0706172134c4cdb16a96949e98e279bb5d0824d2.gif"]

        self.bot.jeongin_gif = ["https://tenor.com/view/clapping-stray-kids-in-yang-jeongin-vocalist-gif-17816584",
            "https://tenor.com/view/in-yang-jeongin-shocked-stray-kids-kpop-gif-14357751",
            "https://tenor.com/view/stray-kids-cute-smile-kpop-gif-12423054",
            "https://tenor.com/view/straykids-skz-wave-jeongin-gif-18444736",
            "https://tenor.com/view/stray-kids-in-yang-jeongin-vocalist-maknae-gif-17946216",
            "https://cdn.discordapp.com/attachments/802983955733282816/802987402914299914/image0.gif",
            "https://tenor.com/view/stray-kids-stray-kids-in-gif-18127668",
            "https://tenor.com/view/in-stray-kids-cute-gif-15224075",
            "https://tenor.com/view/stray-kids-in-stray-kids-in-stray-kids-jeongin-jeongin-gif-19534868",
            "https://tenor.com/view/stray-kids-in-jeongin-yang-gif-20050340",
            "https://tenor.com/view/stray-kids-stray-kinds-in-in-stray-kids-jeongin-jeongin-gif-20118365",
            "https://tenor.com/view/stray-kids-stray-kids-in-stray-kids-jeongin-in-jeongin-gif-19525232",
            "https://tenor.com/view/stray-kids-stray-kids-in-in-jeongin-miroh-gif-19908537",
            "https://gfycat.com/emotionalboilinghapuku-absolutely-definitely-hilarious-mixtape",
            "https://tenor.com/view/stray-kids-stray-kids-in-in-jeongin-miroh-gif-19908799",
            "https://tenor.com/view/stray-kids-stray-kids-in-in-jeongin-miroh-gif-19908528",
            "https://tenor.com/view/stray-kids-stray-kids-in-in-stray-kids-jeongin-jeongin-gif-19985991",
            "https://tenor.com/view/stray-kids-stray-kids-in-in-stray-kids-jeongin-jeongin-gif-19985868",
            "https://tenor.com/view/stray-kids-stray-kids-in-in-stray-kids-jeongin-jeongin-gif-19985862",
            "https://tenor.com/view/stray-kids-stray-kids-in-in-stray-kids-jeongin-jeongin-gif-19985860",
            "https://tenor.com/view/stray-kids-in-stray-kids-in-stray-kids-jeongin-jeongin-gif-19505918",
            "https://tenor.com/view/stray-kids-skz-kpop-smile-clap-gif-16360530",
            "https://tenor.com/view/stray-kids-stray-kids-in-in-jeongin-get-cool-gif-19811243",
            "https://tenor.com/view/stray-kids-stray-kids-in-in-jeongin-get-cool-gif-19812093",
            "https://tenor.com/view/jeongin-yang-jeongin-stray-kids-skz-blueprint-gif-19048446",
            "https://tenor.com/view/jeongin-yang-jeongin-stray-kids-skz-blueprint-gif-19048439",
            "https://tenor.com/view/jeongin-yang-jeongin-stray-kids-skz-blueprint-gif-19048453",
            "https://tenor.com/view/stray-kids-jeongin-cute-gif-14222439",
            "https://gfycat.com/bestyoungfrigatebird",
            "https://gfycat.com/breakableweirdconey",
            "https://giphy.com/gifs/straykids-k-pop-in-stray-kids-LqgZ0SinJkVrSc6Xe9",
            "https://78.media.tumblr.com/76a7fb1d9f84fc2d01227c09e201cd50/tumblr_p3chaizV9m1wdla4io3_400.gif",
            "https://data.whicdn.com/images/316322646/original.gif",
            "https://p.favim.com/orig/2018/12/09/gif-in-yang-jeongin-Favim.com-6674647.gif",
            "https://p.favim.com/orig/2018/11/16/yang-jeongin-slu-brown-hair-Favim.com-6565444.gif",
            "https://64.media.tumblr.com/36267b7dcef7a04e89d1fcc5e7db28ad/4a9635106c2e2870-2f/s250x400/c3a53b877bede603f4d67e2ef0a417b198fc88d3.gif",
            "https://i.pinimg.com/originals/ba/4d/35/ba4d354de90d05362a1881b35e9f9dbf.gif",
            "https://64.media.tumblr.com/698e3f0a833ae3c3d6b772acaa09ff6c/6d408ae0782d0b04-01/s500x750/8d43a8b59c7152ae453ec07a7452f6262400761e.gif",
            "https://data.whicdn.com/images/338242807/original.gif",
            "https://v-phinf.pstatic.net/20201124_161/1606160900187HA8Tc_GIF/tenor.gif?type=w1000",
            "https://data.whicdn.com/images/309133463/original.gif",
            "https://64.media.tumblr.com/7f078faa3a7f61a004263c1fa8c6ddfd/e38e0fdec46af04c-13/s500x750/0fe714b6b583ec34b22ca4a919ca9cd6d8c1be8a.gif",
            "https://64.media.tumblr.com/c9f0126015400905bc7d0086aeed53e4/e98ba0aad154cbd2-2c/s500x750/7dcc49985f52797ad27bc4358d39749c9f211af7.gif",
            "http://pa1.narvii.com/7593/622b959e575db7a85a447b4498b8f4d5a7b30046r1-540-243_00.gif",
            "https://static.wixstatic.com/media/0bb356_4b93139601194dce97780ecde4239e1c~mv2.gif",
            "https://data.whicdn.com/images/339097885/original.gif",
            "https://tomfooleryhome.files.wordpress.com/2018/11/tumblr_phr55c9enp1xz4hgoo4_500.gif",
            "https://data.whicdn.com/images/308243207/original.gif",
            "https://i.pinimg.com/originals/78/fd/f7/78fdf725597fcdebca913bfc8efcf010.gif",
            "https://images6.fanpop.com/image/photos/43200000/Jeongin-LOTTE-DUTY-FREE-stray-kids-F0-9F-8C-BA-43203338-540-240.gif",
            "https://images6.fanpop.com/image/photos/43200000/Jeongin-LOTTE-DUTY-FREE-stray-kids-F0-9F-8C-BA-43203337-500-222.gif",
            "http://images6.fanpop.com/image/photos/43200000/Jeongin-LOTTE-DUTY-FREE-stray-kids-F0-9F-8C-BA-43203339-540-240.gif",
            "https://64.media.tumblr.com/ae2987ba635892f3bad1aa02cb280f6b/e34df49424b195f0-43/s400x600/d8aacbc13b72b5d003fd257280aad0bad3d3859a.gif",
            "https://pa1.narvii.com/6810/037a56d0d55295af47163899835ecbca89dc8db0_hq.gif",
            "https://64.media.tumblr.com/d8d7736573dcbe2ecd2df37e0c9aad7b/f36da7421e544344-52/s400x600/d9298b8b5abb635b6491590e138c570b01213349.gif",
            "https://66.media.tumblr.com/28bcddf25046cda93a4ad4219819783b/tumblr_piw8snTXgy1y0bjnvo1_400.gif",
            "https://i.pinimg.com/originals/7c/4a/29/7c4a29bd4db20ff1810403565a50f2ee.gif",
            "https://media1.tenor.com/images/639876f9e1486ead6e130633d77fe970/tenor.gif?itemid=10728021",
            "https://data.whicdn.com/images/328797955/original.gif",
            "https://64.media.tumblr.com/ba57f4ac5a2e2b204d374b4a45df773c/e03d36691ae65ae6-01/s1280x1920/8f3f49410eb0bac10eec416ec97059cbd8641b87.gif",
            "https://i.pinimg.com/originals/5f/20/58/5f205814364b18da342f0404113643a0.gif"]

        self.bot.seungmin_gif = ["https://tenor.com/view/stray-kids-kim-seungmin-seungmin-cute-kpop-gif-16435548",
            "https://tenor.com/view/kim-seungmin-stray-kids-seungmin-thumbs-up-approve-gif-16363315",
            "https://tenor.com/view/seung-min-kim-straykids-chomp-heart-smile-gif-13471299",
            "https://tenor.com/view/stray-kids-seungmin-kim-seungmin-seungmin-stray-kids-laugh-gif-14375802",
            "https://tenor.com/view/kim-seungmin-stray-kids-seungmin-cute-kpop-gif-16363329",
            "https://tenor.com/view/stray-kids-seungmin-kim-seungmin-seungmin-stray-kid-pose-gif-14375800",
            "https://tenor.com/view/stray-kids-seungmin-kim-seungmin-shocked-gif-14375812",
            "https://tenor.com/view/kim-seungmin-seugmin-stray-kids-miroh-im-okay-gif-14227218",
            "https://tenor.com/view/stray-kids-stray-kids-seungmin-seungmin-skz-code-gif-20118379",
            "https://tenor.com/view/stray-kids-stray-kids-seungmin-seungmin-blueprint-gif-19525203",
            "https://tenor.com/view/seungmin-kim-seungmin-stray-kids-skz-kpop-gif-19048492",
            "https://tenor.com/view/stray-kids-stray-kids-seungmin-seungmin-blueprint-gif-19525140",
            "https://tenor.com/view/stray-kids-seungmin-stray-kids-seungmin-blueprint-gif-19512266",
            "https://tenor.com/view/stray-kids-skz-kpop-blueprint-seungmin-gif-19048496",
            "https://gfycat.com/distinctpossiblebluegill",
            "https://tenor.com/view/seungmin-kim-seungmin-dance-stray-kids-skz-gif-18617877",
            "https://tenor.com/view/stray-kids-seungmin-kim-kim-seungmin-cute-gif-13005384",
            "https://tenor.com/view/stray-kids-seungmin-kim-seungmin-wave-gif-14375814",
            "https://tenor.com/view/stray-kids-seungmin-kim-seungmin-finger-gun-gif-14375803",
            "https://tenor.com/view/kim-seungmin-stray-kids-seungmin-cute-kpop-gif-16363314",
            "https://tenor.com/view/seungmin-cute-happy-stray-kids-kim-seungmin-gif-19099810",
            "https://tenor.com/view/stray-kids-seungmin-kim-seungmin-smile-kpop-gif-16280320",
            "https://tenor.com/view/seungmin-kim-seungmin-skz-stray-kids-angst-gif-18780676",
            "https://tenor.com/view/stray-kids-stray-kids-seungmin-seungmin-gif-19534924",
            "https://tenor.com/view/stray-kids-skz-seungmin-heart-hi-gif-14481432",
            "https://tenor.com/view/seungmin-gif-18618851",
            "https://tenor.com/view/stray-kids-seungmin-kim-seungmin-stray-kids-seungmin-gif-12938624",
            "https://tenor.com/view/stray-kids-love-stray-kids-seungmin-skz-love-skz-seungmin-gif-19590939",
            "https://tenor.com/view/stray-kids-wave-seungmin-kim-kim-seungmin-gif-12929164",
            "https://giphy.com/gifs/straykids-k-pop-stray-kids-clzLLM7TwMKA4X5OV6",
            "https://giphy.com/gifs/straykids-k-pop-stray-kids-gods-menu-KxzBqEJ9aPH9qnqYkl",
            "https://64.media.tumblr.com/473c365eb21ff6cfe4a8727b4e113777/0b78e70430d1b2a3-47/s540x810/c4f2c6f8e7d9a617d1869a59e163bf78e1cad1fc.gif",
            "https://i.pinimg.com/originals/94/7c/9c/947c9cdaa972103147266f671e1bef6f.gif",
            "https://64.media.tumblr.com/a433b615479aad621034d4b733c85dd1/dc8cacbd317472ed-8a/s540x810/8746fbc004b6658ac9877acc02992f5fb8dacf91.gif",
            "https://64.media.tumblr.com/7bd19f2685f7b7879d921bf33d175131/tumblr_pdvf8orOzv1x5pa8no2_500.gif",
            "https://data.whicdn.com/images/328319941/original.gif",
            "https://i.pinimg.com/originals/e2/ea/df/e2eadf144b45151881528937eb87acbe.gif",
            "https://i.pinimg.com/originals/0a/c3/64/0ac36412de0ff2e2ae061de075488ccd.gif",
            "https://78.media.tumblr.com/289f2addb6ab388818afb593eaf72ed8/tumblr_p6so8o7VSE1whz8b5o1_400.gif",
            "https://i.pinimg.com/originals/e1/e3/c1/e1e3c1fdc0eee81cd3c630b688775da3.gif",
            "https://2.bp.blogspot.com/-Ebtt5L-IyL8/XD6977oLMvI/AAAAAAAANJs/wf396cG91owDhEK1XPg2QH3rFUgOpY-nACLcBGAs/s400/d.gif",
            "https://64.media.tumblr.com/f923880f147a8c04a79767051eeb8242/f1d5f1825f410846-64/s540x810/3872b92e802d43544f37cb96191d1463429b2c8e.gif",
            "https://i.pinimg.com/originals/a2/c7/00/a2c700bd522348f8a31ff8050cdf0c25.gif",
            "https://i.pinimg.com/originals/8e/4f/ee/8e4fee56ea961029f7711f8128ffd250.gif",
            "https://64.media.tumblr.com/8107ace4eba33f1b64d33be3308e4755/tumblr_inline_ps1n12uPQZ1w6o0f0_500.gif",
            "https://d.wattpad.com/story_parts/727104930/images/159ab7d3f4edc87d40297965869.gif",
            "https://64.media.tumblr.com/969a6af9eae58f933040a04ec1b02651/849c82ba3071132b-84/s540x810/551ab3b3a28931ef158ad3148b310b24f176e70d.gif",
            "http://images6.fanpop.com/image/photos/42800000/Tmt-stray-kids-F0-9F-8C-BA-42888541-540-220.gif",
            "https://64.media.tumblr.com/1b01099239f35fd0051102227393508c/1c9916a95ef700f8-8f/s500x750/9682805e4409479b60bd55011dd0b2965d5f0692.gif",
            "https://64.media.tumblr.com/a28dc21e4e58f91cc76d3ba1aa489a83/50dee50c27303640-8e/s540x810/749d6ed04faedb5f4a319e34c7ae07eea4fc9338.gif",
            "https://64.media.tumblr.com/d4300e3cb9667aaff3d5da236cd25715/11f2619816e6aa7c-85/s400x600/fd20437db53d971701ee35154af4dc5a339bada3.gif",
            "https://64.media.tumblr.com/639e0525f2b008753bd5733dafb03bcb/c1984ff770e67e72-08/s250x400/11ae5a7032fd35b87c8829d821b27e829e6f2851.gif",
            "https://64.media.tumblr.com/1166328a5a82401748484cc182bca43f/8be01c8f4516aa13-cb/s500x750/08adec196c1bdbf2398e92b7eb234efccba0c387.gif",
            "https://64.media.tumblr.com/24d74dd805e017dd23812fb20b89044b/tumblr_p7ulcctuxu1wxtw28o2_500.gif",
            "https://64.media.tumblr.com/376c1d410d4a1ac4d1f35e2855a329ad/tumblr_p7ulcctuxu1wxtw28o5_500.gif",
            "https://pa1.narvii.com/7071/0580f2ac2953a2b1bc319d6cc8a963d243b977d1r1-268-350_hq.gif",
            "https://pa1.narvii.com/7190/35c19730a5ec7ba8689773aac228318491e5b661r1-540-236_hq.gif",
            "https://64.media.tumblr.com/ed5c6bf191f3c3bb472352a2a8726674/f695778c0bcf1327-64/s540x810/f989d5f6347b289f45c7348956f6278e6c426ad2.gif",
            "https://64.media.tumblr.com/d270e9bd96c8339c2918d3bb8fa892ea/5c7e4a69ef731889-af/s250x400/58af853b7d323567361ca522224e4d0cf68b12bf.gif",
            "https://64.media.tumblr.com/d3b65e02089a14b28590a5918e5746c7/724e089c83c5376a-ba/s400x600/bf2f36670c2e5bdfca68b1dcdefb276888cc5265.gif",
            "https://64.media.tumblr.com/02bf35c18532b75973202ade0fd14af1/b9a152d3c81296e6-24/s540x810/a3551bdd710cc3a1b9d29e7241f0bbf5409e4172.gif"]


    @commands.command()
    async def stray(self, ctx, kids, *, arg="yessir"):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Stray Kids {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if kids == "kids":
            if arg == "felix":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@!{ctx.author.id}> is talking about Felix :heart:')
                        await ctx.send(random.choice(self.bot.felix_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Felix :heart:')
                    await ctx.send(random.choice(self.bot.felix_gif))
                    await ctx.message.delete()
            elif arg == "bang chan":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@!{ctx.author.id}> is talking about Bang Chan :heart:')
                        await ctx.send(random.choice(self.bot.bangchan_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Bang Chan :heart:')
                    await ctx.send(random.choice(self.bot.bangchan_gif))
                    await ctx.message.delete()
            elif arg == "lee know" or arg == "minho":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@!{ctx.author.id}> is talking about Lee Know :heart:')
                        await ctx.send(random.choice(self.bot.leeknow_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Lee Know :heart:')
                    await ctx.send(random.choice(self.bot.leeknow_gif))
                    await ctx.message.delete()
            elif arg == "changbin":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@!{ctx.author.id}> is talking about Changbin :heart:')
                        await ctx.send(random.choice(self.bot.changbin_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Changbin :heart:')
                    await ctx.send(random.choice(self.bot.changbin_gif))
                    await ctx.message.delete()
            elif arg == "han":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@!{ctx.author.id}> is talking about Han :heart:')
                        await ctx.send(random.choice(self.bot.han_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Han :heart:')
                    await ctx.send(random.choice(self.bot.han_gif))
                    await ctx.message.delete()
            elif arg == "jeongin" or arg == "in" or arg == "i.n":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@!{ctx.author.id}> is talking about I.N :heart:')
                        await ctx.send(random.choice(self.bot.jeongin_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about I.N :heart:')
                    await ctx.send(random.choice(self.bot.jeongin_gif))
                    await ctx.message.delete()
            elif arg == "seungmin":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@!{ctx.author.id}> is talking about Seungmin :heart:')
                        await ctx.send(random.choice(self.bot.seungmin_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Seungmin :heart:')
                    await ctx.send(random.choice(self.bot.seungmin_gif))
                    await ctx.message.delete()
            elif arg == "hyunjin":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Hyunjin :heart:')
                    await ctx.send(random.choice(self.bot.shyunjin_gif))
                    await ctx.message.delete()



def setup(client):
    client.add_cog(StrayPings(client))