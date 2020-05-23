from multiprocessing import Pool, cpu_count
import argparse
from time import sleep

def readfile(file):
  with open(file, 'r') as f:
    for line in f:
      try:
        readline = line.strip('\n')
        work(line)
      except:
        pass

def work(line):
        print(f"going to do some work on {line}")
        countdown(2)

def countdown(time=30):
  #defaults to 30secs unless you pass it a different value
  sleep(3)
  '''for remaining in range(time, 0, -1):
    print(f"\r<<<<  {remaining} seconds remain before auto-resume >>>>", end=" ", flush=True)
    sleep(1)'''

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
  
  pool = Pool(threads) # Number of threads going to use
  pool.map(work)
  readfile(filename)
  pool.close()
  pool.join()
