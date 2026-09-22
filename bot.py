import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = os.getenv("TOKEN")

TIKTOK_LINK = "https://www.tiktok.com/@sdr7131318094?_r=1&_t=ZS-99x6XH0yszo"


# ─────────────────────────────
# /start
# ─────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("ехала 🤍", callback_data="start_quest")]
    ]

    await update.message.reply_text(
        "доброго времени суток 🤍\n\n"
        "сегодня те предстоит кое че поискать\n"
        "но я же загадка 🤫\n\n"
        "реди?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ─────────────────────────────
# Начало квеста
# ─────────────────────────────

async def start_quest(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    context.user_data["step"] = 1

    await query.edit_message_text(
        "поехали 🤍\n\n"
        "первое...\n\n"
        "самое простое пока что\n\n"
        "твое любимое число?"
        "введи только цифру😇"
    )


# ─────────────────────────────
# Задание 4 — подсказка
# ─────────────────────────────

async def angel_hint(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    await query.message.reply_text(
        "подсказочка тут😎\n\n"
        "4ngel\n\n"
        "shh..."
        "shh..."
        "shh..."
    )


# ─────────────────────────────
# Проверка ответов
# ─────────────────────────────

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):

    answer = update.message.text.strip().lower()
    step = context.user_data.get("step", 0)

    # ЗАДАНИЕ 1
    if step == 1:

        if answer == "7":

            context.user_data["step"] = 2

            await update.message.reply_text(
                "✅ умничка\n\n"
                "не расслабляй батоны😘\n\n"
                "второе...\n\n"
                "тебе понадобится наш чат\n\n"
                "найди соо 21 сентября в 13:23"
                "там кое что заметишь странное"
                "пиши сюда без пробелов😇"
            )

        else:

            await update.message.reply_text(
                "чивооо \n"
                "попробуй еще раз🥺"
            )

    # ЗАДАНИЕ 2
    elif step == 2:

        answer_clean = answer.replace(" ", "")

        if answer_clean in ["13:13", "1313"]:

            context.user_data["step"] = 3

            await update.message.reply_text(
                "✅ молодец\n\n"
                "запомни 1️⃣3️⃣1️⃣3️⃣\n\n"
                "нееекст\n\n"
                "трейтье...\n\n"
                "заходи в инсту"
                "посмотри на последнее фото"
                "выкладывал которое недавно🤪"
                "нужна только дата\n"
                "напиши ее в формате ДД.ММ."
            )

        else:

            await update.message.reply_text(
                "шото нето🥺\n\n"
                "внимательнее смотри 21 сентября в 13:23"
            )

    # ЗАДАНИЕ 3
    elif step == 3:

        answer_clean = (
            answer
            .replace(" ", "")
            .replace("/", ".")
            .replace("-", ".")
        )

        if answer_clean in ["1809", "18.09"]:

            context.user_data["step"] = 4

            keyboard = [
                [
                    InlineKeyboardButton(
                        "подсказка",
                        callback_data="angel_hint"
                    )
                ]
            ]

            await update.message.reply_text(
                "✅ лучшая\n\n"
                "ластовая осталась\n\n"
                "четвертое...\n\n"
                "я тот кто смотрит с небес но моя первая буква не буква\n\n"
                "shh...\n\n"
                "shh...\n\n"
                "shh...\n\n"
                "shh...\n\n"
                "вышло чтото?\n\n"
                "бери подсказку",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        else:

            await update.message.reply_text(
                "нето\n\n"
                "там всего две фотки бож ну емае🥺"
            )

    # ЗАДАНИЕ 4
    elif step == 4:

        if answer in ["4", "4".lower()]:

            context.user_data["step"] = 5

            await update.message.reply_text(
                "✅ в точку родная\n\n"
                "это 4️⃣\n\n"
                "теперь все вместе из 🔟 цифр:\n\n"
                "7\n"
                "1313\n"
                "1809\n"
                "4\n\n"
                "иии должно получится "
                "десятизначное число\n\n"
                "напиши ка его."
            )

        else:

            await update.message.reply_text(
                "чето нето совсем\n\n"
                "замени первую букву на цифру ANGEL "
                "на самую похожую цифру\n\n"
                "ну чтож такое🥺"
            )

    # ФИНАЛЬНЫЙ КОД
    elif step == 5:

        number = answer.replace(" ", "")

        if number == "7131318094":

            context.user_data["step"] = 6

            keyboard = [
                [
                    InlineKeyboardButton(
                        "тт",
                        url=TIKTOK_LINK
                    )
                ]
            ]

            await update.message.reply_text(
                "🤍\n\n"
                "все собрала крутецкая самая\n\n"
                "и что получилось?\n\n"
                "7131318094\n\n"
                "но это не пароль🤭\n"
                "это адрес следующей части🤯\n\n"
                "найди юз с этими цифрами в тт\n\n"
                "допишии перед числом sdr и там будет ава с альбомом года тебе туда🤫",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        else:

            await update.message.reply_text(
                "ну ка еще разок\n\n"
                "ты сможешь🥺"
                "десятизначное число."
            )


# ─────────────────────────────
# Запуск бота
# ─────────────────────────────

def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(
            start_quest,
            pattern="^start_quest$"
        )
    )

    app.add_handler(
        CallbackQueryHandler(
            angel_hint,
            pattern="^angel_hint$"
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_answer
        )
    )

    print("Бот запущен!")

    app.run_polling()


if __name__ == "__main__":
    main()
