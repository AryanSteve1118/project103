import pandas as pd
import plotly.express as px

co=pd.read_csv("data.csv")
c19=px.scatter(co,x="date",y="cases",color="country")
c19.show()