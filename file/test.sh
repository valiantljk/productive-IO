#!/bin/bash
rm $SCRATCH/h5temp/*.h5
module load python/2.7-anaconda
module load cray-hdf5/1.8.16
m=$(date | awk '{print $3}')
d=$(date | awk '{print $2}')
rp=report.${m}.${d}
echo "report in "${rp}
touch $rp
printf '\nh5py creation time:' > ${rp}
(time python file_create.py $SCRATCH/h5temp 1000 ) >> ${rp} 2>&1
rm file_create
cc -o file_create file_create.c
printf 'h5py created:'
ls $SCRATCH/h5temp | wc 
rm $SCRATCH/h5temp/*
printf '\nhdf5 creation time:' >> ${rp}
(time ./file_create $SCRATCH/h5temp 1000 )  >> ${rp} 2>&1
printf 'hdf5 created:'
ls $SCRATCH/h5temp |wc
cat ${rp}
