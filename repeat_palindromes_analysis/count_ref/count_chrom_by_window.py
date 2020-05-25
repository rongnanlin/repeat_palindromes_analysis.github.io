#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
 
##导入模块，初始变量
import re
 
fasta_file = 'GCA_004355905.1_PgNI_genomic.fna'
stat_file = 'base.stat.txt'
window = 50       #在这里指定滑动窗口的碱基长度，例如这里设置 5000 个碱基为一统计滑窗区间
 
#读取基因组
genome_dict = {}
with open(fasta_file, 'r') as genome_fasta:
    for line in genome_fasta:
        line = line.strip()
        if line[0] == '>':
            seq = line.split('>')[1]
            genome_dict[seq] = ''
        else:
            genome_dict[seq] += line
 
genome_fasta.close()
 
#统计并输出（A、T、G、C、GC）
base_stat = open(stat_file, 'w')
print('seq_ID\tseq_start\tseq_end\tA\tT\tG\tC\tGC', file = base_stat)
for seq_ID,seq_seq in genome_dict.items():
    seq_length = len(seq_seq)
    seq_start = list(range(0, seq_length - window, window))
    seq_end = list(range(window, seq_length, window))
    if seq_end == []:
        seq_start.append(0)
        seq_end.append(seq_length)
    elif seq_end[-1] < seq_length:
        seq_start.append(seq_start[-1] + window)
        seq_end.append(seq_length)
    for i in range(0, len(seq_start)):
        split_seq = seq_seq[seq_start[i]:seq_end[i]]
        split_len = seq_end[i] - seq_start[i]
        print(f'{seq_ID}\t{seq_start[i] + 1}\t{seq_end[i]}', file = base_stat, end = '\t')
        print(str(round(100 * len(re.findall('[Aa]', split_seq)) / split_len, 2)), file = base_stat, end = '\t')
        print(str(round(100 * len(re.findall('[Tt]', split_seq)) / split_len, 2)), file = base_stat, end = '\t')
        print(str(round(100 * len(re.findall('[Gg]', split_seq)) / split_len, 2)), file = base_stat, end = '\t')
        print(str(round(100 * len(re.findall('[Cc]', split_seq)) / split_len, 2)), file = base_stat, end = '\t')
        print(str(round(100 * len(re.findall('[GCgc]', split_seq)) / split_len, 2)), file = base_stat)
 
base_stat.close()
