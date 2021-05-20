def single_integer(args):
    if len(args) != 2:
        print("Function takes exactly 1 argument which should be a positive integer. Example use: python3? "
              "sync_requests.py 12")
        return -1
    if not args[1].isdigit():
        print("Function takes exactly 1 argument which should be a positive integer. Example use: python3? "
              "sync_requests.py 12")
        return -1
    return 0
