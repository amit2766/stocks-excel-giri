import datetime
from datetime import date, timedelta
import numpy as np
from  common_stock_analysis import *
import pandas as pd
from nsepy import history


def generate_complete_csv(stock_symbol):
    print("Generating csv for : ", stock_symbol)
    STOCK_SYMBOL = stock_symbol
    start_eq = date.today() - timedelta(days=213)
    end_eq = date.today()
    dec_expiry_date = datetime.date(2020, 12, 31)
    jan_expiry_date = datetime.date(2021, 1, 28)
    feb_expiry_date = datetime.date(2021, 2, 25)
    mar_expiry_date = datetime.date(2021, 3, 25)
    apr_expiry_date = datetime.date(2021, 4, 29)
    may_expiry_date = datetime.date(2021, 5, 27)
    jun_expiry_date = datetime.date(2021, 6, 24)
    jul_expiry_date = datetime.date(2021, 7, 29)
    aug_expiry_date = datetime.date(2021, 8, 26)
    sep_expiry_date = datetime.date(2021, 9, 28)

    # start_future = date.today() - timedelta(days=60)
    # end_future = date.today()
    # future_expiry = datetime.date(2021, 7, 29)

    equities_df = history.get_history(STOCK_SYMBOL, start=start_eq, end=end_eq)
    equities_df['%Deliverble'] = equities_df['%Deliverble'] * 100

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)


    # pdf.to_csv("tata_motors_equities.csv")
    equities_df['Month'] = pd.to_datetime(equities_df.index).month
    equities_df['Blank'] = ""

    # pdf_future_jan = history.get_history(STOCK_SYMBOL, start=dec_expiry_date+timedelta(1), end=jan_expiry_date, futures=True, expiry_date=jan_expiry_date)
    pdf_future_jan_0 = history.get_history(STOCK_SYMBOL, start=dec_expiry_date+timedelta(1), end=jan_expiry_date, futures=True, expiry_date=jan_expiry_date)
    pdf_future_feb_0 = history.get_history(STOCK_SYMBOL, start=jan_expiry_date+timedelta(1), end=feb_expiry_date, futures=True, expiry_date=feb_expiry_date)
    pdf_future_mar_0 = history.get_history(STOCK_SYMBOL, start=feb_expiry_date+timedelta(1), end=mar_expiry_date, futures=True, expiry_date=mar_expiry_date)
    pdf_future_apr_0 = history.get_history(STOCK_SYMBOL, start=mar_expiry_date+timedelta(1), end=apr_expiry_date, futures=True, expiry_date=apr_expiry_date)
    pdf_future_may_0 = history.get_history(STOCK_SYMBOL, start=apr_expiry_date+timedelta(1), end=may_expiry_date, futures=True, expiry_date=may_expiry_date)
    pdf_future_jun_0 = history.get_history(STOCK_SYMBOL, start=may_expiry_date+timedelta(1), end=jun_expiry_date, futures=True, expiry_date=jun_expiry_date)
    pdf_future_jul_0 = history.get_history(STOCK_SYMBOL, start=jun_expiry_date+timedelta(1), end=jul_expiry_date, futures=True, expiry_date=jul_expiry_date)
    pdf_future_aug_0 = history.get_history(STOCK_SYMBOL, start=jul_expiry_date+timedelta(1), end=aug_expiry_date, futures=True, expiry_date=aug_expiry_date)
    pdf_future_feb_1 = history.get_history(STOCK_SYMBOL, start=dec_expiry_date+timedelta(1), end=jan_expiry_date, futures=True, expiry_date=feb_expiry_date)
    pdf_future_mar_1 = history.get_history(STOCK_SYMBOL, start=jan_expiry_date+timedelta(1), end=feb_expiry_date, futures=True, expiry_date=mar_expiry_date)
    pdf_future_apr_1 = history.get_history(STOCK_SYMBOL, start=feb_expiry_date+timedelta(1), end=mar_expiry_date, futures=True, expiry_date=apr_expiry_date)
    pdf_future_may_1 = history.get_history(STOCK_SYMBOL, start=mar_expiry_date+timedelta(1), end=apr_expiry_date, futures=True, expiry_date=may_expiry_date)
    pdf_future_jun_1 = history.get_history(STOCK_SYMBOL, start=apr_expiry_date+timedelta(1), end=may_expiry_date, futures=True, expiry_date=jun_expiry_date)
    pdf_future_jul_1 = history.get_history(STOCK_SYMBOL, start=may_expiry_date+timedelta(1), end=jun_expiry_date, futures=True, expiry_date=jul_expiry_date)
    pdf_future_aug_1 = history.get_history(STOCK_SYMBOL, start=jun_expiry_date+timedelta(1), end=jul_expiry_date, futures=True, expiry_date=aug_expiry_date)

    # pdf_future['%Deliverble'] = pdf_future['%Deliverble']*100

    # pdf_joined = pdf.join(pdf_future )


    # 'Date'
    # pdf_future_jan_1['Symbol']
    pdf_future_feb_1 = pdf_future_feb_1.rename(columns={"Expiry" : "Expiry _1", "Open" : "Open _1", "High" : "High _1", "Low" : "Low _1", "Close" : "Close _1", "Last" : "Last _1", "Settle Price" : "Settle Price _1", "Number of Contracts" : "Number of Contracts _1", "Turnover" : "Turnover _1", "Open Interest" : "Open Interest _1", "Change in OI" : "Change in OI _1", "Underlying" : "Underlying _1"})
    pdf_future_mar_1 = pdf_future_mar_1.rename(columns={"Expiry" : "Expiry _1", "Open" : "Open _1", "High" : "High _1", "Low" : "Low _1", "Close" : "Close _1", "Last" : "Last _1", "Settle Price" : "Settle Price _1", "Number of Contracts" : "Number of Contracts _1", "Turnover" : "Turnover _1", "Open Interest" : "Open Interest _1", "Change in OI" : "Change in OI _1", "Underlying" : "Underlying _1"})
    pdf_future_apr_1 = pdf_future_apr_1.rename(columns={"Expiry" : "Expiry _1", "Open" : "Open _1", "High" : "High _1", "Low" : "Low _1", "Close" : "Close _1", "Last" : "Last _1", "Settle Price" : "Settle Price _1", "Number of Contracts" : "Number of Contracts _1", "Turnover" : "Turnover _1", "Open Interest" : "Open Interest _1", "Change in OI" : "Change in OI _1", "Underlying" : "Underlying _1"})
    pdf_future_may_1 = pdf_future_may_1.rename(columns={"Expiry" : "Expiry _1", "Open" : "Open _1", "High" : "High _1", "Low" : "Low _1", "Close" : "Close _1", "Last" : "Last _1", "Settle Price" : "Settle Price _1", "Number of Contracts" : "Number of Contracts _1", "Turnover" : "Turnover _1", "Open Interest" : "Open Interest _1", "Change in OI" : "Change in OI _1", "Underlying" : "Underlying _1"})
    pdf_future_jun_1 = pdf_future_jun_1.rename(columns={"Expiry" : "Expiry _1", "Open" : "Open _1", "High" : "High _1", "Low" : "Low _1", "Close" : "Close _1", "Last" : "Last _1", "Settle Price" : "Settle Price _1", "Number of Contracts" : "Number of Contracts _1", "Turnover" : "Turnover _1", "Open Interest" : "Open Interest _1", "Change in OI" : "Change in OI _1", "Underlying" : "Underlying _1"})
    pdf_future_jul_1 = pdf_future_jul_1.rename(columns={"Expiry" : "Expiry _1", "Open" : "Open _1", "High" : "High _1", "Low" : "Low _1", "Close" : "Close _1", "Last" : "Last _1", "Settle Price" : "Settle Price _1", "Number of Contracts" : "Number of Contracts _1", "Turnover" : "Turnover _1", "Open Interest" : "Open Interest _1", "Change in OI" : "Change in OI _1", "Underlying" : "Underlying _1"})
    pdf_future_aug_1 = pdf_future_aug_1.rename(columns={"Expiry" : "Expiry _1", "Open" : "Open _1", "High" : "High _1", "Low" : "Low _1", "Close" : "Close _1", "Last" : "Last _1", "Settle Price" : "Settle Price _1", "Number of Contracts" : "Number of Contracts _1", "Turnover" : "Turnover _1", "Open Interest" : "Open Interest _1", "Change in OI" : "Change in OI _1", "Underlying" : "Underlying _1"})
    pdf_future_jan_0 = pdf_future_jan_0.rename(columns={"Expiry" : "Expiry _0", "Open" : "Open _0", "High" : "High _0", "Low" : "Low _0", "Close" : "Close _0", "Last" : "Last _0", "Settle Price" : "Settle Price _0", "Number of Contracts" : "Number of Contracts _0", "Turnover" : "Turnover _0", "Open Interest" : "Open Interest _0", "Change in OI" : "Change in OI _0", "Underlying" : "Underlying _0"})
    pdf_future_feb_0 = pdf_future_feb_0.rename(columns={"Expiry" : "Expiry _0", "Open" : "Open _0", "High" : "High _0", "Low" : "Low _0", "Close" : "Close _0", "Last" : "Last _0", "Settle Price" : "Settle Price _0", "Number of Contracts" : "Number of Contracts _0", "Turnover" : "Turnover _0", "Open Interest" : "Open Interest _0", "Change in OI" : "Change in OI _0", "Underlying" : "Underlying _0"})
    pdf_future_mar_0 = pdf_future_mar_0.rename(columns={"Expiry" : "Expiry _0", "Open" : "Open _0", "High" : "High _0", "Low" : "Low _0", "Close" : "Close _0", "Last" : "Last _0", "Settle Price" : "Settle Price _0", "Number of Contracts" : "Number of Contracts _0", "Turnover" : "Turnover _0", "Open Interest" : "Open Interest _0", "Change in OI" : "Change in OI _0", "Underlying" : "Underlying _0"})
    pdf_future_apr_0 = pdf_future_apr_0.rename(columns={"Expiry" : "Expiry _0", "Open" : "Open _0", "High" : "High _0", "Low" : "Low _0", "Close" : "Close _0", "Last" : "Last _0", "Settle Price" : "Settle Price _0", "Number of Contracts" : "Number of Contracts _0", "Turnover" : "Turnover _0", "Open Interest" : "Open Interest _0", "Change in OI" : "Change in OI _0", "Underlying" : "Underlying _0"})
    pdf_future_may_0 = pdf_future_may_0.rename(columns={"Expiry" : "Expiry _0", "Open" : "Open _0", "High" : "High _0", "Low" : "Low _0", "Close" : "Close _0", "Last" : "Last _0", "Settle Price" : "Settle Price _0", "Number of Contracts" : "Number of Contracts _0", "Turnover" : "Turnover _0", "Open Interest" : "Open Interest _0", "Change in OI" : "Change in OI _0", "Underlying" : "Underlying _0"})
    pdf_future_jun_0 = pdf_future_jun_0.rename(columns={"Expiry" : "Expiry _0", "Open" : "Open _0", "High" : "High _0", "Low" : "Low _0", "Close" : "Close _0", "Last" : "Last _0", "Settle Price" : "Settle Price _0", "Number of Contracts" : "Number of Contracts _0", "Turnover" : "Turnover _0", "Open Interest" : "Open Interest _0", "Change in OI" : "Change in OI _0", "Underlying" : "Underlying _0"})
    pdf_future_jul_0 = pdf_future_jul_0.rename(columns={"Expiry" : "Expiry _0", "Open" : "Open _0", "High" : "High _0", "Low" : "Low _0", "Close" : "Close _0", "Last" : "Last _0", "Settle Price" : "Settle Price _0", "Number of Contracts" : "Number of Contracts _0", "Turnover" : "Turnover _0", "Open Interest" : "Open Interest _0", "Change in OI" : "Change in OI _0", "Underlying" : "Underlying _0"})
    pdf_future_aug_0 = pdf_future_aug_0.rename(columns={"Expiry" : "Expiry _0", "Open" : "Open _0", "High" : "High _0", "Low" : "Low _0", "Close" : "Close _0", "Last" : "Last _0", "Settle Price" : "Settle Price _0", "Number of Contracts" : "Number of Contracts _0", "Turnover" : "Turnover _0", "Open Interest" : "Open Interest _0", "Change in OI" : "Change in OI _0", "Underlying" : "Underlying _0"})

    # Use first time fno data to create new columns
    equities_df['Expiry _0'] = pdf_future_jan_0['Expiry _0']
    equities_df['Open _0'] = pdf_future_jan_0['Open _0']
    equities_df['High _0'] = pdf_future_jan_0['High _0']
    equities_df['Low _0'] = pdf_future_jan_0['Low _0']
    equities_df['Close _0'] = pdf_future_jan_0['Close _0']
    equities_df['Last _0'] = pdf_future_jan_0['Last _0']
    equities_df['Settle Price _0'] = pdf_future_jan_0['Settle Price _0']
    equities_df['Number of Contracts _0'] = pdf_future_jan_0['Number of Contracts _0']
    equities_df['Turnover _0'] = pdf_future_jan_0['Turnover _0']
    equities_df['Open Interest _0'] = pdf_future_jan_0['Open Interest _0']
    equities_df['Change in OI _0'] = pdf_future_jan_0['Change in OI _0']
    equities_df['Underlying _0'] = pdf_future_jan_0['Underlying _0']
    equities_df['Blank3'] = ''

    equities_df['Expiry _1'] = pdf_future_feb_1['Expiry _1']
    equities_df['Open _1'] = pdf_future_feb_1['Open _1']
    equities_df['High _1'] = pdf_future_feb_1['High _1']
    equities_df['Low _1'] = pdf_future_feb_1['Low _1']
    equities_df['Close _1'] = pdf_future_feb_1['Close _1']
    equities_df['Last _1'] = pdf_future_feb_1['Last _1']
    equities_df['Settle Price _1'] = pdf_future_feb_1['Settle Price _1']
    equities_df['Number of Contracts _1'] = pdf_future_feb_1['Number of Contracts _1']
    equities_df['Turnover _1'] = pdf_future_feb_1['Turnover _1']
    equities_df['Open Interest _1'] = pdf_future_feb_1['Open Interest _1']
    equities_df['Change in OI _1'] = pdf_future_feb_1['Change in OI _1']
    equities_df['Underlying _1'] = pdf_future_feb_1['Underlying _1']



    # Merge all futures properly (it will simply append data to existing df)

    equities_df.update(pdf_future_mar_1)
    equities_df.update(pdf_future_apr_1)
    equities_df.update(pdf_future_may_1)
    equities_df.update(pdf_future_jun_1)
    equities_df.update(pdf_future_jul_1)
    equities_df.update(pdf_future_aug_1)
    equities_df.update(pdf_future_feb_0)
    equities_df.update(pdf_future_mar_0)
    equities_df.update(pdf_future_apr_0)
    equities_df.update(pdf_future_may_0)
    equities_df.update(pdf_future_jun_0)
    equities_df.update(pdf_future_jul_0)
    equities_df.update(pdf_future_aug_0)


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


    equities_df.to_csv(PATH + STOCK_SYMBOL + ".csv")
