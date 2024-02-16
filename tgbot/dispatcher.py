from telegram.ext import (
    CommandHandler,
    CallbackQueryHandler,
)
import handlers


def setup_dispatcher(dp):
    # start
    dp.add_handler(CommandHandler("start", handlers.start_callback))
    dp.add_handler(CommandHandler(
        "pdconsent_refuse", handlers.pdconsent_refuse))
    dp.add_handler(CommandHandler(
        "pdconsent_agreed", handlers.pdconsent_agreed))

    # main menu
    dp.add_handler(CommandHandler("show_prices", handlers.show_prices))
    dp.add_handler(CommandHandler(
        "show_client_orders", handlers.show_client_orders))
    dp.add_handler(CommandHandler(
        "show_delivery_time", handlers.show_delivery_time))
    dp.add_handler(CommandHandler("leave_complaint", handlers.leave_complaint))

    # any callback
    dp.add_handler(CallbackQueryHandler(handlers.callback_handler))

    return dp
