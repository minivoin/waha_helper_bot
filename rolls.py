from random import randint as random
import asyncio


async def roll_deploy():
    card = random(1, 5)
    return f'deploy/{card}.jpg'

async def roll_second():
    card = random(1, 16)
    return f'second/{card}.jpg'


async def roll_rule():
    card = random(1, 12)
    return f'rule/{card}.jpg'
    


if __name__ == "__main__":
    roll_second('1.jpg')