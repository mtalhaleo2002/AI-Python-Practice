# Task 2: NumPy Array Creation and Type Conversion
import numpy as np

def main():
    print("=" * 45)
    print("        NumPy Array Operations")
    print("=" * 45)

    # 1. Create a NumPy array containing the marks [78, 85, 92, 67, 88]
    marks = np.array([78, 85, 92, 67, 88])

    # 2. Display the array
    print("\n1. Original Marks Array:")
    print("Array:", marks)
    print("Data Type:", marks.dtype)

    # 3. Convert the array into float data type
    marks_float = marks.astype(float)

    # 4. Display the converted array
    print("\n2. Converted Marks Array (Float):")
    print("Array:", marks_float)
    print("Data Type:", marks_float.dtype)
    print("=" * 45)


if __name__ == "__main__":
    main()
