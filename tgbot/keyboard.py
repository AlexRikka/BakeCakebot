from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def create_keyboard(queryset): а здесь это тпараметр есть... как так.
    """Создает вертикальную клавиатуру с именами объектов из Queryset."""
    keyboard = [
        [InlineKeyboardButton(
            item.name,
            callback_data=item.name
        )] for item in queryset
    ]
    return InlineKeyboardMarkup(keyboard)