import re

from EdgeGPT import Chatbot, ConversationStyle
from asyncio import Lock

MAX_COUNT = 6
MAX_WORD = 2000
TRY_COUNT = 3

replace_list = [(r'\[\^\d+\^\]', '')]


class Bot:
    def __init__(self, path):
        self.chat_bot = Chatbot(cookiePath=path)
        self.count = 0
        self.lock = Lock()

    async def reset(self):
        await self.chat_bot.reset()
        self.count = 0

    async def send(self, word) -> str:
        if len(word) > MAX_WORD:
            return "word is to long!"

        if self.count >= MAX_COUNT:
            await self.reset()

        answer = ''

        await self.lock.acquire()
        for i in range(TRY_COUNT):
            try:
                answer = await self.chat_bot.ask(prompt=word, conversation_style=ConversationStyle.precise)
            except Exception as e:
                print(f"Error: {e}, try: {i + 1}")
                await self.reset()
                continue
            break
        self.lock.release()

        if not answer:
            return "no answer!"

        self.count += 1

        messages = answer.get('item', {}).get('messages', [])
        if len(messages) != 2:
            return f"messages len != 2: {str(answer)}"

        answer = messages[1].get('text', "出错啦，没找到回答内容")

        for replace in replace_list:
            answer = re.sub(replace[0], replace[1], answer)

        return answer
