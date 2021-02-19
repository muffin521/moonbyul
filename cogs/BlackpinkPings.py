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

#//people
muffin = 488423352206229505
gareth = 389897179701182465
jon = 109914198544240640
princessuwu = 716841614185857086

class BlackpinkPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.rose_gif = ["https://tenor.com/view/blackpink-cute-ros%C3%A9-mini-heart-kpop-gif-14143584",
            "https://tenor.com/view/rose-blackpink-heart-sign-happy-smile-gif-11901224",
            "https://tenor.com/view/looking-let-me-see-ros%C3%A9-blackpink-rosie-gif-18118559",
            "https://tenor.com/view/blackpink-ros%C3%A9-dance-kpop-gif-14043692",
            "https://tenor.com/view/rose-blackpink-kpop-happy-smile-gif-16205441",
            "https://tenor.com/view/blackpink-gif-9219329",
            "https://tenor.com/view/rose-lovesickgirls-blackpink-kpop-thealbum-gif-18726475",
            "https://tenor.com/view/chipmunk-cute-puppy-cheeks-rose-rosie-gif-15623613",
            "https://tenor.com/view/rose-blackpink-ros%C3%A9-roseanne-cute-gif-16257627",
            "https://tenor.com/view/blackpink-rose-uwu-kpop-cute-gif-15402030",
            "https://tenor.com/view/lisa-smiling-black-pink-k-pop-cute-gif-9389777",
            "https://tenor.com/view/blackpink-blink-rose-boombayah-gif-11950271",
            "https://tenor.com/view/rose-kpop-blackpink-pairwork-recordwork-gif-14460401",
            "https://tenor.com/view/rose-jennie-black-pink-k-pop-pose-gif-9389644",
            "https://tenor.com/view/%E0%B9%82%E0%B8%A3%E0%B9%80%E0%B8%8B%E0%B9%88-clapping-cute-rose-blackpink-gif-15063856",
            "https://tenor.com/view/blackpink-rose-gif-18802619",
            "https://tenor.com/view/blackpink-rose-sexy-gif-19127868",
            "https://tenor.com/view/blackpink-rose-lovesick-girls-gif-18683755",
            "https://tenor.com/view/blackpink-roseanne-park-ros%C3%A9-surprised-gif-18344584",
            "https://tenor.com/view/blackpink-rose-gif-18802617",
            "https://tenor.com/view/rose-blackpink-balloons-cute-pretty-gif-15405146",
            "https://tenor.com/view/ros%C3%A9-kpop-blackpink-confused-gif-16895336",
            "https://tenor.com/view/blackpink-rose-heart-love-park-chae-young-gif-11783851",
            "https://tenor.com/view/blackpink-blink-rose-boombayah-gif-11950271",
            "https://tenor.com/view/blackpink-rose-gif-18530274",
            "https://cdn.discordapp.com/attachments/808766013302243367/808940098132901898/rose_3.gif",
            "https://giphy.com/gifs/yNIvmlL6qTbDhI1DuD",
            "https://giphy.com/gifs/ETBRLQUSgil31Otb8F",
            "https://giphy.com/gifs/DwJl8UijyUSra8RIh7",
            "https://gfycat.com/briefminorichneumonfly-blackpink-chaeyoung-park-chaeyoung",
            "https://gfycat.com/bountifulyellowatlanticridleyturtle",
            "https://gfycat.com/affectionategreenagama-blackpink-rose",
            "https://gfycat.com/artisticuntimelyblackmamba-lovesick-girls-blackpink-rose",
            "https://gfycat.com/accomplishedthisglowworm-kpop",
            "https://gfycat.com/confusedgrandiosegallowaycow-blackpink-diaries-kpop-rose",
            "https://gfycat.com/accuratesingleiberianchiffchaff",
            "https://gfycat.com/backunpleasantcrocodileskink",
            "https://gfycat.com/concernedscarcegerenuk",
            "https://gfycat.com/adorablegoldenbagworm-blackpink-rose",
            "https://gfycat.com/fairfrailbass-blackpink-rose",
            "https://gfycat.com/harmfulvioletant-blackpink",
            "https://gfycat.com/feminineshortalbacoretuna",
            "https://gfycat.com/astonishingwellwornfinwhale-blackpink-concert-park-chaeyoung",
            "https://gfycat.com/embarrassedfearfulfinch-blackpink-rose-kpop",
            "https://gfycat.com/ashamedlineargrayfox-blackpink-rose-kpop",
            "https://gfycat.com/hollowglumguanaco-blackpink-rose",
            "https://gfycat.com/nicemellowfanworms",
            "https://gfycat.com/hospitableremarkableflies-blackpink-rose",
            "https://gfycat.com/corrupteverybudgie-rose",
            "https://gfycat.com/velvetyunawarecolt-blackpink-rose",
            "https://gfycat.com/agedancientjellyfish-yves-saint-laurent-blackpink-rose-ysl",
            "https://gfycat.com/babyishharmoniousduckbillcat-blackpink-x-billboard-park-chaeyoung",
            "https://gfycat.com/goodaggravatinghammerkop-blackpink-rose-kpop",
            "https://gfycat.com/likablelimpaardvark-blackpink-celebrity-rose-kpop",
            "https://gfycat.com/plasticweepyjerboa",
            "https://gfycat.com/unhealthyaridfluke",
            "https://gfycat.com/rawselfishharpseal",
            "https://gfycat.com/piercingplasticdassierat-beauty",
            "https://gfycat.com/serenerepentantdowitcher-beauty",
            "https://gfycat.com/celebratedspottedaoudad-blackpink",
            "https://gfycat.com/cheerybleakelver-blackpink-fancam-rose-mera-beulraegpingkeu",
            "https://gfycat.com/flatboringjaguar-blackpink-rose",
            "https://gfycat.com/massivefragrantbaiji",
            "https://gfycat.com/dishonestwholeicelandicsheepdog-dashboard",
            "https://gfycat.com/powerlessthinharvestmouse-blackpink",
            "https://gfycat.com/unawaretendereasteuropeanshepherd-blackpink-rose-park-chaeyoung",
            "https://gfycat.com/distinctashamedhyrax",
            "https://gfycat.com/embellisheddownrightdegu-blackpink-24365-rose-kpop",
            "https://gfycat.com/glassforcefulkakapo-blackpink-rose",
            "https://gfycat.com/unnaturalamazingangelwingmussel",
            "https://gfycat.com/thornyperkyinsect-park-chae-young-blackpink-rose-idol",
            "https://gfycat.com/hideousuntriedafricangoldencat-blackpink-rose",
            "https://gfycat.com/astonishingdiligentfalcon-blackpink-rtijlo-kpop-rose",
            "https://gfycat.com/eagerembarrassedgrouper-blackpink-rose-kpop",
            "https://gfycat.com/impossiblejaggedhochstettersfrog-blackpink-rose",
            "https://gfycat.com/everlastingnaivecrow-24365-with-blackpink-kpop-rose",
            "https://gfycat.com/querulousinsecureirrawaddydolphin-blackpink-rose-kpop",
            "https://gfycat.com/largerapidhawaiianmonkseal-blackpink-rose-beauty",
            "https://gfycat.com/annualshinyafricanporcupine-blackpink-rose",
            "https://gfycat.com/unlawfultangiblecottonmouth-blackpink-rose",
            "https://gfycat.com/unknownsadafricanrockpython-girl-group-blackpink-kpop-laugh-rose",
            "https://gfycat.com/fragrantoddcanvasback-seasons-greetings-blackpink-kpop-rose",
            "https://gfycat.com/blanksmugallosaurus-kpop-blackpink-rose",
            "https://gfycat.com/illiteratesnappyharborseal",
            "https://gfycat.com/boilingfrightenedcivet",
            "https://gfycat.com/tallgenerousammonite",
            "https://gfycat.com/bothrepulsivehorseshoebat-beauty",
            "https://gfycat.com/appropriateoptimisticgoshawk",
            "https://gfycat.com/frenchmediocrehawk-kill-this-love-blackpink-kpop-rose",
            "https://gfycat.com/happyacrobaticlabradorretriever-kpop-rose-blackpink",
            "https://gfycat.com/pitifulphonyilladopsis-yg-entertainment-blackpink-k-pop-beulraegpingkeu",
            "https://data.whicdn.com/images/344762730/original.gif",
            "https://data.whicdn.com/images/323213290/original.gif",
            "https://data.whicdn.com/images/326830028/original.gif",
            "https://data.whicdn.com/images/323303224/original.gif",
            "https://i.pinimg.com/originals/0f/15/5b/0f155b4e07d6437e52f1f2d8e3c37957.gif"]

        self.bot.jennie_gif = ["https://tenor.com/view/blackpink-jennie-kpop-pretty-cute-gif-14797267",
            "https://tenor.com/view/jennie-blackpink-pretty-kpop-pose-gif-15947380",
            "https://tenor.com/view/jenniekim-gif-18818029",
            "https://tenor.com/view/blackpink-jennie-kiss-cute-gif-18818161",
            "https://tenor.com/view/blackpink-jennie-cute-smile-kpop-gif-14004531",
            "https://tenor.com/view/kiss-jennie-gif-14662350",
            "https://tenor.com/view/jennie-kim-blackpink-bed-jennie-kpop-gif-12627702",
            "https://tenor.com/view/jenny-jennie-kim-blackpink-cute-gif-12481536",
            "https://tenor.com/view/blackpink-jennie-kpop-saranghae-gif-14797258",
            "https://tenor.com/view/blackpink-jennie-jenniekim-jendeukkie-jenjen-gif-9256813",
            "https://tenor.com/view/jennie-blackpink-gif-14036697",
            "https://tenor.com/view/jennie-blackpink-swag-rap-blink-gif-11950210",
            "https://tenor.com/view/jennie-blackpink-gif-18630502",
            "https://tenor.com/view/kim-jennie-jennie-solo-jennie-edit-gif-18046700",
            "https://gfycat.com/agitatedsparklingagouti-jennie-kpop-blackpink",
            "https://gfycat.com/adolescentcelebratedirrawaddydolphin-beauty",
            "https://gfycat.com/femininewavykillerwhale-blackpink-jennie",
            "https://gfycat.com/abandonedbrilliantaddax",
            "https://gfycat.com/adoredvapidisabellineshrike-blackpink-jennie-kpop",
            "https://gfycat.com/acidicoptimalblacknorwegianelkhound",
            "https://gfycat.com/nimblewiltedapatosaur-blackpink-jennie",
            "https://gfycat.com/limitedkeenamethystgemclam-blackpink-jennie",
            "https://gfycat.com/agiledimpledbeagle-jennie-blackpink-kpop",
            "https://gfycat.com/bruisedscholarlydwarfmongoose",
            "https://gfycat.com/agedfickleaegeancat",
            "https://gfycat.com/ambitiousterrificdunnart-blackpink-jennie",
            "https://gfycat.com/amplepettydobermanpinscher",
            "https://gfycat.com/bareeverychinchilla-blackpink-jennie",
            "https://gfycat.com/braveblankindianhare-jennie-kim-blackpink",
            "https://gfycat.com/blandsnivelingdromaeosaur",
            "https://gfycat.com/biodegradableverifiablelhasaapso",
            "https://gfycat.com/bothweepyamericanmarten-j",
            "https://gfycat.com/circularinfatuatedalbino-blackpink-jennie-kpop-beauty",
            "https://gfycat.com/achingmasculineirishredandwhitesetter",
            "https://gfycat.com/cluelesswealthybumblebee",
            "https://gfycat.com/clumsyspanishcaribou",
            "https://gfycat.com/clumsywickedgraysquirrel",
            "https://gfycat.com/carefuldarlinggrassspider",
            "https://gfycat.com/frighteningfearfulaphid-kill-this-love-blackpink-jennie-kpop",
            "https://gfycat.com/idolizedbriskchamois-weekly-idol-jennie-kim-blackpink-kpop",
            "https://gfycat.com/hiddenidealisticbrontosaurus-jennie-kim-blackpink-kpop",
            "https://gfycat.com/skinnyshabbyindianrhinoceros",
            "https://gfycat.com/tightslimattwatersprairiechicken-jennie-kim-blackpink",
            "https://gfycat.com/unconsciouscoldconure-jennie",
            "https://gfycat.com/understatedabandoneddarwinsfox-blackpink-jennie",
            "https://gfycat.com/angelicseveralgerbil-blackpink-jennie-kpop",
            "https://gfycat.com/alienatedseriousherculesbeetle-marie-claire-blackpink-jennie-kpop",
            "https://gfycat.com/allblanderne-how-you-like-that-blackpink-jennie-hylt",
            "https://gfycat.com/baggynicecob-blackpink-jennie-kpop",
            "https://gfycat.com/beneficialneighboringindianrhinoceros-blackpink-jennie",
            "https://gfycat.com/betterweakhermitcrab-blackpink-musiccore",
            "https://gfycat.com/blissfulimpartialcobra-blackpink-adorable-jennie-cute",
            "https://gfycat.com/browntheseichidna-blackpink-jennie-kpop",
            "https://gfycat.com/celebratedfaithfulclingfish-blackpink-jennie",
            "https://gfycat.com/easyglamorousblackrussianterrier",
            "https://gfycat.com/uglynearbuzzard-blackpink-jennie-nin0r-kpop",
            "https://gfycat.com/cheeryraggedkakarikis-jennie-kim-blackpink-kpop",
            "https://gfycat.com/flashyfamouscrow",
            "https://gfycat.com/compassionatehandyhairstreak",
            "https://gfycat.com/coldscholarlydutchshepherddog-blackpink-inkigayo-jennie-music-ddududdudu",
            "https://gfycat.com/conventionalblueammonite",
            "https://gfycat.com/cookedacclaimedape-blackpink-jennie-kpop",
            "https://gfycat.com/handsomeheartyanemoneshrimp",
            "https://gfycat.com/handsomeheartyanemoneshrimp",
            "https://gfycat.com/beneficialunfoldedcougar",
            "https://gfycat.com/anyqualifiedlarva",
            "https://gfycat.com/bruisedscholarlydwarfmongoose",
            "https://gfycat.com/exemplarygoldenfulmar",
            "https://gfycat.com/cleargloomybagworm-blackpink-jennie-kpop",
            "https://gfycat.com/circularthirstyhorseshoebat-yg-entertainment-blackpink-jennie",
            "https://gfycat.com/cloudyindolentbeardedcollie-blackpink-jennie-aegyo-cute",
            "https://gfycat.com/completedappercrocodile",
            "https://gfycat.com/blondforsakenarrowana-jennie-kpop-blackpink",
            "https://gfycat.com/corruptpepperyborer",
            "https://gfycat.com/grossshimmeringcrab-blackpink-confident-fabulous-hairflip",
            "https://gfycat.com/radiantoptimisticdugong",
            "https://gfycat.com/agitatedsparklingagouti-jennie-kpop-blackpink",
            "https://media1.tenor.com/images/59c3ec2a585a9085040a24711deddfc3/tenor.gif?itemid=14036697",
            "https://i.pinimg.com/originals/16/da/d7/16dad7a457ee0306ccc0b4bea49bd93d.gif",
            "https://pa1.narvii.com/7037/5c3b3645a0b40001ab7bf6379a1e6fbec8b84de4r1-478-540_hq.gif",
            "https://pa1.narvii.com/6505/72f10ada419a7319aaeff4a2283d001662e6a015_hq.gif",
            "https://64.media.tumblr.com/a4e55ebd5a5ae9e4b9f9731bedebbdbf/tumblr_oxaukxpo8G1uqef5eo2_400.gif"]

        self.bot.lisa_gif = ["https://tenor.com/view/lalisa-manoban-lisa-blackpink-lollipop-kpop-gif-17772815",
            "https://tenor.com/view/lisa-smile-black-pink-kpop-cute-gif-16464316",
            "https://tenor.com/view/lisa-blackpink-cute-girl-gif-15983564",
            "https://tenor.com/view/hi-hello-wave-lisa-lalisa-gif-14924995",
            "https://tenor.com/view/lisa-lisa-blackpink-blackpink-blackpink-lisa-gif-18095773",
            "https://tenor.com/view/ayeah-ayeah-pointing-smile-cute-lisa-gif-16007292",
            "https://tenor.com/view/lisa-lalisa-lalisa-manoban-mentor-lisa-kpop-gif-17299890",
            "https://gfycat.com/alienateddelayedgermanpinscher-playingwithfire-blackpink-lisa",
            "https://gfycat.com/tightlimpgoosefish",
            "https://gfycat.com/smallshinygalapagosdove",
            "https://gfycat.com/esteemedinfinitechinesecrocodilelizard-blackpink-mechabear-kpop",
            "https://gfycat.com/elderlyfatalbooby-tiktok-stage-blackpink-reaction-lalisa-kpop",
            "https://gfycat.com/colorlesspopularchinesecrocodilelizard-blackpink",
            "https://gfycat.com/nimbleincompatibleeskimodog-playing-with-fire-behind-the-scenes-blackpink",
            "https://gfycat.com/glisteningspryarieltoucan",
            "https://gfycat.com/smarthappygoluckyblueshark",
            "https://gfycat.com/actualsoggykakapo-blackpink-cute-kpop-lisa",
            "https://gfycat.com/pointlessflippantindusriverdolphin",
            "https://gfycat.com/miserableweeklyhydra",
            "https://gfycat.com/peacefulthirdchinchilla",
            "https://gfycat.com/rigidvaluablehatchetfish-voodoobear-blackpink-dance-kpop-lisa",
            "https://gfycat.com/organicunfitgraywolf-blackpink-kpop-lisa",
            "https://gfycat.com/deficientidealisticantelope",
            "https://gfycat.com/conventionalgenerousarmednylonshrimp",
            "https://gfycat.com/feistylimitedamericanbadger",
            "https://gfycat.com/abledesertedcrow",
            "https://gfycat.com/flawedagitatedimago-blackpink-lisa-kpop",
            "https://gfycat.com/greatbothhydra",
            "https://gfycat.com/magnificentwarmantelope-blackpink",
            "https://gfycat.com/reasonablejaggedbullmastiff-blackpink-mechabear-kpop",
            "https://gfycat.com/fittingfloweryarthropods-blackpink",
            "https://gfycat.com/sophisticatedfixedindigobunting",
            "https://gfycat.com/clutteredbetterjay-blackpink-lisa-pits",
            "https://gfycat.com/responsiblebetterfrigatebird",
            "https://gfycat.com/vacantwindyboa-blackpink-koop-lisa-kpop",
            "https://gfycat.com/dazzlinggranularcrocodile-blackpink",
            "https://gfycat.com/babyishmealyisabellinewheatear-blackpink-kpop-lisa",
            "https://gfycat.com/criminalfirmaquaticleech-lisa-manoban-blackpink-kpop",
            "https://gfycat.com/deaduntidybats",
            "https://gfycat.com/commonequalballpython",
            "https://gfycat.com/chieftepidhornet-blackpink-kpop-lisa",
            "https://gfycat.com/acceptablefrighteningjavalina",
            "https://gfycat.com/compassionatebigheartedamericancreamdraft",
            "https://gfycat.com/elegantscentedgreatwhiteshark",
            "https://gfycat.com/nextadorableclownanemonefish-blackpink",
            "https://gfycat.com/arcticloathsomeafricanelephant",
            "https://gfycat.com/necessaryhandsomeiaerismetalmark-beauty",
            "https://gfycat.com/jealousnippyarrowana-blackpink-beautiful-lalisa-kpop-sexy-hot",
            "https://gfycat.com/astonishingshortcheetah-blackpink-lisa",
            "https://gfycat.com/blackandwhitedigitaleider-blackpink-lisa",
            "https://gfycat.com/pastcheerfulechidna-blackpink-lisa",
            "https://gfycat.com/enchantingilliterategoose-how-you-like-that-blackpink-lalisa-hylt",
            "https://gfycat.com/firmregularamericanquarterhorse-how-you-like-that-blackpink-lalisa-hylt",
            "https://gfycat.com/glassdisgustinggopher-ddu-du-ddu-du-blackpink-squareup-music",
            "https://gfycat.com/graciousdelectablegenet-ddu-du-ddu-du-blackpink-squareup-ddududdudu",
            "https://gfycat.com/feistycandidaplomadofalcon-blackpink-reaction-24365-lalisa-aegyo-flirt-kiss",
            "https://gfycat.com/occasionalradiantadeliepenguin-blackpink-whistle-beulraegpingkeu-kpop",
            "https://gfycat.com/babyishkaleidoscopicfruitfly-blackpink-lisa",
            "https://gfycat.com/definiterepulsivehectorsdolphin",
            "https://gfycat.com/gleamingshabbyhadrosaurus-blackpink-kpop-lisa",
            "https://gfycat.com/personalseverealabamamapturtle-blackpink-lisa",
            "https://gfycat.com/gentleglassdeinonychus-blackpink-lisa-kpop",
            "https://gfycat.com/limpingdeliriousanemoneshrimp",
            "https://gfycat.com/hollowchiefcleanerwrasse-24365-with-blackpink-kpop-lisa",
            "https://gfycat.com/dangerousmajorgrouper-24365-with-blackpink-kpop-lisa",
            "https://gfycat.com/slimadmirableharvestmen",
            "https://gfycat.com/elderlydearestamethystsunbird-blackpink-kpop-lisa",
            "https://gfycat.com/hatefulindolentarcticseal",
            "https://gfycat.com/verifiablelimitedafricanclawedfrog-ddu-du-ddu-du-blackpink-squareup-music",
            "https://gfycat.com/bogushiddenamericanbadger",
            "https://gfycat.com/vastgivingkakapo-blackpink-news",
            "https://gfycat.com/medicalshockedjackal",
            "https://gfycat.com/insecureillfatedamericanalligator-ddu-du-ddu-du-blackpink-lisa",
            "https://gfycat.com/carefulemotionalgyrfalcon",
            "https://gfycat.com/betterethicalchital",
            "https://gfycat.com/secondunevenhoneybee-mind-blown-blown-away-surprised-blackpink-24365",
            "https://gfycat.com/imaginativesnarlingcaracal-blackpink-penshoppe-lalisa-kpop",
            "https://gfycat.com/equatorialpoisedbluemorphobutterfly-blackpink-beulraegpingkeu-lisa",
            "https://gfycat.com/plushagitatedchinchilla-blackpink-kpop-lisa-hot",
            "https://gfycat.com/leadingflatalabamamapturtle-youth-with-you-2-blackpink-lalisa-kpop",
            "https://gfycat.com/impishgravebengaltiger",
            "https://gfycat.com/lonefakeeasternnewt-blackpink-kpop-lisa",
            "https://gfycat.com/dearniceicefish-yg-entertainment-kill-this-love-blackpink",
            "https://gfycat.com/adeptsphericalanemonecrab-kill-this-love-blackpink-lalisa-beauty",
            "https://gfycat.com/keentornlamprey",
            "https://gfycat.com/enchantedunfinishedjellyfish",
            "https://gfycat.com/heartfeltbabyishblobfish-behind-the-scenes-kill-this-love"]

        self.bot.jisoo_gif = ["https://tenor.com/view/jisoo-kimjisoo-visual-kpop-blackpink-gif-10720121",
            "https://tenor.com/view/blackpink-kpop-kim-jisoo-jisoo-lead-vocalist-gif-17967342",
            "https://tenor.com/view/blackpink-kpop-kim-jisoo-jisoo-lead-vocalist-gif-17944860",
            "https://tenor.com/view/jisoo-gif-18486243",
            "https://tenor.com/view/blackpink-kim-jisoo-why-what-the-gif-12589646",
            "https://tenor.com/view/jisoo-sexy-blackpink-kpop-gif-15419500",
            "https://tenor.com/view/jisoo-weekly-idol-blackpink-lisa-rose-gif-8481189",
            "https://cdn.discordapp.com/attachments/808765830019153941/808939170789195786/jisoobeauty_1.gif",
            "https://cdn.discordapp.com/attachments/808765830019153941/808939243857510420/jisoobeauty_2.gif",
            "https://cdn.discordapp.com/attachments/808765830019153941/808939316599980042/jisoobeauty_3.gif",
            "https://cdn.discordapp.com/attachments/808765830019153941/808939410145542204/jisoobeauty_4.gif",
            "https://cdn.discordapp.com/attachments/808765830019153941/808939494514229258/jisoobeauty_5.gif",
            "https://cdn.discordapp.com/attachments/808765830019153941/808939566462402600/jisoobeauty_6.gif",
            "https://cdn.discordapp.com/attachments/808765830019153941/808939631412117554/jisoobeauty_7.gif",
            "https://cdn.discordapp.com/attachments/808765830019153941/808939694590787614/jisoobeauty_8.gif",
            "https://giphy.com/gifs/rt9b5kdGLMEX3GR0ID",
            "https://giphy.com/gifs/zGQVoFhhICEJCRcTtX",
            "https://giphy.com/gifs/Cn7ZDD95iX0X5SThnC",
            "https://giphy.com/gifs/zXYb1Z8Zzv4BpHe1J4",
            "https://gfycat.com/achingfriendlyiridescentshark",
            "https://gfycat.com/adoredvioletlark-blackpink-jisoo-beauty",
            "https://gfycat.com/agitatedorganiceyas",
            "https://gfycat.com/bouncyrequiredibadanmalimbe",
            "https://gfycat.com/calculatingkeenharpseal-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/massiveniftyimperatorangel",
            "https://gfycat.com/showyflatbuzzard-jisoo-kpop-blackpink",
            "https://gfycat.com/chubbyafraidjavalina-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/adolescenthighcommongonolek",
            "https://gfycat.com/contentpeacefulkarakul-blackpink-jisoo-kiss",
            "https://gfycat.com/chubbyafraidjavalina-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/glossydecisiveannelid",
            "https://gfycat.com/complicatednaiveindianjackal",
            "https://gfycat.com/fortunatedecisivediamondbackrattlesnake-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/sardonicdeafeninggreatargus-blackpink-beautiful-jisoo-kpop",
            "https://gfycat.com/teeminguncommonelephant-blackpink-pikachu-dary146-jisoo-kpop",
            "https://gfycat.com/cooltamecardinal",
            "https://gfycat.com/sociabledeadfanworms-blackpink-jisoo-kpop",
            "https://gfycat.com/insistentbesteidolonhelvum-blackpink-jisoo-kpop",
            "https://gfycat.com/harddeepassassinbug-light-up-the-sky-blackpink-reaction-netflix-kiss",
            "https://gfycat.com/lawfulraggedgnat-light-up-the-sky-blackpink-reaction-netflix",
            "https://gfycat.com/colossalthankfulgrub-black-pink-cute-kpop",
            "https://gfycat.com/alarmingacrobaticfiddlercrab-blackpink-jisoo",
            "https://gfycat.com/blackandwhitetidybeauceron-beauty",
            "https://gfycat.com/glossyfakebagworm-blackpink-diaries-jisoo-kpop",
            "https://gfycat.com/poshoddblackbear-blackpink-diaries-variety-jisoo-kpop",
            "https://gfycat.com/ethicalsecretgnatcatcher-blackpink-jisoo",
            "https://gfycat.com/unsungscholarlybass-blackpink-reaction-chichyu-jisoo-kpop-soul-kia",
            "https://gfycat.com/linearhonorableeyelashpitviper",
            "https://gfycat.com/achingchubbyasianporcupine-blackpink-rapping-24365-jisoo-kpop",
            "https://gfycat.com/personallinedgull-blackpink-beautiful-jisoo-kpop-sexy-hot",
            "https://gfycat.com/nauticalbruisedgrayfox-blackpink-beautiful-adorable-jisoo-kpop-cute",
            "https://gfycat.com/shabbyancientcricket-playingwithfire-blackpink-jisoo",
            "https://gfycat.com/gifteddistinctfireant-mechabear-blackpink-jisoo-kpop",
            "https://gfycat.com/grayultimateaustralianfurseal",
            "https://gfycat.com/angelicrequiredkookaburra-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/arcticskinnyannelid-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/bossyclumsybrownbutterfly-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/closedglamorousgalapagosdove-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/clearcutacclaimedcirriped-mechabear-blackpink-jisoo-kpop",
            "https://gfycat.com/excellentshortalaskanhusky-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/glitteringwideeyedgrayreefshark-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/fluiddismalfoal-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/kindheartedvibrantindianjackal",
            "https://gfycat.com/regalwellmadeharborseal-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/rightflusteredborderterrier-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/anxiousbarrenaustraliansilkyterrier-blackpink-kim-ji-soo-kim-ji-soo-blackpink",
            "https://gfycat.com/darkrawivorybilledwoodpecker-blackpink-jisoo",
            "https://gfycat.com/willinglegitimateicterinewarbler",
            "https://gfycat.com/rashunnaturalboto-24365-with-blackpink-jisoo-kpop",
            "https://gfycat.com/embarrassedbrownincatern-blackpink-jennie-jisoo-rose-kpop",
            "https://gfycat.com/watchfuluneveneagle-blackpink-house-jisoo",
            "https://gfycat.com/equalnaughtyharvestmen",
            "https://gfycat.com/masculinecompassionateequine-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/coldsphericalasianpiedstarling-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/blushingelegantarabianhorse-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/tastyflawedgemsbok-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/wiltedlinedafricangoldencat-blackpink-jisoo-kpop",
            "https://gfycat.com/tepidcoldfluke-blackpink-forever-young-live-gif",
            "https://gfycat.com/forkeddisgustingkouprey-running-man-blackpink-jisoo",
            "https://gfycat.com/simplisticmeancurlew-blackpink-mechabear-jisoo-kpop",
            "https://gfycat.com/thirdlegitimatefirefly-blackpink-jisoo-gif-jisooblackpink",
            "https://gfycat.com/liverecentgreatdane-blackpink-jisoo-kill-this-love",
            "https://gfycat.com/defenselessgloriousherculesbeetle-yg-entertainment-blackpink-k-pop-beulraegpingkeu",
            "https://gfycat.com/elaborateblackandwhitefennecfox-yg-entertainment-blackpink-k-pop-beulraegpingkeu",
            "https://gfycat.com/meagerthankfulindianpalmsquirrel-yg-entertainment-blackpink-k-pop-beulraegpingkeu",
            "https://gfycat.com/bittercalmdiscus",
            "https://i.pinimg.com/originals/5d/bb/13/5dbb13535a74b145f79de3effc04734b.gif",
            "https://media1.tenor.com/images/7373f560429be90883dfaad772fd242d/tenor.gif?itemid=18331036",
            "https://blog.kakaocdn.net/dn/nS3FN/btqKnqgPSXP/q4smOv08IU58bLCoRTYCcK/img.gif",
            "https://64.media.tumblr.com/7409bd2985d948fde3e494657c15d1d1/dcee34c3f8654023-3e/s540x810/f0228be7c2492661c0e786e913849df86ad6e3ef.gif",
            "https://64.media.tumblr.com/3ece1de15ffa9064da3962b31846e122/tumblr_pb8gts79Ih1rzt6xso2_500.gif",
            "https://64.media.tumblr.com/8b1ec8bad0c36552fc665782bf986571/a6ff10285d4e2225-d8/s540x810/f679ba1ff552a36add37489f6f96ce3cf5e2c616.gif",
            "https://64.media.tumblr.com/a275393d6030bb1325e4ce2ba026fcc5/0c908319cbab806d-9d/s400x600/9d230106b862153a1eb3b35974b86889110b6efb.gif",
            "https://i.pinimg.com/originals/1a/20/1a/1a201a5b4cb9e0742013513ebf6132b0.gif",
            "https://pa1.narvii.com/7392/97d107dbb4f8777dac0a359f28448f4c5761eb33r1-540-379_hq.gif",
            "https://i.pinimg.com/originals/c5/51/6c/c5516cd46d3f333906ac53c8c1b7f0b8.gif",
            "https://64.media.tumblr.com/f7f925231670628447b01e4a8735671a/tumblr_ospx6kflOE1ujhrw2o1_400.gif",
            "https://i.pinimg.com/originals/f4/b7/8b/f4b78b15f000af3ba891ce492ad58920.gif",
            "https://i.pinimg.com/originals/ab/cd/8c/abcd8ccfede2fafbbae86d8b463fb304.gif",
            "https://pa1.narvii.com/6869/3194051c3ccd363b887ea732ab61070363bf70e0r1-500-500_hq.gif",
            "https://i.pinimg.com/originals/6e/3f/5c/6e3f5c834df6b0a34e28c5db999f9144.gif",
            "https://i.pinimg.com/originals/bf/b4/40/bfb4402c7efedf97df5b53fdebb80824.gif",
            "https://data.whicdn.com/images/349487577/original.gif",
            "https://64.media.tumblr.com/7aea5cf0796c501cfdf60db6685539a7/tumblr_oiyw3hQ2pe1v9nfrqo4_540.gif",
            "https://2.bp.blogspot.com/-uhOwrqhDwMA/W0LaOYdCU8I/AAAAAAAAK8Q/LA7ShEzLQyUfyDQLSeI_GZSgAZlbDU4SwCLcBGAs/s1600/475cc31398dae907c84bb6e8999d1c77.gif",
            "https://media1.tenor.com/images/f40d434d3531e8373d820b67d9aa435d/tenor.gif?itemid=9555280",
            "https://media4.giphy.com/media/l2YWryIjnAZyj7Cms/giphy.gif",
            "https://data.whicdn.com/images/291150225/original.gif",
            "http://images6.fanpop.com/image/photos/40900000/BLACKPINK-Kim-Jisoo-kpop-girl-power-40931799-250-348.gif",
            "https://64.media.tumblr.com/81e359b9aef3defa966035c912c860c5/tumblr_ow17fjHgeD1sxpjiro8_r1_250.gif",
            "https://data.whicdn.com/images/293557533/original.gif",
            "https://data.whicdn.com/images/291150309/original.gif",
            "https://data.whicdn.com/images/300771040/original.gif",
            "https://64.media.tumblr.com/aae42ff2a72d5c02793665a10b738d97/tumblr_ow17fjHgeD1sxpjiro7_r3_250.gif",
            "https://i.pinimg.com/originals/24/cf/8c/24cf8c94810a1f0f9825a46393510eb8.gif",
            "http://images6.fanpop.com/image/photos/40600000/-Jisoo-black-pink-40695211-227-320.gif",
            "http://images6.fanpop.com/image/photos/40400000/-Jisoo-black-pink-40487584-287-347.gif",
            "https://64.media.tumblr.com/ee9deb6ac47c4e0477c4635987bbaffc/tumblr_osmpt1ZiQW1ui9xsvo8_250.gif",
            "https://64.media.tumblr.com/b1f90b82a87aef7ca7aa4d99d51d9ae7/tumblr_osmpt1ZiQW1ui9xsvo5_250.gif",
            "https://64.media.tumblr.com/9a3295a75aafe51a795e1a0cebe6fd01/tumblr_otcx3hA4Fc1vc5dxto4_r1_400.gif",
            "https://64.media.tumblr.com/09ae1c5913154e094a70d7fd2c545459/tumblr_otcynj8PN01vjco6so2_400.gif",
            "https://data.whicdn.com/images/345950395/original.gif",
            "http://images6.fanpop.com/image/photos/40900000/BLACKPINK-Kim-Jisoo-kpop-girl-power-40931797-250-301.gif",
            "https://images6.fanpop.com/image/photos/41400000/-Kim-Jisoo-black-pink-41440680-268-400.gif",
            "https://pa1.narvii.com/7324/9bf9abc49bc9558f53c33f5f45595d6698b00088r1-268-400_hq.gif",
            "https://thumbs.gfycat.com/IllustriousLividBass-size_restricted.gif",
            "https://thumbs.gfycat.com/PoshOddBlackbear-size_restricted.gif",
            "https://i.gifer.com/AraR.gif",
            "https://i.pinimg.com/originals/ba/ca/79/baca7937f1a7645ec0709519ec26558a.gif",
            "https://i.gifer.com/Arae.gif",
            "https://64.media.tumblr.com/1ed8ad4610ab08728ca824d18bb17949/tumblr_obmrqiPosc1rofxd3o1_500.gif",
            "https://media1.giphy.com/media/XieRx2R8O6ZxQQOqIw/giphy.gif",
            "https://thumbs.gfycat.com/GleamingVibrantBagworm-size_restricted.gif",
            "https://p.favim.com/orig/2018/12/29/kim-jisoo-gif-jisoo-Favim.com-6736588.gif",
            "https://i.pinimg.com/originals/e1/80/0e/e1800ed28d4d06c44c77039b6b181db5.gif",
            "https://i.pinimg.com/originals/15/10/61/151061f488aeca85f41b635b37738826.gif",
            "https://i.pinimg.com/originals/18/f4/a2/18f4a26a2e5926af001bdeb25459d5ab.gif",
            "https://data.whicdn.com/images/324656204/original.gif",
            "https://i.pinimg.com/originals/c6/e8/bc/c6e8bcce1f3409e2524872112e919fd4.gif",
            "https://i.pinimg.com/originals/04/7f/d0/047fd01b07d1c30d64fc9cfdefa1dd71.gif",
            "https://64.media.tumblr.com/ab7bd2de3632fe5840c23620fb86fbef/tumblr_pg3k4o0dxI1vc5dxto5_250.gif",
            "https://78.media.tumblr.com/3b14b5a65d4c9e99421a87b35e8d1e3b/tumblr_peqnlim2lf1xx4jy2o3_400.gif",
            "https://images6.fanpop.com/image/photos/41700000/-Jisoo-jisoo-blackpink-41717212-268-360.gif",
            "https://i.pinimg.com/originals/07/ed/ba/07edba69393bb2d0adf630bebd791947.gif",
            "http://images6.fanpop.com/image/photos/40900000/-Happy-Choo-Day-black-pink-40931591-268-350.gif",
            "https://64.media.tumblr.com/6300760d6c6a29627ead39e5b00e778e/tumblr_inline_omop140dcC1udgapp_250.gif"]



    @commands.command()
    async def blackpink(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Blackpink {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "jennie" or arg == "jendeukkie":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{muffin}>, <@{gareth}>, <@{jon}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jennie :dumpling:')
                    await ctx.send(random.choice(self.bot.jennie_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jennie :dumpling:')
                await ctx.send(random.choice(self.bot.jennie_gif))
                await ctx.message.delete()
        elif arg == "rose" or arg == "rosé" or arg == "chaeyoung":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@{jon}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Rosé :rose:')
                    await ctx.send(random.choice(self.bot.rose_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=6)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Rosé :rose:')
                await ctx.send(random.choice(self.bot.rose_gif))
                await ctx.message.delete()
        elif arg == "lisa":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@{jon}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Lisa :cat:')
                    await ctx.send(random.choice(self.bot.lisa_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Lisa :cat:')
                await ctx.send(random.choice(self.bot.lisa_gif))
                await ctx.message.delete()
        elif arg == "jisoo":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@{jon}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jisoo :turtle: :rabbit2:')
                    await ctx.send(random.choice(self.bot.jisoo_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jisoo :turtle: :rabbit2:')
                await ctx.send(random.choice(self.bot.jisoo_gif))
                await ctx.message.delete()


    @commands.command(aliases=['jendeukkie'])
    async def jennie(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@{gareth}>, <@{jon}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jennie :dumpling:')
                await ctx.send(random.choice(self.bot.jennie_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jennie :dumpling:')
            await ctx.send(random.choice(self.bot.jennie_gif))
            await ctx.message.delete()

    @commands.command(aliases=['rosé'])
    async def rose(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{gareth}>, <@{jon}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Rosé :rose:')
                await ctx.send(random.choice(self.bot.rose_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=6)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Rosé :rose:')
            await ctx.send(random.choice(self.bot.rose_gif))
            await ctx.message.delete()

    @commands.command()
    async def lisa(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{gareth}>, <@{jon}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Lisa :cat:')
                await ctx.send(random.choice(self.bot.lisa_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Lisa :cat:')
            await ctx.send(random.choice(self.bot.lisa_gif))
            await ctx.message.delete()

    @commands.command()
    async def jisoo(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{gareth}>, <@{jon}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jisoo :turtle: :rabbit2:')
                await ctx.send(random.choice(self.bot.jisoo_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jisoo :turtle: :rabbit2:')
            await ctx.send(random.choice(self.bot.jisoo_gif))
            await ctx.message.delete()


def setup(client):
    client.add_cog(BlackpinkPings(client))