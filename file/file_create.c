#include<stdio.h>
#include<hdf5.h>
#include<string.h>
int main(){
 char filename[255];
 strncpy(filename,"test_c.h5",255);
 //printf("Creating file %s\n",filename);
 hid_t fileid;
 //fileid=H5Fcreate(filename,H5F_ACC_RDWR|H5F_ACC_EXCL,H5P_DEFAULT,H5P_DEFAULT);
 //fileid=H5Fcreate(filename,H5F_ACC_EXCL,H5P_DEFAULT,H5P_DEFAULT);
 fileid=H5Fcreate(filename,H5F_ACC_RDWR & H5F_ACC_EXCL,H5P_DEFAULT,H5P_DEFAULT);
 return 0;
}

