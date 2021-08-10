import multiprocessing
import shutil

print("Number of available CPU cores: ", multiprocessing.cpu_count())

total, used, free = shutil.disk_usage("/")

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Total: %d GiB" % (free // (2**30)))
