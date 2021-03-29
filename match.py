#!/usr/bin/env python
#
# Created by Iain George

import re

# Puf of interest
puf = 'puf3'

# Load motifs to check
motifsFile = open('input_' + puf + '.txt')
matchList = motifsFile.read().split('\n')
motifsFile.close()

# Load UTRs to check against
utrFile = open('3utr.txt')
utrList = utrFile.read().split('>')
utrFile.close()

utrSequences = {}

# Parse out genes and sequences from UTR list
for line in utrList:
    line = line.split('\n')
    gene = re.sub('[|]+\w{0,5}', '', line[0])
    sequence = ''
    for j in range(1, len(line)):
        sequence += line[j]
    utrSequences[gene] = sequence

# Look for matches and output as separate files with position
for motif in matchList:
    output = open('results-' + puf + '-' + motif  + '.txt','w')
    results = ''

    for geneName in utrSequences.keys():
        if motif in utrSequences[geneName]:
            results += geneName + '\t' + motif + '\t' + str(utrSequences[geneName].index(motif))
            position = utrSequences[geneName].index(motif) + 1
            while (utrSequences[geneName])[position:].count(motif) >= 1:
                position = position + (utrSequences[geneName])[position:].index(motif) + 1
                results += ', ' + str(position - 1)
            results += '\n'
    output.write(results)