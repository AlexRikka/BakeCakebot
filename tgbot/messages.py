def pdconsent_refuse(update, context):
    """Попрощаться после отказа предоставления персональных данных."""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="К сожалению, без согласия нельзя продолжить заказ через бота."
    )

def show_prices(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Вы выбрали функцию узнать цены"
    )


def make_an_order(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Вы выбрали функцию сделать заказ"
    )


def show_client_orders(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Вы выбрали функцию показать заказы"
    )


def show_delivery_time(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Вы выбрали функцию показать время отправки"
    )


def leave_complaint(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Вы выбрали функцию показать оставить жалобу"
    )
