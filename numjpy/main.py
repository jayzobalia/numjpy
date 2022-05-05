def main(stri):
    if stri == "minmax":
        text ="#divide_and_conqure_method\ndef divideAndConquer_Max(arr, ind, len):\nmaximum = -1;\n\nif (ind >= len - 2):\nif (arr[ind] > arr[ind + 1]):\nreturnarr[ind];\n\nelse:\nreturn arr[ind + 1];\n\nmaximum = divideAndConquer_Max(arr, ind + 1, len);\n\nif (arr[ind] > maximum):\nreturn arr[ind];\nelse:\nreturn maximum;\n\ndef divideAndConquer_Min(arr, ind, len):\nminimum = 0;\nif (ind >= len - 2):\nif (arr[ind] < arr[ind + 1]):\nreturn arr[ind];\nelse:\nreturn arr[ind + 1];\n\nminimum = divideAndConquer_Min(arr, ind + 1, len);\nif (arr[ind] < minimum):\nreturn arr[ind];\nelse:\nreturn minimum;\n\nif __name__ == '__main__':\n\nminimum, maximum = 0, -1;\narr = [6, 4, 8, 90, 12, 56, 7, 1, 63];\n\nmaximum = divideAndConquer_Max(arr, 0, 9);\nminimum = divideAndConquer_Min(arr, 0, 9);\n\nprint('The minimum number in the array is: ', minimum);\nprint('The maximum number in the array is: ', maximum);\n\n\n\n\n#for_loop_method\nnumbers = [55, 4, 92, 1, 104, 64, 73, 99, 20]\nmax_value = None\nfor num in numbers:\n\tif (max_value is None or num > max_value):\n\t\tmax_value = num\nprint('Maximum value:', max_value)"

    elif stri =="":
        text= ""
    else:
        text = "menu:\n1)minmax"
    return text

if __name__ =="__main__":
    print(main("minmax"))

# text = "def divideAndConquer_Max(arr, ind, len):\n\tmaximum = -1;\n\n\tif (ind >= len - 2):\n\t\tif (arr[ind] > arr[ind + 1]):\n\t\t\treturn arr[ind];\n\t\telse:\n\t\t\treturn arr[ind + 1];\n\n\n\nmaximum = divideAndConquer_Max(arr, ind + 1, len);\n\n\tif (arr[ind] > maximum):\n\t\t\treturn arr[ind];\n\telse:\n\t\t\treturn maximum;\n\n\ndef divideAndConquer_Min(arr, ind, len):\n\tminimum = 0;\n\tif (ind >= len - 2):\n\t\tif (arr[ind] < arr[ind + 1]):\n\t\t\treturn arr[ind];\n\t\telse:\n\t\t\treturn arr[ind + 1];\n\n\tminimum = divideAndConquer_Min(arr, ind + 1, len);\n\n\tif (arr[ind] < minimum):\n\t\treturn arr[ind];\n\telse:\n\t\treturn minimum;\n\n\nif __name__ == '__main__':\n\n\nminimum, maximum = 0, -1;\n\n\n\tarr = [6, 4, 8, 90, 12, 56, 7, 1, 63];\n\n\tmaximum = divideAndConquer_Max(arr, 0, 9);\n\tminimum = divideAndConquer_Min(arr, 0, 9);\n\n\tprint('The minimum number in the array is: ', minimum);\n\tprint('The maximum number in the array is: ', maximum);\n\n\n\n\n#for_loop_method\nnumbers = [55, 4, 92, 1, 104, 64, 73, 99, 20]\nmax_value = None\nfor num in numbers:\n\tif (max_value is None or num > max_value):\n\t\tmax_value = num\nprint('Maximum value:', max_value)"
# print(text)


