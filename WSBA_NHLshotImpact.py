import pandas as pd
import gspread
import csv
import datetime
import os
import NST_Scrape

seasons=['20242025']
dfs = []
bio = []
tdfs = []

print("Starting scrape of all NHL seasons via Natural Stat Trick...")

for i in range(0,len(seasons)):
    dfs.append(NST_Scrape.NSTSkaterScrape(seasons[i]))
    bio.append(NST_Scrape.NSTBioScrape(seasons[i]))
    tdfs.append(NST_Scrape.NSTTeamScrape(seasons[i]))

skaters = pd.concat(dfs)
bios = pd.concat(bio)
teams = pd.concat(tdfs)

try:
    os.mkdir("Export")
except FileExistsError:
    ""

skaters.to_csv("Export/SkaterExport.csv",index=False)
bios.to_csv("Export/BiosExport.csv",index=False)
teams.to_csv("Export/TeamsExport.csv",index=False)

gc = gspread.oauth()

sh = gc.open("WSBA - NHL 5v5 Shooting Metrics Public v1.0")
sh.values_update(
    "Live Skaters",
    params={'valueInputOption': 'USER_ENTERED'},
    body={'values': list(csv.reader(open('SkaterExport.csv')))}
)
sh.values_update(
    "Live Bios",
    params={'valueInputOption': 'USER_ENTERED'},
    body={'values': list(csv.reader(open('BiosExport.csv')))}
)
sh.values_update(
    "Live Teams",
    params={'valueInputOption': 'USER_ENTERED'},
    body={'values': list(csv.reader(open('TeamsExport.csv')))}
)

date = datetime.datetime.now()
worksheet = sh.worksheet("Update Log")
log = worksheet.get_all_values()
log.append(["",str(date),"","Data Update",""])

sh.values_update(
    "Update Log",
    params={'valueInputOption': 'USER_ENTERED'},
    body = {'values':log}
)

print("All data has been exported to the root directory and uploaded to the Viz sheet.")