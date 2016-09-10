from FileReadLib import get_array
from GreedySchedulerLib import greedy_scheduler

# Calculates optimal scheduling using two greedy algorithms, only one on of which is correct.
jobs = get_array("jobs")

cost_diff = greedy_scheduler(jobs, "difference")
cost_ratio = greedy_scheduler(jobs, "ratio")

print("cost with difference score:\t" + str(cost_diff))
print("cost with ratio score:\t\t" + str(cost_ratio))

print("done.")