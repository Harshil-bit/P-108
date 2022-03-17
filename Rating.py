import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv('P-108.csv')
avg_rating_list=df["Avg Rating"].to_list()
fig=ff.create_distplot([avg_rating_list],["Average Rating"],show_hist=False)
fig.show()
