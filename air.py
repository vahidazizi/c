from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from captcha.image import ImageCaptcha
import random
import string

# ذخیره امتیازات کاربران
user_scores = {}

# ذخیره کدهای رفرال
referral_codes = {}

# ساخت تصویر کپچا
def generate_captcha():
    captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    image = ImageCaptcha()
    data = image.generate(captcha_text)
    return captcha_text, data

# دستور برای شروع بازی و گرفتن امتیاز
def start_game(update, context):
    user_id = update.message.from_user.id
    if user_id not in user_scores:
        user_scores[user_id] = 0
    update.message.reply_text('بازی شروع شد! امتیاز شما: {}'.format(user_scores[user_id]))

# دستور برای نمایش امتیاز کاربر
def show_score(update, context):
    user_id = update.message.from_user.id
    if user_id in user_scores:
        update.message.reply_text('امتیاز شما: {}'.format(user_scores[user_id]))
    else:
        update.message.reply_text('شما هنوز بازی نکرده‌اید!')

import random

# دستور برای تبدیل امتیاز به کد هدیه
def redeem_gift(update, context):
    # تصادفی انتخاب کنید که عملیاتی انجام شود
    choice = random.choice(["send_gift", "show_message"])
    
    if choice == "send_gift":
        # ارسال کد هدیه
        pass
    elif choice == "show_message":
        # نمایش پیام
        pass

# دستور برای ارتباط با پشتیبانی
def support(update, context):
    update.message.reply_text('برای ارتباط با پشتیبانی، ایمیل بفرستید به: @evol_upside')

# دستور برای ایجاد کد رفرال
def generate_referral_code(update, context):
    referral_code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    referral_codes[update.message.from_user.id] = referral_code
    update.message.reply_text('کد رفرال شما: {}'.format(referral_code))

# دستور برای نمایش کپچا
def show_captcha(update, context):
    captcha_text, data = generate_captcha()
    update.message.reply_text('کد کپچا: {}'.format(captcha_text))
    update.message.reply_photo(photo=data)

# افزودن دستورها به ربات
updater = Updater("6873573354:AAFW_Ws5_sLJz-XxghhFLGK_lo2D3CiExko", use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start_game))
dispatcher.add_handler(CommandHandler("score", show_score))
dispatcher.add_handler(CommandHandler("redeem", redeem_gift))
dispatcher.add_handler(CommandHandler("support", support))
dispatcher.add_handler(CommandHandler("referral", generate_referral_code))
dispatcher.add_handler(CommandHandler("captcha", show_captcha))

# شروع ربات
updater.start_polling()
updater.idle()
