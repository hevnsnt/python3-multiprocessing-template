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

def parseArgs(args):
  if args.verbose:
    verbose = True
    print("[+] Verbosity turned on")
  else:
    verbose = False
  if args.threads:
    threads = args.threads
  else:
    threads = cpu_count()
  print(f'[+] Using {threads} threads')
  return threads, verbose, args.file


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-f", "--file", required = True, help="Insert the flie you plan on parsing")
  parser.add_argument("-t", "--threads", help="Number of threads, by default will use all available processors")
  parser.add_argument("-v", "--verbose", help="increase output verbosity",
                       action="store_true")
  threads, verbose, filename = parseArgs(parser.parse_args())
  #read the entire file and store it in a variable:
  data = readfile(filename)
  #Init the data pool
  pool = ThreadPool(threads) # Number of threads going to use
  try:
    pool.map(work,data) # This launches the workers at the function to do work
    pool.close()
    pool.join()
  except KeyboardInterrupt:
    print("Exiting Cleanly...")
  except Exception as error:
    print(error)
