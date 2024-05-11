import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardButton
from aiogram.filters import CommandStart
from config import *
import os
import openai

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    kb = [
            [
            types.KeyboardButton(text="Новини"),
            types.KeyboardButton(text="Вчителі"),
            types.KeyboardButton(text="Адміністрація")
            ],
            [
            types.KeyboardButton(text="Розклад"),
            types.KeyboardButton(text="Контакти"),
            types.KeyboardButton(text="Інше питання")
            ],
            [
            types.KeyboardButton(text="Підготовка до НМТ"),
            types.KeyboardButton(text="ШІ-асистент"),
            types.KeyboardButton(text="Адмінпанель")
            ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Оберіть одну з кнопок:"
    )
    await message.answer("Вас вітає Бот-Козак, який завжди готовий прийти на допомогу! Оберіть одну з кнопок, щоб я зміг бути Вам корисним:", reply_markup=keyboard)

@dp.message(F.text.lower() == "повернутися")
async def cmd_start(message: types.Message):
    kb = [
            [
            types.KeyboardButton(text="Новини"),
            types.KeyboardButton(text="Вчителі"),
            types.KeyboardButton(text="Адміністрація")
            ],
            [
            types.KeyboardButton(text="Розклад"),
            types.KeyboardButton(text="Контакти"),
            types.KeyboardButton(text="Інше питання")
            ],
            [
            types.KeyboardButton(text="Підготовка до НМТ"),
            types.KeyboardButton(text="ШІ-асистент"),
            types.KeyboardButton(text="Адмінпанель")
            ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Оберіть одну з кнопок:"
    )
    await message.answer("Вас вітає Бот-Козак, який завжди готовий прийти на допомогу! Оберіть одну з кнопок, щоб я зміг бути Вам корисним:", reply_markup=keyboard)

@dp.message(F.text.lower() == "новини")
async def news(message: types.Message):
    await message.reply("У нас є гарні новини! Перейдіть за посиланням, щоб побачити свіжу інформацію: http://inter4.zp.ua/news\nТакож завітайте до наших соц-мереж:\nInstagram: https://www.instagram.com/zp.cossack_lyceum/\nFacebook: https://www.facebook.com/profile.php?id=100094544324104&locale=uk_UA")

@dp.message(F.text.lower() == "вчителі")
async def teachers(message: types.Message):
    await message.reply("Вчителі завжди готові вам допомогти! Ось педагоги нашої школи: http://inter4.zp.ua/teacher/view_one/?parent_id=2")

admin1 = FSInputFile("img/1.jpg")
admin2 = FSInputFile("img/2.jpg")
admin3 = FSInputFile("img/3.jpg")
admin4 = FSInputFile("img/4.jpg")

@dp.message(F.text.lower() == "адміністрація")
async def administration(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=admin1, caption='Губіна Оксана Олександрівна\nДиректор, вчитель української мови та літератури ("спеціаліст вищої категорії", "старший учитель")')
    await bot.send_photo(chat_id=message.chat.id, photo=admin2, caption='Котова Тетяна Миколаївна\nЗаступник директора з виховної роботи, вчитель географії ("спеціаліст вищої категорії", "старший учитель")')
    await bot.send_photo(chat_id=message.chat.id, photo=admin3, caption='Дмитрів Лариса Миколаївна\nЗаступник директора з методичної роботи, вчитель української мови та літератури ("спеціаліст вищої категорії", "старший учитель")')
    await bot.send_photo(chat_id=message.chat.id, photo=admin4, caption='Ушатий Володимир Миколайович\nЗаступник директора з навчальної роботи, вчитель географії, економіки, інформатики ("спеціаліст вищої категорії")')

@dp.message(F.text.lower() == "розклад")
async def schedule(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="5"),
            types.KeyboardButton(text="6"),
            types.KeyboardButton(text="7")
        ],
        [
            types.KeyboardButton(text="8"),
            types.KeyboardButton(text="9"),
            types.KeyboardButton(text="10")
        ],
        [
            types.KeyboardButton(text="11"),
            types.KeyboardButton(text="Повернутися")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Оберіть свій клас:"
    )
    await message.answer("Оберіть свій клас:", reply_markup=keyboard)

@dp.message(F.text.lower() == "5")
async def five(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "6")
async def six(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "7")
async def seven(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")
@dp.message(F.text.lower() == "8")
async def eight(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "9")
async def nine(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "10")
async def ten(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "11")
async def eleven(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "контакти")
async def contacts(message: types.Message):
    await message.reply("Контакти:\nНазва закладу: Комунальний заклад 'Запорізька спеціалізована школа-інтернат ІІ-ІІІ ступенів 'Козацький ліцей'' Запорізької обласної ради\nСкорочена назва: Запорізька школа-інтернат 'Козацький ліцей'\nАдреса: 69065, Запоріжжя, Дніпровський район, вул. Щаслива, 2\nТелефон/факс: +38 (061) 224-79-67\nЕ-mail: zp.inter4@ukr.net")

@dp.message(F.text.lower() == "інше питання")
async def another(message: types.Message):
    await message.reply("Якщо тут нема відповіді на ваше питання, то залиште його тут і ми надамо відповідь впродовж 24-х годин!")

@dp.message(F.text.lower() == "підготовка до нмт")
async def choose_nmt(message: types.Message):
    await message.reply("Телеграм-канали, які можуть вам допомогти із підготовкою:\nМатематика:\nhttps://t.me/znohub_math\nhttps://t.me/twobeeschool_math\nhttps://t.me/kevin_math_zno\nУкраїнська мова:\nhttps://t.me/kevin_ukrainian_zno\nhttps://t.me/znohub_ukr\nhttps://t.me/ukr_movaaa\nhttps://t.me/ukr_mova\nАнглійська мова:\nhttps://t.me/znohub_eng\nhttps://t.me/kevin_english_zno\nБіологія/хімія:\nhttps://t.me/znohub_bio\nГеографія:\nhttps://t.me/znohub_geo\nІсторія:\nhttps://t.me/znohub_hist\nhttps://t.me/historyinthemem\n")

@dp.message(F.text.lower() == "ші-асистент")
async def ai(message: types.Message):
    await message.reply("Ось посилання на бета-версію бота з ші, скоро він з'явиться і у цьому чаті: https://t.me/aiii_test_bot")

@dp.message(F.text.lower() == "адмінпанель")
async def admin(message: types.Message):
    await message.reply("Скоро для адміністраторів з'явиться можливість додавати оголошення для інших користувачів, очікуйте на оновлення!")

@dp.message()
async def message_handler(message: types.Message):
    answer = await ai(message.text)
    if answer != None:
        await message.reply(answer)
    else:
        await message.reply("Виникла помилка, спробуйте ще раз.")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())