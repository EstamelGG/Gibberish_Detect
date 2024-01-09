#!/usr/bin/python

import pickle
import gib_train

model_data = pickle.load(open('gib_model.pki', 'rb'))
model_mat = model_data['mat']
threshold = model_data['thresh']
print("Threshold: %s" % threshold)

while True:
    l = input(">>> input:")
    res = gib_train.avg_transition_prob(l, model_mat)
    if res > threshold:
        print("<<< [-] not Random(%s)" % res)
    else:
        print("<<< [+] is Random(%s)" % res)
    print()
