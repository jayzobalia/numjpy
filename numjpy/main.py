def main(stri):
    if stri == "minmax":
        text = "def divideAndConquer_Max(arr, ind, len):\nmaximum = -1;\n\nif (ind >= len - 2):\nif (arr[ind] > arr[ind + 1]):\nreturnarr[ind];\n\nelse:\nreturn arr[ind + 1];\n\nmaximum = divideAndConquer_Max(arr, ind + 1, len);\n\nif (arr[ind] > maximum):\nreturn arr[ind];\nelse:\nreturn maximum;\n\ndef divideAndConquer_Min(arr, ind, len):\nminimum = 0;\nif (ind >= len - 2):\nif (arr[ind] < arr[ind + 1]):\nreturn arr[ind];\nelse:\nreturn arr[ind + 1];\n\nminimum = divideAndConquer_Min(arr, ind + 1, len);\nif (arr[ind] < minimum):\nreturn arr[ind];\nelse:\nreturn minimum;\n\nif __name__ == '__main__':\n\nminimum, maximum = 0, -1;\narr = [6, 4, 8, 90, 12, 56, 7, 1, 63];\n\nmaximum = divideAndConquer_Max(arr, 0, 9);\nminimum = divideAndConquer_Min(arr, 0, 9);\n\nprint('The minimum number in the array is: ', minimum);\nprint('The maximum number in the array is: ', maximum);"
    else:
        text = "menu:\n1)minmax"
    return text

if __name__ =="__main__":
    print(main("minmax"))