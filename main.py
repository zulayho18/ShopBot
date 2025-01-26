from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
import os

# Inline tugmalar
inline_buttons = [
    [InlineKeyboardButton("Choyshablar", callback_data='Choyshablar'),
     InlineKeyboardButton("Sochiqlar", callback_data='Sochiqlar')],
    [InlineKeyboardButton("Dasturxon", callback_data='Dasturxon'),
     InlineKeyboardButton("Pijamalar", callback_data='Pijamalar')],
    [InlineKeyboardButton("Barcha maxsulotlar", url="https://t.me/+7BWgQHnSRhtlYTcy")]
]

# Loyihaning asosiy papkasi
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mahsulotlar ma'lumotlari
product_details = {
    'choyshablar': {
        'Flamingo': {'narx': "350,000 so'm", "o'lcham": '240x280'},
        'Flamingo-pushti': {'narx': "320,000 so'm", "o'lcham": '240x280'},
        'xitoy': {'narx': "280,000 so'm", "o'lcham": '240x280'},
        'xitoy.': {'narx': "250,000 so'm", "o'lcham": '240x280'},
        'Xitoy,': {'narx': "350,000 so'm", "o'lcham": '240x280'},
        'Xitoy..': {'narx': "260,000 so'm", "o'lcham": '240x280'},
        'spring': {'narx': "280,000 so'm", "o'lcham": '240x280'},
        'FRAME': {'narx': "310,000 so'm", "o'lcham": '240x280'},
        'Vafli': {'narx': "280,000 so'm", "o'lcham": '240x280'},
        'spring.': {'narx': "350,000 so'm", "o'lcham": '240x280'},
        "ko'rpa": {'narx': "250,000 so'm", "o'lcham": '160x280'},
        'smile': {'narx': "260,000 so'm", "o'lcham": '160x280'},
        'beautiful': {'narx': "220,000 so'm", "o'lcham": '160x280'},
        'best': {'narx': "270,000 som", "o'lcham": '200x220'},
        'kosmos': {'narx': "270,000 so'm", "o'lcham": '200x220'},
        'panda': {'narx': "270,000 so'm", "o'lcham": '200x220'},
        "xitoy ko'rpa": {'narx': "280,000 so'm", "o'lcham": '200x220'},
        'matras': {'narx': "150,000 so'm", "o'lcham": '90x200'},
        '2lik matras': {'narx': "180,000 so'm", "o'lcham": '180x200'},
        'zebra': {'narx': "120,000 so'm", "o'lcham": '100x200'},
        'star': {'narx': "120,000 so'm", "o'lcham": '100x200'},
        'chanel': {'narx': "120,000 so'm", "o'lcham": '100x200'},
        'pakrival': {'narx': "150,000 so'm", "o'lcham": '100x200'},
        "Xitoy ko'rpa.": {'narx': "330,000 so'm", "o'lcham": '240x280'},
    },
    'sochiqlar': {
        'xitoy salfetka': {'narx': "80,000 so'm", "o'lcham": '50x100'},
        'salfetka': {'narx': "75,000 so'm", "o'lcham": '70x140'},
        'salfetka nabor': {'narx': "85,000 so'm", "o'lcham": '50x100'},
        'nabor': {'narx': "55,000 so'm", "o'lcham": ''},
        'sochiq koplekt': {'narx': "120,000 so'm", "o'lcham": '70x140'},
        'Xitoy sochiq': {'narx': "95,000 so'm", "o'lcham": '70x140'},
    },
    'dasturxon': {
        'Bayramona dasturxon': {'narx': "220.000 so'm", "o'lcham": '110x220'},
        'kundalik va bayramona dasturxon': {'narx': "140.000 so'm", "o'lcham":'150x190'},
        'gulli dasturxon': {'narx': "170.000 so'm", "o'lcham": '160x190'},
        'nozik gulli dasturxon': {'narx': "180.000 so'm", "o'lcham": '110x200'},
        'nozik torli dasturxon': {'narx': "210.000 so'm", "o'lcham": '80x160'},
        'nozik vishovkali dasturxon': {'narx': "200.000 so'm", "o'lcham": '110x220'},
        'popukli dasturxon': {'narx': "180.000 so'm", "o'lcham": '110x200'},
        'tor vishovkali dasturxon': {'narx': "250.000 so'm", "o'lcham": '120x240'},
    },
    'pijamalar': {
        'Xitoy': {'narx': "90,000 so'm", "o'lcham": 'M L XL XXL'},
        'Xitoy oreginal': {'narx': "95,000 so'm", "o'lcham": 'M L XL XXL'},
        'Xitoy.': {'narx': "85,000 so'm", "o'lcham": 'M L XL XXL'},
        'oreginal': {'narx': "90,000 so'm", "o'lcham": 'M L XL XXL'},
        'Xitoy,': {'narx': "85,000 so'm", "o'lcham": 'M L XL XXL'},
        '.Xitoy': {'narx': "80,000 so'm", "o'lcham": 'M L XL XXL'},
        'Xitoy..': {'narx': "95,000 so'm", "o'lcham": 'M L XL XXL'},
        'black': {'narx': "85,000 so'm", "o'lcham": 'M L XL XXL'},
        '.Xitoy.': {'narx': "90,000 so'm", "o'lcham": 'M L XL XXL'},
        'love': {'narx': "90,000 so'm", "o'lcham": 'M L XL XXL'},
        'Xitoy-': {'narx': "85,000 so'm", "o'lcham": 'M L XL XXL'},
        'bear': {'narx': "75,000 so'm", "o'lcham": 'M L XL XXL'},
        'karma': {'narx': "95,000 so'm", "o'lcham": 'M L XL XXL'},
        'karma.': {'narx': "90,000 so'm", "o'lcham": 'M L XL XXL'},
        'gorox': {'narx': "85,000 so'm", "o'lcham": 'M L XL XXL'},
    },
}

# Savatcha uchun user ma'lumotlari
user_carts = {}

# /start buyrug'iga javob beruvchi funksiya
def start(update: Update, context: CallbackContext):
    user_first_name = update.effective_user.first_name
    main_button = [KeyboardButton(text="Kataloglar"), KeyboardButton(text="Savatcha")]
    reply_markup = ReplyKeyboardMarkup([main_button], resize_keyboard=True)
    welcome_message = f"Salom, {user_first_name}! Biz bilan ekanligingizdan minnatdormiz! ☕️🛍\nYangi mahsulotlarimizni ko'rish uchun 'Kataloglar' tugmasini bosing."
    update.message.reply_text(welcome_message, reply_markup=reply_markup)

# Rasm yuborish va savatchaga qo'shish tugmasi
def send_images_from_folder(folder_name, query, caption_prefix):
    folder_path = os.path.join(BASE_DIR, 'images', folder_name)
    if not os.path.exists(folder_path):
        query.message.reply_text(f"{folder_name} papkasi topilmadi.")
        return
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.png')):
            photo_path = os.path.join(folder_path, filename)
            image_name = os.path.splitext(filename)[0]  # image_name olish
            product_info = product_details.get(folder_name, {}).get(image_name, {'narx': 'Narx mavjud emas', 'olcham': 'Olcham mavjud emas'})
            narx = product_info.get('narx', 'Narx mavjud emas')
            olcham = product_info.get("o'lcham", 'Olcham mavjud emas')
            caption = f"{caption_prefix}: {image_name}\nNarxi: {narx}\nO'lchami: {olcham}"
            button = InlineKeyboardMarkup([[InlineKeyboardButton("Savatchaga qo'shish", callback_data=f"add_{folder_name}_{image_name}")]])
            with open(photo_path, 'rb') as photo:
                query.message.reply_photo(photo=photo, caption=caption, reply_markup=button)

# Rasmiylashtirish va Bosh Menuga Qaytish tugmalari
def complete_purchase(query, context: CallbackContext):
    user_id = query.from_user.id
    cart = user_carts.get(user_id, [])
    if cart:
        items = "\n".join([f"- {item}" for item in cart])
        query.message.reply_text(f"Mahsulotlarni olish uchun quyidagi telefon raqamiga qo'ng'iroq qiling: +998 99 999 99 99\nSavatchangizdagi mahsulotlar:\n{items}")
    else:
        query.message.reply_text("Savatchangiz hozircha bo'sh.")

def return_to_menu(query, context: CallbackContext):
    main_button = [KeyboardButton(text="Kataloglar"), KeyboardButton(text="Savatcha")]
    reply_markup = ReplyKeyboardMarkup([main_button], resize_keyboard=True)


# Xabarlarni qayta ishlovchi funksiya
def message_handler(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    message = update.message.text
    if message == "Kataloglar":
        reply_markup = InlineKeyboardMarkup(inline_buttons)
        update.message.reply_text(text="Katalogni tanlang:", reply_markup=reply_markup)
    elif message == "Savatcha":
        cart = user_carts.get(user_id, [])
        if cart:
            items = "\n".join([f"- {item} ({product_details[item.split(' - ')[0].lower()][item.split(' - ')[1]]['narx']})" for item in cart])
            buttons = [
                [InlineKeyboardButton("Rasmiylashtirish", callback_data='complete_purchase')],
                ]
            update.message.reply_text(f"Savatchangizdagi mahsulotlar:\n{items}", reply_markup=InlineKeyboardMarkup(buttons))
        else:
            update.message.reply_text("Savatchangiz hozircha bo'sh.")
    else:
        update.message.reply_text("Iltimos, menyudan tanlang.")


# Inline tugmalarga javob beruvchi funksiya
def inline_messages(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    query.answer()

    if query.data.startswith("add_"):
        _, category, item_name = query.data.split('_', 2)
        user_carts.setdefault(user_id, []).append(f"{category.capitalize()} - {item_name}")
        query.message.reply_text(f"{item_name} savatchaga qo'shildi!")
    elif query.data == 'Choyshablar':
        send_images_from_folder('choyshablar', query, 'Choyshab')
    elif query.data == 'Sochiqlar':
        send_images_from_folder('sochiqlar', query, 'Sochiq')
    elif query.data == 'Dasturxon':
        send_images_from_folder('dasturxon', query, 'Dasturxon')
    elif query.data == 'Pijamalar':
        send_images_from_folder('pijamalar', query, 'Pijama')
    elif query.data == 'complete_purchase':
        complete_purchase(query, context)
    elif query.data == 'return_to_menu':
        return_to_menu(query, context)

# Botni ishga tushuruvchi kod
def main():
    TOKEN = '8114195716:AAFpeDG5OyLaPOSJ1Up2HdRTQV-3MsFF_v8'
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, message_handler))
    dp.add_handler(CallbackQueryHandler(inline_messages))

    print("Bot ishga tushdi!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


