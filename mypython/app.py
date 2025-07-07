from flask import Flask, jsonify, request
from flask_cors import CORS
from views import views
import yfinance as yf
import json
from datetime import datetime, timedelta

# Initialize Flask app
app = Flask(__name__, template_folder='templates') 
CORS(app, origins=['*'])

app.register_blueprint(views, url_prefix="/")

@app.route('/api/stock/<ticker>', methods=['GET'])
def get_stock_data(ticker):
    try:
        # Get optional parameters
        period = request.args.get('period', '1d')  # 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
        interval = request.args.get('interval', '1m')  # 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
        
        # Create ticker object
        stock = yf.Ticker(ticker.upper())
        
        # Get stock info
        info = stock.info
        
        # Get historical data
        hist = stock.history(period=period, interval=interval)
        
        if hist.empty:
            return jsonify({'error': 'No data found for ticker symbol'}), 404
        
        # Get current price (latest close)
        current_price = float(hist['Close'].iloc[-1])
        
        # Calculate price change
        if len(hist) > 1:
            prev_price = float(hist['Close'].iloc[-2])
            price_change = current_price - prev_price
            price_change_percent = (price_change / prev_price) * 100
        else:
            price_change = 0
            price_change_percent = 0
        
        # Format historical data
        historical_data = []
        for index, row in hist.iterrows():
            historical_data.append({
                'date': index.strftime('%Y-%m-%d %H:%M:%S'),
                'open': float(row['Open']),
                'high': float(row['High']),
                'low': float(row['Low']),
                'close': float(row['Close']),
                'volume': int(row['Volume'])
            })
        
        # Compile response
        response = {
            'ticker': ticker.upper(),
            'name': info.get('longName', 'N/A'),
            'sector': info.get('sector', 'N/A'),
            'industry': info.get('industry', 'N/A'),
            'current_price': current_price,
            'price_change': round(price_change, 2),
            'price_change_percent': round(price_change_percent, 2),
            'market_cap': info.get('marketCap', 'N/A'),
            'pe_ratio': info.get('trailingPE', 'N/A'),
            'dividend_yield': info.get('dividendYield', 'N/A'),
            '52_week_high': info.get('fiftyTwoWeekHigh', 'N/A'),
            '52_week_low': info.get('fiftyTwoWeekLow', 'N/A'),
            'avg_volume': info.get('averageVolume', 'N/A'),
            'historical_data': historical_data,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': f'Failed to fetch stock data: {str(e)}'}), 500

@app.route('/api/stocks/multiple', methods=['POST'])
def get_multiple_stocks():
    try:
        data = request.get_json()
        if not data or 'tickers' not in data:
            return jsonify({'error': 'Tickers array is required'}), 400
        
        tickers = data['tickers']
        if not isinstance(tickers, list) or len(tickers) == 0:
            return jsonify({'error': 'Invalid tickers array'}), 400
        
        results = {}
        for ticker in tickers:
            try:
                stock = yf.Ticker(ticker.upper())
                info = stock.info
                hist = stock.history(period='1d', interval='1m')
                
                if not hist.empty:
                    current_price = float(hist['Close'].iloc[-1])
                    if len(hist) > 1:
                        prev_price = float(hist['Close'].iloc[-2])
                        price_change = current_price - prev_price
                        price_change_percent = (price_change / prev_price) * 100
                    else:
                        price_change = 0
                        price_change_percent = 0
                    
                    results[ticker.upper()] = {
                        'name': info.get('longName', 'N/A'),
                        'current_price': current_price,
                        'price_change': round(price_change, 2),
                        'price_change_percent': round(price_change_percent, 2),
                        'market_cap': info.get('marketCap', 'N/A')
                    }
                else:
                    results[ticker.upper()] = {'error': 'No data available'}
            except:
                results[ticker.upper()] = {'error': 'Failed to fetch data'}
        
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'message': 'SAVVY Stock Dashboard API is running'})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)