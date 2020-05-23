from multiprocessing import Pool
import sys
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
  urls = []
  readfile(sys.argv[1])
  pool = Pool(4)
  pool.map(work, urls)
  pool.close()
  pool.join()
