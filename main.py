from config import API
from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery
from prayrequests import PrayRequests
from praytime import PrayTime
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from asyncio import run
from aiogram import F
from aiogram.filters.callback_data import CallbackData
class MainBot:
    def __init__(self, token=API) -> None:
        self.__dp = Dispatcher()
        self.__bt = Bot(token=token)
        ls_btn = ["Toshkent","Andijon","Samarqand","Buxoro","Farg'ona","Qo'qon","Namangan","Jizzax","Qashqadaryo","Xorazm","Surxandaryo","Qora qalpog'iston Respublikasi"]
        box = InlineKeyboardBuilder()
        for reg in ls_btn:
            box.add(InlineKeyboardButton(text=reg, callback_data = "reg:"+reg))
        box.adjust(4,4)
        self.bx = box.as_markup()

    async def start_message(self, msg:Message):
        await msg.answer(text="Assalomu alaykum viloyatingizni  tanlang!", reply_markup=self.bx)

    async def region_callback(self, clb:CallbackQuery):
        data = clb.data.split(":")
        vil = data[1]
        pr = PrayRequests(vil)
        pr.requests()
        pt = PrayTime(pr.Content)
        pt.scrapping()
        await clb.message.answer(f"Ayni paytda {vil}dagi namoz vaqtlari:", reply_markup=pt.get_keyboards())
        await clb.answer(text="ANSWER")

    def register(self):
        self.__dp.message.register(self.start_message,Command("start"))
        self.__dp.callback_query.register(self.region_callback)

    async def start(self):
        try:
            self.register()
            await self.__dp.start_polling(self.__bt)
        except:
            await self.__bt.session.close()

if __name__ == "__main__":
    mn = MainBot()
    run(mn.start())
