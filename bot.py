from EdgeGPT import Chatbot


class Bot:
    def __init__(self, path):
        self.chat_bot = Chatbot(cookiePath=path)

    async def send(self, msg) -> str:
        d = await self.chat_bot.ask(prompt=msg)
        return d['item']['messages'][1]['text']
