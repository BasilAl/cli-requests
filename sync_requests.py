import requests
import sys
import time


def get_many(arg):
    """
    Performs a get request <input> amount of times and returns the total times it fetched the site and the amount of time it took to do so.
    Example use: python3? sync_requests.py 12
    """

    if len(arg) != 2:
        print("Function takes exactly 1 argument which should be a positive integer. Example use: python3? "
              "sync_requests.py 12")
        return -1
    if not arg[1].isdigit():
        print("Function takes exactly 1 argument which should be a positive integer. Example use: python3? "
              "sync_requests.py 12")
        return -1

    n = int(arg[1])
    start = time.time()

    for i in range(n):
        resp = requests.get("https://google.gr")

    dt = time.time() - start
    print("get {} sites in {:.4f} seconds".format(n, dt))


if __name__ == "__main__":
    get_many(sys.argv)
