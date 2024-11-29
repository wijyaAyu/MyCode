from fastapi import FastAPI, HTTPException
import requests
import nest_asyncio
import uvicorn

nest_asyncio.apply()

app = FastAPI()

API_KEY = "a73cc1771d02c573ba58008f7a80909f"
BASE_URL = "https://api.exchangeratesapi.io/v1/latest"

@app.get("/convert_rate/")
def get_convert(base_currency: str, target_currency: str):
    """ 
    Mengambil data mata uang berdasarkan nama negara.
    """
    # params = {
    #     "q":base_currency,
    #     "appid":API_KEY,
    #     "units": "metric"
    # }

    params = {
        "base": base_currency.upper(),   # Base currency (e.g., USD)
        "symbols": target_currency.upper()  # Target currency (e.g., IDR)
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching convert data.")
    data = response.json()

    if "rates" not in data or target_currency.upper() not in data["rates"]:
        raise HTTPException(status_code=404, detail="Target currency not found in the response.")


    # return {
    #     "base_currency": data["country"],
    #     "target_currency": data["country"],
    #     "exchange_rate": data["currency"]

    # }

    return {
        "base_currency": base_currency.upper(),
        "target_currency": target_currency.upper(),
        "exchange_rate": data["rates"][target_currency.upper()]
    }

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8100)

run_server()

