from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Ваш токен, который вам выдал BotFather
TOKEN = '8095508285:AAGU5pApgQuCmJijPU7VLrgoSen2QGTy59c'

# Данные для выбора
categories = {
   "1": "ПВП аспект",
    "2": "ПВЕ аспект",
    "3": "Боссы",
    "4": "СУПЕР БОСЫ НЕ НАЖИМАЙ"
}

# Данные для каждой категории
items = {
     "1": ["Ловкость, Сила атаки, Крит урон,"],
    "2": ["Сила Атаки, Крит урон, Урон по босам"],
    "3": ["кью, фуся, хил"],
   "4": ["послать его нахуй"]
}

# Функция для старта
async def start(update: Update, context: CallbackContext):
    # Приветственное сообщение с перечнем выбора
    keyboard = [
        [InlineKeyboardButton(text=categories["1"], callback_data="1")],
        [InlineKeyboardButton(text=categories["2"], callback_data="2")],
        [InlineKeyboardButton(text=categories["3"], callback_data="3")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Выберите категорию:', reply_markup=reply_markup)

# Функция для обработки кнопок
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    category_id = query.data
    
    # Ответ с товарами по выбранной категории
    if category_id in items:
        item_list = "\n".join(items[category_id])
        # Редактируем сообщение с товарами и добавляем кнопки для выбора категории
        keyboard = [
            [InlineKeyboardButton(text=categories["1"], callback_data="1")],
            [InlineKeyboardButton(text=categories["2"], callback_data="2")],
            [InlineKeyboardButton(text=categories["3"], callback_data="3")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(f"Список товаров:\n{item_list}\n\nВыберите другую категорию:", reply_markup=reply_markup)

def main():
    # Создаем объект Application и передаем ему токен
    application = Application.builder().token(TOKEN).build()

    # Обработчики команд и запросов
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
