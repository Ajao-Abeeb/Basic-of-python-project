from wordClouds import wordClouds
import matplotlib.pyplot as plt

with open('clcoding.txt' , 'r') as f:
    text = f.read()
wordcloud = wordClouds().generate(text)
plt.imshow(wordClouds, interpolation='bilinear')
plt.axis("off")
plt.show()