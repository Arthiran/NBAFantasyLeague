# import pandas library as pd
import pandas as pd
  
df = pd.read_csv('UnrankedPlayers.csv')
rslt_df = df.sort_values(by = 'Total', ascending=False)
rslt_df.to_csv('RankedPlayers.csv')
