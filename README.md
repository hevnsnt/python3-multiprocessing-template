# python3-multiprocessing-template
This is just an empty python3 multiprocessing template. It is my main framework for multi-threaded applications. 

CTRL-C works great in Linux, not exactly sure what is going on with windows (any help here would be appreciated) but if you need to break the program in windows, use CTRL-Break.


Map is a cool little function, and the key to easily injecting parallelism into your Python code. For those unfamiliar, map is something lifted from functional languages like Lisp. It is a function which maps another function over a sequence. e.g.

This single statement handles everything we did in the seven line build_worker_pool function from example2.py. Namely, It creates a bunch of available workers, starts them up so that they’re ready to do some work, and stores all of them in variable so that they’re easily accessed.

The pool objects take a few parameters, but for now, the only one worth noting is the first one: processes. This sets the number of workers in the pool. If you leave it blank, it will default to the number of Cores in your machine.

In the general case, if you’re using the multiprocessing pool for CPU bound tasks, more cores equals more speed (I say that with a lot of caveats). However, when threading and dealing with network bound stuff, things seem to vary wildly, so it’s a good idea to experiment with the exact size of the pool.



## Sources:
https://www.ellicium.com/python-multiprocessing-pool-process/
https://chriskiehl.com/article/parallelism-in-one-line
