import discord, random, datetime
from discord.ext import commands
from datetime import datetime

        #= Dreamcatcher

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

#//people
k8 = 573974040679809044

class GGS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.logs = 786515662214397973
    #. Apink
        self.bot.apink_bomi_gif = ["https://tenor.com/view/yoon-bomi-one-one-more-time-chance-again-gif-13724908",
            "https://tenor.com/view/yoon-bomi-play-recorder-musical-instrument-flutes-gif-11868145",
            "https://tenor.com/view/thanks-thank-you-apink-bomi-yoon-gif-9243373",
            "https://tenor.com/view/bomi-apink-bomi-apink-bomi-apink-im-so-sick-im-so-sick-gif-14772262",
            "https://64.media.tumblr.com/dd810660b761c01b16ab635e6cc50981/tumblr_plev3yT1v41vb2ospo2_250.gif",
            "https://64.media.tumblr.com/7826fa5e6b457c9d56dfb7525e434d19/tumblr_plev3yT1v41vb2ospo1_250.gif",
            "https://64.media.tumblr.com/0f098171263cf75ede009e6de3755772/40624a9f884798bb-17/s400x600/6cf41108fad0285eb96ef2a789123e860068ac4d.gif",
            "https://64.media.tumblr.com/e0bbed231dc57af681cb1e7917c6cc24/tumblr_pb8r13RsIe1xxqotao4_250.gif",
            "https://64.media.tumblr.com/f9fdcb51f0b11a5688cbad2bb877f2a6/tumblr_pxf2gmmky91xw84pqo3_250.gif",
            "https://64.media.tumblr.com/8b2d354e6ab8709302b6643567a7f57f/46150fc377fc1dde-58/s400x600/dc630d009160fda6f1fa08e90a60d0066dd755e4.gif",
            "https://64.media.tumblr.com/7fb4f65b4a9850c7efbd76ec04b5dc7a/tumblr_pbc0uyxa7w1tj2lfbo2_250.gif",
            "https://64.media.tumblr.com/3c259a7c539903e95c980482427cd541/tumblr_pbaoqzu2LF1xoxm6to5_400.gif",
            "https://64.media.tumblr.com/1162467e8d5f004975a6e1096804dad1/tumblr_pmz9tabkjX1y6jppqo4_250.gif",
            "https://64.media.tumblr.com/381211a18182dcfa4f15c45c3a46bb24/f9acf2a8326e581f-c5/s400x600/458383e56cf3b0184bb82b14289024212e8961be.gif",
            "https://64.media.tumblr.com/8caf8a358a466abea7e3845cf774a4f0/b50f2e3cfac1c29e-e7/s250x400/cad00c97ea627d19034b30e33b7ac3b43b7c9c0c.gif"]

        self.bot.apink_chorong_gif = ["https://tenor.com/view/chorong-gif-7780924",
            "https://tenor.com/view/nevermind-thegodbomi-chorong-apink-laughs-gif-20131482",
            "https://64.media.tumblr.com/b7c8567e26e6de856c0317e411ec6a51/6efec9cb5919446f-06/s250x400/07ee88e940934ab1decf405470618ecb1fa8c8ee.gif",
            "https://64.media.tumblr.com/0a15491d0099bf86d6efa9e56e60dc8f/f5b2db8052ad7310-e4/s250x400/f2e6fd3491005af3c00c84fd1a7a885de2795598.gif",
            "https://64.media.tumblr.com/76db3e8113cad8a745a99d2ba5ecf882/cd2f7c7158dab85f-29/s250x400/f7ddd754a7163fd0f51e0d36c143d8bc37743d70.gif",
            "https://64.media.tumblr.com/5ac5fc1205779fc71631b15db729d06c/1aa4e275cf310306-3c/s400x600/5034f4e1fcfdc6ee8fe889bd566e0935aaddd434.gif",
            "https://64.media.tumblr.com/0c521b500a5b56ab83eda2978a09e725/tumblr_pbxnzzyaze1qg5nyao1_250.gif",
            "https://64.media.tumblr.com/857375fc74bf5ad5020bd333076114f6/tumblr_p1xkhuJxc71uu2l2ko1_250.gif",
            "https://64.media.tumblr.com/c78b890816ff8386769d89a3ac3a4e0f/tumblr_plg1tmTgP61sh3g3mo4_250.gif",
            "https://64.media.tumblr.com/944c623ee530d081598b585ccf1b95a9/tumblr_pj3027nio11ui9s1qo1_250.gif",
            "https://64.media.tumblr.com/291136a62272f109ab1e7556ffc8fca6/b50f2e3cfac1c29e-57/s250x400/b7a7dffede3dd44dca3261b9e84a06a535103340.gif",
            "https://64.media.tumblr.com/f4e673c1b1fa8e9503439efddbe5eae6/tumblr_pkyf3dB3l81somnmfo4_400.gif",
            "https://64.media.tumblr.com/a429d70ac9f04122a8c94c4b8f346be4/ccb85531d41c47c9-7c/s250x400/d94c1e5a59ea1c72222f99e2af2cae623a9b4c74.gif",
            "https://64.media.tumblr.com/8f9a990668c6c369e77e85aa025ea0f0/66db3935b2a70e92-46/s250x400/77982d242842405a154d753ea16321c4dc49816e.gif",
            "https://64.media.tumblr.com/e217c0c012d57c39d188cf500552f67a/tumblr_pd35sn83rJ1uqmda6o1_400.gif",
            "https://64.media.tumblr.com/d20a8ad49a03f75e8b4992a5074e73d0/tumblr_pbg561NRo41tlaxyuo3_250.gif"]

        self.bot.apink_eunji_gif = ["https://tenor.com/view/apink-girl-group-sing-music-kpop-gif-5669042",
            "https://tenor.com/view/apink-eunji-gif-18881050",
            "https://cdn.discordapp.com/attachments/800205891365371915/808932802892005396/eunji_1.gif",
            "https://cdn.discordapp.com/attachments/800205891365371915/808932957683318804/eunji_2.gif",
            "https://giphy.com/gifs/0vFsUFprMMN3SodOCn",
            "https://tenor.com/view/apink-girl-group-sing-music-kpop-gif-5669042",
            "https://tenor.com/view/apink-eunji-gif-18881046",
            "https://64.media.tumblr.com/0e0ab1a0bc637d3ed0d9ed70162cec81/tumblr_pj462phOly1tj2lfbo1_250.gif",
            "https://64.media.tumblr.com/b895cf04253657a1aab78402bd9d4835/b50f2e3cfac1c29e-77/s250x400/93c55c760f462e28a3a45dc844e81d602d57f9ac.gif",
            "https://64.media.tumblr.com/560d44188ecf986376bcd0ee3bbb08f8/tumblr_pla6d9BB581y0ir8uo3_250.gif",
            "https://64.media.tumblr.com/7f2f5e46bd4b703fad23fa031978a957/0b517273314f4dfd-d2/s400x600/bdbeb683dab873a25476e76a82d2a622fe2c0d7c.gif",
            "https://64.media.tumblr.com/9d7216feeb31845a2a7c9d06fc2b9dd2/0b517273314f4dfd-58/s400x600/b234f6c0972ffb3f843f4fb4efc5e2f6bbe451ca.gif",
            "https://64.media.tumblr.com/f5e51b2234e8f368bb43470621ba9a36/tumblr_plaksj2CEN1r3hdhfo3_r1_250.gif",
            "https://64.media.tumblr.com/beb9d4191d0ffc29f4f1668fdd09eda0/9ee34cc60937c184-e0/s250x400/ddf68d730ea946d44334972b58a37663d9a0fa34.gif",
            "https://64.media.tumblr.com/4376169717ab3b8c8dbb6883a9866789/1aa4e275cf310306-4c/s400x600/e35c6c3a51d4b8a8800a4d6150c4688089f60454.gif",
            "https://64.media.tumblr.com/0b280d8a1302f12e56782486a23ff595/tumblr_pcg51qMYDj1tjypkvo2_250.gif",
            "https://64.media.tumblr.com/c1bdadf1685ce547986d1ab819de077e/tumblr_pc0sngysuJ1tjypkvo2_250.gif",
            "https://64.media.tumblr.com/182b7c18a5fb2b37faf1e561cf0e44e5/tumblr_pkyjdtExOw1uqmda6o3_400.gif",
            "https://64.media.tumblr.com/ee5fc5d9ea64d9bd3260b4257b1b8306/tumblr_pcvkeqpQhl1vjftjjo1_250.gif",
            "https://64.media.tumblr.com/90ddab76cf42a60c6117239541598ba7/tumblr_p64sxtGSm61rhz16go1_250.gif",
            "https://64.media.tumblr.com/d5afb6ee75c7304928e4da9950b443f2/tumblr_p64sxtGSm61rhz16go3_250.gif"]

        self.bot.apink_hayoung_gif = ["https://tenor.com/view/hayoung-shrug-idgaf-not-my-problem-not-my-business-gif-10589324",
            "https://tenor.com/view/hayoung-apink-hayoung-apink-gif-18814544",
            "https://64.media.tumblr.com/5d55d7250d55a3b78aefa02a85a2672d/tumblr_pbti2xLH7g1ui9s1qo2_250.gif",
            "https://64.media.tumblr.com/56838a734084f8d7d297fb494811469e/tumblr_pbti2xLH7g1ui9s1qo3_r1_250.gif",
            "https://64.media.tumblr.com/238cee244ca932fa7dec9f6f3d24edd6/tumblr_pl8topcca01y0ir8uo3_250.gif",
            "https://64.media.tumblr.com/0c1193d049cf76797d75029a9e1498ca/tumblr_pb9824WL1R1v8cwg0o1_250.gif",
            "https://64.media.tumblr.com/60f43de82e82c9fc15373ab5cfff8eda/b50f2e3cfac1c29e-4d/s250x400/77460a7aadac4bd6c61187031363f05c6a1c20dd.gif",
            "https://tenor.com/view/hayoung-hayoung-apink-apink-gif-18814739",
            "https://64.media.tumblr.com/91626d29100d767142185a8431e9185b/c7d2c9d19daf33be-48/s250x400/cd32ab388b44d7749dcc2e8a7314f7ed32d6dd40.gif",
            "https://64.media.tumblr.com/4cbb029c2d2708bdababaa0c772041c5/c7d2c9d19daf33be-89/s250x400/718006fd3849db92dbbd255eb1e16387df6fe392.gif",
            "https://64.media.tumblr.com/53c49df83e8592cae62dfe7d6ea87064/tumblr_pwl81onkDs1xdglqzo4_250.gif",
            "https://64.media.tumblr.com/7a976e6cc7c42b3fc89f8cbcef6731a4/0506204366eb0deb-bf/s250x400/9087b725c77af0eeff29c397639546efd706af84.gif",
            "https://64.media.tumblr.com/6bed2f863899d3cd252b256826e7c03d/65710eedc8f711eb-fc/s250x400/f2d2c0f83ad2a5d1aa0141c64a75d324ba90b5b3.gif",
            "https://64.media.tumblr.com/25b99c419e636d2e5e1d6841bc677930/tumblr_pbch5r5iRJ1uqmda6o3_400.gif",
            "https://64.media.tumblr.com/6719eb3128e786152759b270f5003b60/4d429b2732a6a2f1-58/s250x400/72c26afb5391c4901e8482ba0365f6dbd17ea5d9.gif"]

        self.bot.apink_naeun_gif = ["https://tenor.com/view/naeun-apink-gif-18574437",
            "https://tenor.com/view/apink-son-naeun-nhicatung-kpop-korean-gif-5486987",
            "https://64.media.tumblr.com/c1934f7688d0c0656e6f5ee46b5f38e0/tumblr_pc9rtcuwgX1tj2lfbo3_250.gif",
            "https://64.media.tumblr.com/f12fdaf26b03b6da3707a4c23a8603c7/tumblr_pc9rtcuwgX1tj2lfbo2_250.gif",
            "https://64.media.tumblr.com/f4cdef238fcddde5e85cf4244860f456/1aa4e275cf310306-46/s400x600/909aef1616c14a6e23670524a7633c34ffb4f1c9.gif",
            "https://64.media.tumblr.com/295d4bef324388526151034057fb4b05/tumblr_pcofgcg3fG1r9f1l9o3_250.gif",
            "https://64.media.tumblr.com/90362776482ed8b1537cfe54d8364241/tumblr_pl72h4qCOe1r3hdhfo1_r1_250.gif",
            "https://64.media.tumblr.com/f4d6b247b22972e87025c5c5fd639a0c/7bc3e9c9873b828b-5d/s250x400/fa27e67dfa124bb2cbda16d4f0cd59cfa1f71300.gif",
            "https://64.media.tumblr.com/ed0898fe9540a52b5b33b255bbf4fbe6/tumblr_pkyh6y4Shm1uqmda6o1_400.gif",
            "https://64.media.tumblr.com/f4f51fd0848c93db2333183ee93c088a/tumblr_pkh0r4Gqhf1s2vcg0o3_250.gif",
            "https://64.media.tumblr.com/ffaa2e3b952d1a6a46fe033312d3ada8/tumblr_pe0cdnc1Ux1tj2lfbo5_250.gif",
            "https://64.media.tumblr.com/579fe53e34951b4a99f627e2e93f3f84/tumblr_ptft5v0k6l1ui9s1qo1_r1_250.gif",
            "https://64.media.tumblr.com/87e19b38cb757705ec452b13b64e887e/tumblr_p7g6xrBlHb1uqmda6o3_r2_250.gif",
            "https://64.media.tumblr.com/f836670a86fbe377da4530c5c111f864/tumblr_po8sbx87Yy1ui9s1qo2_250.gif",
            "https://64.media.tumblr.com/b0c68bc58a58baf364c3a8affcd5d4fa/tumblr_po8sbx87Yy1ui9s1qo1_250.gif",
            "https://tenor.com/view/naeun-apink-kpop-sexy-white-gif-7708243"]

        self.bot.apink_namjoo_gif = ["https://tenor.com/view/apink-kim-namjoo-k-pop-korean-gif-10024790",
            "https://tenor.com/view/namjoo-apink-oop-and-i-oop-namjoo-cover-mouth-gif-19379187",
            "https://64.media.tumblr.com/d9887526832bf609edf5221cd520663d/8d086cffd945cefe-ed/s250x400/167ec6d90841e5ec94b42ef4a44f09e0eaa68a36.gif",
            "https://64.media.tumblr.com/68af8ff34f20347eaaa89702e960bfdc/1aa4e275cf310306-9b/s400x600/9631045ed773b2cbc5a078846a757e69dceb1ffa.gif",
            "https://64.media.tumblr.com/3ea9106e1182daaf780b21c1071398dc/8d086cffd945cefe-15/s250x400/327a87f1499249e39181d277b07c3aec51ad91d2.gif",
            "https://64.media.tumblr.com/4598b877f2065a1c5801c27c70fd7777/7b28403c33e1a681-b2/s400x600/5ec517d3d07f36f06b648fe65ad2458af09b776f.gif",
            "https://64.media.tumblr.com/71472056960ce79fd034df974548a9ce/c264df28891ab678-68/s250x400/ff26a0be0142e6c035a4820d8782a1b7de5e805a.gif",
            "https://64.media.tumblr.com/971b656d451cc86322041429d94e844c/5adb8e6d2fb15a89-cd/s250x400/0af77f8de0572a18c8ff1f0261406f24dcf7e1dc.gif",
            "https://64.media.tumblr.com/40dec0b4645782d81bba5ddf9dc31351/1e6f513c54301cdf-6d/s250x400/795743708cda73adb21c2733eabaa47797066f12.gif",
            "https://64.media.tumblr.com/639d0f23496483f74975eeebf7b6d8ef/1e6f513c54301cdf-ed/s250x400/05e205454c6cc2d46457e629a3b335d2cac4f39e.gif",
            "https://64.media.tumblr.com/daed4fc3c09c735bbbe999cbf3241845/f9acf2a8326e581f-b6/s400x600/df38f7338cb526890802ba11e351d2b5539fa58f.gif",
            "https://64.media.tumblr.com/f13cd4b8a94b6cc6348416bc9d6db0f7/b50f2e3cfac1c29e-cb/s250x400/6651101b6b305e1f6a07afda3930d808e600a952.gif",
            "https://64.media.tumblr.com/7195d7314fe311ef8a0bf1646ee01e0f/1eef5da31cda2a7b-83/s250x400/d089fe5fe7c3614c2f0fe1b967752e561492b272.gif",
            "https://64.media.tumblr.com/09c7f567209e25029962662379f740aa/tumblr_pbe0x9v2Qf1qg5nyao4_r2_250.gif",
            "https://64.media.tumblr.com/965d2a23f9e59bde7d08703365f526f4/2fff8d4018c3a2bd-d7/s400x600/cb8fb71b679a6c561e20c03e6470ee823d4e97d6.gif"]
    #. Dreamcatcher
        self.bot.dreamcatcher_jiu_gif = ["https://tenor.com/view/onex-1x-jiu-hawt-kim-minji-hawt-jiu-gif-18812596",
            "https://cdn.discordapp.com/attachments/771238115255255060/785294061996605470/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/785294063871721472/image3.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506214181896230/FreshAnimatedGrizzlybear-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506140445114408/9060e6f5755986b8bad6707d28f55649.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800508431282470952/original_4.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800509445779882014/MediocreNegligibleBlacknorwegianelkhound-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800509989127061544/o6MpBX.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513124603920414/BossyForkedCreature-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513181625352192/tenor_10.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513274918469662/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513325955284992/e2b8b6fa04a1bf097c86b109517b57eb782bfdc9_hq.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513381790515210/c4ac99d86111b96375050c1677352adaf58e39ff.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513440396869652/NauticalGranularBufeo-small.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513493702541323/original_1.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513585008214026/tenor_8.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513755678900224/tumblr_a357a008e837857bf59e87b82d20876b_21f50875_250.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513826377695262/tumblr_061717b27912f6ef3d1a15c86aea2f54_8b77746a_540.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513877405073438/tenor-2.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513938458542110/tumblr_op8ssqIAi81tmc4fuo1_400.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800514030656553000/tumblr_okcn65yiNA1ue8w9eo1_400.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800514172197666856/a809c032f560b7c8563bdf59d6dcac1d9eb3bb91.gif"]

        self.bot.dreamcatcher_dami_gif = ["https://tenor.com/view/dreamcatcher-%EB%93%9C%EB%A6%BC%EC%BA%90%EC%B3%90-dami-cute-dance-gif-12255241",
            "https://tenor.com/view/dami-dreamcatcher-dcboca-gif-18178539",
            "https://tenor.com/view/dreamcatcher-dami-gif-18622933",
            "https://tenor.com/view/dreamcatcher-dami-full-moon-dreamcatcher-dami-arrow-gif-18971647",
            "https://tenor.com/view/lee-yubin-dami-dreamcatcher-meemoy-boca-gif-18893268",
            "https://tenor.com/view/dami-zombie-dreamcatcher-lee-yubin-boca-gif-18882718",
            "https://tenor.com/view/dami-dreamcatcher-boca-dc-dcboca-gif-18201110",
            "https://tenor.com/view/dreamcatcher-cute-yoohyeon-dami-gif-12143809",
            "https://tenor.com/view/dami-kwave-sexy-dance-dreamcatcher-gif-12249892",
            "https://tenor.com/view/dami-dami-dreamcatcher-dreamcatcher-dance-gif-13832007",
            "https://tenor.com/view/dreamcatcher-dami-lee-yoobin-kpop-pretty-gif-15563905",
            "https://tenor.com/view/dami-dami-dreamcatcher-dreamcatcher-cute-smile-gif-13831991",
            "https://tenor.com/view/dreamcatcher-dami-lee-yubin-main-rapper-lead-dancer-gif-17558548",
            "https://tenor.com/view/dami-dami-dreamcatcher-dreamcatcher-sexy-dance-gif-13832025",
            "https://tenor.com/view/dami-dreamcatcher-boca-dcboca-dc-gif-18229330",
            "https://tenor.com/view/dreamcatcher-su-a-kim-bora-dami-havana-gif-12130542",
            "https://tenor.com/view/dreamcatcher-su-a-kim-bora-dami-havana-gif-12130543",
            "https://tenor.com/view/dream-catcher-kpop-girl-group-piri-insomnia-gif-16831355",
            "https://tenor.com/view/king-kong-dreamcatcher-dami-lee-yubin-main-rapper-gif-15879177",
            "https://tenor.com/view/kpop-dream-catcher-dami-chewing-gif-15563908",
            "https://tenor.com/view/dreamcatcher-dami-lee-yoobin-kpop-pretty-gif-15563904",
            "https://tenor.com/view/dream-catcher-lee-yubin-cute-dami-kpop-gif-17900509",
            "https://tenor.com/view/dami-dream-catcher-cute-wave-kpop-gif-15515589",
            "https://tenor.com/view/dami-dreamcatcher-smile-happy-cute-gif-11972846",
            "https://tenor.com/view/dami-dreamcatcher-boca-dcboca-kpop-gif-18229558",
            "https://tenor.com/view/dami-dreamcatcher-boca-dcboca-kpop-gif-18229536",
            "https://tenor.com/view/dreamcatcher-dami-lee-yubin-main-rapper-lead-dancer-gif-17720409",
            "https://tenor.com/view/dreamcatcher-dami-lee-yubin-kpop-pretty-gif-15811393",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507388138094592/e1f635f10fdd9ee970a96f767392a0ee.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800509691888533565/e9e4ab22e4b8f52a38d5981b1b75ffc6.gif",
            "https://cdn.discordapp.com/attachments/795581963229462538/800511798431449099/50a753848cc3ebb4400b78043bca728801d1969b_hq.gif",
            "https://c.tenor.com/OL-V69yiM7gAAAAM/dami-dreamcatcher-odd-eye.gif",
            "https://cdn.discordapp.com/attachments/795581963229462538/812904983518248980/tumblr_ooo0obB0PF1wn1qbyo1_400.gif",
            "https://c.tenor.com/lXpUhmWLFSQAAAAM/dreamcatcher-red-sun.gif",
            "https://c.tenor.com/uLfVVTbKcIwAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/rPe6V0xFeeUAAAAM/dami-dreamcatcher.gif",
            "https://c.tenor.com/-Bq1AZ4hDxMAAAAM/dami-dreamcatcher.gif",
            "https://c.tenor.com/FRjG2-cNJd8AAAAM/dreamcatcher-%EB%93%9C%EB%A6%BC%EC%BA%90%EC%B3%90.gif",
            "https://thumbs.gfycat.com/AcrobaticHugeGordonsetter-max-1mb.gif",
            "https://i.pinimg.com/originals/a3/1d/ed/a31ded97432ccda2c7afb2376ab2b681.gif",
            "https://thumbs.gfycat.com/GlossyHopefulAmberpenshell-max-1mb.gif",
            "https://thumbs.gfycat.com/LittleSparklingChameleon-max-1mb.gif"]

        self.bot.dreamcatcher_gahyeon_gif = ["https://tenor.com/view/onex-1x-dreamcatcher-dreamcatcher-gahyeon-gahyeon-kiss-gif-18704085",
            "https://cdn.discordapp.com/attachments/795584752127311873/800511696837148692/0cabae4a0b98cd2e26eb345427b06a71.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800511398278725642/6de9c8d3afbd2726b0704a564872a2cb520f06c1.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800511277725646858/025260ecb02d38a465081e352ab48905.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800511176147730432/20145a59ad912ee0cd1953c7f30e527045c811f4r1-744-412_hq.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800510635116724254/AllDisfiguredAlaskanhusky-max-1mb.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800510565239881768/ggulbest_41-38.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800510489813712966/603ec6f2b5c15b1ea58f10f1b143c22a.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800510418731794472/YearlyGlumDeviltasmanian-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800510369445183528/151adfdb7d9eea18650426598180.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800510323903299604/original_2.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800509989127061544/o6MpBX.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800509840983851028/tenor_6.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800509691888533565/e9e4ab22e4b8f52a38d5981b1b75ffc6.gif"]

        self.bot.dreamcatcher_handong_gif = ["https://tenor.com/view/dreamcatcher-handong-gif-18881069",
            "https://cdn.discordapp.com/attachments/795585170974834728/800503987455524914/97ebb09a06e49b03cd687ede3b1f5d0e.gif",
            "https://cdn.discordapp.com/attachments/795584572405317683/800512953438830602/tumblr_omnvp00YI21vc5dxto1_500.gif",
            "https://tenor.com/view/handong-dreamcatcher-yoohyeon-hug-handong-dreamcatcher-gif-19121213",
            "https://tenor.com/view/handong-dreamcatcher-dreamcatcher-handong-gif-14876335",
            "https://tenor.com/view/handong-dreamcatcher-performance-dance-kpop-gif-17568347",
            "https://tenor.com/view/dream-catcher-handong-kpop-dongie-pose-gif-17305836",
            "https://tenor.com/view/handong-dreamcatacher-dongie-choke-gif-20128380",
            "https://c.tenor.com/em3WGxsqjDQAAAAM/dreamcatcher-handong.gif",
            "https://c.tenor.com/9RLWu36mhQIAAAAM/dreamcatcher-%EB%93%9C%EB%A6%BC%EC%BA%90%EC%B3%90.gif"]

        self.bot.dreamcatcher_siyeon_gif = ["https://tenor.com/view/dreamcatcher-siyeon-lee-siyeon-vocalist-kpop-gif-17254566",
            "https://cdn.discordapp.com/attachments/786714676506394654/800514172197666856/a809c032f560b7c8563bdf59d6dcac1d9eb3bb91.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800509445779882014/MediocreNegligibleBlacknorwegianelkhound-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506038264397824/eff2cf3317f8af127c647b7b91ec5f80a5eb3841.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800508665831620668/rep.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800508431282470952/original_4.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800508354044755988/AmusingNippyAyeaye-max-1mb.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800508225841659904/7e8de75c4c5329438fefe0c193b8043c.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800508154046578698/PleasantShyAnemonecrab-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507793970692156/GlisteningDentalAkitainu-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507737543802900/FarflungFantasticAfricanmolesnake-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507691516559380/tumblr_460bb80ebf2bb74f682300bffc29296b_9098afbc_400.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507636205486080/tumblr_ec92eca1315fc072017cb3a1de5c73ba_11b40bd2_500.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507591414382612/def0b0bac64dd7cc446e494acf83c758.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507553628028928/c4aa723c71b44cf7b2274b75597e42c7.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507503959212082/3b4e993c34068851caa30282abd68740.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507388138094592/e1f635f10fdd9ee970a96f767392a0ee.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507323546075167/tumblr_pz298hlbDc1rqb6hgo4_400.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507255593762819/b4de5eed6d285cf70435b46dc43f2761.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506140445114408/9060e6f5755986b8bad6707d28f55649.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506214181896230/FreshAnimatedGrizzlybear-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505747473301554/dreamcatcher-really-really-gif.gif",
            "https://c.tenor.com/nr_Pncn9h2AAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/0sxvsEr2BEsAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/6qn_z7OfX-cAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/3CmT25pvlPgAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/nawnuCOZYkwAAAAM/dreamcatcher-siyeon.gif",
            "https://c.tenor.com/hB70qco_w2cAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/Es9TtvIh1zwAAAAM/dream-catcher-si-yeon.gif",
            "https://c.tenor.com/ZBdvCI6LEVAAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/AsJcgiH8R1kAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/sEgCXWbtom4AAAAM/red-sun.gif",
            "https://c.tenor.com/VpNQGvpp_qQAAAAM/siyeon-sexy.gif",
            "https://c.tenor.com/UUsDGjc6VPMAAAAM/siyeon-clown-siyeon.gif",
            "https://c.tenor.com/pKHTsvaw4oYAAAAM/red-sun.gif",
            "https://c.tenor.com/BzB3vOwFX_gAAAAM/dreamcatcher-siyeon.gif",
            "https://c.tenor.com/8IYkj15x7r8AAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/sLLFyyWbJhcAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/Pl5VrsD7_gAAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/avMK9r819QcAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/D7l-HZhFMwoAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/C5bZW2o9M0MAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/wfzSmfZdRHQAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/SOnYhFq1rE4AAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/S2RbNaTonsAAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/O7gJfs1x02IAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/2cAF-17TceUAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/95sJElqjaMUAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/JUm3eLYrzlgAAAAM/siyeon-dreamcatcher.gif",
            "https://c.tenor.com/WD3Cuihv8z0AAAAM/siyeon-dreamcatcher.gif"]

        self.bot.dreamcatcher_sua_gif = ["https://tenor.com/view/dreamcatcher-dreamcatcher-sua-sua-sua-funny-look-around-gif-19331893",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505148002402344/7eae1402c662ce572a78374227c36adbd0cd2bea.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505310154063902/7d415f7c8e7591afd7811dc050dd1307.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505362964545556/fb621cde8599cbe403bb7805cd76ed2c4468c26e_hq.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505451984715807/0c2ba2e5eb17280c29f3baaad6efd557e589ed20_00.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505541452627998/98e8162b6405ba504659e3bb934306d1cb69612d.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505698009481216/dd01008a098143dbd16761cdf736bd1b.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505747473301554/dreamcatcher-really-really-gif.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800508225841659904/7e8de75c4c5329438fefe0c193b8043c.gif",
            "https://cdn.discordapp.com/attachments/795584572405317683/800512953438830602/tumblr_omnvp00YI21vc5dxto1_500.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800514172197666856/a809c032f560b7c8563bdf59d6dcac1d9eb3bb91.gif",
            "https://tenor.com/view/dreamcatcher-%EB%93%9C%EB%A6%BC%EC%BA%90%EC%B3%90-sua-dance-gif-12255205",
            "https://tenor.com/view/%EB%93%9C%EB%A6%BC%EC%BA%90%EC%B3%90-dreamcatcher-sua-kim-bora-gif-19962764",
            "https://tenor.com/view/dreamcatcher-sua-happy-smile-cheer-gif-19961384",
            "https://tenor.com/view/dreamcatcher-sua-shake-smile-gif-18573306",
            "https://tenor.com/view/dreamcatcher-sua-dance-dancing-gif-18573310",
            "https://tenor.com/view/dreamcatcher-sua-gif-18981876",
            "https://tenor.com/view/dreamcatcher-sua-angry-cloverfield-found-footage-gif-18573314",
            "https://tenor.com/view/dreamcatcher-sua-ji-u-annoyed-smile-gif-18573311"]

        self.bot.dreamcatcher_yoohyeon_gif = ["https://tenor.com/view/yoohyeon-dream-catcher-heart-shape-cute-kpop-gif-16952098",
            "https://tenor.com/view/yoohyeon-in-fear-yoohyeon-kim-yoohyeon-dreamcatcher-yoohyeon-dreamcatcher-gif-19500039",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513181625352192/tenor_10.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800510418731794472/YearlyGlumDeviltasmanian-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800509445779882014/MediocreNegligibleBlacknorwegianelkhound-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505747473301554/dreamcatcher-really-really-gif.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506297907806219/tumblr_p8ib2x5eOu1rqb6hgo1_r1_500.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506214181896230/FreshAnimatedGrizzlybear-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506140445114408/9060e6f5755986b8bad6707d28f55649.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506038264397824/eff2cf3317f8af127c647b7b91ec5f80a5eb3841.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800505015278108672/Yoohyeon-Yoohyeon-in-2019-Dream-catcher-Girl-group-.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800504883765444659/The-DreamCatcher-Thread-InJapan-Page-1624-Groups-.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800504782334853150/ggulbest_38-33.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800504671268503572/Dreamcatcher-Gif-Thread_-e_oeeSzes_el-allkpop-Forums.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800504561776984114/ba7019804d112e6e649bac4c09c09dbf.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800504498493325372/b7f7cebe82b631415bc3c4d2b6e14c38.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800504277146796103/77ac81500e0bf2af4bfcd472adb00763.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800504188906897418/AliveTotalIbadanmalimbe-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800503987455524914/97ebb09a06e49b03cd687ede3b1f5d0e.gif"]
    #. fromis_9
        self.bot.fromis_9_jisun_gif = ["https://gfycat.com/acrobaticadoredleafhopper-mechabear-fromis-kpop",
            "https://gfycat.com/arididolizeddugong-fromis-pretty-beauty-kpop-cute",
            "https://gfycat.com/biginconsequentialherculesbeetle-mechabear-fromis-kpop",
            "https://gfycat.com/affectionateimpishdamselfly-mechabear-fromis-kpop",
            "https://gfycat.com/briskfaithfulblueandgoldmackaw-mechabear-fromis-kpop",
            "https://gfycat.com/dimwittedvastblueandgoldmackaw-beauty",
            "https://gfycat.com/coolspicyamethystsunbird-mechabear-fromis-kpop",
            "https://gfycat.com/eachbaggygosling-mechabear-fromis-kpop",
            "https://gfycat.com/amusingcelebratedbuckeyebutterfly",
            "https://gfycat.com/apprehensiveearlygardensnake",
            "https://gfycat.com/dishonestbigheartedbinturong-mechabear-fromis-kpop",
            "https://gfycat.com/miserlymadalpinegoat-mechabear-fromis-kpop",
            "https://gfycat.com/chillyhoarseeider-mechabear-fromis-kpop",
            "https://gfycat.com/acidicdefiniteamericanbobtail-roh-jisun-fromis-9-kpop",
            "https://gfycat.com/likelyorganicatlanticblackgoby-mechabear-fromis-kpop",
            "https://gfycat.com/enviouscornycoral-mechabear-fromis-kpop",
            "https://gfycat.com/enchantedsmoggyflyingsquirrel-mechabear-fromis-kpop",
            "https://gfycat.com/considerateharshhyracotherium-mechabear-fromis-kpop",
            "https://gfycat.com/idealisticoddconey-mechabear-fromis-kpop",
            "https://gfycat.com/yellowishethicalfrillneckedlizard-mechabear-fromis-kpop",
            "https://gfycat.com/celebratedwellmadedwarfrabbit",
            "https://gfycat.com/blackrigidjuliabutterfly-mechabear-fromis-kpop",
            "https://gfycat.com/defiantserenedore-mechabear-fromis-kpop",
            "https://gfycat.com/craftyfalsebirdofparadise-mechabear-fromis-kpop"]

        self.bot.fromis_9_hayoung_gif = ["https://gfycat.com/alienatedcheapgalapagosmockingbird-song-hayoung-fromis-9-kpop",
            "https://gfycat.com/hideoushalfamurminnow",
            "https://gfycat.com/likelydrearyfallowdeer-hayoung-fromis",
            "https://gfycat.com/bronzeunhappycockroach-fromis-9-hayoung-saerom-kpop",
            "https://gfycat.com/achinghiddenislandcanary",
            "https://gfycat.com/plastichappyfugu",
            "https://gfycat.com/nextofficialbee-hayoung-fromis",
            "https://gfycat.com/rashuncommonhogget-fromis-9-hayoung-kpop",
            "https://gfycat.com/silkybothharrierhawk-fromis-9-hayoung-beauty",
            "https://gfycat.com/appropriatefittingcrow-fromis-9-hayoung-korean-kpop",
            "https://gfycat.com/firsthandjadedcowrie-fromis-9-hayoung-kpop",
            "https://gfycat.com/belovedmindlessastarte-fromis-9-hayoung",
            "https://gfycat.com/secondaryharmoniousannashummingbird",
            "https://gfycat.com/majesticgiantbird",
            "https://gfycat.com/defensiveearlydunlin",
            "https://gfycat.com/negligiblespanishbelugawhale-fromis-9-hayoung",
            "https://gfycat.com/afraidfortunateeastsiberianlaika",
            "https://gfycat.com/grippingaggressiveleafcutterant",
            "https://gfycat.com/oldfashioneddisastrousiberianbarbel",
            "https://gfycat.com/cheapagitateddarklingbeetle-fromis-kpop",
            "https://gfycat.com/belatedbelatedalaskanhusky",
            "https://gfycat.com/educatedoddballaddax-elope",
            "https://gfycat.com/jointcheerfulelver-elope",
            "https://gfycat.com/spiffymelodicleopard-pole-dancing-exercise-hayoung-fromis-beauty-kpop",
            "https://gfycat.com/unpleasantbestcougar",
            "https://gfycat.com/blackandwhitepersonalequine-hayoung-fromis-gyuri-jiwon",
            "https://gfycat.com/deliciouscarefreeclingfish-fromis-9-hayoung",
            "https://gfycat.com/jauntycaringamoeba",
            "https://gfycat.com/animatedlimitedgalapagospenguin",
            "https://gfycat.com/scornfulobesearizonaalligatorlizard"]

        self.bot.fromis_9_saerom_gif = ["https://gfycat.com/arcticimpuredutchsmoushond-fromis-saerom-190727",
            "https://gfycat.com/bothvacanthypacrosaurus",
            "https://gfycat.com/advancedvariablecrocodile-mechabear-fromis-saerom-kpop",
            "https://gfycat.com/angelicobviousbushbaby",
            "https://gfycat.com/afraidmindlessbighorn-mechabear-fromis-saerom-kpop",
            "https://gfycat.com/academicimpassionedcheetah-fromis-saerom-190608",
            "https://gfycat.com/carelessamusinghoneybee-flying-yoga-mechabear-excersice-fromis-health",
            "https://gfycat.com/breakablebackfoxterrier-mechabear-fromis-saerom-kpop",
            "https://gfycat.com/calmlimpchuckwalla-mechabear-saerom-fromis-kpop",
            "https://gfycat.com/majorsardonicaffenpinscher",
            "https://gfycat.com/alarmingnexthoneycreeper",
            "https://gfycat.com/antiquehastyantelopegroundsquirrel-saerom-fromis-pretty-beauty-cute-kpop-blue",
            "https://gfycat.com/agitateddeterminedjapanesebeetle-fromis-kpop-cute",
            "https://gfycat.com/bowedfearlessharvestmouse-beauty",
            "https://gfycat.com/illpinkindochinahogdeer-fromis-nine-petsweat-kiss-kpop-hug",
            "https://gfycat.com/adoredethicalcobra-fromis-9-saerom-kpop",
            "https://gfycat.com/accomplishedcomposeddeinonychus-mechabear-saerom-fromis-kpop",
            "https://gfycat.com/brownwindingkitty-fromis9-saerom-kuro-gurokami-lee-saerom-romsae",
            "https://gfycat.com/affectionatewebbedjunebug-fromis-9-romsae-lee-saerom-idol-kpop",
            "https://gfycat.com/smoothadeptjaeger-fromis-9-saerom-korean-kpop",
            "https://gfycat.com/aggravatinglimpamericanriverotter-fashion-saerom-fromis-pretty-beauty-cute-kpop-blue",
            "https://gfycat.com/glitteringexaltedbluewhale-fromis9-saerom-kuro-gurokami-lee-saerom-romsae",
            "https://gfycat.com/acidicflashycorydorascatfish",
            "https://gfycat.com/actualuntriedinganue-popular-saerom-fromis-pretty-beauty-kpop-cute",
            "https://gfycat.com/barrenorangebobcat-mechabear-fromis-kpop",
            "https://gfycat.com/barrencloudykingsnake-mechabear-saerom-fromis-kpop",
            "https://gfycat.com/eminentneatgraywolf-fromis9-saerom-kuro-gurokami-lee-saerom-romsae",
            "https://tenor.com/view/saerom-lee-saerom-fromis-fromis_9-gif-19168566",
            "https://tenor.com/view/saerom-fromis-fromis_9-lee-saerom-gif-20461253",
            "https://tenor.com/view/applying-makeup-fromis-fromis_9-lee-saerom-saerom-gif-20375930",
            "https://tenor.com/view/fromis-fromis9-saerom-lee-saerom-gif-20283180",
            "https://tenor.com/view/fromis-fromis_9-saerom-lee-saerom-gif-20000869",
            "https://tenor.com/view/fun-fromis9-kpop-lee-sae-rom-saerom-gif-14743546",
            "https://tenor.com/view/fromis_9-saerom-romsae-lee-saerom-f9-gif-18288045",
            "https://tenor.com/view/saerom-fromis9-saying-hello-posing-gif-14634603",
            "https://tenor.com/view/saerom-fromis_9-gif-18669517",
            "https://tenor.com/view/saerom-gif-20443499",
            "https://tenor.com/view/lee-saerom-saerom-fromis-fromis_9-gif-20416936"]

        self.bot.fromis_9_chaeyoung_gif = ["https://gfycat.com/adorablethornyflee-fromis9-chaeyoung-lee-chaeyoung-kuro-gurokami",
            "https://gfycat.com/dimpleduniquekillerwhale-mechabear-fromis-kpop",
            "https://gfycat.com/dopeytepidblacklab-chaeyoung-mechabear-fromis-kpop",
            "https://gfycat.com/creepyposhjackal-fromis9-chaeyoung-lee-chaeyoung-fromis-9-idol",
            "https://gfycat.com/emotionalwhichbeardedcollie",
            "https://gfycat.com/finisheddetailedgonolek-mechabear-fromis-kpop",
            "https://gfycat.com/emptyspryenglishsetter-mechabear-fromis-kpop",
            "https://gfycat.com/admiredveneratedblackbear-mechabear-fromis-kpop-cute",
            "https://gfycat.com/ambitiousheartybooby-fromis-fromis9-fromis9-fun-funfactory",
            "https://gfycat.com/dirtykeycomet-mechabear-fromis-kpop",
            "https://gfycat.com/emotionalplaindotterel-fromis-beauty-kpop-cute",
            "https://gfycat.com/elasticdelayedcamel-mechabear-fromis-kpop",
            "https://gfycat.com/adeptachinghartebeest-chaeyoung-mechabear-fromis-kpop",
            "https://gfycat.com/distinctrealgosling-mechabear-chaeyoung-fromis-kpop",
            "https://gfycat.com/alienatedalarmedleopardseal",
            "https://gfycat.com/ashamedsoupyboa-mechabear-chaeyoung-fromis-kpop",
            "https://gfycat.com/anothersmugadouri-mechabear-fromis-kpop",
            "https://gfycat.com/amazingwiltedbadger-mechabear-fromis-kpop",
            "https://gfycat.com/uglyshowyflicker-chaeyoung-mechabear-squirrel-fromis",
            "https://gfycat.com/unknownembellishedacornbarnacle-mechabear-chaeyoung-fromis-kpop",
            "https://gfycat.com/villainousdazzlingdrever-mechabear-fromis-kpop",
            "https://gfycat.com/weakreasonableasp-chaeyoung-fromis-beauty-cute-kpop",
            "https://gfycat.com/warpeddamagedcreature-mechabear-fromis-kpop",
            "https://gfycat.com/wellgroomedshockinghamster-mechabear-fromis-kpop",
            "https://gfycat.com/ashamedhastyamericanwarmblood-mechabear-fromis-kpop",
            "https://gfycat.com/bountifulscentedalbatross-beauty",
            "https://gfycat.com/zanygorgeousicefish-chaeyoung-fromis-9-kpop",
            "https://gfycat.com/smallrealisticcleanerwrasse-chaeyoung-fromis-9-korean-kpop",
            "https://gfycat.com/gleamingflippantindochinesetiger-fromis-9-beauty",
            "https://gfycat.com/impolitejealoushectorsdolphin",
            "https://gfycat.com/emotionalplaindotterel-fromis-beauty-kpop-cute",
            "https://gfycat.com/adepthardtofindairedale"]

        self.bot.fromis_9_nakyung_gif = ["https://gfycat.com/aromaticwillingcricket-mechabear-nakyung-fromis-kpop",
            "https://gfycat.com/acceptablevaguehorsechestnutleafminer-mechabear-nakyung-fromis-kpop",
            "https://gfycat.com/amusinguniformflyingfox-mechabear-fromis-kpop",
            "https://gfycat.com/darlingdistinctfairybluebird",
            "https://gfycat.com/bonynauticalclingfish-fromis-9-nakyung-kpop-beauty",
            "https://gfycat.com/daringamusingdamselfly-fromis-9-nakyung-salsa-2",
            "https://gfycat.com/brightunawarejabiru",
            "https://gfycat.com/diligentmenacingalabamamapturtle-nakyung-fromis",
            "https://gfycat.com/darkcraftygarpike-nakyung-fromis",
            "https://gfycat.com/cooperativesandycondor-nakyung-fromis",
            "https://gfycat.com/elderlysleepyimperialeagle-nakyung-fromis",
            "https://gfycat.com/reliableuncomfortablecanadagoose-fromis9-fromis-9-nakyung-aegyo-cute",
            "https://gfycat.com/blushinghiddenindianskimmer-fromis-9-nakyung",
            "https://gfycat.com/jaggedunnaturalfrilledlizard-fromis9-nakyung-kpop",
            "https://gfycat.com/menacingadmiredlemming",
            "https://gfycat.com/friendlyamusedgalapagosalbatross-nakyung-fromis",
            "https://gfycat.com/alarmedhiddenalbino-mechabear-fromis-kpop",
            "https://gfycat.com/oldfashionedslushychinesecrocodilelizard-mechabear-fromis-kpop",
            "https://gfycat.com/appropriateaffectionatecoypu",
            "https://gfycat.com/uniformyellowcusimanse-mechabear-fromis-kpop",
            "https://gfycat.com/consideratehappygoluckybirdofparadise-nakyung-fromis",
            "https://gfycat.com/daringamusingdamselfly-fromis-9-nakyung-salsa-2",
            "https://gfycat.com/enlightenednaughtydipper-mechabear-fromis-kpop",
            "https://gfycat.com/floweryscientifichoverfly-beautiful-nakyung-fromis-pretty-kpop"]

        self.bot.fromis_9_jiwon_gif = ["https://gfycat.com/darlingacceptableapisdorsatalaboriosa",
            "https://gfycat.com/famoushotitalianbrownbear-fromis9-jiwon",
            "https://gfycat.com/acrobaticbrilliantairedale",
            "https://gfycat.com/adoredvigorouseyra",
            "https://gfycat.com/adeptwellwornbrant",
            "https://gfycat.com/responsibledistanthorsechestnutleafminer-fromis9-jiwon",
            "https://gfycat.com/bruiseddrearychimneyswift-channel9-fromis9-fm1-24-jiwon-kpop",
            "https://gfycat.com/corruptclearborer",
            "https://gfycat.com/windyarcticangelwingmussel",
            "https://gfycat.com/equalhideousarctichare",
            "https://gfycat.com/poshgloriousinvisiblerail",
            "https://gfycat.com/heartfeltunfoldedbushbaby-fromis9-jiwon",
            "https://gfycat.com/inferiorwelltodobobolink-stage-mix-fromis9-jiwon-kpop-fun",
            "https://gfycat.com/paltrycaringcarp-fromis9-jiwon",
            "https://gfycat.com/acceptablescarcedungbeetle",
            "https://gfycat.com/scalyallarrowcrab-fromis-9-jiwon",
            "https://gfycat.com/infantileimpeccablehammerkop-chaeyoungs-challenge-channel-9-love-bomb",
            "https://gfycat.com/decentreadyalaskanhusky-park-jiwon-fromis9-flover-megan-kpop",
            "https://gfycat.com/miniaturenervousislandcanary-fromis9",
            "https://gfycat.com/klutzyemptyblackfly",
            "https://gfycat.com/anothersnappyfieldmouse",
            "https://gfycat.com/anybitesizedleafbird-fromis-9-jiwon",
            "https://gfycat.com/fearfulperiodicfrogmouth-fromis-9-jiwon-beauty",
            "https://gfycat.com/jollywaterloggedarcherfish"]

        self.bot.fromis_9_seoyeon_gif = ["https://gfycat.com/ajarkeencorydorascatfish",
            "https://gfycat.com/absolutemasculinegalapagoshawk-beauty",
            "https://gfycat.com/agilegleefulestuarinecrocodile-mechabear-fromis-kpop",
            "https://gfycat.com/verifiableidlebluebreastedkookaburra-beautiful-seoyeon-fashion-fromis-makeup-black-dark",
            "https://gfycat.com/ecstaticplaintivechanticleer",
            "https://gfycat.com/wellgroomedimmaculateafghanhound-seoyeon-fromis-kpop",
            "https://gfycat.com/bossyaffectionateflicker-beauty",
            "https://gfycat.com/bossyfakeblackrussianterrier-mechabear-fromis-kpop",
            "https://gfycat.com/heartfeltlonelykite-mechabear-fromis-kpop",
            "https://gfycat.com/cheerfulpleasedarcherfish-beauty",
            "https://gfycat.com/compassionateellipticalhog-fromis-pretty-beauty-kpop-cute",
            "https://gfycat.com/incomparableorneryinsect-seoyeon-fromis-kpop",
            "https://gfycat.com/sanedaringachillestang-seoyeon-fromis-kpop",
            "https://gfycat.com/frigiddismalbrant-fromis-9-seoyeon-korean-kpop",
            "https://gfycat.com/malehelplessadeliepenguin-beauty",
            "https://gfycat.com/grandiosequestionablechameleon-seoyeon-fromis",
            "https://gfycat.com/oblongfortunateanemone",
            "https://gfycat.com/edibleshinydoe-fromis-9-seoyeon-jisun",
            "https://gfycat.com/latefemalefrigatebird",
            "https://gfycat.com/nippyadoreddartfrog-fromis-9-seoyeon-jiheon",
            "https://gfycat.com/genuinedeterminedgoat-fromis9",
            "https://gfycat.com/educatedshockingchanticleer-beauty",
            "https://gfycat.com/allshowyitaliangreyhound-fromis9"]

        self.bot.fromis_9_jiheon_gif = ["https://gfycat.com/alertfaroffleopardseal",
            "https://gfycat.com/palatableadolescentitaliangreyhound",
            "https://gfycat.com/negligiblebrightbelugawhale-elope",
            "https://gfycat.com/talljollydunlin",
            "https://gfycat.com/desertedregularhalibut-fromis-jiheon",
            "https://gfycat.com/circularheavyarrowworm-fromis-jiheon",
            "https://gfycat.com/waterywideeyedcaracal",
            "https://gfycat.com/hardshadygypsymoth-jiheon-fromis-baek",
            "https://gfycat.com/hastyshabbycrow-jiheon-fromis-baek",
            "https://gfycat.com/electricmildgreatwhiteshark-jiheon-baek",
            "https://gfycat.com/safematuredungenesscrab-jiheon-baek",
            "https://gfycat.com/hideousshimmeringeagle-fromis-9-salsa-13-jiheon",
            "https://gfycat.com/secondarypolishedasianpiedstarling-jiheon",
            "https://gfycat.com/clearpessimisticemeraldtreeskink-fromis",
            "https://gfycat.com/defenselesscostlyeel-fromis",
            "https://gfycat.com/famoushilariousgenet-fromis",
            "https://gfycat.com/gleefulhugegrouse-fromis",
            "https://gfycat.com/limpingcompassionatebird-fromis",
            "https://gfycat.com/livelytallgiantschnauzer-fromis",
            "https://gfycat.com/obesegraciousfreshwatereel-fromis",
            "https://gfycat.com/minorchillybison-fromis",
            "https://gfycat.com/nextunkemptabyssiniancat-fromis",
            "https://gfycat.com/rareunhealthyindianelephant-fromis",
            "https://gfycat.com/simplewarmhoneybadger-fromis",
            "https://gfycat.com/ablevillainouseland-fromis-jiheon-baek",
            "https://gfycat.com/oddfrigidfly-fromis",
            "https://gfycat.com/masculinecostlyirishredandwhitesetter",
            "https://gfycat.com/saltyuniformchinesecrocodilelizard-baek-jiheon-beautiful-fromis-kpop-cute",
            "https://gfycat.com/inferiorgratefulboutu-jiheon-baek",
            "https://gfycat.com/wavytastyamberpenshell-jiheon-baek",
            "https://gfycat.com/naughtyqualifiedleafhopper",
            "https://gfycat.com/smoggyembellishedkinkajou",
            "https://gfycat.com/melodicsimilardormouse-baek-jiheon",
            "https://gfycat.com/smoggypleasedcatfish-baek-jiheon",
            "https://gfycat.com/enormousvapidfinnishspitz-fromis-fromis9-fromis9-fun-funfactory"]

        self.bot.fromis_9_gyuri_gif = ["https://gfycat.com/ableesteemedangwantibo-beauty",
            "https://gfycat.com/messypartialbarnswallow",
            "https://gfycat.com/flashyglaringgoa-gfycat-approve-pls-thanksss-fromis-beauty-gyuri",
            "https://gfycat.com/barequestionableintermediateegret-mechabear-fromis-gyuri-kpop",
            "https://gfycat.com/gleefulslightamericanredsquirrel",
            "https://gfycat.com/cluelessfrankhalicore",
            "https://gfycat.com/thornyyoungarcticduck-jang-gyuri-fromis-9-200507-flover-vlive",
            "https://gfycat.com/gleefulthirstyamurratsnake-mechabear-fromis-kpop",
            "https://gfycat.com/opulentwellwornassassinbug-mechabear-fromis-kpop",
            "https://gfycat.com/severalcooperativeicelandgull",
            "https://gfycat.com/thosebabyishbunting-fromis-beauty-kpop",
            "https://gfycat.com/unlinedlonghuia",
            "https://gfycat.com/frigidinsecuredevilfish",
            "https://gfycat.com/possiblerightbluefintuna",
            "https://gfycat.com/sphericalalienatedhumpbackwhale",
            "https://gfycat.com/conventionalamusinglaughingthrush-mechabear-fromis-gyuri-kpop",
            "https://gfycat.com/dazzlingdiligentdodobird-fromis-9-gyuri",
            "https://gfycat.com/frankwarmheartedfrenchbulldog-fromis9-gyuri-kuro-gurokami-jang-gyuri-fromis-9",
            "https://gfycat.com/darlingserenealligator-fromis9-gyuri-kuro-gurokami-jang-gyuri-fromis-9",
            "https://gfycat.com/generousvengefulaquaticleech",
            "https://gfycat.com/simplisticneighboringduckbillplatypus",
            "https://gfycat.com/adorableecstaticcuttlefish",
            "https://gfycat.com/accomplishedquerulousimperatorangel-fromis9-gyuri",
            "https://gfycat.com/belatedunevenlemming-fromis9",
            "https://gfycat.com/flippantconfusedblackbear-beauty",
            "https://gfycat.com/barrenconsiderateasiandamselfly-produce-48-fromis-9-gyuri-jang-kpop",
            "https://gfycat.com/alienatedaccurategreendarnerdragonfly-beauty",
            "https://gfycat.com/biodegradablenauticalangelfish-beauty",
            "https://gfycat.com/hideousblandcrayfish-fromis-9-gyuri",
            "https://gfycat.com/repentantseverecopperbutterfly",
            "https://gfycat.com/diligentfoolhardyblobfish",
            "https://gfycat.com/shamelessjadedarrowana",
            "https://gfycat.com/clumsyadventurousirishsetter-mechabear-fromis-gyuri-kpop"]
    #. Weki Meki
        self.bot.wekimeki_doyeon_gif = ["https://tenor.com/view/doyeon-wekimeki-gif-18867883",
            "https://cdn.discordapp.com/attachments/800224052312277003/800555413023752212/45071c5422735c1e97f162ec1cf15cbf.gif",
            "https://tenor.com/view/doyeon-wekimeki-gif-18867880",
            "https://tenor.com/view/cover-eyes-kim-doyeon-doyeon-weki-meki-kpop-gif-17688928",
            "https://tenor.com/view/doyeon-cry-produce101-hurt-kpop-gif-10276415",
            "https://tenor.com/view/kim-doyeon-hair-flip-ioi-flirt-smile-gif-9869521",
            "https://tenor.com/view/kpop-dazzle-weki-meki-kim-doyeon-music-video-gif-16419083",
            "https://tenor.com/view/kim-doyeon-gif-19253844",
            "https://tenor.com/view/doyeon-kim-doyeon-weki-meki-weki-meki-doyeon-doyeon-weki-meki-gif-20108425",
            "https://tenor.com/view/doyeon-gif-9952856",
            "https://tenor.com/view/%EA%B9%80%EB%8F%84%EC%97%B0-gif-18181702",
            "https://tenor.com/view/doyeon-wekimeki-cool-gif-18963359",
            "https://tenor.com/view/wekimeki-doyeon-gif-18847477",
            "https://tenor.com/view/wekimeki-doyeon-gif-18847492",
            "https://tenor.com/view/wekimeki-doyeon-gif-18908062",
            "https://tenor.com/view/doyeon-wekimeki-cool-gif-18963344",
            "https://tenor.com/view/doyeon-wekimeki-gif-10344450",
            "https://tenor.com/view/doyeon-wekimeki-gif-10344452",
            "https://tenor.com/view/doyeon-kim-wekimeki-gif-20189589",
            "https://tenor.com/view/doyeon-wekimeki-gif-18867880",
            "https://tenor.com/view/wekimeki-doyeon-tongue-gif-19035974",
            "https://tenor.com/view/doyeon-kim-wekimeki-gif-20189587",
            "https://i.makeagif.com/media/3-11-2019/YR44hN.gif",
            "https://i.pinimg.com/originals/fd/35/6c/fd356c6e00b289c7738bdd3e20ec654a.gif",
            "https://i.pinimg.com/originals/e6/58/14/e65814436e7d4776b51f0cb633c7c2bd.gif",
            "https://i.pinimg.com/originals/31/6c/53/316c534e04571ca36218417f6f3675ea.gif",
            "https://media.tenor.com/images/080204b8f6869ea45341343d0546a3ea/tenor.gif",
            "https://data.whicdn.com/images/320734667/original.gif",
            "https://78.media.tumblr.com/3b8d2fe9a2c8f83e91042aff47f2d066/tumblr_p4t2mbkSKq1x460sso2_400.gif",
            "https://p.favim.com/orig/2018/08/24/weki-meki-doyeon-gif-Favim.com-6185558.gif",
            "https://i.pinimg.com/originals/a6/01/5f/a6015fe39df91910633f190b99d497b3.gif",
            "https://gfycat.com/darkcarefreeargentinehornedfrog",
            "https://gfycat.com/enlighteneddizzyballoonfish-choiyoojung-kimdoyeon-weki-meki-jisuyeon",
            "https://gfycat.com/complexleancommongonolek-weki-meki-doyeon-kpop",
            "https://gfycat.com/calmfewhoneycreeper",
            "https://gfycat.com/apprehensivecookedamethystgemclam",
            "https://gfycat.com/beneficialblackandwhitekakarikis",
            "https://gfycat.com/tinyunfoldedfallowdeer-dazzle-dazzle-weki-meki-yoojung-doyeon",
            "https://gfycat.com/cheapplushbackswimmer",
            "https://gfycat.com/grandimmensedotterel",
            "https://gfycat.com/artisticillinformedgrayreefshark",
            "https://gfycat.com/lazydetailedamericanpainthorse-weki-meki-doyeon-kpop",
            "https://gfycat.com/bigheartedredalaskankleekai",
            "https://gfycat.com/smoothfrailibis",
            "https://gfycat.com/grandbraveechidna",
            "https://gfycat.com/alarmingboilingafricanaugurbuzzard-yoojung-doyeon-ioi",
            "https://gfycat.com/grossmindlessdwarfrabbit-yoojung-god-rap",
            "https://gfycat.com/illhotbarnowl",
            "https://gfycat.com/firstanimatedgrouse-weki-meki-mechabear-doyeon-kpop",
            "https://gfycat.com/grippingwarmheartedindochinesetiger-mechabear-weki-meki-doyeon-kpop",
            "https://gfycat.com/euphoricmessyleafhopper"]

        self.bot.wekimeki_elly_gif = ["https://tenor.com/view/elly-weki-meki-heart-gif-14294213",
            "https://cdn.discordapp.com/attachments/800224106384982027/800557668783357962/original.gif",
            "https://cdn.discordapp.com/attachments/800224106384982027/800567657220931645/tumblr_4d924f0ebbeed200cd494b3a3fb9fb57_da9d32c0_400.gif",
            "https://tenor.com/view/elly-weki-meki-oopsy-kpop-mv-gif-17589261",
            "https://tenor.com/view/elly-haerim-hi-hello-wave-gif-16426946",
            "https://gfycat.com/DisguisedKindlyHedgehog",
            "https://gfycat.com/UnrulyMiserableHake",
            "https://kpopsource.com/data/attachment-files/2020/10/162205_212AE534-2798-426A-ACF0-09A21D69487B.gif",
            "https://thumbs.gfycat.com/DeterminedRecklessChimpanzee-size_restricted.gif",
            "https://64.media.tumblr.com/5b05fc602f908d6a6c3f9a2d4d55162a/33a58ceedf93380c-db/s400x600/7ff6f0c3ed42db9251f876e6ee1d7b0203f56aa6.gif",
            "https://thumbs.gfycat.com/SlipperyWarpedChicken-size_restricted.gif",
            "https://64.media.tumblr.com/97b3963bc8a933fb1958b2b035799f39/b3217cbd43c46619-b2/s250x400/ec9dab015ce22966dbbc9c94d43996715f756d76.gif",
            "https://64.media.tumblr.com/a0870f1e36dbdd8e0a4db9cf526737a6/bda1e3c89214653f-f9/s250x400/607634a0e00e52da6a4aff6c2ff75bab0b73fe6a.gif",
            "https://64.media.tumblr.com/e5ff9d1db4e8372464b6f7d8b8ea5af7/000f11b2cb4891ba-0f/s400x600/60efbd26e9387c4cd56b4db42f67aac5c056851f.gif",
            "https://pa1.narvii.com/6674/c546b5f57335a613032bf0ef863b56d5992b0d66_hq.gif",
            "https://data.whicdn.com/images/320748152/original.gif",
            "https://64.media.tumblr.com/cb93e3eee8355ec6b18c9ca773865dd1/49c646152762f44d-b8/s250x400/b5c5ef0775bfbf260ff6ec499660cab9032dd4df.gif",
            "https://64.media.tumblr.com/409b81a459b246a149b86701f7625f2c/c61df2dec7c1aaa7-c3/s250x400/f67480227f06e6231e9fff44d2fdb2c730dc8b51.gif",
            "https://64.media.tumblr.com/029ec55d76f342771f081245bde39f8c/c61df2dec7c1aaa7-f5/s250x400/103a559fd194f9cffd01e78e320e3c548e119d2f.gif",
            "https://cdn1.diodeo.kr/cdn/webzine/2020/03/02/20200302091549_shlorxkh.gif",
            "https://gfycat.com/bitterachingconch-weki-meki-yoojung-elly-kpop",
            "https://gfycat.com/criminalblackesok-weki-meki-yoojung-elly-kpop",
            "https://gfycat.com/acclaimedillustriouscrustacean",
            "https://gfycat.com/alertwholeichthyosaurs",
            "https://gfycat.com/farawaymagnificentcorydorascatfish-weki-meki-yoojung-elly-kpop",
            "https://gfycat.com/chillyfatalanura",
            "https://gfycat.com/honoredshoddyarcticwolf",
            "https://gfycat.com/dearornerycopperhead",
            "https://gfycat.com/incompleteshockingcurassow-weki-meki-yoojung-elly-kpop",
            "https://gfycat.com/infinitewastefulflatcoatretriever-weki-meki-yoojung-wlly-kpop",
            "https://gfycat.com/disfiguredbothkatydid-weki-meki-yoojung-elly-kpop",
            "https://gfycat.com/bitterachingconch-weki-meki-yoojung-elly-kpop",
            "https://gfycat.com/criminalblackesok-weki-meki-yoojung-elly-kpop",
            "https://gfycat.com/descriptiveclutteredballoonfish-weki-meki-yoojung-elly-kpop"]

        self.bot.wekimeki_lua_gif = ["https://cdn.discordapp.com/attachments/800224194482274345/801694025346187274/original_1.gif",
            "https://cdn.discordapp.com/attachments/800224194482274345/800560199026606100/7a212bf86037a492f5355889a2441032.gif",
            "https://gfycat.com/DeafeningSillyCanadagoose",
            "https://tenor.com/view/birthday-flowers-hair-green-kpop-gif-18736777",
            "https://tenor.com/view/lua-weki-meki-girl-kpop-music-video-gif-17688814",
            "https://tenor.com/view/kpop-dazzle-weki-meki-lua-cute-gif-16419326",
            "https://tenor.com/view/kpop-dazzle-weki-meki-dance-gif-16912848",
            "https://gfycat.com/AshamedGreedyJanenschia",
            "https://cdn.discordapp.com/attachments/800224194482274345/801700137004564481/giphy.gif",
            "https://64.media.tumblr.com/793f5793189d3a8c443a58d070af178e/c02ba4fdf91f9037-15/s400x600/c36e1b605759f5bb504ddf378b3c08e8e995c5ec.gif",
            "https://media1.giphy.com/media/gjZGVIZhxAQ94hkZpr/giphy.gif",
            "https://64.media.tumblr.com/580a8b372709e3537f4b4a8c3c3c9e54/9c8c2f857d7a8f98-3d/s400x600/09d48f24247c9320a2d614901486d93e6c29bdfb.gif",
            "https://64.media.tumblr.com/96913cfa9583fbf1737227ac6124b181/faa3224d7d47dbc0-a2/s400x600/6ef350d2905e74bca68ca3797bcfcbb9184c1718.gif",
            "https://64.media.tumblr.com/1374dc0d7e9ff146fed402f6e95e610c/faa3224d7d47dbc0-2f/s400x600/f439f8ea0a67ec93ee87df1efcf1f6fb9fdf9f5d.gif",
            "https://gfycat.com/dentalpowerfulastarte",
            "https://gfycat.com/masculinecelebratedgrison",
            "https://gfycat.com/bigrigidbullmastiff",
            "https://gfycat.com/dangeroussizzlinggreendarnerdragonfly",
            "https://gfycat.com/milkymarvelousaidi",
            "https://gfycat.com/unimportantwiltedaltiplanochinchillamouse",
            "https://gfycat.com/firsttartblackfootedferret",
            "https://gfycat.com/gratefulobedientauklet",
            "https://gfycat.com/flippantquaintbonobo",
            "https://gfycat.com/fittinghardtofinddeviltasmanian",
            "https://gfycat.com/hollowgiganticcottontail-weki-meki-sookyung-kiling-wikimiki-lua",
            "https://gfycat.com/unfittartblacklemur-wekimeki-picky-kpop-lua",
            "https://gfycat.com/fearlessamusingacornbarnacle",
            "https://gfycat.com/dampmildaxolotl-wekimeki-kpop-lua",
            "https://gfycat.com/marvelousforcefulantarcticgiantpetrel-weki-meki-mechabear-kpop-lua",
            "https://gfycat.com/hardtofindrecklessgalapagosalbatross",
            "https://gfycat.com/amplefocusedcrane",
            "https://gfycat.com/badyounghuia",
            "https://gfycat.com/angelicwholegyrfalcon",
            "https://64.media.tumblr.com/edfa37044ecf95dce0c8b30e73b4dbae/9c8c2f857d7a8f98-1d/s400x600/5af9af495dbc0bb0fb74dbadc28b657d61e3f06a.gif",
            "https://64.media.tumblr.com/4b07f94793bd51a8a5b11facef9f3a91/0cede72b6c9e626c-e8/s400x600/925b8cc064c5afba24af666169e599099dc4060a.gif",
            "https://64.media.tumblr.com/edfa37044ecf95dce0c8b30e73b4dbae/9c8c2f857d7a8f98-1d/s400x600/5af9af495dbc0bb0fb74dbadc28b657d61e3f06a.gif",
            "https://1.bp.blogspot.com/-qTY4cBbsrKw/XuuNbvf-V5I/AAAAAAAAUB0/GU4jqM0V-vMad8d7WGl40Bi10CWWqrHqwCLcBGAsYHQ/s1600/DeficientOilyCapeghostfrog-size_restricted.gif"]

        self.bot.wekimeki_lucy_gif = ["https://gfycat.com/alarmedclutteredbobwhite",
            "https://cdn.discordapp.com/attachments/800224232759754772/800562065613914152/tenor.gif",
            "https://tenor.com/view/kpop-oopsy-weki-meki-lucy-music-video-gif-17518247",
            "https://gfycat.com/advancedplainfalcon-weki-meki-noh-lucy",
            "https://cdn.discordapp.com/attachments/800224232759754772/801697123807526912/NastyMisguidedClownanemonefish-max-1mb.gif",
            "https://tenor.com/view/wekimeki-lucy-cool-gif-18868364",
            "https://cdn.discordapp.com/attachments/800224232759754772/801698382091124776/tumblr_p4eoesUwmM1wisj25o3_540.gif",
            "https://gfycat.com/confuseddependableconch-mechabear-weki-meki-kpop-lucy",
            "https://gfycat.com/hatefulpoliticalgerbil-weki-meki-lucy-weme-cool",
            "https://media1.tenor.com/images/7faeaf073b5bca5e0aa56ca2ceaa030d/tenor.gif?itemid=18855932",
            "https://64.media.tumblr.com/c4d24f28c5902664c6b029d3b0f34dea/12dda53cd4f4f410-47/s250x400/fec7f82ea030c3d8f78fa057c887bfb337d92310.gif",
            "https://media1.tenor.com/images/2d904250ba13238b422f7c5b860ef942/tenor.gif?itemid=18855997",
            "https://64.media.tumblr.com/990e11cfa95b594e8a26390fe32dc61c/16f0659215527f10-f9/s400x600/d2b1098e48ba56f1ba8859b1565bcb7faef63a33.gif",
            "https://64.media.tumblr.com/427a5b4abf735e0c447376015e59e3c4/97b7120ea1979efa-1b/s250x400/16bdb7acb964ebee0de755f80d05e8df79d4d08e.gif",
            "https://64.media.tumblr.com/6efc021d7034993b2a038c3107f13296/97b7120ea1979efa-4a/s250x400/98ffc91d7858ac3fda33a2c3f55a4f2fe3ecd825.gif",
            "https://64.media.tumblr.com/f072ce6123b7c5e59f013b7652a29aa5/97b7120ea1979efa-b7/s250x400/8039587a664e5f45ec300543d557717aa7f57b4c.gif",
            "https://64.media.tumblr.com/533454c90cb6975aa36bab9ea6c29d16/97b7120ea1979efa-94/s250x400/c1ac9e08320ebc1291346a2c837cd121a2da0e14.gif",
            "https://gfycat.com/boilingunitedbarnacle",
            "https://gfycat.com/brilliantqueasyaoudad",
            "https://gfycat.com/advancedplainfalcon-weki-meki-noh-lucy",
            "https://gfycat.com/advancedeminentbichonfrise",
            "https://gfycat.com/accomplishedwellgroomedbangeltiger",
            "https://gfycat.com/shockedrectangulargermanshepherd",
            "https://gfycat.com/dentalkeenamethystsunbird",
            "https://gfycat.com/clearfakehoneycreeper",
            "https://gfycat.com/generousobedientandeancat",
            "https://gfycat.com/dishonestfargentoopenguin-weki-meki-mechabear-kpop-lucy"]

        self.bot.wekimeki_rina_gif = ["https://tenor.com/view/rina-weki-meki-kpop-gif-14709543",
            "https://cdn.discordapp.com/attachments/800224289810677821/800562573548191744/dd1e1c2491e3eb9d912ccd214e33145c.gif",
            "https://tenor.com/view/rina-weki-meki-idol-kpop-gif-14916651",
            "https://tenor.com/view/rina-weki-meki-kpop-cute-pretty-gif-15735688",
            "https://tenor.com/view/rina-weki-meki-kpop-cute-gif-16587745",
            "https://tenor.com/view/rina-weki-meki-kpop-fierce-gif-15517942",
            "https://gfycat.com/AdolescentPinkBug",
            "https://tenor.com/view/rina-weki-meki-kpop-gif-18219670",
            "https://gfycat.com/AgileGiddyIberiannase",
            "https://gfycat.com/blankdefiantannelida",
            "https://gfycat.com/faroffinsidiousbufflehead",
            "https://gfycat.com/specificdefinitivecamel",
            "https://gfycat.com/thoroughgorgeouslarva",
            "https://gfycat.com/brilliantsoulfulgharial-weki-meki",
            "https://gfycat.com/advancedvapidhylaeosaurus-weki-meki-kpop-rina",
            "https://gfycat.com/canineshoddygemsbok-weki-meki-kpop-rina",
            "https://gfycat.com/poisedcooperativegonolek-weki-meki-rina",
            "https://gfycat.com/spectacularniftyafricanjacana-weki-meki-rina-kpop",
            "https://gfycat.com/revolvingoddemperorpenguin-weki-meki-rina-kpop",
            "https://gfycat.com/raremindlessicelandicsheepdog",
            "https://gfycat.com/untimelyviciouscoati",
            "https://gfycat.com/saltyshamefularcherfish-weki-meki",
            "https://gfycat.com/sarcasticdistantguanaco-weki-meki",
            "https://gfycat.com/pastelbitterboto-weki-meki-crush-kpop-rina",
            "https://gfycat.com/measlybruisedivorybackedwoodswallow"]

        self.bot.wekimeki_sei_gif = ["https://tenor.com/view/wekimeki-sei-gif-18891261",
            "https://tenor.com/view/wekimeki-sei-gif-18891289",
            "https://tenor.com/view/wekimeki-sei-gif-19169813",
            "https://tenor.com/view/weki-meki-sei-weki-meki-sei-sei-weki-meki-my-beloved-gif-19859712",
            "https://tenor.com/view/sei-tiki-taka-choreography-weki-meki-dance-gif-15955302",
            "https://tenor.com/view/kpop-sei-diamond-dazzle-weki-meki-gif-16418938",
            "https://cdn.discordapp.com/attachments/800224316888973312/800574717760634950/c3498028cb5f5671e98f8212ca00bc33.gif",
            "https://cdn.discordapp.com/attachments/800224316888973312/800562983633027122/tenor-1.gif",
            "https://gfycat.com/DiscreteGrimyCurassow",
            "https://gfycat.com/DefiniteGraveHarrier",
            "https://gfycat.com/TatteredGregariousFlyingfox",
            "https://gfycat.com/ClutteredNeighboringAlabamamapturtle",
            "https://gfycat.com/MisguidedRichGangesdolphin",
            "https://media1.tenor.com/images/1d7b775282587a493c74aa6c5c3be086/tenor.gif?itemid=18891263",
            "https://imgur.com/PSiYC28",
            "https://thumbs.gfycat.com/DisguisedRewardingDrongo-max-1mb.gif",
            "https://64.media.tumblr.com/453272a52fb45c9dc9618fa5c61d16f9/0c77f6fc7044863b-da/s250x400/3313385ec355d56f837f45e124c4972c6cf3b0a3.gif",
            "https://64.media.tumblr.com/7c275eeeacb7ca223a4d363f7034d4ea/0c77f6fc7044863b-fe/s250x400/11e3989f18d26643bbafcfdf93a9f0ef1f5c7411.gif",
            "https://data.whicdn.com/images/304056936/original.gif",
            "https://64.media.tumblr.com/d4af956aa6fdb70c40aa1a1b21250b62/tumblr_p284hrsLoH1utck9fo1_400.gif",
            "https://64.media.tumblr.com/638953d38401d975e8d96fe9cb3bdea7/tumblr_p4t3trSQFd1wgkgwro1_400.gif",
            "https://thumbs.gfycat.com/FairBlondBluewhale-size_restricted.gif",
            "https://media1.tenor.com/images/0d469a3878a72e4585080b96032abe10/tenor.gif?itemid=18934298",
            "https://media1.tenor.com/images/0610ef472c8b16cbe5146c973c320b79/tenor.gif?itemid=18934293",
            "https://gfycat.com/flowerypoorgoshawk-choiyoojung-butterfly-kimdoyeon-weki-meki",
            "https://gfycat.com/bruisedthirdamericansaddlebred",
            "https://gfycat.com/frankfancyjackrabbit-weki-meki-wikimiki-sei",
            "https://gfycat.com/wellinformedmenacingdogwoodclubgall",
            "https://gfycat.com/whichsandyguineapig-sei-weki-meki-snap"]

        self.bot.wekimeki_suyeon_gif = ["https://tenor.com/view/wave-hi-hello-kpop-happy-gif-16968572",
            "https://tenor.com/view/kpop-crush-suyeon-weki-meki-music-video-gif-16268466",
            "https://tenor.com/view/surprised-oopsy-oops-oopsie-weki-meki-gif-18170395",
            "https://tenor.com/view/kpop-weki-meki-suyeon-ji-suyeon-weki-meki-suyeon-gif-18712771",
            "https://cdn.discordapp.com/attachments/800224361935274004/800565729052459098/4e45b67529977ec2941e3c3dcd853ec6.gif",
            "https://giphy.com/gifs/KPopSource-mv-weki-meki-oopsy-ZD23n6SRWsI9jUHGeq",
            "https://thumbs.gfycat.com/ConstantHeartyDwarfmongoose-max-1mb.gif",
            "https://i.pinimg.com/originals/c2/26/58/c2265820ebf3f0631e56e653d1f83cd6.gif",
            "https://64.media.tumblr.com/fc39d2c0f0fa9fcd6487b05fba97c065/tumblr_pghy9uFssE1w6jp1qo1_400.gif",
            "https://data.whicdn.com/images/293839681/original.gif",
            "https://media1.tenor.com/images/f13a331f235c79c2ca90516a9ffb7d85/tenor.gif?itemid=15217095",
            "https://media1.tenor.com/images/032c7d3f94d6e1b66873c48855c532d1/tenor.gif?itemid=16419110",
            "https://64.media.tumblr.com/793329e634d64eb44c5b9f7fed6192ac/f2344bf2172f0511-b2/s400x600/b0e0759a43f57181032f9f7fc827e24254b862b4.gif",
            "https://thumbs.gfycat.com/IgnorantFavorableIndri-size_restricted.gif",
            "https://data.whicdn.com/images/307590566/original.gif",
            "https://gfycat.com/carelessexcitablefreshwatereel-weki-meki-yoojung-suyeon",
            "https://gfycat.com/coldgracefulaquaticleech-weki-meki-suyeon",
            "https://gfycat.com/pinkserpentinebovine-weki-meki-suyeon-picky-nose",
            "https://gfycat.com/contentdirectgoat-girlgroup-suyeon-weki-meki",
            "https://gfycat.com/impressionablegrosskomododragon-mechabear-weki-meki-suyeon-kpop-beauty",
            "https://gfycat.com/tartspitefulinexpectatumpleco-weki-meki-mechabear-suyeon-kpop",
            "https://gfycat.com/formaleminentbluebottle-weki-meki-suyeon-kpop",
            "https://gfycat.com/foolishoddamericantoad-girlgroup-wekimeki-suyeon-kpop-sei",
            "https://gfycat.com/impossibletastyaztecant-mechabear-weki-meki-suyeon-kpop",
            "https://gfycat.com/mediumjoyfulleafcutterant",
            "https://gfycat.com/gracefulpiercingleopardseal-weki-meki-suyeon",
            "https://gfycat.com/glisteningweecatfish-weki-meki-suyeon"]

        self.bot.wekimeki_yoojung_gif = ["https://tenor.com/view/yoojung-choi-yoodaeng-daeng-choiyoojung-gif-19404386",
            "https://tenor.com/view/umm-um-yoojung-gif-8099931",
            "https://tenor.com/view/yoojung-choiyoojung-weki-meki-love-heart-gif-13589327",
            "https://tenor.com/view/choi-yoojung-yoodaeng-weki-meki-cute-baby-gif-13444237",
            "https://gfycat.com/WeepyCleverKakarikis",
            "https://cdn.discordapp.com/attachments/800224391258439721/800565546701160458/f1fc5f292c3132ff952b3b50e952698b.gif",
            "https://tenor.com/view/weki-meki-yoojung-choi-yoo-jung-gif-18765076",
            "https://giphy.com/gifs/KPopSource-mv-weki-meki-oopsy-XGaOrWHVVR669VXprf",
            "https://tenor.com/view/choiyoojung-wekimeki-gif-13666421",
            "https://media1.tenor.com/images/14f1da957061819ee05026de2790e33c/tenor.gif?itemid=16117095",
            "https://gfycat.com/imaginativevacantfieldspaniel-choiyoojung-kimdoyeon-weki-meki-jisuyeon",
            "https://gfycat.com/classicpastelamericancurl",
            "https://gfycat.com/opulentinfantilecricket-weki-meki",
            "https://gfycat.com/legitimatepoisedkestrel",
            "https://gfycat.com/foolishwelllitkissingbug",
            "https://gfycat.com/saltyperiodicdromedary",
            "https://gfycat.com/waryopengoldfish",
            "https://gfycat.com/agonizingselfreliantherring-wekimeki-weme-kpop",
            "https://gfycat.com/celebratedselfrelianthypsilophodon",
            "https://gfycat.com/elegantsomberarizonaalligatorlizard",
            "https://gfycat.com/amazingcostlydutchshepherddog-weki-meki-yoojung",
            "https://gfycat.com/eagerthreadbarecricket-weki-meki-yoojung-kpop-wave",
            "https://gfycat.com/questionableimaginaryblueandgoldmackaw",
            "https://gfycat.com/cleanaccomplishedjaeger",
            "https://gfycat.com/parchedfrayedarawana",
            "https://gfycat.com/heavenlyafraidegg",
            "https://gfycat.com/farawaydecentbluewhale-weki-meki-yoojung-food-kpop",
            "https://gfycat.com/shadyfrigiddamselfly",
            "https://gfycat.com/poisedsoftafricanrockpython",
            "https://gfycat.com/menacingelementaryfalcon-weki-meki-wikimiki-gimdoyeon-jisuyeon-coeyujeong-rusi-rua-rina-sei-elri",
            "https://gfycat.com/comfortablecarelesshammerkop-weki-meki-yoojung-kpop",
            "https://gfycat.com/windycreativeafricangoldencat-weki-meki-yoojung-kpop",
            "https://gfycat.com/cookedoilyadmiralbutterfly-weki-meki-yoojung",
            "https://gfycat.com/cleverillustriousindianspinyloach-weki-meki-yoojung-kpop",
            "https://gfycat.com/creamypeskydove-weki-meki-yoojung-kpop",
            "https://gfycat.com/easytastyeft-weki-meki-yoojung",
            "https://gfycat.com/pinkelementarykakarikis-weki-meki-yoojung",
            "https://gfycat.com/silkyraggedirishredandwhitesetter-weki-meki-yoojung",
            "https://gfycat.com/incrediblegrimyaustraliancattledog-weki-meki-yoojung",
            "https://gfycat.com/unsightlyvigorousgiraffe-weki-meki-yoojung-kpop",
            "https://gfycat.com/violetunfortunatechupacabra-weki-meki-yoojung",
            "https://gfycat.com/determinedthoroughcrayfish",
            "https://gfycat.com/discretepositiveasp",
            "https://gfycat.com/nastymediocrekingsnake-weki-meki-yoojung",
            "https://gfycat.com/amusedmenacingleafbird",
            "https://gfycat.com/defenselessteemingacornbarnacle-weki-meki-yoojung-kpop",
            "https://gfycat.com/paltrysillyasianpiedstarling",
            "https://gfycat.com/graysnoopyatlanticspadefish-weki-meki-eng-subs-yoojung-taemin-cover",
            "https://gfycat.com/dapperunlinedboutu",
            "https://gfycat.com/quaintcloudygardensnake-weki-meki-yoojung-kpop"]
    #. WJSN
        self.bot.wjsn_bona_gif = ["https://tenor.com/view/wjsn-bona-heart-gif-9368960",
            "https://tenor.com/view/wjsn-bona-gif-9369544",
            "https://tenor.com/view/wjsn-bona-gif-9369542",
            "https://tenor.com/view/wjsn-bona-gif-9369548",
            "https://tenor.com/view/bona-wjsn-cute-heart-gif-14540847",
            "https://tenor.com/view/wjsn-bona-gif-9368967",
            "https://tenor.com/view/wjsn-bona-gif-9369345",
            "https://tenor.com/view/kpop-wjsn-cosmic-girls-eating-bona-gif-18586148"]

        self.bot.wjsn_cheng_xiao_gif = ["https://tenor.com/view/surprised-shocked-cheng-xiao-gif-12031984",
            "https://tenor.com/view/cheng-xiao-heart-heart-shape-love-shape-gif-12031978",
            "https://tenor.com/view/cheng-xiao-not-bad-good-gif-12031989",
            "https://tenor.com/view/cheng-xiao-wjsn-gif-5896151",
            "https://tenor.com/view/chengxiao-cheng-xiao-wjsn-cosmic-gif-5176863",
            "https://tenor.com/view/cheng-xiao-wjsn-gif-19293644",
            "https://tenor.com/view/cheng-xiao-wjsn-gif-5896142",
            "https://tenor.com/view/cheng-xiao-wjsn-jump-flip-gif-5896127",
            "https://tenor.com/view/cheng-xiao-wjsn-wink-gif-5896145",
            "https://tenor.com/view/chengxiao-cheng-xiao-wjsn-cosmicgirls-gif-10710829"]

        self.bot.wjsn_dawon_gif = ["https://tenor.com/view/dawon-you-wjsn-pointing-akorp-gif-10023897",
            "https://tenor.com/view/kpop-wjsn-cosmic-girls-dawon-gif-18585918",
            "https://tenor.com/view/kpop-wjsn-cosmic-girls-dawon-heart-gif-18585940",
            "https://tenor.com/view/dawon-wjsn-cosmic-girls-cosmic-girls-gif-9760986",
            "https://tenor.com/view/kpop-wjsn-cosmic-girls-dawon-gif-18585910"]

        self.bot.wjsn_dayoung_gif = ["https://tenor.com/view/im-dayoung-dayoung-wjsn-cosmic-girls-gif-14794012",
            "https://tenor.com/view/im-dayoung-dayoung-wjsn-cosmic-girls-gif-14794019",
            "https://tenor.com/view/im-dayoung-dayoung-wjsn-cosmic-girls-gif-14794050",
            "https://tenor.com/view/im-dayoung-dayoung-wjsn-cosmic-girls-gif-14799931",
            "https://tenor.com/view/im-dayoung-dayoung-wjsn-cosmic-girls-gif-14794023",
            "https://tenor.com/view/im-dayoung-dayoung-wjsn-cosmic-girls-gif-14794085"]

        self.bot.wjsn_eunseo_gif = ["https://tenor.com/view/wjsn-cosmic-girls-eunseo-gif-18627810",
            "https://tenor.com/view/wjsn-cosmic-girls-kpop-eunseo-bunny-gif-18627757",
            "https://tenor.com/view/wjsn-cosmic-girls-eunseo-gif-18627819",
            "https://tenor.com/view/kpop-wjsn-cosmic-girls-eunseo-kiss-gif-18628222",
            "https://tenor.com/view/wjsn-wjsn-eunseo-eunseo-eunseo-butterfly-wjsn-eunseo-butterfly-gif-17455382"]

        self.bot.wjsn_exy_gif = ["https://tenor.com/view/exy-wjsn-kpop-cosmic-girls-kiss-gif-17356005",
            "https://tenor.com/view/exy-wjsn-kpop-cosmic-girls-good-job-gif-17356001",
            "https://tenor.com/view/yukziu-wjsn-exy-gif-19126649",
            "https://tenor.com/view/wjsn-cosmic-girls-exy-cute-gif-15481223",
            "https://tenor.com/view/wjsn-cosmic-girls-exy-chu-so-jung-kpop-gif-15479801"]

        self.bot.wjsn_luda_gif = ["https://tenor.com/view/luda-wjsn-gif-18881057",
            "https://tenor.com/view/luda-wjsn-cosmic-girls-cosmic-girls-gif-9534362",
            "https://tenor.com/view/luda-wink-wjsn-kpop-gif-14322078",
            "https://tenor.com/view/luda-witch-spell-cute-wjsn-gif-19920488",
            "https://tenor.com/view/luda-wjsn-gif-18881052"]

        self.bot.wjsn_seola_gif = ["https://tenor.com/view/wjsn-seola-cosmicgirls-kpop-gif-7837800",
            "https://tenor.com/view/kpop-wjsn-seola-heart-love-gif-18585890",
            "https://tenor.com/view/wjsn-seola-cosmicgirls-kpop-gif-7837797",
            "https://tenor.com/view/wjsn-seola-cosmicgirls-luda-exy-gif-7962940"]

        self.bot.wjsn_soobin_gif = ["https://tenor.com/view/soobin-wjsn-k-pop-korean-gif-9989530",
            "https://tenor.com/view/kpop-cosmic-girls-wjsn-soobin-gif-18586007",
            "https://tenor.com/view/kpop-cosmic-girls-wjsn-soobin-gif-18586011",
            "https://tenor.com/view/wjsn-cosmic-girls-kpop-soobin-kiss-gif-18586034",
            "https://tenor.com/view/wjsn-cosmic-girls-kpop-soobin-gif-18586040"]

        self.bot.wjsn_yeonjung_gif = ["https://tenor.com/view/yeonjung-cosmic-girls-wjsn-ioi-produce-gif-9932084",
            "https://tenor.com/view/kcon2019japan-kcon-%EC%BC%80%EC%9D%B4%EC%BD%98-singing-high-note-gif-14562921",
            "https://tenor.com/view/%EC%9A%B0%EC%A3%BC%EC%86%8C%EB%85%80-%EC%9C%A0%EC%97%B0%EC%A0%95-%EC%97%B0%EC%A0%95-stare-serious-gif-15594348",
            "https://gfycat.com/shamefulthoughtfulappaloosa-wjsn-yeonjung-beauty",
            "https://thumbs.gfycat.com/FarawayWeakKatydid-mobile.mp4",
            "https://64.media.tumblr.com/e661656f4c0a69df2a743de2746b4582/71a9721563887da6-59/s400x600/ea04cfe446f86cea085c362cd095f490e7d6f94e.gif"]

        self.bot.wjsn_yeoreum_gif = ["https://tenor.com/view/yeoreum-wjsn-gif-18828859",
            "https://tenor.com/view/yeoreum-wjsn-gif-19302984",
            "https://tenor.com/view/wjsn-la-la-love-yeoreum-lee-yeoreum-dancing-gif-17952511",
            "https://tenor.com/view/%EC%97%AC%EB%A6%84-%EC%9D%B4%EC%97%AC%EB%A6%84-yorm-wjsn-yeoreum-gif-19970067",
            "https://tenor.com/view/wjsn-yeoreum-gif-18829843"]

        self.bot.wjsn_mei_qi_gif = ["https://tenor.com/view/meng-mei-qi-cell-phone-cry-call-hold-back-tears-gif-11918655",
            "https://tenor.com/view/meiqi-laughing-wjsn-lmao-lol-gif-10022964",
            "https://tenor.com/view/meng-meiqi-%E7%81%AB%E7%AE%AD%E5%B0%91%E5%A5%B3101-rocket-girls-gif-19971810",
            "https://tenor.com/view/meng-meiqi-%E7%81%AB%E7%AE%AD%E5%B0%91%E5%A5%B3101-hjsn-gif-19971908",
            "https://tenor.com/view/meng-mei-qi-come-on-lets-party-wink-gif-11918640"]

        self.bot.wjsn_xuan_yi_gif = ["https://tenor.com/view/kpop-wjsn-cosmic-girls-xuan-yi-gif-19038371",
            "https://tenor.com/view/kpop-wjsn-cosmic-girls-xuan-yi-kiss-gif-19038397",
            "https://tenor.com/view/xuanyi-wjsn-cosmic-girls-gif-10949761",
            "https://tenor.com/view/xuanyi-cosmic-girls-wjsn-gif-10304350",
            "https://tenor.com/view/xuan-yi-wjsn-k-pop-cosmic-girls-gif-11474789"]
    #. end of gifs

    @commands.command()
    async def apink(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Apink {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "bomi":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Bomi :heart:') 
                await ctx.send(random.choice(self.bot.apink_bomi_gif))
                await ctx.message.delete()
        elif arg == "chorong":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Chorong :heart:') 
                await ctx.send(random.choice(self.bot.apink_chorong_gif))
                await ctx.message.delete()
        elif arg == "eunji":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Eunji :heart:') 
                await ctx.send(random.choice(self.bot.apink_eunji_gif))
                await ctx.message.delete()
        elif arg == "hayoung":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Hayoung :heart:') 
                await ctx.send(random.choice(self.bot.apink_hayoung_gif))
                await ctx.message.delete()
        elif arg == "naeun":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Naeun :heart:') 
                await ctx.send(random.choice(self.bot.apink_naeun_gif))
                await ctx.message.delete()
        elif arg == "namjoo":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Namjoo :heart:') 
                await ctx.send(random.choice(self.bot.apink_namjoo_gif))
                await ctx.message.delete()

    @commands.command(aliases = ['dream'])
    async def dreamcatcher(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Dreamcatcher {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "jiu" or arg == "catcher jiu":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{k8}>, <@!{ctx.author.id}> is talking about JiU :rabbit: ')
                    await ctx.send(random.choice(self.bot.dreamcatcher_jiu_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about JiU :rabbit:')
                await ctx.send(random.choice(self.bot.dreamcatcher_jiu_gif))
                await ctx.message.delete()
        elif arg == "dami" or arg == "catcher dami":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Dami :heart:') 
                await ctx.send(random.choice(self.bot.dreamcatcher_dami_gif))
                await ctx.message.delete()
        elif arg == "gahyeon" or arg == "catcher gahyeon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Gahyeon :heart:') 
                await ctx.send(random.choice(self.bot.dreamcatcher_gahyeon_gif))
                await ctx.message.delete()
        elif arg == "handong" or arg == "catcher handong":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Handong :heart:') 
                await ctx.send(random.choice(self.bot.dreamcatcher_handong_gif))
                await ctx.message.delete()
        elif arg == "siyeon" or arg == "catcher siyeon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Siyeon :heart:') 
                await ctx.send(random.choice(self.bot.dreamcatcher_siyeon_gif))
                await ctx.message.delete()
        elif arg == "sua" or arg == "catcher sua":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about SuA :heart:') 
                await ctx.send(random.choice(self.bot.dreamcatcher_sua_gif))
                await ctx.message.delete()
        elif arg == "yoohyeon" or arg == "catcher yoohyeon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Yoohyeon :heart:') 
                await ctx.send(random.choice(self.bot.dreamcatcher_yoohyeon_gif))
                await ctx.message.delete()

    @commands.command(aliases = ['fromis', 'fromis9'])
    async def fromis_9(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [fromis_9 {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            if arg == "jisun":
                await ctx.send(f'<@{ctx.author.id}> is talking about Jisun :heart:') 
                await ctx.send(random.choice(self.bot.fromis_9_jisun_gif))
                await ctx.message.delete()
            elif arg == "hayoung":
                await ctx.send(f'<@{ctx.author.id}> is talking about Hayoung :heart:') 
                await ctx.send(random.choice(self.bot.fromis_9_hayoung_gif))
                await ctx.message.delete()
            elif arg == "saerom":
                await ctx.send(f'<@{ctx.author.id}> is talking about Saerom :heart:') 
                await ctx.send(random.choice(self.bot.fromis_9_saerom_gif))
                await ctx.message.delete()
            elif arg == "chaeyoung":
                await ctx.send(f'<@{ctx.author.id}> is talking about Chaeyoung :heart:') 
                await ctx.send(random.choice(self.bot.fromis_9_chaeyoung_gif))
                await ctx.message.delete()
            elif arg == "nakyung":
                await ctx.send(f'<@{ctx.author.id}> is talking about Nakyung :heart:') 
                await ctx.send(random.choice(self.bot.fromis_9_nakyung_gif))
                await ctx.message.delete()
            elif arg == "jiwon":
                await ctx.send(f'<@{ctx.author.id}> is talking about Jiwon :heart:') 
                await ctx.send(random.choice(self.bot.fromis_9_jiwon_gif))
                await ctx.message.delete()
            elif arg == "seoyeon":
                await ctx.send(f'<@{ctx.author.id}> is talking about Seoyeon :heart:') 
                await ctx.send(random.choice(self.bot.fromis_9_seoyeon_gif))
                await ctx.message.delete()
            elif arg == "jiheon":
                await ctx.send(f'<@{ctx.author.id}> is talking about Jiheon :heart:') 
                await ctx.send(random.choice(self.bot.fromis_9_jiheon_gif))
                await ctx.message.delete()
            elif arg == "gyuri":
                await ctx.send(f'<@{ctx.author.id}> is talking about Gyuri :heart:') 
                await ctx.send(random.choice(self.bot.fromis_9_gyuri_gif))
                await ctx.message.delete()

    @commands.command()
    async def weki(self, ctx, meki, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Weki Meki {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if meki == "meki":
            if arg == "doyeon":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Doyeon :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_doyeon_gif))
                    await ctx.message.delete()
            elif arg == "elly":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Elly :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_elly_gif))
                    await ctx.message.delete()
            elif arg == "lua":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Lua :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_lua_gif))
                    await ctx.message.delete()
            elif arg == "lucy":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Lucy :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_lucy_gif))
                    await ctx.message.delete()
            elif arg == "rina":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Rina :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_rina_gif))
                    await ctx.message.delete()
            elif arg == "sei":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Sei :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_sei_gif))
                    await ctx.message.delete()
            elif arg == "suyeon":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Suyeon :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_suyeon_gif))
                    await ctx.message.delete()
            elif arg == "yoojung":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Yoojung :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_yoojung_gif))
                    await ctx.message.delete()

    @commands.command()
    async def wjsn(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [WJSN {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "bona":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Bona :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_bona_gif))
                await ctx.message.delete()
        elif arg == "cheng xiao":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Cheng Xiao :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_cheng_xiao_gif))
                await ctx.message.delete()
        elif arg == "dawon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Dawon :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_dawon_gif))
                await ctx.message.delete()
        elif arg == "dayoung":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Dayoung :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_dayoung_gif))
                await ctx.message.delete()
        elif arg == "eunseo":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Eunseo :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_eunseo_gif))
                await ctx.message.delete()
        elif arg == "exy":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Exy :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_exy_gif))
                await ctx.message.delete()
        elif arg == "luda":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Luda :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_luda_gif))
                await ctx.message.delete()
        elif arg == "seola":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Seola :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_seola_gif))
                await ctx.message.delete()
        elif arg == "soobin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Soobin :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_soobin_gif))
                await ctx.message.delete()
        elif arg == "yeonjung":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Yeonjung :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_yeonjung_gif))
                await ctx.message.delete()
        elif arg == "yeoreum":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Yeoreum :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_yeoreum_gif))
                await ctx.message.delete()
        elif arg == "mei qi":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Mei Qi :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_mei_qi_gif))
                await ctx.message.delete()
        elif arg == "xuan yi":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Xuan Yi :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_xuan_yi_gif))
                await ctx.message.delete()

    

    

def setup(client):
    client.add_cog(GGS(client))