# TypeSINE

TypeSINE is designed to detect short interspersed nuclear element (SINE) retrotransposon insertion polymorphisms directly from raw next-generation sequencing (NGS) data. The analytical workflow comprises two complementary pipelines：

- **Pipeline A** identifies putative polymorphic SINE insertions that are present in the reference genome but may be absent in the test genomes.
- **Pipeline B** detects novel polymorphic SINE insertions found in the test genomes but missing from the reference genome.

![](./workflow.jpg)



### 

## Dependencies

1. bwa-mem2 (version 2.2.1 or later), which can be downloaded from [https://github.com/bwa-mem2](https://github.com/bwa-mem2/bwa-mem2).
2. samtools (version 1.0 or later), which can be downloaded from [https://github.com/samtools](https://github.com/samtools).
3. bedtools (version 2.30.0 or later), which can be downloaded from [https://github.com/arq5x/bedtools2](https://github.com/arq5x/bedtools2).
4. Python 3.6+
   - For the following packages, o
   - pandas

```shell
bwa-mem2, samtools, bedtools
```

