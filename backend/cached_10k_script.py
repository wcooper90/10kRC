from secedgar.filings import Filing, FilingType
import os
from tqdm import tqdm

f = open('tickers.txt', 'r')
tickers = []

for x in f:
    tickers.append(x)


for ticker in tqdm(tickers):
    ticker = ticker[:-1]
    try:
        file_dir = os.getcwd() + '/filings/'
        my_filings = Filing(cik_lookup=ticker, filing_type=FilingType.FILING_10K, count=1)
        my_filings.save(file_dir)
        print(ticker + " 10k downloaded")


    except OSError as err:
        print("OS error: {0}".format(err))
        print('Unable to download ' + ticker + ' 10k!')
