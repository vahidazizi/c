from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

# ذخیره امتیازات کاربران
user_scores = {}

# دستور برای شروع بازی و گرفتن امتیاز
def start_game(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id not in user_scores:
        user_scores[user_id] = 0
    update.message.reply_text('بازی شروع شد! امتیاز شما: {}'.format(user_scores[user_id]))

# دستور برای نمایش امتیاز کاربر
def show_score(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id in user_scores:
        update.message.reply_text('امتیاز شما: {}'.format(user_scores[user_id]))
    else:
        update.message.reply_text('شما هنوز بازی نکرده‌اید!')

# دستور برای تبدیل امتیاز به کد هدیه
def redeem_gift(update: Update, context: CallbackContext) -> None:
    # کد هدیه را از امتیاز کاربر تولید کنید و به کاربر ارسال کنید
    pass  # به عنوان مثال، اینجا یک عملیات دیگر اضافه کنید

# دستور برای ارتباط با پشتیبانی
def support(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('برای ارتباط با پشتیبانی، ایمیل بفرستید به: support@example.com')

# دستور برای ایجاد کد رفرال
def generate_referral_code(update: Update, context: CallbackContext) -> None:
    referral_code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    referral_codes[update.message.from_user.id] = referral_code
    update.message.reply_text('کد رفرال شما: {}'.format(referral_code))

# دستور برای نمایش کپچا
def show_captcha(update: Update, context: CallbackContext) -> None:
    captcha_text, data = generate_captcha()
    update.message.reply_text('کد کپچا: {}'.format(captcha_text))
    update.message.reply_photo(photo=data)

# تابع اصلی برای شروع ربات
def main() -> None:
    # تنظیم و شروع ربات
    updater = Updater("6618575314:AAEhdwtRFhFelEvQDUn11n5bpZiwe4OEjUs")
    dispatcher = updater.dispatcher

    # افزودن دستورها به ربات
    dispatcher.add_handler(CommandHandler("start", start_game))
    dispatcher.add_handler(CommandHandler("score", show_score))
    dispatcher.add_handler(CommandHandler("redeem", redeem_gift))
    dispatcher.add_handler(CommandHandler("support", support))
    dispatcher.add_handler(CommandHandler("referral", generate_referral_code))
    dispatcher.add_handler(CommandHandler("captcha", show_captcha))
    dispatcher.add_handler(MessageHandler(Filters.text, support))  # به عنوان مثال فقط پیام‌های متنی را پاسخ می‌دهد

    # شروع ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
