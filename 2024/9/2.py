import os, sys
import time

class File:
    def __init__(self, size: int, idx: int, is_disk: bool):
        self.size = size
        self.is_disk = is_disk
        self.idx = idx
    def __str__(self):
        if self.is_disk:
            return f"{self.idx}" * self.size
            # for _ in range(self.size):
            #     result += str(self.idx)
            # return result
        else:
            return "." * self.size
    def __repr__(self) -> str:
        return self.__str__()

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    disk: list[File] = []
    mode = 0
    idx = 0
    for char in text:
        # disk
        if mode == 0:
            length = int(char)
            disk.append(File(length, idx, True))
            idx += 1
        # free space
        else:
            length = int(char)
            disk.append(File(length, -1, False))
        mode ^= 1
    #print(disk)

    left = 0
    right = len(disk) - 1
    while True:
        # find first disk
        for i in range(right, left - 1, -1):
            if disk[i].is_disk is True:
                right = i
                break
        
        # search left until space fits
        for i in range(0, right + 1,):
            if disk[i].is_disk is False and disk[i].size >= disk[right].size:
                disk_to_move = disk[right]
                disk[right] = File(disk[right].size, -1, False)
                left_over_space = disk[i].size - disk_to_move.size
                disk[i] = disk_to_move
                if (left_over_space) > 0:
                    disk.insert(i + 1, File(left_over_space, -1, False))
                    right += 1
                #print(disk)
                break
        right -= 1
        if right <= 0:
            break
    #print(disk)
    total = 0
    current_file = 0
    for i, idx in enumerate(disk):
        if idx.is_disk is False:
            current_file += idx.size
            continue
        for _ in range(idx.size):
            total += current_file * idx.idx
            current_file += 1
    print(total)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
