import csv 
import pandas as pd 
import plotly.graph_objects as go 

df = pd.read_csv("st.csv")

st_df = df.loc[df["student_id"] == "TRL_zny" ]

print(st_df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Scatter(
            x = ["level 1", "level 2", "level 3" ,"level 4"],
            y = st_df.groupby("level")["attempt"].mean(),
            
))
fig.show()