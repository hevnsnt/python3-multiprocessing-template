"""
Script Name
"""
__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

from multiprocessing import cpu_count
from multiprocessing.dummy import Pool as ThreadPool
import argparse
from time import sleep
import signal
import sys


def readfile(file):
  with open(file, 'r') as file:
    data = file.readlines()
  return data

def work(line):
  while(True):
    try:
      print(f"\rgoing to do some work on {line}")
      countdown(5)
    except (KeyboardInterrupt, SystemExit):
      print("Exiting work...")
      break

def countdown(time=30):
  sleep(time)

def cmdline_args():
  # Make parser object
  p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
  p.add_argument("-f", "--file", required = True, help="Insert the flie you plan on parsing")
  p.add_argument("-t", "--threads", default=cpu_count(), help="Number of threads, by default will use all available processors")
  p.add_argument("-v", "--verbose", help="increase output verbosity",
                       action="store_true")
  return(p.parse_args())
  ''' Other Example Arguments

    p.add_argument("required_positional_arg", help="desc") # Required positional argument
    p.add_argument("-n", "--name", action="store", dest="name")
    p.add_argument("required_int", type=int, help="req number") # Required Integer argument
    p.add_argument("--on", action="store_true", default=False,  # Optional argument which requires a parameter (eg. -d test)
                   help="include to enable") # Optional argument flag which defaults to False
    p.add_argument("-v", "--verbosity", type=int, choices=[0,1,2], default=0,
                   help="increase output verbosity (default: %(default)s)") # Optional verbosity argument
    p.add_argument("--version", action="version",
        version="%(prog)s (version {version})".format(version=__version__)) # Optional version argument
                   
    group1 = p.add_mutually_exclusive_group(required=True)
    group1.add_argument('--enable',action="store_true")
    group1.add_argument('--disable',action="store_false")'''

def versionCheck(version):
  if version<(3,5,0):
    sys.stderr.write(f"Python Version: {sys.version}.\nPython 3.5 or later is required to run this script\n")
    sys.exit(1) 


if __name__ == '__main__':
  versionCheck(sys.version_info) #If you require a certain version of python to run script.
  try:
    args = cmdline_args() # Parse the commandline args
  except:
    print(f'\nArgument Failure: Try {sys.argv[0]} -h')
    sys.exit(1)

  data = readfile(args.file) #read the entire file and store it in a variable:
  pool = ThreadPool(args.threads) #Init the data pool w/number of threads going to use
  try:
    pool.map(work,data) # This launches the workers at the function to do work
    pool.close()
    pool.join()
  except KeyboardInterrupt:
    print("Exiting Cleanly...")
  except Exception as error:
    print(error)
