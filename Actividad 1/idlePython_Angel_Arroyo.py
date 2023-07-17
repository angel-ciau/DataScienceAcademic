import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv ("data.csv")

data.head()

data.plot(y = 'Income', x = 'Year', kind = 'line')
plt.show()
