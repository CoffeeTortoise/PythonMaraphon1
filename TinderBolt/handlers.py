from util import send_text, send_photo, send_text_buttons
from util import load_prompt, dialog_user_info_to_str
from constants import Constants


async def opener_dialog(update, context):
    text = update.message.text
    Constants.DIALOG.count += 1
    cntr = Constants.DIALOG.count
    if cntr == 1:
        Constants.DIALOG.user['name'] = text
        await send_text(update, context, 'Возраст?')
    elif cntr == 2:
        Constants.DIALOG.user['age'] = text
        await send_text(update, context, 'Внешность: 1-10 баллов?')
    elif cntr == 3:
        Constants.DIALOG.user['attractivity'] = text
        await send_text(update, context, 'Профессия?')
    elif cntr == 4:
        Constants.DIALOG.user['job'] = text
        await send_text(update, context, 'Цель знакомства?')
    elif cntr == 5:
        Constants.DIALOG.user['goal'] = text
        prompt = load_prompt('opener')
        user_info = dialog_user_info_to_str(Constants.DIALOG.user)
        msg = await send_text(update, context, 'Обработка...')
        answer = await Constants.CHAT_GPT.send_question(prompt, user_info)
        await msg.edit_text(answer)
    else:
        await send_text(update, context, 'Все ответы получены')


async def profile_dialog(update, context):
    text = update.message.text
    Constants.DIALOG.count += 1
    cntr = Constants.DIALOG.count
    if cntr == 1:
        Constants.DIALOG.user['age'] = text
        await send_text(update, context, 'Какая у вас профессия?')
    elif cntr == 2:
        Constants.DIALOG.user['job'] = text
        await send_text(update, context, 'Есть ли у вас хобби?')
    elif cntr == 3:
        Constants.DIALOG.user['hobby'] = text
        await send_text(update, context, 'Что вам не нравится в людях?')
    elif cntr == 4:
        Constants.DIALOG.user['annoys'] = text
        await send_text(update, context, 'Какова ваша цель знакомства?')
    elif cntr == 5:
        Constants.DIALOG.user['goal'] = text
        prompt = load_prompt('profile')
        user_info = dialog_user_info_to_str(Constants.DIALOG.user)
        msg = await send_text(update, context, 'Обработка...')
        answer = await Constants.CHAT_GPT.send_question(prompt, user_info)
        await msg.edit_text(answer)
    else:
        await send_text(update, context, 'Все ответы получены')


async def gpt_dialog(update, context):
    await send_text(update, context, 'Вы общаетесь с GPT')
    text: str = update.message.text
    prompt: str = load_prompt('gpt')
    answer = await Constants.CHAT_GPT.send_question(prompt, text)
    await send_text(update, context, answer)


async def date_dialog(update, context):
    text = update.message.text
    msg = await send_text(update, context, 'Печатает...')
    answer = await Constants.CHAT_GPT.add_message(text)
    await msg.edit_text(answer)


async def message_dialog(update, context):
    text = update.message.text
    Constants.DIALOG.list.append(text)


async def greetings(update, context) -> None:
    if Constants.DIALOG.mode == 'gpt':
        await gpt_dialog(update, context)
    elif Constants.DIALOG.mode == 'date':
        await date_dialog(update, context)
    elif Constants.DIALOG.mode == 'message':
        await message_dialog(update, context)
    elif Constants.DIALOG.mode == 'profile':
        await profile_dialog(update, context)
    elif Constants.DIALOG.mode == 'opener':
        await opener_dialog(update, context)
    else:
        await send_text(update, context, '*Привет*')
        await send_text(update, context, '_Как дела?_')
        await send_text(update, context, f'Вы написали {update.message.text}')
        await send_photo(update, context, 'date_robbie')
        await send_text_buttons(update, context, 'Запустить',
                                {
                                    'start': 'запущено',
                                    'stop': 'остановлено'
                                }
                                )
