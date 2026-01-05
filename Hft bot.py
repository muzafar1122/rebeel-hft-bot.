import asyncio
from metaapi_cloud_sdk import MetaApi

# Fixed Formatting
TOKEN = ''
ACCOUNT_ID = 'eyJfaWQiOiI3NWU1ZWM0Mzk1MmI3NGMwZWJlMGE1ZmQ3OTAyNGNlNyIsImFjY2Vzc1J1bGVzIjpbeyJpZCI6InRyYWRpbmctYWNjb3VudC1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOmNlNWNkYTE3LWRlYjQtNDgwYy1hN2QxLTRjNTRkOWExOGQxMCJdfSx7ImlkIjoibWV0YWFwaS1yZXN0LWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6Y2U1Y2RhMTctZGViNC00ODBjLWE3ZDEtNGM1NGQ5YTE4ZDEwIl19LHsiaWQiOiJtZXRhYXBpLXJwYy1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOndzOnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDpjZTVjZGExNy1kZWI0LTQ4MGMtYTdkMS00YzU0ZDlhMThkMTAiXX0seyJpZCI6Im1ldGFhcGktcmVhbC10aW1lLXN0cmVhbWluZy1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOndzOnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDpjZTVjZGExNy1kZWI0LTQ4MGMtYTdkMS00YzU0ZDlhMThkMTAiXX0seyJpZCI6Im1ldGFzdGF0cy1hcGkiLCJtZXRob2RzIjpbIm1ldGFzdGF0cy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6Y2U1Y2RhMTctZGViNC00ODBjLWE3ZDEtNGM1NGQ5YTE4ZDEwIl19LHsiaWQiOiJyaXNrLW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJyaXNrLW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOmNlNWNkYTE3LWRlYjQtNDgwYy1hN2QxLTRjNTRkOWExOGQxMCJdfV0sImlnbm9yZVJhdGVMaW1pdHMiOmZhbHNlLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiNzVlNWVjNDM5NTJiNzRjMGViZTBhNWZkNzkwMjRjZTciLCJpYXQiOjE3Njc2Mzc1NzcsImV4cCI6MTc3NTQxMzU3N30'

async def smc_hft():
    api = MetaApi(TOKEN)
    try:
        print("🔍 Connecting to MetaApi...")
        account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
        
        state = await account.get_state()
        if state['status'] != 'DEPLOYED':
            print(f"⏳ Status: {state['status']} | Deploying...")
            await account.deploy()
            await account.wait_deployed()

        connection = account.get_streaming_connection()
        await connection.connect()
        await connection.wait_synchronized()

        print("🏦 Rebel Bot Online | London Node | Latency: 1ms")

        class MyListener:
            async def on_tick(self, symbol, tick):
                if abs(tick['ask'] - tick['last_price']) > 0.00015:
                    print(f"🔥 Spike on {symbol}!")
                    if tick['ask'] > tick['last_price']:
                        await connection.create_market_buy_order(symbol, 0.1)
                    else:
                        await connection.create_market_sell_order(symbol, 0.1)
            async def on_error(self, error):
                print(f"❌ Error: {error}")

        connection.add_synchronization_listener(MyListener())
        while True:
            await asyncio.sleep(1)

    except Exception as e:
        print(f"⚠️ Critical Error: {e}")

if __name__ == "__main__":
    asyncio.run(smc_hft())
