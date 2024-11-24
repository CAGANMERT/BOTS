import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send('Merhaba! Bu gençlerin çevre kirliliği hakkında bilgi edinebileceği bir bottur. İsterseniz bir atık türünün başına $ işareti koyarak bilgi edinmeye başlayabilirsiniz!')

@bot.command()
async def plastik_ambalaj(ctx):
    await ctx.send("Genel olarak, plastik ambalaj atıklarının yaklaşık %9'u geri dönüştürülebilirken, diğer plastik türlerinde bu oran daha düşük olabilir.")

@bot.command()
async def plastik(ctx):
    await ctx.send("Yalıtım malzemeleri, oyuncaklar, filmler, ambalajlar ve sera örtüleri plastik atıklara örnektir.")

@bot.command()
async def metal(ctx):
    await ctx.send("Alüminyum içecek kutuları, yağ ve salça tenekeleri, konserve kutuları, mutfak gereçleri, alüminyum folyolar metal atıklara örnektir.")

@bot.command()
async def cam(ctx):
    await ctx.send("İçecek şişeleri, konserve kavanozları, reçel kavanozları, sürahi ve bardak cam atıklara örnektir.")

@bot.command()
async def karton(ctx):
    await ctx.send("Yazışma kâğıtları, karton koliler, kâğıt peçete ve havlular karton atıklara örnektir.")

@bot.command()
async def okyanus(ctx):
    await ctx.send("Bilim insanları, dünyanın yaklaşık yüzde 70'ini kaplayan okyanuslarda tahmini 171 trilyondan fazla plastik parçası bulunduğunu ortaya koydu.")

@bot.command()
async def orman(ctx):
    await ctx.send("Orman yangınlarının çoğunun sebebi atılan cam atıklardır.")

@bot.command()
async def evsel(ctx):
    await ctx.send("Evsel atık, hane sakinlerinin günlük faaliyetleri sonucunda ortaya çıkan ve genellikle çöp olarak adlandırılan atıkları ifade ediyor.")


@bot.command()
async def rastgele(ctx):
    bilgi = [
        "Su kaynaklarının küçük bir bölümü içilebilir fakat kirlilik bu suları içilemez hale getiriyor.",
        "Piller asla doğaya atılmamalıdır çünkü insan dahil olmak üzere birçok canlı için büyük tehlikeler oluşturur",
        "Denizlerde dev gibi çöp adaları olduğunu biliyor muydunuz?",
        "Bazı insanlar çöplerini geri dönüşüm kutularına atarlar ama çoğu insan hangi kutuyu kullanacağını karıştırır.",
        "Tüm dünyanın 2030 yılına kadar gerekleştirmek istediği bazı hedefler vardır ve bu hedeflerin birkaçı çevre ile ilgilidir. Rastgele bir tanesini görmek için $hedef yazabilirsiniz.",
        "Ekosistemlerin yok edilmesi ve habitat yıkımı sonucu olarak çevre kirliliği ortaya çıkar."
    ]
    random_info=random.choice(bilgi)
    await ctx.send(f" Rastgele bir bilgi: {random_info}")

@bot.command()
async def hedef(ctx):
    hedeff = [
        "Temiz Su ve Sanitasyon",
        "Karasal Yaşam",
        "Sudaki Yaşam",
        "İklim Eylemi",
    ]
    random_goal=random.choice(hedeff)
    await ctx.send(f" Rastgele bir hedef: {random_goal}")

bot.run("TOKENİNİZ")

