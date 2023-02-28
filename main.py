from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

inline_buttons = [
    InlineKeyboardButton('Бэкенд', callback_data='backend'),
    InlineKeyboardButton('Фронтэнд', callback_data='frontend'),
    InlineKeyboardButton('Дизайнер UXUI', callback_data='uxui'),
    InlineKeyboardButton('Андройд', callback_data='android'),
    InlineKeyboardButton('IOS', callback_data='ios')
]

button = InlineKeyboardMarkup().add(*inline_buttons)


@dp.message_handler(commands = ['start'])
async def start(message:types.Message):
    await message.answer(f"Здраствуйте, {message.from_user.full_name}")
    await message.answer(f"Этот Бот предназначен для предоставления информации для пользователя о IT курсах", reply_markup=button)
    await message.answer(f"Если вам что-то непонятно то пропишите /help")

@dp.message_handler(commands=['help'])
async def help(message:types.Message):
    await message.answer(f"В случае если вам что-то не понятно\n/backend\n/frontend\n/uxui\n/android\n/ios")

@dp.callback_query_handler(lambda call: call)
async def all(call):
    if call.data == "backend":
        await backend(call.message)
    elif call.data == "help":
        await help(call.message)
    elif call.data == "frontend":
        await frontend(call.message)
    elif call.data == "uxui":
        await uxui(call.message)
    elif call.data == "android":
        await android(call.message)
    elif call.data == "ios":
        await ios(call.message)


@dp.message_handler(commands=['backend'])
async def backend(message:types.Message):
    await message.answer(f"Бэкенд — это разработка бизнес-логики продукта (сайта или веб-приложения). Бэкенд отвечает за взаимодействие пользователя с внутренними данными, которые потом отображает фронтенд. Попросту говоря, это то, что скрыто от глаз пользователя и происходит вне его браузера и компьютера.\nСтоимость 10000 сом в месяц\nОбучение: 5 месяц", reply_markup=button)


@dp.message_handler(commands=['frontend'])
async def frontend(message:types.Message):
    await message.answer(f"Фронтенд-разработка — это создание пользовательского интерфейса на клиентской стороне веб‑сайта или приложения. Это всё, что видит пользователь, когда открывает веб-страницу, и с чем он взаимодействует: кнопки, баннеры и анимация.\nСтоимость 10000 сом в месяц\nОбучение: 5 месяц", reply_markup=button)

@dp.message_handler(commands=['uxui'])
async def uxui(message:types.Message):
    await message.answer(f"UX/UI-дизайн — это работа над интерфейсом приложения или сайта, чтобы пользователю было интуитивно понятно и визуально приятно контактировать с ним.\nСтоимость 8000 сом в месяц\nОбучение: 4 месяц", reply_markup=button)

@dp.message_handler(commands=['android'])
async def android(message:types.Message):
    await message.answer(f"Android-разработчик создает приложения для устройств на операционной системе Android. Он пишет код, работает над интерфейсом и дизайном, тестирует приложение и исправляет баги, а также адаптирует его под разные модели устройств (которых у Android великое множество).\nСтоимость 10000 сом в месяц\nОбучение: 7 месяц", reply_markup=button)


@dp.message_handler(commands=['ios'])
async def ios(message:types.Message):
    await message.answer(f"iOS-разработчик создает приложения для устройств Apple. Это не только iPhone, но и iPad, Apple Watch и другие гаджеты, входящие в экосистему. Он не только пишет код и работает над интерфейсом, но и занимается поддержкой приложения, адаптацией его под разные модели устройств, тестированием и исправлением багов.\nСтоимость 10000 сом в месяц\nОбучение: 6 месяц", reply_markup=button)

@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply(f"Я вас не понял , введите для просмотра всех доступных направлений /help")



executor.start_polling(dp)