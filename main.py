from FileReadLib import get_array
from GreedySchedulerLib import greedy_scheduler

# Calculates optimal scheduling using two greedy algorithms, only one on of which is correct.
jobs = get_array("jobs")

schedule_diff = greedy_scheduler(jobs, "difference")
schedule_ratio = greedy_scheduler(jobs, "ratio")

# weighted_completion_times_diff =


print("done.")