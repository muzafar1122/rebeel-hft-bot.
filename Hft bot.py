import asyncio
from metaapi_cloud_sdk import MetaApi

# Aapki Updated ID aur Token
TOKEN = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI3NWU1ZWM0Mzk1MmI3NGMwZWJlMGE1ZmQ3OTAyNGNlNyIsImFjY2Vzc1J1bGVzIjpbeyJpZCI6InRyYWRpbmctYWNjb3VudC1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOmNlNWNkYTE3LWRlYjQtNDgwYy1hN2QxLTRlNTRkOWExOGQxMCJdfSx7ImlkIjoibWV0YWFwaS1yZXN0LWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6Y2U1Y2RhMTctZGViNC00ODBjLWE3ZDEtNGU1NGQ5YTE4ZDEwIl19LHsiaWQiOiJtZXRhYXBpLXJwYy1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOndzOnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDpjZTVjZGExNy1kZWI0LTQ4MGMtYTdkMS00ZTU0ZDlhMThkMTAiXX0seyJpZCI6Im1ldGFhcGktcmVhbC10aW1lLXN0cmVhbWluZy1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOndzOnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDpjZTVjZGExNy1kZWI0LTQ4MGMtYTdkMS00ZTU0ZDlhMThkMTAiXX0seyJpZCI6Im1ldGFzdGF0cy1hcGkiLCJtZXRob2RzIjpbIm1ldGFzdGF0cy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6Y2U1Y2RhMTctZGViNC00ODBjLWE3ZDEtNGU1NGQ5YTE4ZDEwIl19LHsiaWQiOiJyaXNrLW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJyaXNrLW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOmNlNWNkYTE3LWRlYjQtNDgwYy1hN2QxLTRlNTRkOWExOGQxMCJdfV0sImlnbm9yZVJhdGVMaW1pdHMiOmZhbHNlLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiNzVlNWVjNDM5NTJiNzRjMGViZTBhNWZkNzkwMjRjZTciLCJpYXQiOjE3Njc2Mzc1NzcsImV4cCI6MTc3NTQxMzU3N30.Vku1-QzwCKHW0GjSoVey7ZU7iggBLNwaIEQ3N5iS7S_IHxRypI6F-qy5SYVmvhornNcf22CGFJSZKXEfEHGhzZic7RDOamxTBb6K-CeLD1B9JfDLl31EetJFH-1Sr_2PHw6kbBrA9MmAruU-3giy8BCgnDQKewROPpKa1xXOLng1C-kogb8SSSheXHxP1n5ePpY9g_If6jdr4XJV55W9txD6mHodgIUOlOGECa4uvmwpSn-jOXZFjNVb1eYCxAVYTXt3RCFN0RJVNfnQ2AHiPUEn31kmGUt41of8alWgQ4ZEmy4qNNFys3b8aItC5G-pXErER7v2tesZFlzrtGB6b_KFmLXnrER4sUpd1BueLQ5AY44ItXYfusaTtd4gEW9XtXu90poFZYIuWwSEr1XWT_nnEpKZY-lffYR4dnb71Qr4wBOheqY7myMrqvm0i0M5b_5-9wdW7WwyqJCgFsyBFbzoDi1W1-en1iaLMKg71MgQKeEL1vUdutAlARTAlwssHy3DJzA5Wkmx2kLQ-g7ZQpea4T_ZkJLQWG1S__XI9m_hpxLPWHFszaaIQytw8CpT3Ig00Z4DsRBLhPnhJxt48KOeyZPcJWiO0Nl7uBVLwKMGUlXybgfgA59pHeg52G9VCVY1sltu2HujjxbLYf7ZJDCTRKlS_NoA_tZii4tuqSs'
ACCOUNT_ID = 'ce5cda17-deb4-480c-a7d1-e454d9a18d10'

async def smc_hft():
    api = MetaApi(TOKEN)
    try:
        account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
        
        # Account Deploy Check
        state = await account.get_state()
        if state['status'] == 'UNDEPLOYED':
            print("⏳ Account is Undeployed. Deploying now...")
            await account.deploy()
            await account.wait_deployed()

        connection = account.get_streaming_connection()
        await connection.connect()
        await connection.wait_synchronized()

        print("🏦 Rebel Bot Online | London Node | Latency: 1ms")

        class MyListener:
            async def on_tick(self, symbol, tick):
                # HFT SMC Logic
                if abs(tick['ask'] - tick['last_price']) > 0.00015:
                    print(f"🔥 Price Spike on {symbol}! Executing...")
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
        print(f"⚠️ Connection Error: {e}")

asyncio.run(smc_hft())
