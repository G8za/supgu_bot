from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Ваш токен, который вам выдал BotFather
TOKEN = '8095508285:AAGU5pApgQuCmJijPU7VLrgoSen2QGTy59c'

# Данные для выбора
categories = {
    "1": "ПВП аспект",
    "2": "ПВЕ аспект",
    "3": "Боссы"
}

# Данные для каждой категории
items = {
    "1": ["Ловкость, Сила атаки, Крит урон,"],
    "2": ["Сила Атаки, Крит урон, Урон по босам"],
    "3": ["кью, фуся, хил"]
}

def start(update: Update, context: CallbackContext):
    # Приветственное сообщение с перечнем выбора
    keyboard = [
        [InlineKeyboardButton(text=categories["1"], callback_data="1")],
        [InlineKeyboardButton(text=categories["2"], callback_data="2")],
        [InlineKeyboardButton(text=categories["3"], callback_data="3")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет! Выберите категорию:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    category_id = query.data
    
    # Ответ с товарами по выбранной категории
    if category_id in items:
        item_list = "\n".join(items[category_id])
        query.edit_message_text(f"Список товаров:\n{item_list}")

def main():
    # Создаем объект Updater и передаем ему токен
    updater = Updater(TOKEN, use_context=True)

    # Получаем диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Обработчик для нажатий на кнопки
    dp.add_handler(CallbackQueryHandler(button))

    # Запускаем бота
    updater.start_polling()

    # Бот будет работать до тех пор, пока не будет остановлен
    updater.idle()

if __name__ == '__main__':
    main()
