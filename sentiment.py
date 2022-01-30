import csv
from pysentimiento import create_analyzer
import pandas as pd

analyzer = create_analyzer(task="sentiment", lang="en")
import csv
with open('reviews.csv','r') as csvinput:
    with open('output1.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)

        for row in csv.reader(csvinput):
            if row[0] == "date":
                writer.writerow(row+["Sentiment"])
            else:
                x= analyzer.predict([row[1]])
                print(x)
                writer.writerow(row)
            

# csv_input = pd.read_csv('reviews.csv')
# csv_input['Sentiment'] = analyzer.predict(str(csv_input['reviews'])).output
# csv_input.to_csv('output.csv', index=False)

# print("hello")
# analyzer = create_analyzer(task="sentiment", lang="en")
# x= analyzer.predict("Gameplay loop is sub par. New upgrades, items, and frames, feel disappointing after they're obtained.")
# print(x.output)
