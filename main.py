# Using yahoo finance api
import yfinance as yf
from config import conn
from dictionary import StockDictionary, normalize_exchange
import datetime
from time import perf_counter
# THIS SCRIPT TAKES ABOUT 7 HOURS - 8 HOURS TO RUN


def get_info(ticker):
    stock = yf.Ticker(ticker)

    infoDict = {

        # current
        "Ticker": None,
        "Name": None,
        "DateTimePulled": datetime.datetime.now(),
        "Price": None,
        "Ask": None,
        "Bid": None,
        "DayLow": None,
        "DayHigh": None,
        "Volume": None,
        "MarketOpen": None,
        "MarketClose": None,

        # details
        "52WeekLow": None,
        "52WeekHigh": None,
        "50DayAvg": None,
        "200DayAvg": None,
        "AvgVolume": None,
        "10DayAvgVolume": None,

        # exchange - sometimes not found (null)
        "Exchange": None,

        # extra details - may not be found
        'Country': None,
        'Sector': None,
        'Industry': None,
        '52WeekChange': None,
        'LastDividendValue': None,
        'PayoutRatio': None,
        'ProfitMargins': None,

        # short details
        "FloatShares": None,
        "ShortShares": None,
        "SharesShortMonthAgo": None,

        # # extra extra details
        "Employees": None,
        "BookValue": None,
        # 'MorningStarRiskRating': None,
        'EarningsQuarterlyGrowth': None,
        'NetIncomeToCommon': None,
        'SharesOutstanding': None,
        "ShortRatio": None,
        'Market': None,
        'LongBusinessSummary': None
    }
 
    keys_info = {
    'Ticker': 'symbol',
    'Name': 'longName',
    'Price': 'regularMarketPrice',
    'Ask': 'ask',
    'Bid': 'bid',
    'DayLow': 'dayLow',
    'DayHigh': 'dayHigh',
    'Volume': 'regularMarketVolume',
    'MarketOpen': 'regularMarketOpen',
    'MarketClose': 'regularMarketPreviousClose',
    '52WeekLow': 'fiftyTwoWeekLow',
    '50DayAvg': 'fiftyTwoWeekHigh',
    '200DayAvg': 'twoHundredDayAverage',
    'AvgVolume': 'averageVolume',
    '10DayAvgVolume': 'averageDailyVolume10Day',
    'Exchange': 'exchange',
    'Country': 'country',
    'Sector': 'sector',
    'Industry': 'industry',
    'FiftyTwoWeekChange': '52WeekChange',
    'LastDividendValue': 'lastDividendValue',
    'PayoutRatio': 'payoutRatio',
    'ProfitMargins': 'profitMargins',
    'FloatShares': 'floatShares',
    'ShortShares': 'sharesShort',
    'SharesShortMonthAgo': 'sharesShortPreviousMonthDate',
    'Employees': 'fullTimeEmployees',
    'BookValue': 'bookValue',
    'EarningsQuarterlyGrowth': 'earningsQuarterlyGrowth',
    'NetIncomeToCommon': 'netIncomeToCommon',
    'SharesOutstanding': 'sharesOutstanding',
    'ShortRatio': 'shortRatio',
    'Market': 'market',
    'LongBusinessSummary': 'longBusinessSummary'
}
    for key, info_key in keys_info.items():
        if key == 'DateTimePulled':
            infoDict[key] = datetime.datetime.now()
        else:
            value = stock.info.get(info_key)
            if value is not None:
                infoDict[key] = value
            else:
                #print(f"Not able to retrieve '{key}' for '{ticker}'")
                infoDict[key] = None
    return infoDict


def add_stock(stockDict):
    cursor = conn.cursor()

    try:
        # Execute SQL Command
        cursor.execute(""" INSERT INTO Stock (Ticker, Exchange, Name, DateTimePulled_EST, Price, Ask, Bid, DayLow, DayHigh, Volume, MarketOpen, MarketClose, FiftyTwoWeekLow, FiftyTwoWeekHigh, FiftyDayAverage, FiftyTwoWeekChange, TwoHundredDayAverage, AverageVolume, TenDayAverageVolume, Country, Sector, Industry, LastDividendValue, PayoutRatio, ProfitMargins, FloatShares, ShortShares, ShortSharesMonthAgo, Employees, BookValue, EarningsQuarterlyGrowth, NetIncomeToCommon, SharesOutstanding, ShortRatio, Market, LongBusinessSummary)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                       , (stockDict['Ticker'], normalize_exchange(stockDict['Exchange']), stockDict['Name'], stockDict['DateTimePulled'], stockDict['Price'], stockDict['Ask'],
                          stockDict['Bid'], stockDict['DayLow'], stockDict['DayHigh'], stockDict['Volume'], stockDict['MarketOpen'],
                    stockDict['MarketClose'], stockDict['52WeekLow'], stockDict['52WeekHigh'], stockDict['50DayAvg'],
                    stockDict['52WeekChange'], stockDict['200DayAvg'], stockDict['AvgVolume'], stockDict['10DayAvgVolume'],
                    stockDict['Country'], stockDict['Sector'], stockDict['Industry'], stockDict['LastDividendValue'],
                    stockDict['PayoutRatio'], stockDict['ProfitMargins'], stockDict['FloatShares'], stockDict['ShortShares'],
                    stockDict['SharesShortMonthAgo'], stockDict['Employees'], stockDict['BookValue'], stockDict['EarningsQuarterlyGrowth'],
                    stockDict['NetIncomeToCommon'], stockDict['SharesOutstanding'], stockDict['ShortRatio'], stockDict['Market'], stockDict['LongBusinessSummary']))

        # Commit Changes to SQL Database
        conn.commit()
        print(f"Successfully added {stockDict['Ticker']} to database!")
    except Exception as e:
        # print(f"Failed to add '{stockDict['Ticker']}'")  # + {str(e)}?")
        # Roll back in case of error
        conn.rollback()

def add_to_sql(stockDict):
    try:
        add_stock(stockDict)
    except Exception as e:
        print(f"Failed to add {stockDict['Ticker']} to database! + {str(e)}")


def create_stock_objects(tickers):
    stockList = []
    for ticker in tickers:
        try:
            # t0 = perf_counter()
            stockDict = get_info(ticker)
            stockList.append(stockDict)
            # print(f"{ticker} was added to objects!")
            # t1 = perf_counter()
            # completion_time = t1 - t0
            # print("Completion time: ", completion_time)
            add_to_sql(stockDict)
        except Exception as e:
            print(f"{ticker} was not added to objects.")  # \n Exception: {str(e)}")
            pass
    if stockList:
        return stockList



if __name__ == "__main__":
    t0 = perf_counter()
    stockList = create_stock_objects(StockDictionary.STOCKS)
    t1 = perf_counter()
    completion_time = t1 - t0
    print("Completion time: ", t1 - t0)