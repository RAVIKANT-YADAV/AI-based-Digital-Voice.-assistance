# Code to Measure time taken by program to execute.
import Allmodul as module
# store starting time
begin = module.time.time()
# program body starts




# program body ends
module.time.sleep(1)
# store end time
end = module.time.time()
# total time taken
print(f"Total runtime of the program is {end - begin}")
