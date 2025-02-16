from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Ваш токен
TOKEN = 'ваш бот'

# Категории
categories = {
    "1": "ПВП",
    "2": "ПВЕ",
    "3": "Босы Сюжетки",
    "4": "Босы Гильдейские",
    "5": "Парвани"
}

# Подкатегории для категории 1
subcategories = {
    "1": ["Оружие", "Артефакт", "Бижутерия"]
}

# Описание подкатегорий
descriptions = {
    "Оружие": "макс сср",
    "Артефакт": "макс сср и туды сюда",
    "Бижутерия": "все по максу"
}

# Данные для каждой категории
items = {
    "1": ["кью фуся хил"],
    "2": ["123"],
    "3": ["321"]
}

# Функция старта
async def start(update: Update, context: CallbackContext, edit_message=False):
    keyboard = [
        [InlineKeyboardButton(text=categories[key], callback_data=key)]
        for key in categories
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if edit_message and update.callback_query:
        await update.callback_query.message.edit_text("Выбери, уважаемый", reply_markup=reply_markup)
    elif update.message:
        await update.message.reply_text("Выбери, уважаемый", reply_markup=reply_markup)

# Обработчик кнопок
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    category_id = query.data
    await query.answer()

    if category_id == "1":
        keyboard = [
            [InlineKeyboardButton(text=sub, callback_data=f"subcat_1_{i+1}")]
            for i, sub in enumerate(subcategories["1"])
        ]
        keyboard.append([InlineKeyboardButton(text="Вернуться в начало", callback_data="start")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text("Выберите подкатегорию для ПВП:", reply_markup=reply_markup)
    
    elif category_id in ["2", "3"]:
        item_list = "\n".join(items[category_id])
        keyboard = [[InlineKeyboardButton(text="Вернуться в начало", callback_data="start")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(f"Список :\n{item_list}\n\nВыберите другую категорию:", reply_markup=reply_markup)

    elif category_id.startswith("subcat_1_"):
        subcategory_name = subcategories["1"][int(category_id.split("_")[2]) - 1]
        description = descriptions[subcategory_name]
        keyboard = [[InlineKeyboardButton(text="Вернуться в начало", callback_data="start")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(f"{subcategory_name}\n{description}", reply_markup=reply_markup)

    elif category_id == "start":
        await start(update, context, edit_message=True)  # Теперь не вызывает ошибку

# Главная функция запуска бота
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()

if __name__ == '__main__':
    main()

