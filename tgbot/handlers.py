from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ConversationHandler

NAME, PHONE_NUMBER, LOCATION, DELIVERY_TIME, COMMENT = range(5)


def callback_handler(update, context):
    """Запуск команд отловленных CallbackQueryHandler-ом."""
    COMMANDS = {
        'pdconsent_refuse': pdconsent_refuse,
        'pdconsent_agreed': pdconsent_agreed,
        'show_prices': show_prices,
        'show_client_orders': show_client_orders,
        'show_delivery_time': show_delivery_time,
        'leave_complaint': leave_complaint,
        'ask_client_name': ask_client_name,
        'ask_comment': ask_comment,
        'registration_success': registration_success,
    }
    COMMANDS[update.callback_query.data](update, context)


def create_keyboard(queryset):
    """Создает вертикальную клавиатуру с именами объектов из Queryset."""
    keyboard = [
        [InlineKeyboardButton(
            item.name,
            callback_data=item.name
        )] for item in queryset
    ]
    return InlineKeyboardMarkup(keyboard)


def start_callback(update, context):
    """Старт работы с ботом для клиента."""
    update.message.reply_text(
        "Добро пожаловать в сервис для заказа тортов от BakeCake!\n")
    doc_path = r'./assets/Согласие на обработку персональных данных.pdf'
    with open(doc_path, 'rb') as f:
        context.bot.sendDocument(chat_id=update.effective_chat.id, document=f)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Для продолжения работы с ботом, пожалуйста, подтвердите согласие на обработку персональных данных",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "✅",
                callback_data="pdconsent_agreed"
            ),
            InlineKeyboardButton(
                "❌",
                callback_data='pdconsent_refuse'
            ),
        ]])
    )


def start_again(update, context):
    doc_path = r'./assets/Согласие на обработку персональных данных.pdf'
    with open(doc_path, 'rb') as f:
        context.bot.sendDocument(chat_id=update.effective_chat.id, document=f)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Для продолжения работы с ботом, пожалуйста, подтвердите согласие на обработку персональных данных",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "✅",
                callback_data="pdconsent_agreed"
            ),
            InlineKeyboardButton(
                "❌",
                callback_data='pdconsent_refuse'
            ),
        ]])
    )


def pdconsent_refuse(update, context):
    """Попрощаться после отказа предоставления персональных данных."""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="К сожалению, без согласия нельзя продолжить заказ через бота."
    )

    start_again(update, context)


def pdconsent_agreed(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Выберите дальнейшее действие:",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "Посмотреть цены",
                callback_data='show_prices'
            )],
            [InlineKeyboardButton(
                "Показать мои предыдущие заказы",
                callback_data='show_client_orders'
            )],
            [InlineKeyboardButton(
                "Показать срок доставки для текущего заказа",
                callback_data='show_delivery_time'
            )],
            [InlineKeyboardButton(
                "Оставить жалобу",
                callback_data='leave_complaint'
            )],
        ])
    )


def show_prices(update, context):
    pass


def show_client_orders(update, context):
    pass


def show_delivery_time(update, context):
    pass


def leave_complaint(update, context):
    pass


# registration
def ask_client_name(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Для оформления заказа нам потребуются ваши данные:" +
        "Имя и Номер телефона.\nПожалуйста, введите ваше имя: "
    )
    return NAME


def ask_phone_number(update, context):
    print(update.message.text)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Введите номер телефона:",
    )
    return PHONE_NUMBER


def ask_location(update, context):
    print(update.message.text)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Введите адрес доставки:",
    )
    return LOCATION


def ask_delivery_time(update, context):
    print(update.message.text)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Пожалуйста, укажите удобную вам дату и время доставки.\n\n" +
        "❗️ За доставку в ближайшие 24 часа прибавляется 20% от стоимости заказа.\n\n" +
        "📅 Укажите дату в формате дд.мм.гггг. Например: 23.05.2023.\n\n "+
        "⏱ Укажите временной промежуток, в который подъедет курьер."+
        "Например: с 10:00 до 12:00. Наш курьер свяжется с вами за 30 минут до приезда.\n\n" +
        "Введите дату и время доставки:"
    )
    return DELIVERY_TIME


def leave_comment(update, context):
    print(update.message.text)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Хотите оставить комментарий к заказу?",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "Да",
                callback_data="ask_comment"
            ),
            InlineKeyboardButton(
                "Нет",
                callback_data='registration_success'
            ),
        ]])
    )
    return COMMENT


def ask_comment(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Введите комментарий к заказу:",
    )
    return COMMENT


def registration_success(update, context):
    if update.message:
        print(update.message.text)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Заказ успешно оформлен!",
    )
    return ConversationHandler.END
