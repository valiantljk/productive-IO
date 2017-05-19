#!/bin/bash
rm *.h5
module load python/2.7-anaconda
module load cray-hdf5/1.8.16
m=$(date | awk '{print $3}')
d=$(date | awk '{print $2}')
rp=report.${m}.${d}
echo "report in "${rp}
touch $rp
printf '\nh5py object listing time:' > ${rp}
(time python object_list.py /global/cscratch1/sd/jialin/h5boss/6499-56571.hdf5 /6499/56571 0 ) >> ${rp} 2>&1
rm object_list
cc -o object_list object_list.c
printf '\nhdf5 object listing time:' >> ${rp}
(time ./object_list /global/cscratch1/sd/jialin/h5boss/6499-56571.hdf5 /6499/56571 0 )  >> ${rp} 2>&1

cat ${rp}
