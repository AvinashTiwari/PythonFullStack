from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

start_date = '2010-01-01'
end_date = '2016-12-31'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = data.DataReader('dell', 'yahoo', start_date, end_date)
outfile=open("c:/temp/dell.txt","w")
outfile.write(str(panel_data))
outfile.close()