import asyncio
from kasa import SmartPlug
import time

async def main():
    
    p = SmartPlug("192.168.0.21")

    await p.update()
    #print(p.alias)

    i = 1
    on = False
    while i <= 12:
        time.sleep(0.5)
        if on:
            await p.turn_off()
            on = False
        else:
            await p.turn_on()
            on = True
        print(i)
        i += 1


if __name__ == "__main__":
    asyncio.run(main())