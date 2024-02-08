import feedparser
import telebot

# Створіть екземпляр бота
bot = telebot.TeleBot("YOUR_BOT_TOKEN")

# Додайте URL-адресу RSS-каналу
rss_url = "YOUR_RSS_FEED_URL"

# Функція для обробки оновлень RSS
def handle_rss_update(feed):
    for entry in feed.entries:
        # Надішліть заголовок та посилання на нову статтю
        bot.send_message(chat_id="@YOUR_CHANNEL_USERNAME",
                         text=f"{entry.title}\n{entry.link}")

# Запустіть бота
bot.polling()

# Отримайте дані RSS
feed = feedparser.parse(rss_url)

# Обробіть оновлення RSS
handle_rss_update(feed)
