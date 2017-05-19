#include<stdio.h>
#include<hdf5.h>
#include "getopt.h"
#include<string.h>
#include <time.h>
#define MAX_NAME 255
void list_object(hid_t gid,long pp){
 hsize_t nobj;
 herr_t err;
 int i;
 ssize_t len;
 err = H5Gget_num_objs(gid, &nobj);
 char memb_name[255];
 printf("\n%d Objects:",nobj);
 for (i=0;i<nobj;i++){
  len = H5Gget_objname_by_idx(gid,(hsize_t)i,memb_name,(size_t)MAX_NAME);
  if(pp)
   printf("%s ",memb_name);
 }
 printf("\n");
}

int main(int argc, char **argv){
 char filename[255];
 char groupname[255];
 strncpy(filename,argv[1],255);
 strncpy(groupname,argv[2],255);
 long x = strtol(argv[3], NULL, 10); //to print objects or not, 1 is yes
 hid_t fid,gid;
 struct timeval t1, t2;
 double elapsedTime;
 gettimeofday(&t1, NULL);
 //open the file
 fid=H5Fopen(filename,H5F_ACC_RDONLY,H5P_DEFAULT);
 //open the group
 gid=H5Gopen(fid,groupname,H5P_DEFAULT); 
 //list the group and dataset in this group, just one level, not deeper level
 list_object(gid,x); 
 
 gettimeofday(&t2, NULL);
 elapsedTime = (t2.tv_sec - t1.tv_sec);
 printf("%.6f seconds\n",elapsedTime);
 
 return 0;
}

