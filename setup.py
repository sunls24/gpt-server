from flask import Flask

from bot import Bot

app = Flask(__name__)

bot = Bot("./cookie.json")


@app.route('/api/translate')
async def hello():
    return await bot.send("hello world 是什么意思")


if __name__ == '__main__':
    app.run()
