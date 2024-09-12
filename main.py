import os
import asyncio

from core.clicker.blum import BlumClicker
from main.static import CREDITSTelegramChannel, AUTOCLICKER_TEXT, DONATE_TEXT


async def main() -> None:
    os.system("cls")

    print(AUTOCLICKER_TEXT)
    print(CREDITSTelegramChannel)
    print(DONATE_TEXT)

    clicker = BlumClicker()
    await clicker.run()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting due to keyboard interrupt.")
