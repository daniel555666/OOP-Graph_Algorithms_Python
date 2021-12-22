if __name__ == '__main__':
    Nodes = {1, 2, 3, 4}
    EdgesIn = {
        1: {

            2: (2, 0.1),
            3: (3, 5.9),
            4: (4, 10.5)
        }
    }
    print("tuple is :")
    print(EdgesIn[1][2])
    print(EdgesIn[1])
