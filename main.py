# Codes by:yusiqo

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
KANAL_ID = os.getenv("KANAL_ID")

IT = Client(
	"襤tiraf Bot",
	api_id=API_ID,
	api_hash=API_HASH,
	bot_token=BOT_TOKEN
	)

CHL = -1001585881397

PM = 1342133634

@IT.on_message(
	filters.command("start")
	& filters.private
	)
async def start(client: IT, message: Message):
	await message.reply_text(f"<b> {message.from_user.mention} Ho?? Geldim??弘,Ben @yusiqo Taraf覺ndan Kodlanan Bir 襤tiraf Botuyum \nEtiraflar覺n覺z @itirafHanem Kanal覺nda Payla??覺lacakt覺r????.\n\n\nAnonim 襤tiraf: /ano mesaj\nA癟覺k 襤tiraf: /itiraf mesaj</b>")

@IT.on_message(
	filters.command("ano") 
	& filters.private
	)
async def ano(client: IT, message: Message):
	text = " ".join(message.command[1:])
	if text == "":
		await message.reply_text("L羹tfen Bi 襤tiraf Yaz覺p Tekrar Deneyiniz????.")
	else:
		await IT.send_message(chat_id=CHL, text=f"G繹nderen: ANON襤M\n襤tiraf: {text}")
		time.sleep(0.5)
		await IT.send_message(chat_id=PM, text=f"G繹nderen: {message.from_user.mention}\n襤tiraf: {text}")
		time.sleep(0.5)
		await message.reply_text("襤tiraf Onayland覺ktan Hemen Sonra Kanalda Payla??覺lacakt覺r??弘.")

@IT.on_message(
	filters.command("itiraf")
	& filters.private
	)
async def etf(client: IT, message: Message):
	t = " ".join(message.command[1:])
	if t == "":
		await message.reply_text("L羹tfen Bi 襤tiraf Yaz覺p Tekrar Deneyiniz????.")
	else:
		await IT.send_message(chat_id=CHL, text=f"G繹nderen: {message.from_user.mention}\n襤tiraf: {t}")
		time.sleep(0.5)
		await message.reply_text("襤tiraf Onayland覺ktan Hemen Sonra Kanalda Payla??覺lacakt覺r??弘.")

IT.run()
