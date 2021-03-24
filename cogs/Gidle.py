import discord, random
from discord.ext import commands
from datetime import datetime


#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

class IdlePings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.minnie_gif = ["https://tenor.com/view/minnie-gidle-singing-performance-kpop-gif-16204817",
            "https://tenor.com/view/%EC%97%AC%EC%9E%90%EC%95%84%EC%9D%B4%EB%93%A4-minnie-%EB%AF%BC%EB%8B%88-%E7%B1%B3%E5%A6%AE-cute-gif-18186679",
            "https://tenor.com/view/minnie-gidle-ohmygod-omg-kpop-gif-18256855",
            "https://tenor.com/view/minnie-minnie-nicha-minnie-nicha-yontararak-nicha-yontararak-nicha-gif-18888803",
            "https://tenor.com/view/minnie-gidle-gif-15784676",
            "https://tenor.com/view/minnie-g-idle-nicha-yontararak-kpop-pretty-gif-16351087",
            "https://tenor.com/view/minnie-minnie-nicha-minnie-nicha-yontararak-nicha-yontararak-nicha-gif-18888791",
            "https://tenor.com/view/minnie-gidle-%EB%AF%BC%EB%8B%88-%EC%97%AC%EC%9E%90%EC%95%84%EC%9D%B4%EB%93%A4-%EC%95%84%EC%9D%B4%EB%93%A4-gif-17062450",
            "https://tenor.com/view/gidle-minnie-gif-19705161",
            "https://tenor.com/view/minnie-minnie-nicha-minnie-nicha-yontararak-nicha-nicha-yontararak-gif-18888820",
            "https://tenor.com/view/minnie-minnie-nicha-minnie-nicha-yontararak-nicha-nicha-yontararak-gif-18888817",
            "https://tenor.com/view/minnie-kim-minnie-gidle-minnie-nicha-minnie-nicha-yontararak-gif-19979784",
            "https://tenor.com/view/%EC%97%AC%EC%9E%90%EC%95%84%EC%9D%B4%EB%93%A4-%EC%95%84%EC%9D%B4%EB%93%A4-idle-gidle-minniegidle-gif-19954171",
            "https://tenor.com/view/%EC%97%AC%EC%9E%90%EC%95%84%EC%9D%B4%EB%93%A4-%EC%95%84%EC%9D%B4%EB%93%A4-%EB%AF%BC%EB%8B%88-gidle-idle-gif-19954146",
            "https://tenor.com/view/g-idle-minnie-gidle-minnie-cute-oh-my-god-gif-16806549",
            "https://tenor.com/view/%EB%82%B4%EA%B2%8C%EB%A1%9C%EC%99%80-%EC%9C%A0%ED%98%B9%ED%95%98%EB%8B%A4-%EC%9B%83%EB%8B%A4-%EB%AF%B8%EC%86%8C-%EB%AF%BC%EB%8B%88-gif-18634830",
            "https://tenor.com/view/minnie-kim-minnie-gidle-minnie-nicha-minnie-nicha-yontararak-gif-19979800",
            "https://tenor.com/view/minnie-kim-minnie-gidle-minnie-nicha-minnie-nicha-yontararak-gif-19979785",
            "https://tenor.com/view/minnie-minnie-nicha-minnie-nicha-yontararak-nicha-yontararak-nicha-gif-18888805",
            "https://64.media.tumblr.com/3fbecf8123d33b1c3c93ce8ce71b41f1/76b2cfb688e360a6-77/s400x600/42eab06c498f396256e2d343d80ef46cd90e0f68.gif",
            "https://64.media.tumblr.com/dc086412aeb83850cd79eabe176cb0f2/76b2cfb688e360a6-b0/s400x600/7206ab1c3a420a99e9477ec23d66dfba90ff623f.gif",
            "https://64.media.tumblr.com/f7b8cfea7a72854350208119644eefbf/9dbb184f890d9bd8-64/s250x400/6629202e8b3921e44e1956e2798afbdac095fe4d.gif",
            "https://64.media.tumblr.com/9cb5b81e6a015ed6eede94a1d0a01106/tumblr_pda1k82SiD1somnmfo5_400.gif",
            "https://64.media.tumblr.com/f87fc020ba49bbe77cfce70f844b9636/tumblr_pb3g3fn1pi1tj2lfbo3_r1_250.gif",
            "https://64.media.tumblr.com/8c6719dca97cf582b877fa47b51da490/tumblr_pb3g3fn1pi1tj2lfbo2_r2_250.gif",
            "https://64.media.tumblr.com/4a4a5b209e3fe7a92c9b0e7923193045/tumblr_pb3g3fn1pi1tj2lfbo1_r3_250.gif",
            "https://64.media.tumblr.com/c0e5a3c57425f0a4fa056dea7e540774/tumblr_pb3g3fn1pi1tj2lfbo4_r1_250.gif",
            "https://64.media.tumblr.com/57a2a9ad81e71c73809f4b1c5f939e56/tumblr_pe28zvMb2R1tj2lfbo1_250.gif",
            "https://64.media.tumblr.com/97ab974f82d935d46e8567d6e8f9cdff/tumblr_pe28zvMb2R1tj2lfbo2_250.gif",
            "https://64.media.tumblr.com/abe576d3bc85781133b385615428f5c8/tumblr_pe28zvMb2R1tj2lfbo4_250.gif",
            "https://64.media.tumblr.com/741354f31686ba1a6342bde7d8ed21b4/tumblr_pe28zvMb2R1tj2lfbo5_250.gif",
            "https://64.media.tumblr.com/a7d3d49239d8a07256f2195568e2d256/tumblr_pnlof67GO91r7qnpao1_250.gif",
            "https://64.media.tumblr.com/427c04da29d24ec5b5d4b40a359f1144/tumblr_pnlof67GO91r7qnpao3_250.gif",
            "https://64.media.tumblr.com/800dd1feda369589fedce5ff56b3dee8/tumblr_pnlof67GO91r7qnpao4_250.gif",
            "https://64.media.tumblr.com/803db3eac8205f5dd31b4ec217e0f34b/tumblr_p8ajdqoaEk1xqn7lno3_250.gif",
            "https://64.media.tumblr.com/2cf659e4898d76a1d24be7c706bb3394/tumblr_p8ajdqoaEk1xqn7lno1_r1_250.gif",
            "https://64.media.tumblr.com/b630eb23bfc71143a5f139076a6e2552/tumblr_p8ajdqoaEk1xqn7lno2_r1_250.gif",
            "https://64.media.tumblr.com/00fe80415907f2ebd51b379244e77f72/tumblr_p8ajdqoaEk1xqn7lno4_250.gif",
            "https://64.media.tumblr.com/2bedc0c32782bceb4d1404e81e71e791/tumblr_pnpz5uY67D1somnmfo2_250.gif",
            "https://64.media.tumblr.com/1fe47e820c80fd5ced206126c9b3e06b/tumblr_ppzj9h2jG31y4bx0oo1_400.gif",
            "https://64.media.tumblr.com/275517727fbdae069b0d0ab60d4449a5/tumblr_ppzj9h2jG31y4bx0oo2_400.gif",
            "https://64.media.tumblr.com/99e092bdf6c83fbf771408d48b3f4ab3/tumblr_p949wxwj8v1vpomzuo4_250.gif",
            "https://64.media.tumblr.com/c753e3569ca37bd4b382642f0bb17051/tumblr_p949wxwj8v1vpomzuo1_250.gif",
            "https://64.media.tumblr.com/c38b57853a8dfe063091b8a7af38c4b2/7cbb6e6a534351b6-b9/s400x600/f08bbf9ad184e21af7325ca13a4743e0fbe152d4.gif",
            "https://64.media.tumblr.com/74668869bd56f5a81471f206f1f7482f/d0caacc79318354e-6e/s250x400/5b077b55c17cb41e6dfebb743f17259985cce7a8.gif",
            "https://64.media.tumblr.com/58e21d18563d1a6b247130d99eb3b1ec/d0caacc79318354e-1a/s250x400/babd4bb22711b7a2b86716f3f3f521a59893f600.gif",
            "https://64.media.tumblr.com/526eeb5f5ddbf5f926feb4ee5742f92b/d0caacc79318354e-e2/s250x400/dd0eb8a8f53239edbd91963ee9622e6b8e8b2c5f.gif",
            "https://64.media.tumblr.com/a6fbaa438023b9be3ef3ec291f001231/tumblr_ptspjlmSbq1xqn7lno6_r1_250.gif",
            "https://64.media.tumblr.com/597c35ee2fc3fd86bf50d482cff7a551/c9f0548871f8c0c2-bf/s400x600/a2cd0d0305a5a213e4ab1e4ac15f2cba098e851a.gif",
            "https://64.media.tumblr.com/f22428dc1be7e78f525f02b7d9081bb0/a0b54dc99e35f921-05/s250x400/5ada968e16a275094df623207e426cacd7b5194e.gif"]

        self.bot.miyeon_gif = ["https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962243",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962348",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962294",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962324",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962177",
            "https://tenor.com/view/miyeon-miyeon-gidle-cho-miyeon-gif-18403777",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962317",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962152",
            "https://cdn.discordapp.com/attachments/800597433134481458/800601970124783637/tenor_2.gif",
            "https://cdn.discordapp.com/attachments/800597433134481458/800603213308493824/tenor_5.gif",
            "https://cdn.discordapp.com/attachments/800597433134481458/800603577390202920/tenor_6.gif",
            "https://cdn.discordapp.com/attachments/800597433134481458/800603659980374026/tenor_7.gif",
            "https://cdn.discordapp.com/attachments/800597433134481458/800603822430093312/tenor_8.gif",
            "https://gfycat.com/glamorousconventionalharrier-stage-mix-gidle-miyeon-hwaa-fire-kpop",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962246",
            "https://tenor.com/view/cho-miyeon-gidle-cho-miyeon-gidle-passing-gidle-passing-gif-18841500",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-19979650",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-19979738",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-19979648",
            "https://thumbs.gfycat.com/WhirlwindGrouchyAfghanhound-max-1mb.gif",
            "https://data.whicdn.com/images/317856655/original.gif",
            "http://images6.fanpop.com/image/photos/42600000/-G-I-DLE-g-i-dle-42628992-540-300.gif",
            "https://66.media.tumblr.com/a0c2b3b5d19459a75fa06ebf7d0404a1/tumblr_pdg3y8CtVL1xqswnmo1_500.gif",
            "https://pa1.narvii.com/6957/46461b5e00f81cd64ceb061d0f131cfde4bebdccr1-300-300_hq.gif",
            "https://pa1.narvii.com/6986/7840fddf1b300cfaefe0d06721856c8443a8dd22r1-500-225_hq.gif",
            "https://64.media.tumblr.com/39d4bc38d92b5feacf3d271c198988f0/tumblr_p83qizzaZ11xqswnmo1_540.gif",
            "http://pa1.narvii.com/6850/cea76f5859566a4f3f2a89def5c2d14b5c1603a6_00.gif"]

        self.bot.shuhua_gif = ["https://tenor.com/view/pop-taiwanese-kpop-yehshuhua-selfdefense-gif-18118582",
            "https://tenor.com/view/gidle-shuhua-%ec%97%ac%ec%9e%90%ec%95%84%ec%9d%b4%eb%93%a4-%ec%95%84%ec%9d%b4%eb%93%a4-%ec%8a%88%ed%99%94-gif-16949157",
            "https://tenor.com/view/shuhua-idle-gidle-yeh-shu-hua-cube-entertainment-gif-16929431",
            "https://tenor.com/view/glasses-shuhua-idle-yeh-gidle-gif-13052094",
            "https://tenor.com/view/yeh-shu-hua-gidle-heart-love-gif-13052095",
            "https://tenor.com/view/kpop-shuhua-gidle-pretty-gif-14904506",
            "https://tenor.com/view/shuhua-kpop-gif-18740565",
            "https://tenor.com/view/%E8%88%92%E8%8F%AF-gidle-%EC%8A%88%ED%99%94-shuhua-wave-gif-16738706",
            "https://tenor.com/view/shuhua-yeh-shuhua-shuhua-gidle-shuhua-idle-gidle-gif-19200395",
            "https://gfycat.com/pinkunequaledequine",
            "https://gfycat.com/sharpshoddycornsnake",
            "https://gfycat.com/damagedlightheartedamericancrow",
            "https://gfycat.com/sophisticatedequatorialkingfisher",
            "https://gfycat.com/indeliblebadibisbill",
            "https://gfycat.com/creativerealisticfox",
            "https://gfycat.com/innocenttepidkodiakbear",
            "https://gfycat.com/blonddifferentcony",
            "https://gfycat.com/feistymealyequine",
            "https://gfycat.com/tinyfatalkangaroo",
            "https://gfycat.com/pleasantgranularamericantoad",
            "https://gfycat.com/impureappropriateblobfish",
            "https://gfycat.com/weightyverifiablebandicoot",
            "https://gfycat.com/gracefulpositivegreatwhiteshark",
            "https://gfycat.com/warmheartednaiveasianporcupine",
            "https://gfycat.com/vaguejampackedchinchilla",
            "https://gfycat.com/enrageddelectablebongo",
            "https://gfycat.com/measlyacidicgoose",
            "https://gfycat.com/unawarefarflungbumblebee",
            "https://gfycat.com/playfulsimpledassie",
            "https://gfycat.com/nippyrigidkissingbug",
            "https://gfycat.com/eagershallowgnat",
            "https://gfycat.com/hardenormouschrysalis",
            "https://gfycat.com/poorhilarioushairstreakbutterfly",
            "https://gfycat.com/gracefulrapidafricanfisheagle",
            "https://gfycat.com/optimaldefiantbass",
            "https://gfycat.com/dimpleasedkakarikis",
            "https://gfycat.com/unripefancyamazontreeboa",
            "https://gfycat.com/timelyunripehornedviper",
            "https://gfycat.com/determinedembellishedatlanticridleyturtle",
            "https://gfycat.com/darlingsharparabianoryx",
            "https://gfycat.com/leftpitifulaardwolf",
            "https://gfycat.com/pastelleadingcoral",
            "https://gfycat.com/sparklingcomplexarchaeocete",
            "https://gfycat.com/glasseminentcardinal",
            "https://gfycat.com/impishthankfulgardensnake",
            "https://gfycat.com/decimalbeneficiallamb",
            "https://gfycat.com/ficklehideoushumpbackwhale",
            "https://gfycat.com/vapidelementarybactrian",
            "https://gfycat.com/jollysneakycanvasback",
            "https://gfycat.com/celebratedeuphoriccoyote",
            "https://gfycat.com/amazingtiredgosling",
            "https://gfycat.com/idioticgiantaegeancat",
            "https://gfycat.com/incrediblesnivelingdanishswedishfarmdog",
            "https://gfycat.com/whisperedobesehippopotamus",
            "https://gfycat.com/madtepidafricanwildcat",
            "https://gfycat.com/bestgreenchinchilla",
            "https://gfycat.com/jointadoredisabellineshrike",
            "https://gfycat.com/magnificentassuredbison",
            "https://gfycat.com/unkemptaptcatbird",
            "https://gfycat.com/portlypoliticalhylaeosaurus",
            "https://gfycat.com/sprycleverdore",
            "https://gfycat.com/generouswelldocumentedelephantbeetle",
            "https://gfycat.com/indelibleperkygnat",
            "https://gfycat.com/illinformedperkydragonfly",
            "https://gfycat.com/vacantvelvetyamphiuma",
            "https://gfycat.com/niceorderlyjackrabbit",
            "https://gfycat.com/abledrearylhasaapso",
            "https://gfycat.com/heavenlymilkyitalianbrownbear",
            "https://gfycat.com/scratchycanineallensbigearedbat",
            "https://gfycat.com/palatablescientificirishwolfhound",
            "https://gfycat.com/wearyspicyamericanbulldog",
            "https://gfycat.com/hospitablegrandioseinchworm",
            "https://gfycat.com/greatuntriedgermanshepherd",
            "https://gfycat.com/ripeeachcrossbill",
            "https://gfycat.com/secretpoisedangora",
            "https://gfycat.com/rashdirectindianabat",
            "https://gfycat.com/dimpledmellowgoldfinch",
            "https://gfycat.com/faintskeletalhyracotherium",
            "https://gfycat.com/poorearnestharpyeagle",
            "https://gfycat.com/ripedeafeningleopardseal",
            "https://data.whicdn.com/images/342489559/original.gif",
            "https://gfycat.com/finishedfoolhardylemming",
            "https://gfycat.com/giddygiftedgalago",
            "https://gfycat.com/dapperadvancedhusky",
            "https://gfycat.com/bruisedgeneralalbacoretuna",
            "https://gfycat.com/aptrealisticgavial",
            "https://gfycat.com/deficientrepulsivealligator",
            "https://gfycat.com/impartialredcottontail",
            "https://gfycat.com/ecstaticimaginativeasianpiedstarling",
            "https://gfycat.com/optimalmajorguineafowl",
            "https://gfycat.com/deadbogushound",
            "https://gfycat.com/glaringbrokenalaskajingle",
            "https://gfycat.com/unitedyearlycob"]

        self.bot.soojin_gif = ["https://tenor.com/view/soojin-gif-18250849",
            "https://tenor.com/view/gidle-soojin-seo-soojin-idle-gif-15287479",
            "https://tenor.com/view/soojin-gidle-wink-gif-13805713",
            "https://tenor.com/view/soojin-seo-soojin-gidle-idle-soojin-gidle-gif-18888703",
            "https://tenor.com/view/soojin-gif-18526389",
            "https://tenor.com/view/soojin-seo-soojin-gidle-idle-sujin-gif-18866361",
            "https://tenor.com/view/soojin-soojin-gidle-gif-18404859",
            "https://tenor.com/view/soojin-gif-19272378",
            "https://cdn.discordapp.com/attachments/800597377429143554/800604618086023239/tenor_10.gif",
            "https://cdn.discordapp.com/attachments/800597377429143554/800604667448262666/tenor_11.gif",
            "https://cdn.discordapp.com/attachments/800597377429143554/800604718065647656/tenor_12.gif",
            "https://tenor.com/view/soojin-seo-soojin-gidle-idle-soojin-gidle-gif-19979836",
            "https://tenor.com/view/soojin-gidle-dance-seo-soojin-gif-13805717",
            "https://tenor.com/view/seo-soojin-soojin-g-idle-cute-smile-gif-14863179",
            "https://i.pinimg.com/originals/7a/56/e0/7a56e05b745686a393f0510e1d9673c3.gif",
            "https://data.whicdn.com/images/343724971/original.gif",
            "https://data.whicdn.com/images/342651579/original.gif",
            "https://64.media.tumblr.com/6ecfd7f7cb2062529377ff762c99916d/51386a04645f4210-cc/s400x600/02bec209b374a2c0bdbb6888a3e7a50164ee4850.gif",
            "https://64.media.tumblr.com/27cfb6e5cad8672ab4e99ec3fd1b7e71/51386a04645f4210-23/s400x600/98dc62da7ada61928ff1b2f04cd778b54858ad16.gif",
            "https://i.pinimg.com/originals/7f/25/6f/7f256fcc02268c104e0812601724a661.gif",
            "https://i.pinimg.com/originals/49/e1/31/49e1316079c3e206da22a8e07a185c56.gif",
            "https://i.pinimg.com/originals/1b/75/6b/1b756bfe4a832d4e1ee22c2a51621537.gif",
            "https://i.pinimg.com/originals/9e/46/42/9e4642aa6bfa9ae67c89fdfd93d3484d.gif",
            "https://i.pinimg.com/originals/e9/30/92/e93092b535a16333deac8d9f1041e9d5.gif",
            "https://thumbs.gfycat.com/WiltedTatteredKangaroo-max-1mb.gif",
            "https://64.media.tumblr.com/213aadf4b32c680f3e80398cd37a40ea/28467a45e3f9a2b5-66/s250x400/0fb503953925ef9f7217c3650abfbdfb4bfbce1a.gif",
            "https://64.media.tumblr.com/3cf03f246fa3dba7c27fcbaabc49d7e1/28467a45e3f9a2b5-a5/s250x400/ae740f54a151fa96e61ca37b8dd02f6d4281c254.gif",
            "https://i.pinimg.com/originals/9c/1f/dc/9c1fdc0ab40a20d7ad50a72b4dfecb30.gif",
            "https://64.media.tumblr.com/0e405a7000c31c58413239ca541a41bf/b330494631435200-5f/s400x600/a966253d3655e893d696a7a72f3ef0da8e9210a1.gif",
            "https://64.media.tumblr.com/6d60293d679a28eb126e9ba52a875348/b330494631435200-61/s400x600/e7c87607274e28daf5f8da2727a26a727ceaaf7e.gif"]

        self.bot.soyeon_gif = ["https://tenor.com/view/soyeon-jeon-gif-19050110",
            "https://tenor.com/view/soyeon-jeon-soyeon-gidle-idle-soyeon-gidle-gif-18962551",
            "https://tenor.com/view/soyeon-jeon-soyeon-gidle-idle-soyeon-gidle-gif-18962536",
            "https://tenor.com/view/soyeon-jeon-soyeon-soyeon-gidle-soyeon-idle-gidle-gif-19200289",
            "https://tenor.com/view/idle-soyeon-g-idle-soyeon-jeon-soyeon-soyeon-cute-gif-16629896",
            "https://tenor.com/view/soyeon-jeon-soyeon-gidle-idle-soyeon-gidle-gif-18962545",
            "https://tenor.com/view/soyeon-jeon-soyeon-gidle-idle-soyeon-gidle-gif-18962456",
            "https://giphy.com/gifs/GIDLE-gidle-gi-dle-dumdi-ihLlzoKG2gdOV718GN",
            "https://tenor.com/view/jeon-soyeon-gif-19180116",
            "https://tenor.com/view/soyeon-jeon-gidle-gif-19180104",
            "https://tenor.com/view/jeon-soyeon-gif-19180115",
            "https://tenor.com/view/soyeon-jeon-soyeon-gidle-unpretty-rapstars3-smile-gif-15122585",
            "https://tenor.com/view/soyeon-senorita-g-idle-cute-kpop-kpop-girl-group-gif-15338342",
            "https://tenor.com/view/kcon2019thailand-kcon2019th-kcon2019-kcon-%EC%BC%80%EC%9D%B4%EC%BD%98-gif-15500055",
            "https://tenor.com/view/wow-thing-soyeon-soyeon-rap-gif-15842099",
            "https://tenor.com/view/gidle-soyeon-gidle-han-soyeon-kpop-han-mma-gif-17953864",
            "https://tenor.com/view/soyeon-soy-gidle-gif-19050069",
            "https://tenor.com/view/soyeon-jelly-baloon-g-idle-soyeon-jeon-soyeon-kpop-gif-17901528",
            "https://tenor.com/view/dancing-gidle-soyeon-cosmopolitan-dance-moves-gif-18221991",
            "https://tenor.com/view/soyeon-soyeon-gidle-soyeon-idle-gidle-idle-gif-18962475",
            "https://tenor.com/view/soyeon-soyeon-gidle-soyeon-idle-gidle-idle-gif-18962486",
            "https://tenor.com/view/soyeon-soy-gif-19050109",
            "https://tenor.com/view/soyeon-gidle-ohmygod-kpop-omg-gif-18312959",
            "https://tenor.com/view/g-idle-soyeon-jeon-soyeon-kpop-cute-gif-15859587",
            "https://tenor.com/view/g-idle-soyeon-jeon-soyeon-kpop-cute-gif-17901589",
            "https://tenor.com/view/soyeon-jeon-soyeon-gidle-idle-soyeon-gidle-gif-18962437",
            "https://tenor.com/view/gidle-gidle-lion-soyeon-gif-15722063",
            "https://tenor.com/view/soyeon-jeon-soyeon-soyeon-gidle-soyeon-idle-gidle-gif-19200276",
            "https://tenor.com/view/soyeon-jeon-soyeon-soyeon-gidle-soyeon-idle-gidle-gif-19200299",
            "https://tenor.com/view/soyeon-jeon-soyeon-gidle-idle-soyeon-gidle-gif-18962542",
            "https://tenor.com/view/soyeon-kda-the-baddest-gif-18262396",
            "https://cdn.discordapp.com/attachments/800597297704337409/800607108725866546/f8eb8ac2c6e6ee77bc7a5c50ef36df0e.gif",
            "https://cdn.discordapp.com/attachments/800597297704337409/800607406501265458/tenor_14.gif",
            "https://i.pinimg.com/originals/cd/34/72/cd34726a211a5a31071025fd1b19049a.gif",
            "https://thumbs.gfycat.com/WellgroomedNiftyArmyworm-size_restricted.gif"]

        self.bot.yuqi_gif = ["https://tenor.com/view/%EC%95%84%EC%9D%B4%EB%93%A4-%EC%9A%B0%EA%B8%B0-%EC%97%AC%EC%9E%90%EC%95%84%EC%9D%B4%EB%93%A4-g-idle-yuqi-gif-16254335",
            "https://tenor.com/view/yuqi-heart-cute-gif-13344124",
            "https://tenor.com/view/yuqi-song-yuqi-smile-eyes-cute-gif-17354259",
            "https://tenor.com/view/gidle-yuqi-mishuqi-wink-gif-17988600",
            "https://tenor.com/view/yuqi-dog-lover-cute-gif-13943997",
            "https://tenor.com/view/song-yuqi-yuqi-oh-my-god-gidle-ending-fairy-gif-17354516",
            "https://tenor.com/view/yuqi-yuqifancam-yuqigidle-cute-smile-gif-12588694",
            "https://tenor.com/view/g-idle-yuqi-song-yuqi-chinese-singer-pretty-gif-17257186",
            "https://tenor.com/view/kpop-g-idle-yuqi-uwu-oof-gif-12719365",
            "https://tenor.com/view/g-idle-yuqi-song-yuqi-chinese-singer-pretty-gif-17257186",
            "https://tenor.com/view/song-yuqi-yuqi-oh-my-god-gidle-ending-fairy-gif-17354516",
            "https://tenor.com/view/%EC%97%AC%EC%9E%90%EC%95%84%EC%9D%B4%EB%93%A4-%EC%95%84%EC%9D%B4%EB%93%A4-%EC%9A%B0%EA%B8%B0-gidle-idle-gif-19954016",
            "https://tenor.com/view/yuqi-g-idle-kpop-cute-gif-15296803",
            "https://tenor.com/view/g-idle-yuqi-song-yuqi-chinese-singer-pretty-gif-17257186",
            "https://gfycat.com/giantcorruptflee-song-yuqi-gidle-vlive-kpop"]

    @commands.command(aliases = ['(g)i-dle', 'idle'])
    async def gidle(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [(G)I-dle {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "minnie":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Minnie :heart:')
                await ctx.send(random.choice(self.bot.minnie_gif))
                await ctx.message.delete()
        elif arg == "miyeon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Miyeon :heart:')
                await ctx.send(random.choice(self.bot.miyeon_gif))
                await ctx.message.delete()
        elif arg == "shuhua":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Shuhua :heart:')
                await ctx.send(random.choice(self.bot.shuhua_gif))
                await ctx.message.delete()
        elif arg == "soojin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Soojin :heart:')
                await ctx.send(random.choice(self.bot.soojin_gif))
                await ctx.message.delete()
        elif arg == "soyeon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Soyeon :lollipop:')
                await ctx.send(random.choice(self.bot.soyeon_gif))
                await ctx.message.delete() 
        elif arg == "yuqi":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yuqi :heart:')
                await ctx.send(random.choice(self.bot.yuqi_gif))
                await ctx.message.delete()


def setup(client):
    client.add_cog(IdlePings(client))