import requests
import telebot,time
import time
from telebot import types
from gatet import Tele
import os
token = '7576631410:AAF_ZSJzJW6rj2wDug6H1jznz8gIsUSmFDg' #bottoken
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber = '1177047392'
allowed_users = ['1177047392']  #Your ID
@bot.message_handler(commands=["start"])
def start(message):
    if str(message.chat.id) not in allowed_users:
        bot.reply_to(message, "🚫 𝐘𝐨𝐮 𝐜𝐚𝐧𝐧𝐨𝐭 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐭𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫𝐬 𝐭𝐨 𝐩𝐮𝐫𝐜𝐡𝐚𝐬𝐞 𝐚 𝐛𝐨𝐭 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 @Ownerxxxxx")
        return
    bot.reply_to(message, "𝐒𝐞𝐧𝐝 𝐭𝐡𝐞 𝐭𝐱𝐭 𝐟𝐢𝐥𝐞 𝐧𝐨𝐰")
@bot.message_handler(commands=["add"])
def add_user(message):
    if str(message.chat.id) == '6191863486':  # Only bot owner can add new users
        try:
            new_user_id = message.text.split()[1]  # Extract new user ID from the command
            allowed_users.append(new_user_id)
            bot.reply_to(message, f"User ID {new_user_id} Has Been Added Successfully.✅\nCongratulations! Premium New User🎉✅ ")
        except IndexError:
            bot.reply_to(message, "Please provide a valid user ID. Example: /add 123456789")
    else:
        bot.reply_to(message, "You do not have permission to add users.🚫")
@bot.message_handler(content_types=["document"])
def main(message):
	if str(message.chat.id) not in allowed_users:
		bot.reply_to(message, "🚫 𝐘𝐨𝐮 𝐜𝐚𝐧𝐧𝐨𝐭 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐭𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫𝐬 𝐭𝐨 𝐩𝐮𝐫𝐜𝐡𝐚𝐬𝐞 𝐚 𝐛𝐨𝐭 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 @Ownerxxxxx")
		return
	dd = 0
	live = 0
	incorrect = 0
	ch = 0
	ko = (bot.reply_to(message, "𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐂𝐚𝐫𝐝 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 ...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @Ownerxxxxx')
						os.remove('stop.stop')
						return
				try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
				except: pass
				try:
					brand = data['brand']
				except:
					brand = 'Unknown'
				try:
					card_type = data['type']
				except:
					card_type = 'Unknown'
				try:
					country = data['country_name']
					country_flag = data['country_flag']
				except:
					country = 'Unknown'
					country_flag = 'Unknown'
				try:
					bank = data['bank']
				except:
					bank = 'Unknown'
				
				start_time = time.time()
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "Error"
				if 'Stripe Error: Your card was declined.' in last:
					last='Your Card Was Declined'
				elif 'Declined - Call Issuer' in last:
					last='Declined - Call Issuer'
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				status = types.InlineKeyboardButton(f"• 𝐒𝐓𝐀𝐓𝐔𝐒  : {last} ", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• 𝐀𝐏𝐏𝐑𝐎𝐕𝐄𝐃 ✅ : [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝐅𝐀𝐊𝐄 𝐂𝐀𝐑𝐃 ⚠️ : [ {incorrect} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝐃𝐄𝐂𝐋𝐈𝐍𝐄𝐃 ❌ : [ {dd} ] •", callback_data='x')
				cm6 = types.InlineKeyboardButton(f"• 𝐓𝐎𝐓𝐀𝐋 🎉       :  [ {total} ] •", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 🚫 ]", callback_data='stop')
				mes.add(cm1,status, cm3, cm4, cm5, cm6, stop)
				end_time = time.time()
				execution_time = end_time - start_time
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''𝐖𝐚𝐢𝐭 𝐟𝐨𝐫 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 
𝐁𝐲 ➜ <a href='t.me/Approved_Raven'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a> ''', reply_markup=mes)
				msg = f'''
<a href='t.me/Approved_Raven'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/Approved_Raven'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/Approved_Raven'>┃</a>𝐂𝐂 <code>{cc}</code><a href='t.me/Approved_Raven'>┗━━━━━━━⊛</a>
<a href='t.me/Approved_Raven'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Stripe Charge 5$</code>		
<a href='t.me/Approved_Raven'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Payment Successful 🎉</code>

<a href='t.me/Approved_Raven'>-</a> 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank}</code>

<a href='t.me/Approved_Raven'>-</a> 𝐓𝐢𝐦𝐞: <code>1{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/Approved_Raven'>⏤͟͞𝑮𝑺𝑰𝑿 𓆩 𝑪𝑯𝑲 𓆪ꪾᶜⁿꪜ</a>'''
				print(last)
				if 'success' in last or 'Processor Declined - Fraud Suspected' in last or 'Declined - Call Issuer' in last or 'Stripe Error: Your card does not support this type of purchase.' in last or "Stripe Error: Your card's security code is invalid." in last:
					live += 1
					bot.reply_to(message, msg)
				elif 'Card Not Activated' in last:
					incorrect+=1
				elif 'security code is incorrect.' in last:
					msg = f'''
<a href='t.me/Approved_Raven'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅ 
<a href='t.me/Approved_Raven'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/Approved_Raven'>┃</a>𝐂𝐂 <code>{cc}</code><a href='t.me/Approved_Raven'>┗━━━━━━━⊛</a>
<a href='t.me/Approved_Raven'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Stripe Charge 5$</code>		
<a href='t.me/Approved_Raven'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>AUTH Completed 🟢</code>

<a href='t.me/Approved_Raven'>-</a> 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank}</code>

<a href='t.me/Approved_Raven'>-</a> 𝐓𝐢𝐦𝐞: <code>1{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝 </code>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/Approved_Raven'>⏤͟͞𝑮𝑺𝑰𝑿 𓆩 𝑪𝑯𝑲 𓆪ꪾᶜⁿꪜ</a>'''
					live += 1
					bot.reply_to(message, msg)
				elif 'Card Not Activated' in last:
					incorrect+=1
				elif 'security code is incorrect.' in last or 'Stripe Error: Your card has insufficient funds.' in last or 'tree_d' in last:
					msg = f'''
<a href='t.me/Approved_Raven'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅!!
<a href='t.me/Approved_Raven'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/Approved_Raven'>┃</a>𝐂𝐂 <code>{cc}</code><a href='t.me/Approved_Raven'>┗━━━━━━━⊛</a>
<a href='t.me/Approved_Raven'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Stripe Charge 5$</code>		
<a href='t.me/Approved_Raven'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Insufficient Funds ❎</code>

<a href='t.me/Approved_Raven'>-</a> 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank}</code>

<a href='t.me/Approved_Raven'>-</a> 𝐓𝐢𝐦𝐞: <code>2{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝 </code>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/Approved_Raven'>⏤͟͞𝑮𝑺𝑰𝑿 𓆩 𝑪𝑯𝑲 𓆪ꪾᶜⁿꪜ</a>'''
					live += 1
					bot.reply_to(message, msg)
				elif 'Card Not Activated' in last:
					incorrect+=1
				else:
					dd += 1
					time.sleep(10)
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @Ownerxxxxx')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
logop = f'''━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'''
print(logop)
bot.polling()
