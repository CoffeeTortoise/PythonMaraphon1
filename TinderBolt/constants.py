from util import Dialog
from gpt import ChatGptService


class Constants:
    TOKEN: str = '8065065132:AAFMU1e1Lh1jhk5jx2i4gN25wNZbOLqKB4k'
    OPEN_AI_TOKEN: str = 'gpt:AgyOcazJ_9quXv71Cmo5u2qL1h_yytAiMaLywhYDr4xfoPUGP5gydVoBSJn5uc3GqTuBPJbtubJFkblB3TDn6T_un4buKEeUskeZ643kOrIteowKr2YUyjnyrDJyERTkMvgCT-Qm0H05svs_TEjdX546CNgN'
    DIALOG: Dialog = Dialog()
    CHAT_GPT = ChatGptService(token=OPEN_AI_TOKEN)
