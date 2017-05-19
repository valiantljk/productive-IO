#include<stdio.h>
#include<hdf5.h>
#include<string.h>
#include<stdlib.h>
#include <time.h>
#define MAX_NAME 255
int main(int argc, char ** argv){
 hid_t fileid;
 int i;
 if (argc<2){
  printf("args need path name and number of files\n");
  return 0;
 }
 char pathname[255];
 strncpy(pathname,argv[1],255);
 struct timeval t1, t2,t11,t22;
 double elapsedTime=0.0;
 gettimeofday(&t11, NULL);

 int x =(int) strtol(argv[2], NULL, 10);
 for (i=0;i<x;i++){
  char filename[266];
  char temp[10];
  strncpy(filename,pathname,MAX_NAME);
  sprintf(temp,"/%d.h5",i); 
  strcat(filename,temp);
  gettimeofday(&t1, NULL);
  fileid=H5Fcreate(filename,H5F_ACC_RDWR & H5F_ACC_EXCL,H5P_DEFAULT,H5P_DEFAULT);
  H5Fclose(fileid);
  gettimeofday(&t2, NULL);
  elapsedTime += (t2.tv_sec - t1.tv_sec);
 }
 gettimeofday(&t22, NULL);
 double elapsedTimeT = (t22.tv_sec - t11.tv_sec);
 printf("%.6f,%.6f seconds\n",elapsedTime,elapsedTimeT);
 return 0;
}

