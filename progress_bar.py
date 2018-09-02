import sys
import time
import math

n_messages = 650

for index, url_dict in enumerate(range(n_messages)):
    index += 1
    time.sleep(0.01)
    
    progress_index = math.floor(index/n_messages*100)

    percentual = "%.2f%%" % progress_index
    sys.stdout.write('\r[{0}{1}] {2}'.format('#' * progress_index,
                                              ' ' * (100-progress_index),
                                            percentual))
    sys.stdout.flush()
    
print("")
