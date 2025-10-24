import time

import requests
import telebot
from telebot import types

# ⚙️ Токен бота
BOT_TOKEN = "8162284257:AAERzBw_SnIHciLohq_0ZvbDFTfDfx05cDc"
bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')


# --- Сбрасываем webhook и старые обновления ---
def reset_bot():
    bot.remove_webhook()
    print("✅ Webhook удален (если был)")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset=-1"
    try:
        requests.get(url)
        print("✅ Старые обновления сброшены")
    except Exception as e:
        print(f"⚠️ Ошибка при сбросе обновлений: {e}")


# --- Эффект "бот печатает" ---
def bot_typing(chat_id, seconds=1):
    bot.send_chat_action(chat_id, 'typing')
    time.sleep(seconds)


# --- Главное меню ---
main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    types.KeyboardButton('📞 Контакты'),
    types.KeyboardButton('📢 Агитация')
)
main_menu.add(
    types.KeyboardButton('🎖 Льготы и гарантии'),
    types.KeyboardButton('📄 Документы')
)
main_menu.add(
    types.KeyboardButton('🏫 Вузы'),
    types.KeyboardButton('ℹ️ О боте')
)

# --- Меню агитации ---
agitation_options = ["❌В работе❌", "❌В работе❌", "❌В работе❌"]
agitation_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
for option in agitation_options:
    agitation_menu.add(types.KeyboardButton(option))
agitation_menu.add(types.KeyboardButton('⬅️ Назад'))

# --- Меню “Назад” ---
back_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_menu.add(types.KeyboardButton('⬅️ Назад'))


# --- Эффект “бот пишет” ---
def bot_typing(chat_id, seconds=0.2):
    bot.send_chat_action(chat_id, 'typing')
    time.sleep(seconds)


# --- Контент ---
CONTACTS_TEXT = """<b>📞 Контакты военных комиссариатов Омской области:</b>
🔹01. <b>ВК Омской области</b> — 8(3812)53-09-68
🔹02. <b>ВК Азовского и Одесского районов</b> — 8(38141)2-33-23
🔹03. <b>ВК Горьковского и Нижнеомского районов</b> — 8(38157)2-13-52
🔹04. <b>ВК Знаменского, Тевризского и Усть-Ишимского районов</b> — 8(38179)2-17-37
🔹05. <b>ВК г. Исилькуль и Исилькульского района</b> — 8(38173)2-06-85
🔹06. <b>ВК г. Калачинск, Калачинского, Кормиловского и Оконешниковского районов</b> — 8(38155)2-17-30
🔹07. <b>ВК Любинского и Саргатского районов</b> — 8(38175)2-28-29
🔹08. <b>ВК Москаленского и Марьяновского районов</b> — 8(38174)2-15-83
🔹09. <b>ВК Муромцевского и Седельниковского районов</b> — 8(38158)2-37-02
🔹10. <b>ВК г. Называевск и Называевского района</b> — 8(38161)2-34-91
🔹11. <b>ВК Омского района</b> — 8(3812)32-31-21
🔹12. <b>ВК Павлоградского и Русско-Полянского районов</b> — 8(38172)3-13-01
🔹13. <b>ВК Таврического и Нововаршавского районов</b> — 8(38151)2-15-37
🔹14. <b>ВК г. Тара, Тарского, Большереченского и Колосовского районов</b> — 8(38171)2-22-05
🔹15. <b>ВК г. Тюкалинск, Тюкалинского, Большеуковского и Крутинского районов</b> — 8(38176)2-32-63
🔹16. <b>ВК Черлакского района</b> — 8(38153)2-15-95
🔹17. <b>ВК Шербакульского и Полтавского районов</b> — 8(38177)2-13-50
🔹18. <b>ВК Кировского АО г. Омск</b> — 8(3812)55-03-15
🔹19. <b>ВК Центрального и Советского АО г. Омск</b> — 8(3812)60-42-00
🔹20. <b>ВК Ленинского и Октябрьского АО г. Омск</b> — 8(3812)45-07-66
"""

DOCUMENTS_TEXT = """<b>📋 Перечень документов для личного дела кандидата:</b>
1️⃣ Заявление с указанием:
- ФИО, дата рождения, гражданство
- Паспортные данные
- Образование
- Адрес регистрации и проживания
- Телефон и email
2️⃣ Ксерокопии паспорта и свидетельства о рождении
3️⃣ Автобиография
4️⃣ Характеристика с места учебы/работы
5️⃣ Документ об образовании
6️⃣ Справки на льготы (если есть)
7️⃣ Документы об индивидуальных достижениях
8️⃣ Справка о допуске к гос. тайне
9️⃣ Карта мед. освидетельствования
🔟 Карта профотбора
📸 3 фото 4.5×6 см (без головного убора)
"""

BENEFITS_TEXT = """<b>🎖 Льготы и гарантии</b>
Государство берет на себя все расходы по обучению и полному государственному обеспечению курсантов, включающее в себя:
🔹бесплатное высшее образование, получение гражданского и военного диплома федерального государственного общеобразовательного стандарта с гарантированным трудоустройством по оканчанию обучения;
🔹возможнность получения бесплатного дополнительного образования по специальности переводчика;
🔹полное медицинское обеспечение(ежегодное прохождение углубленного медицинского осмотра, бесплатное страхование жизни и здоровья);
🔹денежное довольствие курсанта от 25 тысяч рублей, ежегодная выплата материальной помощи в размере одного оклада денежного содержания, возможность выплаты правительственной и президентской стипендии;
🔹трёхразовое питание по системе шведский стол;
🔹бесплатное проживание в общежитии;
🔹обеспечение спортивной и военной формой одежды;
🔹гарантированный оплачиваемый отпуск 45 суток.
"""

UNIVERSITIES_TEXT = """<b>🏫 Перечень военных вузов для поступления:</b>
🔹01. <b>Московское высшее общевойсковое командное училище</b>
🔹02. <b>Казанское высшее танковое командное училище</b>
🔹03. <b>Новосибирское высшее военное командное училище</b>
🔹04. <b>Дальневосточное высшее общевойсковое командное училище (г. Благовещенск)</b>
🔹05. <b>Донецкое высшее общевойсковое командное училище</b>
🔹06. <b>Рязанское высшее воздушно-десантное командное училище</b>
🔹07. <b>Военно-инженерная академия (п. Нахабино, Московская обл.)</b>
🔹08. <b>Тюменское высшее военно-инженерное командное училище</b>
🔹09. <b>Нижегородское высшее военно-инженерное командное училище</b>
🔹10. <b>Михайловская военная артиллерийская академия (г. Санкт-Петербург)</b>
🔹11. <b>Саратовское высшее артиллерийское командное училище</b>
🔹12. <b>Военная академия РХБЗ (г. Кострома)</b>
🔹13. <b>Саратовское высшее военное инженерное училище РХБ защиты</b>
🔹14. <b>ВУНЦ ВВС Военно-воздушная академия (г. Воронеж)</b>
🔹15. <b>ВУНЦ ВВС "Военно-воздушная академия" (филиал г. Сызрань)</b>
🔹16. <b>ВУНЦ ВВС "Военно-воздушная академия" (филиал г. Челябинск)</b>
🔹17. <b>Краснодарское высшее военное училище лётчиков</b>
🔹18. <b>Военно-космическая академия (г. Санкт-Петербург)</b>
🔹19. <b>Военная академия воздушно-космической обороны (г. Тверь)</b>
🔹20. <b>Военная академия войсковой противовоздушной обороны ВС РФ (г. Смоленск)</b>
🔹21. <b>Ярославское высшее военное училище противовоздушной обороны</b>
🔹22. <b>ВУНЦ ВМФ "Военно-морская академия" (г. Санкт-Петербург)</b>
🔹23. <b>ВУНЦ ВМФ "Военно-морская академия" (военно-морской политехнический, г. Пушкин)</b>
🔹24. <b>Балтийское высшее военно-морское училище (г. Калининград)</b>
🔹25. <b>Тихоокеанское высшее военно-морское училище (г. Владивосток)</b>
🔹26. <b>Черноморское высшее военно-морское училище (г. Севастополь)</b>
🔹27. <b>Военная академия РВСН (г. Балашиха, Московская область)</b>
🔹28. <b>Военная академия РВСН (филиал г. Серпухов, Московская область)</b>
🔹29. <b>Военная академия связи (г. Санкт-Петербург)</b>
🔹30. <b>Новочеркасское высшее военное командное училище связи</b>
🔹31. <b>Краснодарское высшее военное училище</b>
🔹32. <b>Военный университет радиоэлектроники (г. Череповец, Вологодская обл.)</b>
🔹33. <b>Воронежское высшее военное училище радиоэлектроники</b>
🔹34. <b>Военный университет (г. Москва)</b>
🔹35. <b>Военная академия материально-технического обеспечения (г. Санкт-Петербург)</b>
🔹36. <b>Военная академия МТО — Военный институт (ЖДВ и военных сообщений)</b>
🔹37. <b>Военная академия МТО — Военный институт (инженерно-технический)</b>
🔹38. <b>Военная академия МТО (филиал г. Вольск, Саратовская область)</b>
🔹39. <b>Военная академия МТО (филиал г. Пенза)</b>
🔹40. <b>Военная академия МТО (филиал г. Омск)</b>
🔹41. <b>Военно-медицинская академия (г. Санкт-Петербург)</b>
🔹42. <b>Военный институт физической культуры (г. Санкт-Петербург)</b>
"""

ABOUT_TEXT = """<b>ℹ️ О боте</b>
Бот создан для помощи кандидатам в военные вузы. Вы можете:
- ознакомиться с документами;
- узнать телефоны военкоматов Омской области;
- посмотреть список военных вузов;
- получить справочную информацию.
<b>Разработано при поддержке военного комиссариата Омской области 🇷🇺</b>
"""

AGITATION_TEXT = """<b>📢 Агитация</b>
Выберите интересующий материал и получите доступ к нему через кнопки ниже.
"""


# --- Обработчики ---
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        f"👋 <b>Добро пожаловать, {message.from_user.first_name}!</b>\n\nВыберите интересующий раздел:",
        reply_markup=main_menu
    )


@bot.message_handler(commands=['help'])
def help_message(message):
    bot_typing(message.chat.id)
    bot.send_message(
        message.chat.id,
        "<b>🆘 Доступные команды:</b>\n"
        "/start — начать работу\n"
        "/help — список команд\n"
        "/about — информация о боте\n"
        "/location — адрес военкомата\n"
        "/photo — отправка изображения\n"
        "/document — пример документа",
        reply_markup=main_menu
    )


@bot.message_handler(commands=['about'])
def about_message(message):
    inline = types.InlineKeyboardMarkup()
    inline.add(
        types.InlineKeyboardButton("📨 Связаться", url="https://t.me/OSP_VK_OMSK"),
        types.InlineKeyboardButton("🔗 Официальный сайт", url="https://mil.ru")
    )
    bot_typing(message.chat.id)
    bot.send_message(
        message.chat.id,
        ABOUT_TEXT,
        reply_markup=inline
    )


@bot.message_handler(commands=['location'])
def send_location(message):
    bot_typing(message.chat.id)
    bot.send_message(message.chat.id, "📍 Адрес Центрального военкомата Омской области:")
    bot.send_location(message.chat.id, latitude=54.989342, longitude=73.368212)
    bot.send_message(message.chat.id, "🏢 г. Омск, ул. Ленина, д. 45", reply_markup=back_menu)


@bot.message_handler(commands=['photo'])
def send_photo(message):
    bot_typing(message.chat.id)
    photo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Russian_Army_emblem.svg/800px-Russian_Army_emblem.svg.png"
    bot.send_photo(message.chat.id, photo_url, caption="🎖 Эмблема Вооружённых сил РФ", reply_markup=back_menu)


@bot.message_handler(commands=['document'])
def send_document(message):
    bot_typing(message.chat.id)
    bot.send_message(message.chat.id, "📎 Отправляю пример документа...")
    try:
        with open("sample.pdf", "rb") as doc:
            bot.send_document(message.chat.id, doc, visible_file_name="Инструкция.pdf", caption="📄 Пример документа")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "❌ Файл sample.pdf не найден.", reply_markup=back_menu)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.strip()
    chat_id = message.chat.id

    if text in ['⬅️ Назад', 'Назад']:
        bot_typing(chat_id)
        bot.send_message(chat_id, "🔙 Возврат в главное меню:", reply_markup=main_menu)

    elif text == '📞 Контакты':
        bot_typing(chat_id)
        bot.send_message(chat_id, CONTACTS_TEXT, reply_markup=back_menu)

    elif text == '📢 Агитация':
        bot_typing(chat_id)
        bot.send_message(chat_id, AGITATION_TEXT, reply_markup=agitation_menu)

    elif text in agitation_options:
        bot_typing(chat_id)
        inline = types.InlineKeyboardMarkup()
        inline.add(
            types.InlineKeyboardButton("🌐 Перейти на сайт", url="https://mil.ru"),
            types.InlineKeyboardButton("📎 Скачать материалы", url="https://mil.ru/files/sample.pdf")
        )
        bot.send_message(chat_id, f"📢 <b>{text}</b>\n\nМатериалы доступны ниже 👇", reply_markup=inline)

    elif text == '🎖 Льготы и гарантии':
        bot_typing(chat_id)
        bot.send_message(chat_id, BENEFITS_TEXT, reply_markup=back_menu)

    elif text == '📄 Документы':
        bot_typing(chat_id)
        bot.send_message(chat_id, DOCUMENTS_TEXT, reply_markup=back_menu)

    elif text == '🏫 Вузы':
        bot_typing(chat_id)
        bot.send_message(chat_id, UNIVERSITIES_TEXT, reply_markup=back_menu)

    elif text == 'ℹ️ О боте':
        about_message(message)

    else:
        bot.send_message(chat_id, "❓ Неизвестная команда. Выберите пункт меню.", reply_markup=main_menu)


if __name__ == "__main__":
    reset_bot()  # ⚡ Сбрасываем webhook и обновления перед polling
    print("✅ Бот запущен...")
    bot.infinity_polling()
