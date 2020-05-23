from multiprocessing import Pool
import sys
from time import sleep

def readfile(file):
  with open(file, 'r') as f:
    for x in f:
      try:
        link = x.strip('\n')
        key = link.split('/')[3]
        urls.append(link)
      except:
        pass

def work(link):
        print(f"going to dump {link}")
        countdown(2)

def countdown(time=30):
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
