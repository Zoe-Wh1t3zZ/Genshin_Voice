import random
import os
import requests

from nonebot import MessageSegment
import hoshino
from hoshino import R, Service, priv, util
from nonebot import NoticeSession
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Shanghai')

sv = Service('早晚安语音', enable_on_default=True)

@sv.on_fullmatch(('早安', '早安哦', '早上好', '早上好啊', '早上好呀', '早', 'good morning'))
async def random_mornling(bot, ev):
    mornling_folder = R.get('record/mornling/').path
    files = os.listdir(mornling_folder)
    filename = random.choice(files)
    file = R.get('record/mornling/', filename)
    rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
    now_hour=datetime.now(tz).hour
    if 0<=now_hour<6:
        await bot.send(ev, f'好早，现在才{now_hour}点呢', at_sender=True)
    elif 6<=now_hour<10:
        await bot.send(ev, f'早上好！今天打算做什么呢？', at_sender=True)
        await bot.send(ev, rec)
    elif 21<=now_hour<24:
        await bot.send(ev, f'别闹，准备睡觉啦！', at_sender=True)
    else:
        await bot.send(ev, f'{now_hour}点了才起床吗…', at_sender=True)

@sv.on_fullmatch(('午安', '午安哦', '中午好', '中午好啊', '中午好呀', '下午好', 'good noon'))
async def random_noon(bot, ev):
    noon_folder = R.get('record/noon/').path
    files = os.listdir(noon_folder)
    filename = random.choice(files)
    file = R.get('record/noon/', filename)
    rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
    now_hour=datetime.now(tz).hour
    if 11<=now_hour<15:
        await bot.send(ev, f'中午好，旅行者', at_sender=True)
        await bot.send(ev, rec)
    elif 15<=now_hour<16:
        await bot.send(ev, f'下午好！我们去找可莉一起炸鱼吧！', at_sender=True)
    elif 17<=now_hour<18:
        await bot.send(ev, f'马上准备吃饭了！派蒙想吃蜜酱胡萝卜煎肉', at_sender=True)

@sv.on_fullmatch(('晚上好', '晚上好啊', '晚上好呀', '晚好'))
async def random_evening(bot, ev):
    evening_folder = R.get('record/evening/').path
    files = os.listdir(evening_folder)
    filename = random.choice(files)
    file = R.get('record/evening/', filename)
    rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')  
    now_hour=datetime.now(tz).hour
    if 18<=now_hour<24:
        await bot.send(ev, f'晚上好！今晚想做什么呢？', at_sender=True)
        await bot.send(ev, rec)  
    elif 0<=now_hour<6:
        await bot.send(ev, f'{now_hour}点啦，还不睡吗？', at_sender=True)
    elif 6<=now_hour<=9:
        await bot.send(ev, f'晚上好…嗯？我刚起床呢', at_sender=True)
    else:
        await bot.send(ev, f'现在才{now_hour}点，还没天黑呢。嘿嘿', at_sender=True)

@sv.on_fullmatch(('晚安', '晚安哦', '晚安啦', 'good night', '睡了'))
async def random_sleeping(bot, ev):
    now_hour=datetime.now(tz).hour
    sleeping_folder = R.get('record/sleeping/').path
    files = os.listdir(sleeping_folder)
    filename = random.choice(files)
    file = R.get('record/sleeping/', filename)
    rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')    
    if now_hour<=3 or now_hour>=21:
        await bot.send(ev, '晚安~', at_sender=True)
        await bot.send(ev, rec)
    elif 19<=now_hour<21:
        await bot.send(ev, f'现在才{now_hour}点，这么早就睡了吗？', at_sender=True)
    else:
        await bot.send(ev, f'现在才{now_hour}点，还没到晚上咧。嘿嘿', at_sender=True)
        
@sv.on_fullmatch(('生日快乐', '生快', 'happy birthday', '过生日','祝你生日快乐'))
async def random_birthday(bot, ev):
    now_hour=datetime.now(tz).hour
    birthday_folder = R.get('record/birthday/').path
    files = os.listdir(birthday_folder)
    filename = random.choice(files)
    file = R.get('record/birthday/', filename)
    rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')    
    await bot.send(ev, rec)
   
   
@sv.on_fullmatch('在吗', only_to_me=False)
async def woaini(bot, ev):
    if random.random() <= 0.1:
        voice = R.get('record/zai/', 'dear.mp3')
    elif random.random() > 0.1 and random.random() <= 0.8:
        voice = R.get('record/zai/', 'hearme.mp3')
    else:
        voice = R.get('record/zai/', 'goaway.mp3')
    rec = MessageSegment.record(f'file:///{os.path.abspath(voice.path)}')
    await bot.send(ev, rec)
