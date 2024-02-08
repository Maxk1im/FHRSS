import feedparser
import telebot

# Створіть екземпляр бота
bot = telebot.TeleBot("6496665739:AAGRoDM3hT_03hJPB0sclZ4FfvYtLB6ZdkM")

# Додайте URL-адресу RSS-каналу
rss_url = "https://freelancehunt.com/project/skill/113.rss"

# Функція для обробки оновлень RSS
def handle_rss_update(feed):
    for entry in feed.entries:
        # Надішліть заголовок та посилання на нову статтю
        bot.send_message(chat_id="@FreelanseHunt",
                         text=f"{entry.title}\n{entry.link}")

# Запустіть бота
bot.polling()

# Отримайте дані RSS
feed = feedparser.parse(rss_url)

# Обробіть оновлення RSS
handle_rss_update(feed)
