# This file is to test collective io in h5py
 
"""
Author:  Jialin Liu, jalnliu@lbl.gov
Date:    Nov 17, 2015
Prerequisites: python 2.5.0, mpi4py and numpy
Source Codes: This 'collective io' branch is pushed into the h5py master
Note: Must build the h5py with parallel hdf5
"""

from mpi4py import MPI
import numpy as np
import h5py
import time
import sys

#"run as "mpirun -np 64 python-mpi collective_io.py 1 file.h5" 
#(1 is for collective write, ohter number for non-collective write)"

colw=1 #default is collective write
filename="parallel_test.hdf5"
if len(sys.argv)>4:
	colw = int(sys.argv[1])
	filename=str(sys.argv[2])
        length_x = int(sys.argv[3])
        length_y = int(sys.argv[4])
comm =MPI.COMM_WORLD
nproc = comm.Get_size()
comm.Barrier()
timefstart=MPI.Wtime()
f = h5py.File(filename, 'w', driver='mpio', comm=MPI.COMM_WORLD)
rank = comm.Get_rank()
dset = f.create_dataset('test', (length_x,length_y), dtype='f8')
comm.Barrier()
timefend=MPI.Wtime()
f.atomic = False
length_rank=length_x / nproc
length_last_rank=length_x -length_rank*(nproc-1)
comm.Barrier()
timestart=MPI.Wtime()
start=rank*length_rank
end=start+length_rank
if rank==nproc-1: #last rank
    end=start+length_last_rank
temp=np.random.random((end-start,length_y))
comm.Barrier()
timemiddle=MPI.Wtime()
if colw==1:
	with dset.collective:
		dset[start:end,:] = temp
else :
	dset[start:end,:] = temp
comm.Barrier()
timeend=MPI.Wtime()
if rank==0:
    
    print "allocation time %.2f "%(timemiddle-timestart)
    print "file/dataset creation time %.2f "%(timefend-timefstart)
    if colw==1:
    	print "collective write time %.2f " %(timeend-timemiddle)
    else :
	print "independent write time %.2f " %(timeend-timemiddle)
    total_sz_gb=length_x*length_y/1024.0/1024.0/1024.0*8.0
    print "data dim size x: %d y: %d " %(length_x, length_y)
    print "file size %.2f GB " % (total_sz_gb)
    print "bandwidth %.2f GB/s " %(total_sz_gb/(timeend-timemiddle))
    print "number of processes %d " %nproc
timeclose=MPI.Wtime()
f.close()
timecloseend=MPI.Wtime()
if rank==0:
   print "close time:%.2f\n"%(timecloseend-timeclose)

