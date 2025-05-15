#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# here put the import lib
import os
import sys
from utils import *
from core import *
from pathlib import Path

def main():
    """
    The main-function:
        1. 检查软件依赖
    """
    #初始化参数
    args = parse_args()

    mode = args.mode
    output = args.output
    ref = args.ref
    te_bed_file = args.bed
    reads_file = args.fas
    newloci = args.newloci
    threads = args.threads
    results_dir = args.dir
    overwrite = args.overwrite

    try:
        # Check software dependencies
        software_to_check = ["bwa-mem2", "samtools", "bedtools"]  # 需要检查的软件列表
        if not check_software_availability(software_to_check):
            sys.exit(1)

        # Create output directory
        outputdir = Path(output) if args.output else Path.cwd()
        indexdir = Path(outputdir, "index") 
        tmpdir = Path(outputdir, "tmp")

        for dir_path in [outputdir, indexdir, tmpdir]:
            dir_path.mkdir(parents=True, exist_ok=True)

        if mode == "1":
            required_options = {"ref":[ref,"-r, --ref"], "te_bed_file":[te_bed_file, "-b, --bed"], "reads_file":[reads_file,"-f, --fas"]}
            if all([value [0] for value in required_options.values()]):
                print('\n-----Find reference RIP-----\n')
                print(f'Reads file name:\x1b[92m\t{os.path.basename(reads_file)}\x1b[0m')
                te_bed_index_file, upstream_bed_file, upstream_fa_file, joined_bed_file, joined_fa_file, downtream_bed_file, downstream_fa_file = preprocess(mode,ref,te_bed_file,output)
                ref_rip_finder(te_bed_index_file, upstream_bed_file, upstream_fa_file, joined_bed_file, joined_fa_file, downtream_bed_file, downstream_fa_file, reads_file, threads, overwrite, output)
            else:
                for option in required_options.values():
                    if not option[0]:
                        print(f"RIPFinder: error: the following arguments are required: {option[1]}")
        elif mode == "2":
            required_options = {"ref":[ref,"-r, --ref"], "te_bed_file":[te_bed_file, "-b, --bed"], "reads_file":[reads_file,"-f, --fas"]}
            if all([value [0] for value in required_options.values()]):
                print('\n-----de novo RIP Finding-----\n')
                print(f'Reads file name:\x1b[92m\t{os.path.basename(reads_file)}\x1b[0m')
                setup_dirs(output)
                seed_rmdup_fa,ref_chrinfo_file = preprocess(mode,ref,te_bed_file,output)
                new_rip_finder(seed_rmdup_fa,ref_chrinfo_file, ref, reads_file, threads, overwrite, output)
            else:
                for option in required_options.values():
                    if not option[0]:
                        print(f"RIPFinder: error: the following arguments are required: {option[1]}")
        elif mode == "3":
            required_options = {"ref":[ref,"-r, --ref"], "te_bed_file":[te_bed_file, "-b, --bed"], "newloci":[newloci, "-n, --newloci"], "reads_file":[reads_file,"-f, --fas"]}
            if all([value [0] for value in required_options.values()]):
                print('\n-----All de novo RIP loci Refinding-----\n')
                setup_dirs(output)
                seed_rmdup_fa,ref_chrinfo_file = preprocess(mode,ref,te_bed_file,output)
                new_rip_refinder(newloci, seed_rmdup_fa, ref_chrinfo_file, ref, reads_file, threads, overwrite, output)
            else:
                for option in required_options.values():
                    if not option[0]:
                        print(f"RIPFinder: error: the following arguments are required: {option[1]}")
        else:
            if results_dir:
                print('\n-----Merge RIP results-----\n')
                merge_results(results_dir, output)
            else:
                print(f"RIPFinder: error: the following arguments are required: -d, --dir")

    except Exception as e:
        sys.stderr.write("%s\n" % e)

if __name__ == '__main__':
    main() 