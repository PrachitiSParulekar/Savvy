import requests
import sys

BASE_URL = "http://localhost:5000"

def test_health():
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print(f"Health: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health failed: {e}")
        return False

def test_single_stock(ticker="AAPL"):
    try:
        response = requests.get(f"{BASE_URL}/api/stock/{ticker}")
        print(f"Single Stock ({ticker}): {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"  Name: {result.get('name')}")
            print(f"  Current Price: ${result.get('current_price'):.2f}")
            print(f"  Change: {result.get('price_change'):+.2f} ({result.get('price_change_percent'):+.2f}%)")
        return response.status_code == 200
    except Exception as e:
        print(f"Single stock test failed: {e}")
        return False

def test_multiple_stocks():
    try:
        tickers = ["AAPL", "MSFT", "GOOGL"]
        response = requests.post(f"{BASE_URL}/api/stocks/multiple", json={"tickers": tickers})
        print(f"Multiple Stocks: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            for ticker, data in result.items():
                if 'error' not in data:
                    print(f"  {ticker}: ${data.get('current_price', 'N/A'):.2f}")
        return response.status_code == 200
    except Exception as e:
        print(f"Multiple stocks test failed: {e}")
        return False

def test_historical_data(ticker="TSLA"):
    try:
        response = requests.get(f"{BASE_URL}/api/stock/{ticker}?period=5d&interval=1h")
        print(f"Historical Data ({ticker}): {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            hist_data = result.get('historical_data', [])
            print(f"  Historical records: {len(hist_data)}")
        return response.status_code == 200
    except Exception as e:
        print(f"Historical data test failed: {e}")
        return False

def main():
    print("=== SAVVY Stock Dashboard API Tests ===")
    
    health_ok = test_health()
    if not health_ok:
        print("❌ Server not running")
        sys.exit(1)
    
    single_ok = test_single_stock("AAPL")
    multiple_ok = test_multiple_stocks()
    historical_ok = test_historical_data("TSLA")
    
    all_pass = health_ok and single_ok and multiple_ok and historical_ok
    print(f"\n{'✅ ALL TESTS PASSED' if all_pass else '❌ SOME TESTS FAILED'}")

if __name__ == "__main__":
    main()
