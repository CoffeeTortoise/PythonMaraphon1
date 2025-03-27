from util import send_text, send_photo, load_message
from util import show_main_menu, send_text_buttons
from constants import Constants


async def opener(update, context):
    Constants.DIALOG.mode = 'opener'
    text = load_message('opener')
    await send_photo(update, context, 'opener')
    await send_text(update, context, text)
    Constants.DIALOG.user.clear()
    Constants.DIALOG.count = 0
    await send_text(update, context, 'Имя собеседника?')


async def profile(update, context):
    Constants.DIALOG.mode = 'profile'
    text = load_message('profile')
    await send_photo(update, context, 'profile')
    await send_text(update, context, text)
    Constants.DIALOG.user.clear()
    Constants.DIALOG.count = 0
    await send_text(update, context, 'Сколько вам лет?')


async def message(update, context):
    Constants.DIALOG.mode = 'message'
    text = load_message('message')
    await send_photo(update, context, 'message')
    await send_text(update, context, text)
    await send_text_buttons(update, context, text,
                            {
                                'message_next': 'Следующее сообщение',
                                'message_date': 'Пригласить на свидание'
                            }
                            )
    Constants.DIALOG.list.clear()


async def date(update, context):
    Constants.DIALOG.mode = 'date'
    text = load_message('date')
    await send_photo(update, context, 'date')
    await send_text(update, context, text)
    await send_text_buttons(update, context, text,
                            {
                                'date_grande': 'Ариана Гранде',
                                'date_robbie': 'Марго Робби',
                                'date_zendaya': 'Зендея',
                                'date_gosling': 'Райан Гослинг',
                                'date_hardy': 'Том Харди'
                            }
                            )


async def start(update, context):
    text = load_message('main')
    Constants.DIALOG.mode = 'main'
    await send_text(update, context, text)
    await send_photo(update, context, 'main')
    await show_main_menu(update, context,
                         {
                             'start': 'главное меню бота',
                             'profile': 'генерация Tinder-профиля',
                             'opener': 'сообщение для знакомства',
                             'message': 'переписка от вашего имени',
                             'date': 'переписка со звёздами',
                             'gpt': 'задать вопрос чату GPT'
                         }
                         )


async def gpt(update, context):
    text = load_message('gpt')
    Constants.DIALOG.mode = 'gpt'
    await send_photo(update, context, 'gpt')
    await send_text(update, context, text)
