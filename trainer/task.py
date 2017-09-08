import os

mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
mem_gib = mem_bytes/(1024.**3)
print(str(mem_gib)+"GB")

# another
meminfo = dict((i.split()[0].rstrip(':'),int(i.split()[1])) for i in open('/proc/meminfo').readlines())
mem_gib = meminfo['MemTotal']/(1024.**2)
print(str(mem_gib)+"GB")

exit(-1)
