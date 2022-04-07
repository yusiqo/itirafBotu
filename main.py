# Codes by: @Sirvhan

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
KANAL_ID = os.getenv("KANAL_ID")

IT = Client(
	"İtiraf Bot",
	api_id=API_ID,
	api_hash=API_HASH,
	bot_token=BOT_TOKEN
	)

CHL = -1001555466882

PM = 1340618002

@IT.on_message(
	filters.command("start")
	& filters.private
	)
async def start(client: IT, message: Message):
	await message.reply_text(f"<b> {message.from_user.mention} Xoş Gəldin🥰,Mən @Sirvhan tərəfindən hazırlanan bir etiraf botu’yam.\nEtiraflarınız @səninkanalın kanalında paylaşılacaq🤓.\n\nSəndə bir etiraf etmək istəyirsənsə komutlar;\nAnonim Etiraf: /ano mesaj\nAçıq Etiraf: /etiraf mesaj</b>")

@IT.on_message(
	filters.command("ano")
	& filters.private
	)
async def ano(client: IT, message: Message):
	text = " ".join(message.command[1:])
	if text == "":
		await message.reply_text("Xahiş Olunur Bir Etiraf yazıb yenidən cəhd edin📣.")
	else:
		await IT.send_message(chat_id=CHL, text=f"Göndərən: ANONİM\nEtiraf: {text}")
		time.sleep(0.5)
		await IT.send_message(chat_id=PM, text=f"Göndərən: {message.from_user.mention}\nEtiraf: {text}")
		time.sleep(0.5)
		await message.reply_text("Etirafınız Sahibimə göndərildi təsdiq etdikdən sonra @səninkanalın kanalında paylaşılacaq🥰.")

@IT.on_message(
	filters.command("etiraf")
	& filters.private
	)
async def etf(client: IT, message: Message):
	t = " ".join(message.command[1:])
	if t == "":
		await message.reply_text("Xahiş olunur bir etiraf yazıb təkrar cəhd edin😶.")
	else:
		await IT.send_message(chat_id=CHL, text=f"Göndərən: {message.from_user.mention}\nEtiraf: {t}")
		time.sleep(0.5)
		await message.reply_text("Etirafınız Sahibimə göndərildi təsdiq etdikdən sonra @səninkanalın kanalında paylaşılacaq🥰.")

IT.run()
