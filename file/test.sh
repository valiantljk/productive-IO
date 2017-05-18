#!/bin/bash
rm *.h5
module load python/2.7-anaconda
module load cray-hdf5/1.8.16
m=$(date | awk '{print $3}')
d=$(date | awk '{print $2}')
rp=report.${m}.${d}
echo "report in "${rp}
touch $rp
printf '\nh5py creation time:' > ${rp}
(time python file_create.py) >> ${rp} 2>&1
rm file_create
cc -o file_create file_create.c
printf '\nhdf5 creation time:' >> ${rp}
(time ./file_create )  >> ${rp} 2>&1

cat ${rp}
