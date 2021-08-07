import pandas as pd

command=pd.read_excel("Files//Command.xlsx")
screenshot_col=command.get('screenshot')
screenshot=list(screenshot_col)
print(screenshot) 