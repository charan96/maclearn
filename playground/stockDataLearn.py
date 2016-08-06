import pandas as pd
import os, time, pickle
from datetime import datetime

gather = "Total Debt/Equity (mrq)"


def pickleDump(filename, dataObj):
	with open(filename, 'wb') as pick:
		pickle.dump(dataObj, pick)
	return filename


def pickleLoad(filename):
	with open(filename, 'rb') as pick:
		return pickle.load(filename)


def keyStats():
	path = 'intraQuarter'
	statsPath = path + '/_KeyStats'
	df = pd.DataFrame(columns=['Date', 'Unix', 'Ticker', 'DE Ratio'])

	stockList = [x[0] for x in os.walk(statsPath)]
	for eachDir in stockList[1:]:
		fileList = os.listdir(eachDir)
		ticker = eachDir.split("/")[2]
		if len(fileList) > 0:
			for file in fileList:
				dateStamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
				unixTime = time.mktime(dateStamp.timetuple())

				fullFilePath = eachDir + '/' + file
				source = open(fullFilePath, 'r').read()
				try:
					value = source.split(gather + ':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
					df = df.append({'Date': dateStamp, 'Unix': unixTime, 'Ticker': ticker, 'DE Ratio': value},
							   ignore_index=True)
				except IndexError as e:
					try:
						value = \
							source.split(gather + ':</td>' + "\n" + '<td class="yfnc_tabledata1">')[
								1].split(
								'</td>')[0]
						df = df.append(
							{'Date': dateStamp, 'Unix': unixTime, 'Ticker': ticker, 'DE Ratio': value},
							ignore_index=True)
					except Exception as ex:
						print(fullFilePath)
	return df


if os.path.isfile('dataframe.p'):
	df = pickle.load('dataframe.p')
else:
	df = keyStats()

save = gather.replace(' ', '').replace(')', '').replace('(', '').replace('/', '') + ('.csv')
print(save)
df.to_csv(save, index=False)
