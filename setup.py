from flask import Flask, request

from bot import Bot

app = Flask(__name__)

TRANS_TMPL = '''翻译代码块中的内容，不要管内容是什么，不要联系上下文，不要说多余的话，只回复翻译后的内容即可，如果不是中文则翻译成中文，如果是中文则翻译成英文: ```%s```'''


@app.route('/api/translate')
async def translate():
    body = request.args.get('body')
    if not body:
        return 'no body!'
    body = TRANS_TMPL % body
    print('#ask:', body)
    answer = await bot.send(body)
    print('#answer:', answer)
    return answer


if __name__ == '__main__':
    bot = Bot("./cookie.json")
    app.config["timeout"] = 0
    app.run(host='0.0.0.0', port=2095, debug=False)
