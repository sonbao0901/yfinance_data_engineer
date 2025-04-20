# Stock Data Collection System

A Python-based system for collecting and storing stock market data using the Yahoo Finance API (yfinance) and SQL Server.

## Project Structure

```
yfinance_data_engineer/
├── src/
│   ├── __init__.py
│   ├── main.py           # Main data collection script
│   ├── dictionary.py     # Stock ticker dictionary and exchange normalization
│   └── config.py         # Database configuration (not tracked in git)
├── sql/
│   └── yfinance.sql      # SQL Server database schema
├── .gitignore
└── README.md
```

## Features

- Collects comprehensive stock data including:
  - Current market data (price, volume, bid/ask)
  - Company information (sector, industry, employees)
  - Financial metrics (52-week highs/lows, moving averages)
  - Short interest data
  - Company fundamentals
- Stores data in SQL Server database
- Normalizes exchange codes for consistency
- Handles large number of stock tickers

## Prerequisites

- Python 3.7+
- SQL Server
- ODBC Driver 17 for SQL Server
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/yfinance_data_engineer.git
cd yfinance_data_engineer
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up SQL Server:
   - Create a database named 'stock_db'
   - Run the SQL script in `sql/yfinance.sql` to create the necessary tables

5. Configure database connection:
   - Copy `config.py.example` to `config.py`
   - Update the server and database connection details

## Usage

Run the main script to collect stock data:
```bash
python src/main.py
```

Note: The script takes approximately 7-8 hours to run due to API rate limits and the large number of stocks being tracked.

## Database Schema

The system uses two main tables:

1. `Stock`: Stores comprehensive stock information
2. `ASE`: Stores American Stock Exchange specific data

See `sql/yfinance.sql` for complete schema details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Yahoo Finance API (yfinance)
- SQL Server
- Python community
