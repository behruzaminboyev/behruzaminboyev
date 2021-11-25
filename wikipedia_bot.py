import wikipedia
from aiogram import Bot ,Dispatcher, executor, executor, types
API_TOKEN = '2141866125:AAHudp3Khw60f_Bjj9bz3YW0FIcQYlE1MEs'
wikipedia.set_lang('uz')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types):
    
    await message.reply("Assalomu aleykum😊")

    await message.reply("Qidirmoqchi bolgan matningnni kiriting:")


@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        javob = wikipedia.summary(message.text)
        await message.answer(javob)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
