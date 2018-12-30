import time

start_time = time.time()

x = input("test ")
while x != "done":
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)
    print(f"{minutes}:{seconds}")
    x = input("test")