# This reads the CSV one by one and updates all records from last recorded date to current date
import datetime
from common_stock_analysis import *
import numpy as np
import pandas
from nsepy import history

# Assumption: It is being executed at least once per every month
# Take each stock
# Get last date of that stock, get today's date
#
CURRENT_MONTH_EXPIRY = datetime.date(2021, 8, 26)
NEXT_MONTH_EXPIRY = datetime.date(2021, 9, 30)


def get_equity_data(stock, start_date, end_date):
    equities_df = history.get_history(stock, start=start_date, end=end_date)
    equities_df['%Deliverble'] = equities_df['%Deliverble'] * 100
    equities_df['Month'] = pandas.to_datetime(equities_df.index).month
    equities_df['Blank'] = ""


    return equities_df


def update_data_types_for_eq(equities_df):
    equities_df.index = pandas.to_datetime(equities_df.index)

    # equities_df['Number of Contracts _0'] = equities_df['Number of Contracts _0'].astype(float)
    # equities_df['Open Interest _0'] = equities_df['Open Interest _0'].astype(float)
    # equities_df['Change in OI _0'] = equities_df['Change in OI _0'].astype(float)
    # equities_df['Number of Contracts _1'] = equities_df['Number of Contracts _1'].astype(float)
    # equities_df['Open Interest _1'] = equities_df['Open Interest _1'].astype(float)
    # equities_df['Change in OI _1'] = equities_df['Change in OI _1'].astype(float)
    # equities_df['CumulativeOI'] = equities_df['CumulativeOI'].astype(float)
    # equities_df['Longs'] = equities_df['Longs'].astype(float)
    # equities_df['Shorts'] = equities_df['Shorts'].astype(float)

    return equities_df

def update_data_types_for(df):
    # df['Blank'] = df['Blank'].astype(str)
    # df['Blank3'] = df['Blank3'].astype(str)
    # df['BLANK4'] = df['BLANK4'].astype(str)
    # df['BLANK5'] = df['BLANK5'].astype(str)
    # df['BLANK6'] = df['BLANK6'].astype(str)
    return df


def update_files(stock_symbol, file_path):
    df = pandas.read_csv(file_path, index_col='Date')
    last_update_date = pandas.to_datetime(df.index[-1]).date()
    today_date = datetime.date.today()
    equities_df = get_equity_data(stock_symbol, last_update_date + datetime.timedelta(1), today_date)
    current_expiry_data = history.get_history(stock_symbol, start=last_update_date + datetime.timedelta(1),
                                              end=today_date,
                                              futures=True, expiry_date=CURRENT_MONTH_EXPIRY)
    next_expiry_data = history.get_history(stock_symbol, start=last_update_date + datetime.timedelta(1), end=today_date,
                                           futures=True, expiry_date=NEXT_MONTH_EXPIRY)

    current_expiry_data_0 = current_expiry_data.rename(
        columns={"Expiry": "Expiry _0", "Open": "Open _0", "High": "High _0", "Low": "Low _0", "Close": "Close _0",
                 "Last": "Last _0", "Settle Price": "Settle Price _0", "Number of Contracts": "Number of Contracts _0",
                 "Turnover": "Turnover _0", "Open Interest": "Open Interest _0", "Change in OI": "Change in OI _0",
                 "Underlying": "Underlying _0"})

    next_expiry_data_1 = next_expiry_data.rename(
        columns={"Expiry": "Expiry _1", "Open": "Open _1", "High": "High _1", "Low": "Low _1", "Close": "Close _1",
                 "Last": "Last _1", "Settle Price": "Settle Price _1", "Number of Contracts": "Number of Contracts _1",
                 "Turnover": "Turnover _1", "Open Interest": "Open Interest _1", "Change in OI": "Change in OI _1",
                 "Underlying": "Underlying _1"})

    # Creating new columns in equities df
    equities_df['Expiry _0'] = current_expiry_data_0['Expiry _0']
    equities_df['Open _0'] = current_expiry_data_0['Open _0']
    equities_df['High _0'] = current_expiry_data_0['High _0']
    equities_df['Low _0'] = current_expiry_data_0['Low _0']
    equities_df['Close _0'] = current_expiry_data_0['Close _0']
    equities_df['Last _0'] = current_expiry_data_0['Last _0']
    equities_df['Settle Price _0'] = current_expiry_data_0['Settle Price _0']
    equities_df['Number of Contracts _0'] = current_expiry_data_0['Number of Contracts _0']
    equities_df['Turnover _0'] = current_expiry_data_0['Turnover _0']
    equities_df['Open Interest _0'] = current_expiry_data_0['Open Interest _0']
    equities_df['Change in OI _0'] = current_expiry_data_0['Change in OI _0']
    equities_df['Underlying _0'] = current_expiry_data_0['Underlying _0']
    equities_df['Blank3'] = ''

    equities_df['Expiry _1'] = next_expiry_data_1['Expiry _1']
    equities_df['Open _1'] = next_expiry_data_1['Open _1']
    equities_df['High _1'] = next_expiry_data_1['High _1']
    equities_df['Low _1'] = next_expiry_data_1['Low _1']
    equities_df['Close _1'] = next_expiry_data_1['Close _1']
    equities_df['Last _1'] = next_expiry_data_1['Last _1']
    equities_df['Settle Price _1'] = next_expiry_data_1['Settle Price _1']
    equities_df['Number of Contracts _1'] = next_expiry_data_1['Number of Contracts _1']
    equities_df['Turnover _1'] = next_expiry_data_1['Turnover _1']
    equities_df['Open Interest _1'] = next_expiry_data_1['Open Interest _1']
    equities_df['Change in OI _1'] = next_expiry_data_1['Change in OI _1']
    equities_df['Underlying _1'] = next_expiry_data_1['Underlying _1']

    # Merge Here
    # Update existng df with new data
    df.index = pandas.to_datetime(df.index)

    equities_df = update_data_types_for_eq(equities_df)
    df = update_data_types_for(df)
    equities_df = pandas.concat([df,equities_df],join="outer")


    # Start other calculations


    equities_df[CLOSINGPRICE] = equities_df['Close']
    equities_df[DEL_VALUE] = equities_df[TURNOVER]/HUNDRED_CRORE
    equities_df[DAD5] = equities_df[TURNOVER].rolling(window=5).mean()/HUNDRED_CRORE
    equities_df[COI] = equities_df['Open Interest _0'] + equities_df['Open Interest _1']
    equities_df[CHANGE_COI] = equities_df['CumulativeOI'].diff().fillna(equities_df['CumulativeOI'])
    equities_df['BLANK4'] = ''


    equities_df[PERCENTAGE_PRICE] = (((equities_df[CLOSINGPRICE] - equities_df[CLOSINGPRICE].shift(periods=1, fill_value=0))/equities_df[CLOSINGPRICE])*100).astype(float).round(2)
    equities_df[PERCENTAGE_DELIVERY] = ((equities_df[DEL_VALUE]/equities_df[DAD5])*100).round(2)
    equities_df[PERCENTAGE_OI] = (((equities_df[COI] - equities_df[COI].shift(periods=1, fill_value=0))/equities_df[COI])*100).astype(float).round(2)
    equities_df['BLANK5'] = ''

    equities_df[LONG] = np.where(((equities_df[PERCENTAGE_PRICE] > 0) & (equities_df[PERCENTAGE_OI] > 0)) |
                                 ((equities_df[PERCENTAGE_PRICE] <= 0) & (equities_df[PERCENTAGE_OI] < 0)), equities_df[CHANGE_COI],None )
    equities_df[SHORT] = np.where(((equities_df[PERCENTAGE_PRICE] <= 0) & (equities_df[PERCENTAGE_OI] >= 0)) |
                                  ((equities_df[PERCENTAGE_PRICE] > 0 )& (equities_df[PERCENTAGE_OI] < 0)), equities_df[CHANGE_COI],None )

    equities_df[VERDICT] = np.where(equities_df[LONG] > 0 , LONG_BUILDUP,
                                    np.where(equities_df[LONG] < 0 , SHORT_COVERING,
                                             np.where(equities_df[SHORT] > 0 , SHORT_BUILDUP ,
                                                      np.where(equities_df[SHORT] <0 , LONG_LIQUIDATION, 'NAN'))))
    equities_df['BLANK6'] =''

    equities_df[VWAP+'_'] = equities_df[VWAP]
    equities_df[HIGH+'_'] = equities_df[HIGH]
    equities_df[LOW+'_'] = equities_df[LOW]




    equities_df.to_csv(file_path + "_new.csv", mode='w+')

