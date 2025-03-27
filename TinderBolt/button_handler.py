from util import send_text, send_photo, load_prompt
from constants import Constants


async def hello_button(update, context):
    query = update.callback_query.data
    if query == 'start':
        await send_text(update, context, 'Запущено')
    else:
        await send_text(update, context, 'Остановлено')


async def date_button(update, context):
    query = update.callback_query.data
    await update.callback_query.answer()
    await send_photo(update, context, query)
    msg: str = 'Отличный выбор! Пригласите девушку/парня на свидание за 5 сообщений!'
    await send_text(update, context, msg)
    prompt: str = load_prompt(query)
    Constants.CHAT_GPT.set_prompt(prompt)


async def message_button(update, context):
    query = update.callback_query.data
    await update.callback_query.answer()
    prompt = load_prompt(query)
    user_chat_history = '\n\n'.join(Constants.DIALOG.list)
    msg = await send_text(update, context, 'Обработка...')
    answer = await Constants.CHAT_GPT.send_question(prompt, user_chat_history)
    await msg.edit_text(answer)
