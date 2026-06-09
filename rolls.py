from random import randint as random
import asyncio


async def roll_deploy():
    card = random(1, 6)
    return f'deploy/{card}.jpg'

async def roll_second(drop):
    if drop == None:
        print('Сброшена обе карты либо их нет впринцепе')
        
    else:
        print('Сброшена онда карта')
    


if __name__ == "__main__":
    roll_second('1.jpg')