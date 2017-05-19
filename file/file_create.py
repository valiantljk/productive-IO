import h5py
import argparse
import time
def file_create(pathname,n):
  alltime=0.0
  for i in range(n):
   fn=pn+'/'+str(i)+'.h5'
   start=time.time()
   fx=h5py.File(fn,'a')
   fx.close()
   end=time.time()
   alltime+=end-start
  return alltime
if __name__=='__main__':
  parser = argparse.ArgumentParser(prog='create_file')
  parser.add_argument("pathname",  help="path name")
  parser.add_argument("number",help="number of files")
  opts=parser.parse_args()
  pn=opts.pathname
  num=(int)(opts.number)
  start=time.time()
  allt=file_create(pn,num)
  end=time.time()
  print "%.6f,%.6f seconds\n"%(allt,end-start)

