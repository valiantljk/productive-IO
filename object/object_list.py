import h5py
import argparse
import time
def list_object(filename,groupname,pp):
 fx=h5py.File(filename,'r')
 if pp==1:
  ll=fx[groupname].keys()
  print "\n%d objects:"%len(ll),ll,"\n"
 else:
  ll=fx[groupname].keys()
  print "\n%d objects"%len(ll)
if __name__=='__main__':
 parser = argparse.ArgumentParser(prog='list_object') 
 parser.add_argument("filename",  help="file name")
 parser.add_argument("groupname", help="group name, default is /")
 parser.add_argument("toprint",help="to print objects or not")
 opts=parser.parse_args()
 fn=opts.filename
 if opts.groupname:
  gn=opts.groupname
 else:
  gn='/'
 pp=(int)(opts.toprint)
 start=time.time()
 list_object(fn,gn,pp) 
 end=time.time()
 print "%.6f seconds\n"%(end-start) 
