#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import time
import subprocess
from utils import *


# Methods

# Methods
# def check_bed_add_index(te_bed_file,outputdir):
#     name_split = os.path.splitext(os.path.basename(te_bed_file))
#     bed_add_index = os.path.join(outputdir,name_split[0] + '.bed')
#     #print(bed_add_index)
#     cmd = f'wc -l < {te_bed_file} '
#     p = runcmd(cmd).stdout.decode("utf-8")
#     print(f"Total number of loci in {te_bed_file}: {p}",end="")
#     if not os.path.exists(bed_add_index):
#         cmd = f"""sort -k1,1 -k2,2n {te_bed_file} | bedtools merge -s -c 4,5,6 -o distinct,distinct,distinct -i - | awk -F'\\t' -v OFS='\\t' '{{ $5 = NR;$4 = $1":"$2"-"$3"("$6")"; print }}' > {bed_add_index}"""
#         runcmd(cmd)
#     cmd = f'wc -l < {bed_add_index} '
#     p = runcmd(cmd).stdout.decode("utf-8")
#     print(f"The number of loci after merging: {p}",end="")
#     return bed_add_index

# def bedtools_getfasta(fi,bed,fo):
#     cmd = f"bedtools getfasta -s -fi {fi} -bed {bed} -fo {fo}"
#     runcmd(cmd)

# def get_upstream_fa(ref,te_bed_file,outputdir):
#     chr_length = os.path.join(outputdir, f"{ref}.chrinfo") 
#     name_split = os.path.splitext(os.path.basename(te_bed_file))
#     upstream_bed = os.path.join(outputdir,name_split[0] + '.ups' + name_split[1])
#     upstream_fa = os.path.join(outputdir,name_split[0] + '.ups.fa')
#     #print(upstream_bed)
#     if not os.path.exists(upstream_bed):
#         cmd = f"""bedtools flank -l 30 -r 0 -s -i {te_bed_file} -g {chr_length} | awk -F'\\t' -v OFS='\\t' '$3 - $2 >= 30 || $2 - $3 >= 30 {{ $4 = $1":"$2"-"$3"("$6")"; print }}' > {upstream_bed}"""
#         runcmd(cmd)
#     if not os.path.exists(upstream_fa):
#         bedtools_getfasta(ref,upstream_bed,upstream_fa)
#     return [upstream_bed, upstream_fa]

# def get_seed_fa(ref,te_bed_file,outputdir):
#     chr_length = os.path.join(outputdir, f"{ref}.chrinfo") 
#     name_split = os.path.splitext(os.path.basename(te_bed_file))
#     upstream_bed = os.path.join(outputdir,name_split[0] + '.ups' + name_split[1])
#     seed_bed = os.path.join(outputdir,name_split[0] + '.seed' + name_split[1])
#     seed_fa = os.path.join(outputdir,name_split[0] + '.seed.full.fa')
#     seed_rmdup_fa = os.path.join(outputdir,name_split[0] + '.seed.fa')
#     if not os.path.exists(seed_bed):
#         cmd = f"""bedtools flank -l 0 -r 30 -s -i {upstream_bed} -g {chr_length} | awk -F'\\t' -v OFS='\\t' '$3 - $2 >= 30 || $2 - $3 >= 30 {{ $4 = $1":"$2"-"$3"("$6")"; print }}' > {seed_bed}"""
#         runcmd(cmd)
#     if not os.path.exists(seed_fa):
#         bedtools_getfasta(ref,seed_bed,seed_fa)
#     if not os.path.exists(seed_rmdup_fa):
#         cmd = f"""grep -v '>' {seed_fa} | sort | uniq -c | sort -n -r | awk '$1 > 100 {{print ">seed"++i; print $2}}' > {seed_rmdup_fa}"""
#         runcmd(cmd)
#     return seed_fa

# def get_downstream_fa(ref,te_bed_file,outputdir):
#     chr_length = os.path.join(outputdir, f"{ref}.chrinfo") 
#     name_split = os.path.splitext(os.path.basename(te_bed_file))
#     downstream_bed = os.path.join(outputdir,name_split[0] + '.dns' + name_split[1])
#     downstream_fa = os.path.join(outputdir,name_split[0] + '.dns.fa')
#     #print(downstream_bed)
#     if not os.path.exists(downstream_bed):
#         cmd = f"""bedtools flank -l 0 -r 100 -s -i {te_bed_file} -g {chr_length} | awk -F'\\t' -v OFS='\\t' '$3 - $2 >= 100 || $2 - $3 >= 100 {{ $4 = $1":"$2"-"$3"("$6")"; print }}' > {downstream_bed}"""
#         runcmd(cmd)
#     if not os.path.exists(downstream_fa):
#         bedtools_getfasta(ref,downstream_bed,downstream_fa)
#     return [downstream_bed, downstream_fa]

# def get_joined_fa(ref,te_bed_file,outputdir):
#     chr_length = os.path.join(outputdir, f"{ref}.chrinfo") 
#     name_split = os.path.splitext(os.path.basename(te_bed_file))
#     upstream_bed = os.path.join(outputdir,name_split[0] + '.ups' + name_split[1])
#     joined_bed = os.path.join(outputdir,name_split[0] + '.joined' + name_split[1])
#     joined_fa = os.path.join(outputdir,name_split[0] + '.joined.fa')
#     #print(joined_bed)
#     if not os.path.exists(joined_bed):
#         cmd = f"""bedtools slop -l 0 -r 30 -s -i {upstream_bed} -g {chr_length} | awk -F'\\t' -v OFS='\\t' '$3 - $2 >= 60 || $2 - $3 >= 60 {{ $4 = $1":"$2"-"$3"("$6")"; print }}' > {joined_bed}"""
#         runcmd(cmd)
#     if not os.path.exists(joined_fa):
#         bedtools_getfasta(ref,joined_bed,joined_fa)
#     return [joined_bed, joined_fa]

# def bwa_index_cmd(fi):
#     finame = os.path.basename(fi)
#     fi_path =os.path.dirname(fi)
#     index_extent = ['.0123', '.amb', '.ann', '.bwt.2bit.64', '.pac']  # 替换成实际的索引文件名
#     index_file = [os.path.join(fi_path,finame + i) for i in index_extent]
#     index_exists = all(os.path.exists(file) for file in index_file)
#     if  not index_exists:
#         cmd = f"bwa-mem2 index {fi} > /dev/null 2>&1"
#         return cmd

def preprocess(mode,ref,te_bed_file,output):
    
    outputdir = os.path.join(output, "index")
    perfix = os.path.splitext(os.path.basename(te_bed_file))[0]

    #需要初始化的命令

    #1. 格式化转座子bed文件，安装染色体序号排序sort -k1,1 -k2,2n，
    #   将坐标格式化成nzw_ctg1:61148-61512(+)，
    #   并在第五列依次生成索引。
    te_bed_index_file = os.path.join(outputdir,perfix + '.index')
    te_bed_index_file_cmd = f"""sort -k1,1 -k2,2n {te_bed_file} | bedtools merge -s -c 4,5,6 -o distinct,distinct,distinct -i - | awk -F'\\t' -v OFS='\\t' '{{ $5 = NR;$7 = $1":"$2"-"$3"("$6")"; print }}' > {te_bed_index_file}"""

    #2. 创建参考基因组序列长度信息
    ref_chrinfo_file = os.path.join(outputdir, f"{os.path.basename(ref)}.chrinfo") 
    ref_chrinfo_file_cmd = f"seqkit fx2tab -l -n -i {ref} > {ref_chrinfo_file}"

    #3. 创建bed和提取fasta文件
    #上游30bp
    upstream_bed_file = os.path.join(outputdir,perfix + '.ups')
    upstream_fa_file = os.path.join(outputdir,perfix + '.ups.fa')
    upstream_file_cmd = f"""bedtools flank -l 30 -r 0 -s -i {te_bed_index_file} -g {ref_chrinfo_file} | awk -F'\\t' -v OFS='\\t' '$3 - $2 >= 30 || $2 - $3 >= 30 {{ $7 = $1":"$2"-"$3"("$6")"; print }}' > {upstream_bed_file} && bedtools getfasta -s -fi {ref} -bed {upstream_bed_file} -fo {upstream_fa_file}"""
    #自身前30bp, 用于发现新的RIP位点
    seed_bed_file = os.path.join(outputdir,perfix + '.seed')
    seed_fa_file = os.path.join(outputdir,perfix + '.seed.fa')
    seed_rmdup_fa = os.path.join(outputdir,perfix + '.seed.rmdup.fa')
    seed_file_cmd = f"""bedtools flank -l 0 -r 30 -s -i {upstream_bed_file} -g {ref_chrinfo_file} | awk -F'\\t' -v OFS='\\t' '$3 - $2 >= 30 || $2 - $3 >= 30 {{ $7 = $1":"$2"-"$3"("$6")"; print }}' > {seed_bed_file} && bedtools getfasta -s -fi {ref} -bed {seed_bed_file} -fo {seed_fa_file} && grep -v '>' {seed_fa_file} | sort | uniq -c | sort -n -r | awk '$1 > 100 {{print ">seed"++i; print $2}}' > {seed_rmdup_fa}"""

    #上游30bp+自身前30bp
    joined_bed_file = os.path.join(outputdir,perfix + '.joined')
    joined_fa_file = os.path.join(outputdir,perfix + '.joined.fa')
    joined_file_cmd = f"""bedtools slop -l 0 -r 30 -s -i {upstream_bed_file} -g {ref_chrinfo_file} | awk -F'\\t' -v OFS='\\t' '$3 - $2 >= 60 || $2 - $3 >= 60 {{ $7 = $1":"$2"-"$3"("$6")"; print }}' > {joined_bed_file} && bedtools getfasta -s -fi {ref} -bed {joined_bed_file} -fo {joined_fa_file}"""
    
    #下游100bp
    downtream_bed_file = os.path.join(outputdir,perfix + '.downs')
    downstream_fa_file = os.path.join(outputdir,perfix + '.downs.fa')
    downstream_file_cmd = f"""bedtools flank -l 0 -r 100 -s -i {te_bed_index_file} -g {ref_chrinfo_file} | awk -F'\\t' -v OFS='\\t' '$3 - $2 >= 100 || $2 - $3 >= 100 {{ $7 = $1":"$2"-"$3"("$6")"; print }}' > {downtream_bed_file} && bedtools getfasta -s -fi {ref} -bed {downtream_bed_file} -fo {downstream_fa_file}"""

    print('Creating index...',end="", flush=True)

    start_time = time.time()
    index_extent =[i + j for i in ['.ups.fa', '.joined.fa', '.downs.fa', '.seed.rmdup.fa'] for j in ['.0123', '.amb', '.ann', '.bwt.2bit.64', '.pac']] 
    index_file = [os.path.join(outputdir,perfix + i) for i in index_extent]
    index_exists = all(os.path.exists(file) for file in index_file)
    if  not index_exists:
        commands = [te_bed_index_file_cmd,ref_chrinfo_file_cmd]
        run_cmd_parallel(commands)
        # commands = [upstream_file_cmd,downstream_file_cmd]
        run_cmd(upstream_file_cmd)
        run_cmd(downstream_file_cmd)
        # run_cmd_parallel(commands)
        commands = [joined_file_cmd, seed_file_cmd]
        run_cmd_parallel(commands)
        commands = [bwa_index_cmd(fi) for fi in [upstream_fa_file, joined_fa_file, downstream_fa_file, seed_rmdup_fa]]
        run_cmd_parallel(commands)
        end_time = time.time()
        print(f"\tDone!\t{calculate_run_time(start_time,end_time)}")
    else:
        print('\talready exists!')

    if mode == "1":
        return te_bed_index_file, upstream_bed_file, upstream_fa_file, joined_bed_file, joined_fa_file, downtream_bed_file, downstream_fa_file
    elif mode in ['2','3']:
        start_time = time.time()
        index_file = [ref + i for i in ['.0123', '.amb', '.ann', '.bwt.2bit.64', '.pac']]
        index_exists = all(os.path.exists(file) for file in index_file)
        if  not index_exists:
            print('Creating reference genome index...',end="", flush=True)
            run_cmd(bwa_index_cmd(ref))
            end_time = time.time()
            print(f"\tDone!\t{calculate_run_time(start_time,end_time)}")
        return seed_rmdup_fa,ref_chrinfo_file




if __name__ == '__main__':

    preprocess()
    