#!/usr/bin/env python
#
# Created by Iain George

import re

# Puf of interest
puf = 'puf3'

# Load motifs to check
motifsFile = open('input' + puf + '.txt')
    matchList = motifsFile.read().split('\n')
motifsFile.close()

# Load UTRs to check against
utrFile = open('3utr.txt')
    utrList = utrFile.read().split('>')

utrFile.close()

utrSequences = {}

for line in utrList:
    line = line.split('\n')
    gene = re.sub('[|]+\w{0,5}', '', line[0])
    sequence = ''
    for j in range(1, len(line)):
        sequence += line[j]
    utrSequences[gene] = sequence

