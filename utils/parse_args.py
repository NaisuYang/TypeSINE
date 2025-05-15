#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import argparse

def parse_args():
    """Parse command-line arguments for TypeSINE."""
    #parse = argparse.ArgumentParser(prog='TypeSINE',description='Example:\tRIPFinder -m 1 -t 8 -r reference.fa -b TE_loci.bed -f SRR123456.fq -o output_dir\n\n\t\tRIPFinder -m 2 -t 8 -r reference.fa -b TE_loci.bed -f SRR123456.fq -o output_dir\n\n\t\tRIPFinder -m 3 -d results_dir -o merged_results.tsv',  epilog="RIPFinder --- Finding RIP from short read sequence data", formatter_class=argparse.RawTextHelpFormatter)  
    parser = argparse.ArgumentParser(
        prog='TypeSINE',
        description='Example:\n'
                    '  TypeSINE -m 1 -t 8 -r reference.fa -b TE_loci.bed -f SRR123456.fq -o output_dir\n'
                    '  TypeSINE -m 2 -t 8 -r reference.fa -b TE_loci.bed -f SRR123456.fq -o output_dir\n'
                    '  TypeSINE -m 3 -d results_dir -o merged_results.tsv',
        epilog="TypeSINE --- Finding RIP from short read sequence data",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-m', '--mode', required=True, choices=["1", "2", "3", "4", "5"], default="1", help='1: Find reference RIP\n2: de novo RIP Finding\n3: All de novo RIP loci Refinding\n4: Merge results')
    parser.add_argument('-r', '--ref', metavar='', help='reference fasta file') 
    parser.add_argument('-b', '--bed', metavar='', help='A bed file of TE loci in the reference genome') 
    parser.add_argument('-f', '--fas', metavar='', help='short read sequence data FASTQ or FASTA') 
    parser.add_argument('-n', '--newloci', metavar='', help='new loci') 
    parser.add_argument('-o', '--output', type=str, metavar='', help='Path to output directory') 
    parser.add_argument('-d', '--dir', type=str, metavar='', help='Directory containing result files to merge')
    #parser.add_argument('-m', '--mergedfile', default=os.getcwd(), type=str, metavar='', help='Output merged results file') 
    parser.add_argument('-t', '--threads', default=1, type=int, metavar='', help='number of threads, default is 1, not recommended to exceed 16') 
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing result files') 
    # group = parse.add_mutually_exclusive_group()  # 1、在参数对象中添加互斥组
    # group.add_argument('-fa', '--fasta', metavar='', help='Input FASTA file') 
    # group.add_argument('-fq', '--fastq', metavar='', help='Input FASTQ file')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s beta-1.0')

    return parser.parse_args()