from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from crud_functions import *

# api = # Ваш API
api = "7343567045:AAGB_RGzc4qtvTpcOe3GLq9mABL3q8kHq1I"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton('Рассчитать')
button2 = KeyboardButton('Информация')
button3 = KeyboardButton('Купить')
kb.add(button, button2)
kb.row(button3)

ik = InlineKeyboardMarkup()
ibutton = InlineKeyboardButton(text='Расчитать норму каллорий', callback_data='calories')
ibutton2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
ik.add(ibutton, ibutton2)

it = InlineKeyboardMarkup()
iproduct1 = InlineKeyboardButton(text='Продукт №1', callback_data='product_buying')
iproduct2 = InlineKeyboardButton(text='Продукт №2', callback_data='product_buying')
iproduct3 = InlineKeyboardButton(text='Продукт №3', callback_data='product_buying')
iproduct4 = InlineKeyboardButton(text='Продукт №4', callback_data='product_buying')
it.row(iproduct1, iproduct2, iproduct3, iproduct4)

initiate_db()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выбрите опцию:', reply_markup=ik)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    for product in products:
        await message.answer(f'Название: {product[1]} | '
                             f'Описание: {product[2]} | '
                             f'Цена: {product[3]}')

        with open(f'image/img{product[0]}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки', reply_markup=it)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;')
    await call.answer()


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    weight = int(data['weight'])
    growth = int(data['growth'])
    age = int(data['age'])
    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша суточная норма калорий: {calories:.2f} ккал")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
