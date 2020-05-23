from multiprocessing import Pool
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
        print(f"going to du some work on {line}")
        countdown(2)

def countdown(time=30):
  #defaults to 30secs unless you pass it a different value
  for remaining in range(time, 0, -1):
    print(f"\r<<<<  {remaining} seconds remain before auto-resume >>>>", end=" ", flush=True)
    sleep(1)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-f", "--file", help="Insert the flie you plan on parsing")
  parser.add_argument("-t", "--threads", help="Number of threads, by default will use all available processors")
  parser.add_argument("-v", "--verbose", help="increase output verbosity",
                       action="store_true")
  parser.parse_args()
  if args.verbose:
    print("verbosity turned on")
  
  pool = Pool(4) # Number of threads going to use
  pool.map(work, urls)
  pool.close()
  pool.join()
