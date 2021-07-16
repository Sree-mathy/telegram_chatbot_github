from telegram.ext import Updater,MessageHandler,Filters
from Adafruit_IO import Client

aio = Client('Sreemathy', os.getenv('Sreemathy'))

def lighton(bot,update):
  chat_id=bot.message.chat_id
  aio.send('bedroom-light', 1)
  data = aio.receive('bedroom-light')
  print(f'Received value for light: {data.value}')
  path='https://cdn5.vectorstock.com/i/1000x1000/54/04/3d-realistic-turning-on-and-off-light-bulb-vector-27865404.jpg'
  bot.message.reply_text('Light Turned On')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def lightoff(bot,update):
  chat_id=bot.message.chat_id
  aio.send('bedroom-light', 0)
  data = aio.receive('bedroom-light')
  print(f'Received value for light: {data.value}')
  path='https://thumbs.dreamstime.com/z/glowing-light-bulb-icon-off-vector-eps-35075163.jpg'
  bot.message.reply_text('Light Turned Off')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

  
def fan_on(bot,update):
  chat_id=bot.message.chat_id
  aio.send('fan', 1)
  data = aio.receive('fan')
  print(f'Received value for fan: {data.value}')
  path='https://thumbs.dreamstime.com/b/high-speed-fan-running-top-roof-174506393.jpg'
  bot.message.reply_text('Fan Turned On')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def fan_off(bot,update):
  chat_id=bot.message.chat_id
  aio.send('fan', 0)
  data = aio.receive('fan')
  print(f'Received value for fan: {data.value}')
  path='https://www.tricityhvac.net/wp-content/uploads/2021/03/Does-Running-A-Ceiling-Fan-help-keep-room-cooler.jpg'
  bot.message.reply_text('Fan Turned Off')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)


def main(bot,update):
  a=bot.message.text
  print(a)

  if a=="Turn on bedroom light":
    lighton(bot,update)
  elif a=="Turn off bedroom light":
    lightoff(bot,update)
  elif a=="Turn on fan":
    fan_on(bot,update)
  elif a=="Turn off fan":
    fan_off(bot,update)
    


BOT_TOKEN=os.getenv('BOT_TOKEN')
u=Updater(BOT_TOKEN,use_context=True)
dp=u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
