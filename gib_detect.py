#!/usr/bin/python

import pickle
import gib_train

model_data = pickle.load(open('gib_model.pki', 'rb'))

while True:
    l = input(">>> input:")
    model_mat = model_data['mat']
    threshold = model_data['thresh']
    res = gib_train.avg_transition_prob(l, model_mat)
    if res > threshold:
        print("<<< [-] not Random")
    else:
        print("<<< [+] is Random")
    print()
