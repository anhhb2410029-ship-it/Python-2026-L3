import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('scores.csv')

plt.scatter(df.index, df['math'], label='math')
plt.scatter(df.index, df['python'], label='python')
plt.scatter(df.index, df['database'], label='db')
plt.legend()
plt.savefig('scattered.png')
plt.clf()

df.hist(column=['math', 'python', 'database'], layout=(1, 3))
plt.savefig('histo.png')
plt.clf()

df.boxplot(column=['math', 'python', 'database'])
plt.savefig('box.png')
plt.clf()