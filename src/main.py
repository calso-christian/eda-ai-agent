from load import load_data

db=load_data(r'data\march_detalized.xlsx',"performance","detalized")

print(db.run("SELECT * FROM detalized LIMIT 2;"))