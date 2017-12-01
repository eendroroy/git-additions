import time


def duration(commit1, commit2):
    start = commit1.commit_time
    end = commit2.commit_time

    d = divmod(end - start, 86400)  # days
    h = divmod(d[1], 3600)  # hours
    m = divmod(h[1], 60)  # minutes
    s = m[1]  # seconds

    return d[0], h[0], m[0], s


def commit_date(commit):
    return time.ctime(commit.commit_time)
