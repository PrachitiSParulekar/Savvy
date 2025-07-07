# SAVVY - Stock Price Dashboard

SAVVY is a comprehensive stock market dashboard that provides real-time stock data, historical charts, and market insights through an intuitive web interface.

## Features

- 📊 **Real-time Stock Data**: Live stock prices and market updates
- 📈 **Interactive Charts**: TradingView integration for advanced charting
- 📋 **Stock Information**: Detailed company information, market cap, P/E ratios, and more
- � **Multi-Stock Tracking**: Monitor multiple stocks simultaneously
- 📱 **Mobile Responsive**: Works seamlessly on all devices
- 🌙 **Dark/Light Theme**: Toggle between dark and light themes
- � **Historical Data**: Access historical price data with various time intervals

## Tech Stack

### Backend
- **Python 3.8+**
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing
- **yfinance** - Yahoo Finance API for stock data

### Frontend
- **HTML5/CSS3**
- **JavaScript**
- **Bootstrap 5** - UI framework
- **TradingView Widgets** - Financial charts and data

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SAVVY
   ```

2. **Set up Python environment**
   ```bash
   cd mypython
   pip install -r requirements.txt
   ```

3. **Run the Flask application**
   ```bash
   python app.py
   ```

4. **Open the frontend**
   - Navigate to `package/qash/src/`
   - Open `index.html` in your browser
   - Or use a local server like Live Server

## API Endpoints

### Get Single Stock Data
- **URL**: `/api/stock/<ticker>`
- **Method**: `GET`
- **Parameters**:
  - `period` (optional): Time period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
  - `interval` (optional): Data interval (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)

**Example Request:**
```
GET /api/stock/AAPL?period=1mo&interval=1d
```

**Response:**
```json
{
  "ticker": "AAPL",
  "name": "Apple Inc.",
  "sector": "Technology",
  "industry": "Consumer Electronics",
  "current_price": 175.43,
  "price_change": 2.15,
  "price_change_percent": 1.24,
  "market_cap": 2800000000000,
  "pe_ratio": 28.5,
  "dividend_yield": 0.0044,
  "52_week_high": 198.23,
  "52_week_low": 124.17,
  "avg_volume": 58000000,
  "historical_data": [
    {
      "date": "2024-01-15 09:30:00",
      "open": 174.50,
      "high": 176.82,
      "low": 173.91,
      "close": 175.43,
      "volume": 45000000
    }
  ],
  "last_updated": "2024-01-20 16:00:00"
}
```

### Get Multiple Stocks Data
- **URL**: `/api/stocks/multiple`
- **Method**: `POST`
- **Body**:
```json
{
  "tickers": ["AAPL", "MSFT", "GOOGL"]
}
```

**Response:**
```json
{
  "AAPL": {
    "name": "Apple Inc.",
    "current_price": 175.43,
    "price_change": 2.15,
    "price_change_percent": 1.24,
    "market_cap": 2800000000000
  },
  "MSFT": {
    "name": "Microsoft Corporation",
    "current_price": 378.85,
    "price_change": -1.50,
    "price_change_percent": -0.39,
    "market_cap": 2900000000000
  }
}
```

### Health Check
- **URL**: `/api/health`
- **Method**: `GET`
- **Response**: Server health status

## Stock Data Features

The dashboard provides comprehensive stock information including:
- **Real-time Prices**: Current stock prices with live updates
- **Price Changes**: Absolute and percentage price changes
- **Company Information**: Sector, industry, and company details
- **Financial Metrics**: Market cap, P/E ratio, dividend yield
- **52-Week Range**: Yearly high and low prices
- **Volume Data**: Trading volume and average volume
- **Historical Charts**: Customizable time periods and intervals

### Supported Data Periods
- **Intraday**: 1d, 5d
- **Short-term**: 1mo, 3mo, 6mo
- **Long-term**: 1y, 2y, 5y, 10y
- **Special**: ytd (year-to-date), max (all available data)

### Data Intervals
- **Minutes**: 1m, 2m, 5m, 15m, 30m, 60m, 90m
- **Hours**: 1h
- **Days**: 1d, 5d
- **Weeks/Months**: 1wk, 1mo, 3mo

## Frontend Features

### Dashboard Components
- **Stock Price Cards**: Quick overview of major stocks
- **Interactive Charts**: TradingView integration for advanced charting
- **Market Ticker**: Real-time stock price ticker
- **Navigation**: Easy access to different sections

### Supported Stocks
- Apple (AAPL)
- Microsoft (MSFT)
- Intel (INTC)
- NVIDIA (NVDA)
- Disney (DIS)
- JPMorgan Chase (JPM)
- Taiwan Semiconductor (TSM)

## Configuration

### Environment Variables
Create a `.env` file in the `mypython` directory:
```env
FLASK_ENV=development
FLASK_DEBUG=True
```

### CORS Configuration
The application is configured to allow cross-origin requests for development. For production, update the CORS settings in `app.py`.

## Development

### Project Structure
```
SAVVY/
├── mypython/
│   ├── app.py              # Flask application
│   ├── views.py            # Flask routes
│   ├── test_api.py         # API testing script
│   ├── requirements.txt    # Python dependencies
│   └── templates/          # HTML templates
├── package/
│   └── qash/
│       ├── src/            # Frontend HTML files
│       └── package.json    # Node.js dependencies
└── README.md
```

### Adding New Features
1. **New API Endpoints**: Add routes in `app.py`
2. **Frontend Components**: Update HTML files in `package/qash/src/`
3. **Stock Data Sources**: Extend yfinance integration for additional data

## Troubleshooting

### Common Issues

1. **Module Not Found Error**
   ```bash
   pip install -r requirements.txt
   ```

2. **CORS Errors**
   - Ensure Flask-CORS is installed
   - Check CORS configuration in `app.py`

3. **Stock Data Not Loading**
   - Verify internet connection
   - Check if the ticker symbol is valid
   - Ensure yfinance is up to date

4. **TradingView Widgets Not Loading**
   - Check internet connection
   - Verify widget script URLs
   - Ensure JavaScript is enabled

5. **API Rate Limits**
   - Yahoo Finance may have rate limits
   - Add delays between requests for multiple stocks
   - Consider caching frequently requested data

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the GitHub repository
- Check the troubleshooting section
- Review the API documentation

## Roadmap

- [ ] Add more stock exchanges (international markets)
- [ ] Implement portfolio tracking
- [ ] Add user authentication and personal watchlists
- [ ] Create mobile app
- [ ] Add more technical indicators and analysis tools
- [ ] Implement real-time alerts and notifications
- [ ] Add cryptocurrency support
- [ ] Create data export functionality
- [ ] Add market news integration
- [ ] Implement advanced filtering and screening tools

---

**Disclaimer**: This platform is for educational and informational purposes only. Stock data and analysis should not be considered as financial advice. Always do your own research before making investment decisions.
