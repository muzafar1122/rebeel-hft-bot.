import asyncio
from metaapi_cloud_sdk import MetaApi

# Rebel Credentials
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' # Apna token rehne dein
ACCOUNT_ID = 'ce5cda17-deb4-480c-a7d1-e454d9a18d10'

async def smc_hft():
    api = MetaApi(TOKEN)
    account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
    connection = account.get_streaming_connection()
    await connection.connect()
    await connection.wait_synchronized() # Ye line zaroori hai

    print("🏦 Rebel Bot Online | London Node | Latency: 1ms")

    class MyListener:
        async def on_tick(self, symbol, tick):
            if abs(tick['ask'] - tick['last_price']) > 0.00015:
                print(f"🔥 Strike on {symbol}!")
                if tick['ask'] > tick['last_price']:
                    await connection.create_market_buy_order(symbol, 0.1)
                else:
                    await connection.create_market_sell_order(symbol, 0.1)

    # Naya tarika listener add karne ka
    connection.add_synchronization_listener(MyListener())

asyncio.run(smc_hft())
