import calmap 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

all_days = pd.date_range('1/01/2019', periods=730, freq='D')
events = pd.Series(np.random.rand(len(all_days))*20, index=all_days)
# print(events)
calmap.yearplot(events, year=2019)
plt.show()


calmap.calendarplot(events, daylabels='MTWTFSS', cmap='Blues', \
                    fillcolor='grey', linewidth=0, 
                    fig_kws=dict(figsize=(8, 4)))
plt.show()