import sys
import time

index = 0
for url_dict in range(100):
    time.sleep(0.1)
    index += 1

    percentual = "%.2f%%" % index
    sys.stdout.write('\r[{0}{1}] {2}'.format('#' * index,
                                             ' ' * (100-index),
                                           percentual))
    sys.stdout.flush()
    
print("")
