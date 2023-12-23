import sys
def count_move(nums):
    nums.sort()
    median = nums[len(nums) // 2]

    all_move = 0
    for num in nums:
        all_move += abs(num - median)

    return all_move

if len(sys.argv) != 2:
    print("python filename filename.txt")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, 'r') as file:
        nums = [int(line.strip()) for line in file]

    result = count_move(nums)
    print(result)

except FileNotFoundError:
    print(f"нет файла '{file_path}'.")
except ValueError:
    print("Не числа")
except Exception as e:
    print(f"Непредвиденная ошибка: {e}")