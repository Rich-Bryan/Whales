# Smart_Flow

## Step to set up a env 

### Mac
```
python3 -m venv .venv
```

### Window
```
py -3 -m venv .venv
```

## Activate the environment 

### Mac
```
. .venv/bin/activate
```
### Window 
```
.venv\Scripts\activate
```

## need to make a config.py file for your API keys

```python
API_KEYS = "Your API keys"
```
## How to use it 

after getting your API key you have to run insider.py to get the data in a JSON format that looks like this
```json
{
    "aggressor_ind": "0.52",
    "ask": "4.9",
    "bid": "4.65",
    "cost_basis": "47381.399999999994",
    "date": "2024-02-02",
    "date_expiration": "2024-02-09",
    "description": "Apple Option Alert: Feb 9 $190 Puts Sweep (5) near the midpoint: 99 vs 11721 OI",
    "description_extended": "Apple Option Alert: Feb 9 $190 Puts Sweep (5) near the midpoint: 99 @ $4.786 vs 11721 OI; Ref=$186.0",
    "exchange": "NASDAQ",
    "execution_estimate": "AT_ASK",
    "id": "65bd57cab95b290001dc9c6e",
    "midpoint": "4.775",
    "open_interest": "11721",
    "option_activity_type": "SWEEP",
    "option_symbol": "AAPL240209P00190000",
    "price": "4.81",
    "put_call": "PUT",
    "sentiment": "NEUTRAL",
    "size": "99",
    "strike_price": "190.00",
    "ticker": "AAPL",
    "time": "15:59:54",
    "trade_count": 5,
    "underlying_price": "186.0",
    "underlying_type": "STOCK",
    "updated": 1706907594,
    "volume": "3291"
}
```

## website where the data is coming from
https://www.benzinga.com/apis/
