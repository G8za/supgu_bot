from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext

# ��� �����, ������� ����� �������� � BotFather
TOKEN = '8095508285:AAGU5pApgQuCmJijPU7VLrgoSen2QGTy59c'

# ������ ��� ������
categories = {
    "1": "��� ������",
    "2": "��� ������",
    "3": "�����"
}

# ������ ��� ������ ���������
items = {
    "1": ["��������, ���� �����, ���� ����,"],
    "2": ["���� �����, ���� ����, ���� �� �����"],
    "3": ["���, ����, ���"]
}

def start(update: Update, context: CallbackContext):
    # �������������� ��������� � �������� ������
    keyboard = [
        [InlineKeyboardButton(text=categories["1"], callback_data="1")],
        [InlineKeyboardButton(text=categories["2"], callback_data="2")],
        [InlineKeyboardButton(text=categories["3"], callback_data="3")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('������! �������� ���������:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    category_id = query.data
    
    # ����� � �������� �� ��������� ���������
    if category_id in items:
        item_list = "\n".join(items[category_id])
        query.edit_message_text(f"������ �������:\n{item_list}")

def main():
    # ������� ������ Updater � �������� ��� �����
    updater = Updater(TOKEN, use_context=True)

    # �������� ���������� ��� ����������� ������������
    dp = updater.dispatcher

    # ���������� ������� /start
    dp.add_handler(CommandHandler("start", start))

    # ���������� ��� ������� �� ������
    dp.add_handler(CallbackQueryHandler(button))

    # ��������� ����
    updater.start_polling()

    # ��� ����� �������� �� ��� ���, ���� �� ����� ����������
    updater.idle()

if __name__ == '__main__':
    main()