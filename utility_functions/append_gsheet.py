import gspread_dataframe as gd

# Connecting with `gspread` here

ws = gc.open("SheetName").worksheet("xyz")
existing = gd.get_as_dataframe(ws)
updated = existing.append(your_new_data)
gd.set_with_dataframe(ws, updated)