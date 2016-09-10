import numpy as np


def greedy_scheduler(jobs, method):

    # Check jobs array has correct number of columns (2: weights and lengths).
    if jobs.shape[1] != 2:
        raise(NameError, "Incorrect number of columns in jobs argument")

    if method == "difference":
        # score of each job is its weight minus length
        scores = jobs[:, 0] - jobs[:, 1]
    elif method == "ratio":
        # score of each job is its weight divided be its length
        scores = jobs[:, 0] / jobs[:, 1]
    else:
        # method argument is not defined
        raise (NameError, "Invalid method argument")

    job_order = np.lexsort((jobs[:, 0], scores))[::-1]
    completion_times = np.cumsum(jobs[job_order,1])
    cost = np.sum(completion_times * jobs[:,0])

    return cost
