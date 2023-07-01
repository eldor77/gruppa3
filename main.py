import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ChatPermissions
from datetime import timedelta 


API_TOKEN = '5985952193:AAGwKSap1VniWJ5URtlyYMlvHD6X_kNosMM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello")



@dp.message_handler(text="/mute", is_chat_admin=True)
async def echo(message: types.Message):
    if message.chat.type in ["supergroup", "group"]:
        if not message.reply_to_message or not message.reply_to_message.from_user:
            await message.reply("Пожалуйста, выделите определенного пользователя и потом напишите код")
            return


        user_to_mute = message.reply_to_message.from_user
        await bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_to_mute.id,
            permissions=ChatPermissions(
            can_send_messages=False,
            ),
            until_date=message.date + timedelta(minutes=30)
        )

        await message.reply(f"{user_to_mute.mention} 30 секунд не можете писать")




@dp.message_handler(text="/unmute", is_chat_admin=True)
async def unmute_user(message: types.Message):
    if message.chat.type in ["supergroup","group"]:
        if not message.reply_to_message or not message.reply_to_message.from_user:
            await message.reply("Пожалуйста, выделите определенного пользователя и потом напишите код")
            await message.bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            return


        user_to_unmute = message.reply_to_message.from_user
        await bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_to_unmute.id,
            permissions=ChatPermissions(
            can_send_messages=True,can_send_audios=True,can_send_documents=True
            ),
        )




@dp.message_handler(text="!ban", is_chat_admin=True)
async def unmute_user(message: types.Message):
    if message.chat.type in ["supergroup","group"]:
        if not message.reply_to_message or not message.reply_to_message.from_user:
            await message.reply("Пожалуйста, выделите определенного пользователя и потом напишите код")
            await message.bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            return
        

        user_to_kick = message.reply_to_message.from_user
        await bot.kick_chat_member(
            chat_id=message.chat.id,
            user_id=user_to_kick.id,
        )
        await message.reply(f"{user_to_kick.mention} вас кикнули")
        


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)