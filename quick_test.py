#!/usr/bin/env python3
"""
SAVVY Stock Dashboard - Quick Test Script
Run this script to test the dashboard API functionality
"""

import requests
import time

def test_dashboard_api():
    """Test the dashboard API endpoints"""
    base_url = "http://localhost:5000"
    
    print("🚀 SAVVY Stock Dashboard API Test")
    print("=" * 50)
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/api/health", timeout=5)
        if response.status_code == 200:
            print("✅ Health Check: PASSED")
        else:
            print("❌ Health Check: FAILED")
            return
    except requests.exceptions.RequestException:
        print("❌ Server not running on http://localhost:5000")
        print("💡 Make sure to run: python app.py")
        return
    
    # Test single stock
    print("\n📊 Testing Single Stock Data (AAPL)...")
    try:
        response = requests.get(f"{base_url}/api/stock/AAPL", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ {data.get('name', 'Unknown')}")
            print(f"   Price: ${data.get('current_price', 0):.2f}")
            print(f"   Change: {data.get('price_change_percent', 0):+.2f}%")
        else:
            print("❌ Single stock test failed")
    except Exception as e:
        print(f"❌ Single stock test error: {e}")
    
    # Test multiple stocks
    print("\n📈 Testing Multiple Stocks...")
    try:
        tickers = ["AAPL", "MSFT", "GOOGL"]
        response = requests.post(
            f"{base_url}/api/stocks/multiple", 
            json={"tickers": tickers},
            timeout=15
        )
        if response.status_code == 200:
            data = response.json()
            print("✅ Multiple stocks data retrieved:")
            for ticker, info in data.items():
                if 'error' not in info:
                    price = info.get('current_price', 0)
                    change = info.get('price_change_percent', 0)
                    print(f"   {ticker}: ${price:.2f} ({change:+.2f}%)")
        else:
            print("❌ Multiple stocks test failed")
    except Exception as e:
        print(f"❌ Multiple stocks test error: {e}")
    
    # Test historical data
    print("\n📉 Testing Historical Data (TSLA, 5d)...")
    try:
        response = requests.get(
            f"{base_url}/api/stock/TSLA?period=5d&interval=1d", 
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            hist_count = len(data.get('historical_data', []))
            print(f"✅ Historical data: {hist_count} records")
        else:
            print("❌ Historical data test failed")
    except Exception as e:
        print(f"❌ Historical data test error: {e}")
    
    print("\n🎉 Dashboard API testing complete!")
    print("🌐 Open the frontend: package/qash/src/index.html")

if __name__ == "__main__":
    test_dashboard_api()
