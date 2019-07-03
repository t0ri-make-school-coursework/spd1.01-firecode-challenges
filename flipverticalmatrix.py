def flip_vertical_axis(matrix):
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
      
    return matrix


def main():
    print(flip_vertical_axis([[1,1,0], [0,1,0], [0,0,1]]))


if __name__ == "__main__":
    main()