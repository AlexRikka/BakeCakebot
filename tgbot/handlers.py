
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import messages as messages
import keyboard as keyboard


def callback_handler(update, context):
    """Запуск команд отловленных CallbackQueryHandler-ом."""
    COMMANDS = {
        'pdconsent_refuse': pdconsent_refuse,
        'pdconsent_agreed': pdconsent_agreed,
        'show_prices': show_prices,
        'make_an_order': make_an_order,
        'show_client_orders': show_client_orders,
        'show_delivery_time': show_delivery_time,
        'leave_complaint': leave_complaint,
    }
    COMMANDS[update.callback_query.data](update, context)
    
    
keyboard.create_keyboard(queryset) #не понимаю что это такое?


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
    messages.pdconsent_refuse(update, context)
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
                "Сделать заказ",
                callback_data='make_an_order'
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
    messages.show_prices(update, context)


def make_an_order(update, context):
    messages.make_an_order(update, context)


def show_client_orders(update, context):
    messages.show_client_orders(update, context)


def show_delivery_time(update, context):
    messages.show_delivery_time(update, context)


def leave_complaint(update, context):
    messages.leave_complaint(update, context)

