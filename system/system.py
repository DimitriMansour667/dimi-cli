import os


def do_mem(self, line):
    # show memory usage of the program in MB
    import psutil

    process = psutil.Process()
    print(f"Memory usage: {process.memory_info().rss / 1024 / 1024} MB")


def do_ip(self, line):
    # show ip address
    os.system("curl ifconfig.me")
    print()


def do_sys(self, line):
    # run system commands
    try:
        os.system(line)
    except Exception as e:
        print(e)
