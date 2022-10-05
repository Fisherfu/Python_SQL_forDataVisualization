# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 13:00:35 2022

@author: fisherfu
"""

import os
import pandas as pd
import pyodbc
import numpy

# os.chdir("C:/Users/fisherfu/OneDrive - Synopsys, Inc/Desktop/TSMC Machines ResourcesAA/Raw_data")
#os.chdir("C:/Users/fisherfu/OneDrive - Synopsys, Inc/Desktop/TSMC Machines ResourcesAA/Raw_data/W39")
os.chdir("C:/Users/fisherfu/Downloads")



# insert csv raw data
# use pandas

# df = pd.read_csv("Raw_chamber_historyV3_test.csv")
#df = pd.read_csv("TSMC utilization report-0926.2022-Asset_server.csv")
df = pd.read_csv("TSMC utilization report-1004.2022_Asset_Server.csv")
# columns = df.head()

# df.fillna(method='ffill', inplace=True)

# df.isnull()
# df.notnull()
# df.replace([numpy.nan], df.none, inplace=True)

## 空值補''
df.fillna('', inplace=True)

# print(columns)
print(df.columns)

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)


##connect to database
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

server = 'AP34' 
database = 'TSMC_Machine_Util' 
username = 'PGP_admin' 
password = 'c3P@ssword' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


# drop present table
cursor.execute('''
              DROP TABLE [dbo].[Assets_Server1]
              ''')


# Create new Table
# =============================================================================
# notice: the name of columns should follow the original one in SQL, Asset_Server2
# =============================================================================
cursor.execute('''
		CREATE TABLE [dbo].[Assets_Server1](
                     	[CPU%] [nvarchar](255) NULL,
                     	[Mem%] [nvarchar](255) NULL,
                     	[N# Load-5m] [nvarchar](255) NULL,
                     	[AMR] [nvarchar](255) NULL,
                     	[Hostname] [nvarchar](255) NULL,
                     	[Model] [nvarchar](255) NULL,
                     	[Core] [nvarchar](255) NULL,
                     	[pCore] [nvarchar](255) NULL,
                     	[CPU] [nvarchar](255) NULL,
                     	[RAM(GB)] [nvarchar](255) NULL,
                     	[OS] [nvarchar](255) NULL,
                     	[Core Type] [nvarchar](255) NULL,
                     	[HDD] [nvarchar](255) NULL,
                     	[ Peak Mem/GB ] [nvarchar](255) NULL,
                     	[Type] [nvarchar](255) NULL,
                     	[Domain] [nvarchar](255) NULL,
                     	[Inside TSMC Plant] [nvarchar](255) NULL,
                     	[BU] [nvarchar](255) NULL,
                     	[Dedicated For] [nvarchar](255) NULL,
                     	[Cap Date] [nvarchar](255) NULL,
                     	[Warranty status (5yrs)] [nvarchar](255) NULL,
                     	[Asset owner] [nvarchar](255) NULL,
                     	[Remark] [nvarchar](255) NULL,
                     	[Share/Dedicate] [nvarchar](255) NULL,
                     	[Skip] [nvarchar](255) NULL,
                     	[Return Simulation] [nvarchar](255) NULL,
                     	[Return logistic] [nvarchar](255) NULL,
                     	[queue] [nvarchar](255) NULL,
                     	[PO] [nvarchar](255) NULL,
                     	[SN#] [nvarchar](255) NULL,
                     	[Life yr] [nvarchar](255) NULL,
                     	[If no data] [nvarchar](255) NULL
                    ) ON [PRIMARY]
                ''')          
            
# cnxn.commit()
# cursor.close()

####insert new data 
for index, row in df.iterrows():
    # print(row['CPU%'],row['Mem%'],row['N-Load-5m'])
    # print(row[0],row[1],row[2])
    # print(row['8/25/2022'],row['9/5/2022'])    
    
    cursor.execute("INSERT INTO Assets_Server1 ([CPU%], [Mem%],[N# Load-5m],[AMR],[Hostname],   \
                    [Model],[Core],[pCore],[CPU],[RAM(GB)],[OS],[Core Type],[HDD],[ Peak Mem/GB ],[Type],  \
                    [Domain],[Inside TSMC Plant],[BU],[Dedicated For],[Cap Date],[Warranty status (5yrs)],  \
                    [Asset owner],[Remark],[Share/Dedicate],[Skip],[Return Simulation],[Return logistic],  \
                    [queue],[PO],[SN#],[Life yr],[If no data] )  \
                    values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
        
                    row['CPU%'], row['Mem%'],row['N. Load-5m'],row['AMR'],row['Hostname'],row['Model'],row['Core'],
                    row['pCore'],row['CPU'],row['RAM (GB)'],row['OS'],row['Core Type'],row['HDD'],
                    row[' Peak Mem/GB '],row['Type'],
                    row['Domain'], row['Inside TSMC Plant'], row['BU'], row['Dedicated For'], row['Cap Date'],
                    row['Warranty status (5yrs)'],row['Asset owner'],row['Remark'],row['Share/Dedicate'],
                    row['Skip'], row['Return Simulation'], row['Return logistic'],row['queue'], row['PO'],
                    row['SN#'],row['Life yr'],row['If no data'])
                                 
cnxn.commit()
cursor.close()




#  cursor.execute("INSERT INTO History_all_test (Hostname_ch,rtn) values(?,?,?,?,?,?,?,?,?)",
#   row.date_rtn, row.rtn)


# =============================================================================
# # # for index, row in df.iterrows():
# # #     print(row.Hostname_ch, row.date_ch, row.chamber, row.Hostname_de, row.date_de, row.dedicate, row.Hostname_rtn, row.date_rtn, row.rtn)
# # #         # print(row['8/25/2022'],row['9/5/2022'])    
#     
# # #     cursor.execute("INSERT INTO History_all_test (Hostname_ch,date_ch,chamber,Hostname_de,date_de,dedicate,Hostname_rtn,date_rtn,rtn) values(?,?,?,?,?,?,?,?,?)",
# # #                    row.Hostname_ch, row.date_ch, row.chamber, row.Hostname_de, row.date_de, row.dedicate, row.Hostname_rtn, row.date_rtn, row.rtn)
# 
# =============================================================================




