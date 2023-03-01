import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from Config import Config 


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
bot_username = Config.BOT_USERNAME
support = Config.SUPPORT_CHAT
owner = Config.OWNER_USERNAME
bot_name = Config.BOT_NAME


SUDO_USERS = Config.SUDO_USERS


client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []
  

	
	
	
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"**🤖Salam...💭,**\nMənim Adım [Riyad Tag Bot](http://t.me/Riyadtagrobot)-u.\n**Qurupunuz'daki  bütün üzvləri tağ etmək səlahiyyətinə sahibəm.\n\n🤖Ətraflı müəlumat üçün '📚Əmrlər' bölməsinə daxil olun.**", buttons=(
                     [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/RiyadTaggbot?startgroup=a')],
	             [Button.inline(f"📚 Əmrlər", data="help"),
	              Button.inline(f"📑 Təkliflər", data="reklam")],
	             [Button.url('Qrup💬', 'https://t.me/RiyaddBlogg'),
                      Button.url('Sahib 👨‍💻', 'https://t.me/RiyadAndMe')],
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"** [Riyad Tag Bot](http://t.me/RiyadTagrobot)'un Əmrlər üçün?.Bot'a daxil olub.**", buttons=(
                     [Button.url('💡Bota Keç','https://t.me/Riyadtagrobot?start=start')],
	             [Button.url('Sahib 👨‍💻', 'https://t.me/RiyadAndMe'),
		      Button.url('Qrup💬', 'https://t.me/RiyaddBlogg')],
                    ),
                    link_preview=False)



@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"**🤖Salam...💭,**\nMənim Adım [Riyad Tag Bot](http://t.me/Riyadtagrobot)-u.\n**Qurupunuz'daki  bütün üzvüləri tağ etmək səlahiyyətinə sahibəm.\n\n📢Ətraflı müəlumat üçün '📚Əmrlər' bölməsinə keçid edin.**", buttons=(
                     [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/riyadtagrobot?startgroup=a')],
	             [Button.inline(f"📚 Əmrlər", data="help"),
	              Button.inline(f"📑 Təkliflər", data="reklam")],
	             [Button.url('Qrup💬', 'https://t.me/RiyaddBlogg'),
                      Button.url('Sahib 👨‍💻', 'https://t.me/RiyadAndMe')],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):	
    await event.edit(f"**  [Ədalət Tag Bot](http://t.me/Riyadtagbot)-un Kömək '📚 Əmrlər' Bunlardır.⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**🤖➪ /tag <səbəb> - 5-li Tag Atışları.**\n**🤖➪ /etag <səbəb> - Emoji ilə etiketlər.**\n**🤖➪ /stag <səbəb> - Söz'lü Tag etiketlər.**\n**🤖➪ /tektag <səbəb> - Üzvləri Tək-Tək etiketlər.**\n**🤖➪ /admins <səbəb> - İdarəçilər Tək-Tək etiketlər.**\n**🤖➪ /cancel - Tag Ələməyi Dayandır.**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
	             [Button.url('Qrup💬', 'https://t.me/EdaletSup'),
                      Button.url('Sahib 👨‍💻', 'https://t.me/edalet_22')],
	             [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="reklam"))
async def handler(event):	
    await event.edit(f"**📌 [Riyad Tag Bot](http://t.me/Riyadtagrobot)-un & Təkliflər üçün sahib'lə əlaqə saxlaya bilərsiniz...**", buttons=(
		     [Button.url('🧑‍💻 Sahib', 'https://t.me/RiyadAndMe')],
	             [Button.url('Qrup💬', 'https://t.me/RiyaddBlogg'),
                      Button.url('Sahib 👨‍💻', 'https://t.me/RiyadAndMe')],
	             [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)
	
    
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


emoji = "😀 🐵 🍓 😃 🦁 🍒 😄 🐯 🍎 😁 🐱 🍉 😆 🐶 🍑 😅 🐺 🍊 😂 🐻 🥭 🤣 🐨 🍍 😭 🐼 🍌 😗 🐹 🌶 😙 🐭 🍇 😚 🐰 🥝 😘 🦊 🍐 🥰 🦝 🍏 🤩 🐮 🍈 🥳 🐷 🍋 🤗 🐽 🍄 🙃 🐗 🥕 🙂 🦓 🍠 ☺️ 🦄 🧅 😊 🐴 🌽 😏 🐸 🥦 😌 🐲 🥒 😉 🦎 🥬 🤭 🐉 🥑 😶 🦖 🥯 😐 🦕 🥖 😑 🐢 🥐 😔 🐊 🍞 😋 🐁 🌰 😛 🐀 🥔 😝 🐇 🧄 😜 🐈 🍆 🤪 🐩 🧇 🤔 🐕 🥞 🤨 🦮 🥚 🧐 🐕‍🦺 🧀 🙄 🐅 🥓 😒 🐆 🥩 😤 🐎 🍗 😠 🐖 🍖 🤬 🐄 🥙 ☹️ 🐂 🌯 🙁 🐃 🌮 😕 🐏 🍕 😟 🐑 🍟 🥺 🐐 🥨 😳 🦌 🥪 😬 🦙 🌭 🤐 🦥 🍔 🤫 🦘 🧆 😰 🐘 🥘 😨 🦏 🍝 😧 🦛 🥫 😦 🦒 🥣 😮 🐒 🥗 😯 🦍 🍲 😲 🦧 🍛 😱 🐪 🍜 🤯 🐫 🍢 😢 🐿️ 🥟 😥 🦨 🍱 😓 🦡 🍚 😞 🦔 🥡 😖 🦦 🍤 😣 🦇 🍣 😩 🐓 🦞 😫 🐔 🦪 🤤 🐣 🍘 🥱 🐤 🍡 😴 🐥 🥠 😪 🐦 🥮 🤢 🦉 🍧 🤮 🦅 🍨 🤧 🦜 🍫 🤒 🪱 🍪 😶‍🌫 🕊️ 🥜 🤠 🦢 🍭 🤑 🦩 🧈 🤤 🦃 🦚 🥵 🦆 🫑 🥶 🐧 🍥 🥸 🦈 🍦 🤓 🐳 🍳 😇 🐝 🥧 🤭 🐌 🥤 🤫 🦋 🍨".split(" ")
  


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Tag'a başlamaq üçün səbəb yazın...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("** Tag əməliyyatı uğurla dayandırıldı!**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! ** ")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! **")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 5:   
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond(" **Tag əməliyyatı uğurla dayandırıldı! **")
        return
      if usrnum == 5:   
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! **")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! ** ")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**↯ [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	

stag = (
"Qaş qabağın yerlə gedir",
"De görüm neyləmişəm",
"Ürəyim gup-gup edir",
"Bir günahım yoxdur, inan",
"Varsa – de, olum qurban!",
"Dözmərəm bu hala mən",
"Ölürəm az qala mən",

"Bir mənə bax, naz eyləmə",
"Qaş qabaq tökmə belə",
"Gəl mənə dağ çəkmə belə",

"Kim nə deyib, söylə, görüm",
"Səni yoldan eyləyib?",
"Kim sənə nə danışıb",
"Məni xortdan eyləyib?",
"Hardadır o mərdiməzar?",
"Onu qoy tutsun azar!..",

"Dağlarda duman gözəldir",
"Qaşların - kaman gözəldir",
"Sözünə heç bir söz olmaz",
"Gözlərin yaman gözəldir",
"Alıbdır ağlımı başdan",
"Keçmək olmaz bu göz-qaşdan",
"Səni mən yaman sevirəm",
"Ürəkdən, candan sevirəm",
"Mənə gəl eylə vəfa, yar",
"Aşiqə etmə cəfa, yar",
"Söyüdlər başın əyəndə",
"Sənə mən yarım deyəndə",
"Sanıram dünya mənimdir",
"Gözümə gözün deyəndə",
"Alıbdır ağlımı başdan",
"Keçmək olmaz bu göz-qaşdan",
"Səni mən yaman sevirəm",
"Ürəkdən, candan sevirəm",
"Mənə gəl eylə vəfa, yar",
"Aşiqə etmə cəfa, yar",
"O qara göz olmasaydı",
"Əhdimiz düz olmasaydı",
"Sənə heç könül verərdim",
"Sözümüz söz olmasaydı?",

"Gedirəm bu axşam, gedirəm gülüm",
"Bilirəm gül üzün solacaq mənsiz",
"Gedirəm gəlməsəm qalacaq sevgim",
"Bəlkə də gözlərin dolacaq mənsiz",
"Yaşadır sevdalı bir xəyal məni",
"Gedirəm gəlməsəm yada sal məni",
"Bürüyüb göyləri indi çən, duman",
"Torpaq dilə gəlib aman! ay aman!",
"Vətən gözü yaşlı qalsa o zaman",
"Ay Allah, sevgilim qalacaq mənsiz!",

"Axtarıb tapdım səni ",
"Sən dəmi sevdim, yar, məni? ",
"Gör nə haldır görmür gözüm Şadlığımdan dünyanı",
"Gəl gəl, maralım, gəl",
"Gəl, ceyranım, gəl",
"Halal olsun Süleyman",
"Sən nə kələkbazsan, şeytan!",
"Öyrədib məni yola saldın",
 "Mənə rast gəldi yarcan",
"Dünyaya sığdıra bilmədim inan dərdlərimi",
"Bu qədər dərd içində dərman olub neyləmisən?",
"Hər sözünə can deyən insandan əsər qalmadı Bax",
"Nə fayda Can deməyim canan olub neyləmisən?",
"Düşünrsənmi sən hərdən görəsən nə haldadır?",
"Bəlkə mənsiz çətindədir boranda ya Qardadır",
"Bəlkə də məndən uzağ ölümlərdədi dardadı",
"Düşünmədin nə fayda insan olub neyləmisən?",
"Yanımda yad biri ilə xoşbəxtliyi təsvir edir",
"Səni yadlarla görəndə ruh bədəni təslim edir",
"O qədər dərd içində əzab vermə bəsdi dedim",
"Sənə görə yar ürəyim al-qan olub neyləmisən?",
"Hər gecə xəyalınla yuxuya dalır bu gözlərim",
"Mən səni gecəni gözləyən ulduz qədər gözlədim",
"Bir dəfə heç olmasa yanıma qonaq gəl istədim",
"Hər gecə xəyalımda mehman olub neyləmisən?",
"Sənə çox can dedim ey can,can olub neyləmisən?",
"Demə canan özünə, canan olub neyləmisən?",
"Getmisən daima biganəni şad eyləmisən",
"Həsrətinlə ürəyim al-qan olub, neynəmisən?",
"Bax indi min cür əzab var başımın üstün duman",
"Mənsiz xoşbəxtdir uzaqlarda eylə güman",
"Mən sənə xəyanət etməm düşünmə əsla bir an" ,
"Xoşbəxtliyi bəxş etməyə fərman olub neyləmisən?",
"Həyatım səliqəlidir istəsən dağıt yenidən",
"Çox heyif gör kimləri qonağ eylədin yerimə",
"Artıq çox yorulmuşam dönürəm day geri mən",
"Biryerdə yolu yeriməyə imkan olub neyləmisən?",
"Gül olub neyləmisən bağçalarda qar borandı",
"Sevirəm söyləmə məni inandırma yar yalandı",
"Buludlar qan ağlayır hər gecələr bu nə qandı?",
"Ürəyim həsrətinlə viran olub neyləmisən?",
"Nə xəyalım var idi səninlə sən məhv elədin",
"O qədər qırmısan ki ürəyim səni əhv eləmir",
"Deyirsən qurban olum məni bağışla səhv elədim",
"Hər dəfə səhvinə görə qurban olub neyləmisən?",

)	

@client.on(events.NewMessage(pattern="^/stag ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! ** ")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! ** ")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! ** ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def tag_admin(event):
    chat = await event.get_input_chat()
    text = "♕︎Adminlər Siyahısı♕︎"
    async for x in event.client.iter_participants(chat, 100, filter=ChannelParticipantsAdmins):
        text += f" \n ↯ [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)
    raise StopPropagation


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)

	
@client.on(events.NewMessage(pattern="^/Ədalət ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! ** ")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! ** ")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(usta)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(usta)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! ** ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

usta = ('Buda kimmiş də miş miş👀😁😍','🙄👉🤲Aağil','🙄 Sən dediyim sözü elədin? 😐','Həyatımın dolması 🥲 nassın😍','Mənə niyə elə baxırsan? 🌝','İkinci planda olmaqdansa, plana daxil olmamağı seçərəm.  🎯','səni basqa qrublardada görmüsdüm ','Ac olanda sən o sən deyilsən','Niyə yalan danışırsan adamın üstündə patalok var','Həci necəsən ficuuu ','köhnə məkanın yeni sakini ','günün günnən durdun uzax de görüm haramı bəyənmədin','deyrlər ölübsən🤔','Güçlüyüm... Çünkü başka seçeneğim yok düşersem tutanım olmayacak biliyorum...🚬','gəl bir birimizi arka sokaklar bitənə qədər sevək❤️','corona belə böyüdü sən böyümədin','corona belə unduldu səni unuda bilmədim🚬','səni sevirəm sözündə neçə dənə samit var','oğlanlar niyə az yaşayır','bitkilər yaşlandıqcamı ölər yoxsa baxımsızlıqdanmı','isti havada çay içirsən hələdə','allah rəhmət eləsin','tez gəlin hədiyyəli yarışımız basladı','Benim hayelerim kelebeğin ömrü kadar yaşar 💔🥀','Çiçəklərə aşağıdan baxmağa gedirəm..➰','susмuş вir qadın üçün... вiтмiş вir adaмsan.! 🖤','𝚂ə𝚏𝚕ə𝚛𝚒𝚗𝚒 𝚞̈𝚣𝚕ə𝚛𝚒𝚗ə 𝚟𝚞𝚛𝚖𝚊𝚍𝚒𝚐̆𝚒𝚖𝚒𝚣 𝚞̈𝚌̧𝚞̈𝚗 𝚘̈𝚣𝚕𝚎𝚛𝚒𝚗𝚒 𝚚𝚞̈𝚜𝚞𝚛𝚜𝚞𝚣 𝚜𝚊𝚗𝚊𝚗 𝚒𝚗𝚜𝚊𝚗𝚕𝚊𝚛 𝚟𝚊𝚛😒','Güclü olmağa məndən daha çox ehtiyacın var, çünki haqsız olduğunu ürəyinin bir yerində bilirsən.🤙','Makiyaj və üz boyalarınıza güvənməyin. Yollar da gözəldir, lakin altından kanalizasiya keçir.👋😉','𝙸̇𝚝𝚒𝚛𝚍𝚒𝚢𝚒𝚗 𝚟𝚊𝚡𝚝𝚒 𝚚𝚊𝚢𝚝𝚊𝚛𝚊 𝚋𝚒𝚕𝚖ə𝚍𝚒𝚢𝚒𝚗 𝚔𝚒𝚖𝚒 𝚎𝚕ə𝚍𝚒𝚢𝚒𝚗 𝚙𝚒𝚜𝚕𝚒𝚢𝚒 𝚍ə 𝚑𝚎𝚌̧ 𝚟𝚊𝚡𝚝 𝚍𝚞̈𝚣ə𝚕𝚍ə 𝚋𝚒𝚕𝚖𝚎𝚢ə𝚌𝚎𝚔𝚜ən😐','𝙱𝚒𝚛𝚊𝚣 𝚒𝚗𝚜𝚊𝚗 𝚘𝚕 𝚍𝚎𝚢e𝚌ə𝚖 𝚊𝚖𝚖𝚊 𝚜ə𝚗𝚒 𝚍ə 𝚌̧ə𝚝𝚒𝚗 𝚟ə𝚣𝚒𝚢𝚢ə𝚝𝚍ə 𝚚𝚘𝚢𝚖𝚊𝚐̆ 𝚒𝚜𝚝ə𝚖𝚒𝚛ə𝚖🤧','İnsanlığa dəvət etdikdə yolu soruşan insanlar var.🔥😂','Qoyduğum şeyləri öz yerində tapa bilmirəm. Bəzilərini adam yerinə qoydum, indi gəl tap görün necə tapırsan✊','Ayə biri bunu aparsın🫢','Əgər bu həyatda öz tayını tapa bilmirsənsə üzülmə, deməli sən tayı bərabəri olmayan birisən.Qabriel Qarsia Markuez (Meksikalı yazıçı)🥲','Xoş Gəldim Nəfəs🥲','Gəlmirsən Balaca😒','Kimə Yazısan??? 🤨','Çirkin Çocuq Gəl😌','Cikolatam😍','Aaa Səndə Burdasan😳','Al Sənə Çikolata🤓👉🍫','Sevmirsən Məni?🙁 Onda Ol🙂','Haa Düz derisən?🧐','Bu Kimdir😁','Gəl Dava Edəx😁💪','Bax Sənə Nə Aldım😌👉🐒','Nə Gözəlsən🤢 Çirkin Ördək Yavrusu','Sən Kimsən🙄A Gədə👀','Gəl Sənə Sürpürüzüm var🤫','Ooo Çox Gözəlsin🤌🤐Bal','Şəxsiyə Yaz😌dünbələx','Gəl Görüm Hələ🧐 Nə demisən Mənə😬','Ayib Olsun😫 Niyə Yazmırsan😑','Bezdim Səndən🥲','Bu Neçədir✌️🙂','Nömrəni ver də Vpda yazışa🙊','👉👀 Gözün Çıxsın gəl😒','ımmm Gəl yogo yapalım🧘‍♀🤭','gəl sənə bıra süzdüm😪🍻','Ağlımı Başımdan ala şəxs😵‍💫gəl mənə doğru','Səni gördüm qızmam qalxdə🤒',) 


@client.on(events.NewMessage(pattern='/offline'))
async def handler(event):
    # Kimsə "Salam" və başqa bir şey deyəndə cavab verin
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("__Sən mənə sahib deyilsən!__")
    await event.reply('**Bot İşləyir Narahat olmayın** \n https://t.me/RiyadAndMe \n\n╭━━━╮ \n╰╮╭╮┃╱╱╭╮\n╱┃┃┃┣━━╋╋━━┳╮╭┳╮╭╮\n╱┃┃┃┃┃━╋┫╭╮┃╰╯┃┃┃┃\n╭╯╰╯┃┃━┫┃╭╮┣╮╭┫╰╯┃\n╰━━━┻━━┫┣╯╰╯╰╯╰━━╯\n╱╱╱╱╱╱╭╯┃\n╱╱╱╱╱╱╰━╯',
		     buttons=(
	             [Button.url('Sahibi','https://t.me/RiyadAndMe'),
	             Button.url('Qroup','https://t.me/RiyaddBlogg')],
                    ),
                    link_preview=False)

print(">> Bot işləyir narahat olmayın. @RiyadAndMe Məlumat almaq üçün <<")
client.run_until_disconnected()
