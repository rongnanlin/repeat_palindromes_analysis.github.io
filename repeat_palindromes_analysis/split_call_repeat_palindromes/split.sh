awk '/^>/ { gsub(">","",$1)
	FILE=$1 ".fa"
	print ">" $1 >> FILE
	next}
	{ print >> FILE }' GCA_004355905.1_PgNI_genomic.fna


mkdir qsub
mkdir result
for i in `cat gennome_list`;do
        echo "#!/bin/bash
#PBS -N cat_${i}
#PBS -l nodes=1:ppn=2
#PBS -o ./cat_${i}.log
#PBS -e ./cat_${i}.err

python /gpfs01/home/linrongnan/test/01_20200524/ref/split/loop_0_1.py --input /gpfs01/home/linrongnan/test/01_20200524/ref/split/${i} > /gpfs01/home/linrongnan/test/01_20200524/ref/split/result/${i}_loop_0_1_result.xls


python /gpfs01/home/linrongnan/test/01_20200524/ref/split/loop_2_3.py --input /gpfs01/home/linrongnan/test/01_20200524/ref/split/${i} > /gpfs01/home/linrongnan/test/01_20200524/ref/split/result/${i}_loop_2_3_result.xls


python /gpfs01/home/linrongnan/test/01_20200524/ref/split/loop_4_5.py --input /gpfs01/home/linrongnan/test/01_20200524/ref/split/${i} > /gpfs01/home/linrongnan/test/01_20200524/ref/split/result/${i}_loop_4_5_result.xls
" >./qsub/find_${i}.pbs
done

