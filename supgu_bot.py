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

# Подкатегории
subcategories = {
    "1": ["Оружие", "Артефакт", "Бижутерия"],
    "2": ["Оружие", "Артефакт", "Бижутерия"],
    "3": ["5-19", "5-26", "6-23"],
    "4": ["Свет", "Тьма", "Огонь", "Ветер", "Земля", "Вода"],
    "5": ["1я пачка", "2я пачка"]
}

# Описание подкатегорий
descriptions = {
    "Оружие": "макс сср",
    "Артефакт": "макс сср и туды сюда",
    "Бижутерия": "все по максу",
    "5-19": "https://t.me/c/2485731561/4456/57527",
    "5-26": "https://t.me/c/2485731561/4456/57416",
    "6-23": "https://t.me/c/2485731561/4456/57435",
    "1я пачка": "танк, хил, лас, все в блок и жир, хила в жир и хп восстановление",
    "2я пачка": "другое описание",
    "Свет": "https://t.me/c/2485731561/60974/61971",
    "Тьма": "другое описание",
    "Огонь": "другое описание",
    "Ветер": "другое описание",
    "Земля": "https://t.me/c/2485731561/60974/62015",
    "Вода": "другое описание"
}

# Функция старта
async def start(update: Update, context: CallbackContext, edit_message=False):
    keyboard = [[InlineKeyboardButton(text=categories[key], callback_data=key)] for key in categories]
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

    if category_id in subcategories:
        keyboard = [[InlineKeyboardButton(text=sub, callback_data=f"subcat_{category_id}_{i}")]
                    for i, sub in enumerate(subcategories[category_id], start=1)]
        keyboard.append([InlineKeyboardButton(text="Вернуться в начало", callback_data="start")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(f"Выберите подкатегорию для {categories[category_id]}", reply_markup=reply_markup)

    elif category_id.startswith("subcat_"):
        _, cat_id, sub_id = category_id.split("_")
        subcategory_name = subcategories[cat_id][int(sub_id) - 1]
        description = descriptions.get(subcategory_name, "Нет описания")
        keyboard = [[InlineKeyboardButton(text="Вернуться в начало", callback_data="start")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(f"{subcategory_name}\n{description}", reply_markup=reply_markup)
    
    elif category_id == "start":
        await start(update, context, edit_message=True)

# Главная функция запуска бота
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()

if __name__ == '__main__':
    main()
