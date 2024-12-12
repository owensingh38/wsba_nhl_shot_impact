import pandas as pd
import gspread


gc = gspread.oauth()

sh = gc.open("WSBA - NHL 5v5 Shooting Metrics Public v1.0")

pws = sh.worksheet('Skaters DB')
bws = sh.worksheet('Bios DB')
tws = sh.worksheet('Teams DB')

players = pd.DataFrame(pws.get_all_records())
bios = pd.DataFrame(bws.get_all_records())
teams = pd.DataFrame(tws.get_all_records())

players.to_csv("SkatersDB.csv",index=False)
bios.to_csv("BiosDB.csv",index=False)
teams.to_csv("TeamsDB.csv",index=False)