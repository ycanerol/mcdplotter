#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read and plot mcd files using neuroshare
"""

import numpy as np
import matplotlib.pyplot as plt

import neuroshare as ns

file = ('/media/ycan/Erol1/20180712_YE_60MEA_Marmoset_eye2_21/1_fff_'
        'gauss1blink.mcd')
file = '/media/ycan/Erol1/20180802_YE_252MEA_Marmoset_eye1_421/1_fff_gauss1blink.mcd'
print(file)

fd = ns.File(file)
labels = []
analog = []
for entity in fd.list_entities():
#    print(entity.label, entity.entity_type)
    labelsplit = entity.label.split()
    labels.append(labelsplit[3])
    analog.append(labelsplit[0] == 'anlg0001')
analog = np.array(analog)

if fd.entity_count == 63:
    x, y = 8, 8
    corners = [0, 6, 54, 60]
elif fd.entity_count == 256:
    x, y = 16, 16
    corners = [0, 14, 238, 252]
# %%
# TODO: Ordering needs to be checked and fixed, 252 is wrong
sortedarg = np.argsort(labels)
analog = analog[sortedarg]
tres = fd.time_stamp_resolution
tstart = 10  # Time in seconds to start plotting
tspan = 1  # Time after tstart to plot (in seconds)
indstart = int(np.round(tstart/tres))
indspan = int(np.round(tspan/tres))

data = np.zeros((fd.entity_count, indspan))

for i, entitity in enumerate(fd.list_entities()):
    data[i, :] = entitity.get_data(indstart, indspan)[0]

data = data[sortedarg, :]

analogsig = data[analog, :]
filtsig = data[~analog, :]

filtsig = np.insert(filtsig, corners,  np.nan*indspan, axis=0)

# %%
fig, axes = plt.subplots(x, y, sharex=True, sharey=True)

for i in range(x):
    for j in range(y):
        ax = axes[i, j]
        for key in ax.spines.keys():
            ax.spines[key].set_visible(False)
        ax.set_axis_off()
        ax.plot(filtsig[i*x+j, :])

plt.show()
# %%
for i in range(analogsig.shape[0]):
    ax = plt.subplot(2, 2, i+1)
    ax.plot(analogsig[i, :])
plt.show()
