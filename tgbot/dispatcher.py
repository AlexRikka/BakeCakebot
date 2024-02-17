from telegram.ext import (
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    MessageHandler,
    Filters

)
import handlers

NAME, PHONE_NUMBER, LOCATION, DELIVERY_TIME, COMMENT = range(5)


def setup_dispatcher(dp):
    # start
    dp.add_handler(CommandHandler("start", handlers.start_callback))
    dp.add_handler(CommandHandler(
        "pdconsent_refuse", handlers.pdconsent_refuse))
    dp.add_handler(CommandHandler(
        "pdconsent_agreed", handlers.pdconsent_agreed))

    # main menu
    dp.add_handler(CommandHandler(
        "show_prices", handlers.show_prices))
    dp.add_handler(CommandHandler(
        "show_client_orders", handlers.show_client_orders))
    dp.add_handler(CommandHandler(
        "show_delivery_time", handlers.show_delivery_time))
    dp.add_handler(CommandHandler("leave_complaint", handlers.leave_complaint))

    # any callback
    dp.add_handler(CallbackQueryHandler(handlers.callback_handler))

    # reistration
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler(
            "ask_client_name", handlers.ask_client_name)],

        states={
            NAME: [MessageHandler(Filters.text, handlers.ask_phone_number)],
            PHONE_NUMBER: [
                MessageHandler(Filters.text, handlers.ask_location)
            ],
            LOCATION: [
                MessageHandler(Filters.text, handlers.ask_delivery_time)
            ],
            DELIVERY_TIME: [
                MessageHandler(Filters.text, handlers.leave_comment)
            ],
            COMMENT: [
                MessageHandler(Filters.text, handlers.registration_success)
            ]
        },
        fallbacks=[CommandHandler(
            "ask_client_name", handlers.ask_client_name)]
    )
    dp.add_handler(conv_handler)

    return dp
