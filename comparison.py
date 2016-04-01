#!/usr/bin/env python

# ------------------------------------------------------------------------
# Imports

import sys
import matplotlib.pyplot as plt
from pygeo.segyread import SEGYFile
from pygeo.analysis import wiggle

# ------------------------------------------------------------------------
# Parameters

sfOpts = {
    'endian': 'Big',
}


nsrc = 201
nrec = 201

wiggleOpts = {
    'skipt':    5,
    'lwidth':   0.5,
    'color':    'black',
}

newColor = 'red'

# ------------------------------------------------------------------------
# Code

infileA = sys.argv[1]
infileB = sys.argv[2]
sg = int(sys.argv[3])

sfA = SEGYFile(infileA, **sfOpts)
sfB = SEGYFile(infileB, **sfOpts)

tracesA = sfA[sg*nrec:(sg+1)*nrec]
tracesB = sfB[sg*nrec:(sg+1)*nrec]

ntr = sfA.ntr

assert sfB.ntr == sfA.ntr
assert ntr == nsrc*nrec

ns = sfA.ns
dt = sfA.bhead['hdt'] / 1e3

wiggleOpts.update({
    'sampr':    dt,
})

# --------
# Plotting

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

wiggle(tracesA, **wiggleOpts)

wiggleOpts['color'] = newColor
wiggle(tracesB, **wiggleOpts)

plt.xlabel('Channel No.')
plt.ylabel('Time (ms)')

plt.axis((-2, nrec+1, ns*dt, 0.))

plt.show()
