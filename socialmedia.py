
toxic_words = ["stupid", "boring", "lame"]
sentence = input("enter your string:")
is_toxic = lambda comment:[word in comment.lower() for word in toxic_words]
print(is_toxic(sentence))


def toxic(sen):
    a = [i in sen.lower() for i in toxic_words]
    print(a)
toxic(sentence)
import numpy as np
cm = [[20, 40], [50, 80]]
b = np.array(cm).flatten()
print(b)
splitted = lambda m:np.array([lm for lm in cm]).flatten()
print(splitted(cm))