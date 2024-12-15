import pandas as pd
import gspread

res = input("What action would you like to perform? Press R to retrieve the DB or press U to update it...")
res.lower()

if res.lower() != 'r':
    if res.lower() != 'u': 
        print("Invalid Response.")

if res.lower() == 'r' or 'u':
    if res.lower() == "u":
        print("Upload not implemented yet!!!")

    print("Retreiving Database...")

    gc = gspread.oauth()

    sh = gc.open("WSBA - NHL 5v5 Shooting Metrics Public v1.0")

    pws = sh.worksheet('Skaters DB')
    bws = sh.worksheet('Bios DB')
    tws = sh.worksheet('Teams DB')

    players = pd.DataFrame(pws.get_all_records())
    bios = pd.DataFrame(bws.get_all_records())
    teams = pd.DataFrame(tws.get_all_records())

    players.to_csv("C:\\Users\\owenb\\OneDrive\\Desktop\\Owen\\Python Projects\\Hockey Analytics\\WSBA_NHL_Shot\\wsba_nhl_shot_impact\\Database\\SkatersDB.csv",index=False)
    bios.to_csv("C:\\Users\\owenb\\OneDrive\\Desktop\\Owen\\Python Projects\\Hockey Analytics\\WSBA_NHL_Shot\\wsba_nhl_shot_impact\\Database\\BiosDB.csv",index=False)
    teams.to_csv("C:\\Users\\owenb\\OneDrive\\Desktop\\Owen\\Python Projects\\Hockey Analytics\\WSBA_NHL_Shot\\wsba_nhl_shot_impact\\Database\\TeamsDB.csv",index=False)

    