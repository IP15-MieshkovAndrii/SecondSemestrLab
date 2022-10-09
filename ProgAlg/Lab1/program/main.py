from sorter import Sorter


def main():
    sorter = Sorter("a.bin", "b.bin", "c.bin")
    sorter.generate_file(1024**2, 1000000)
    sorter.sort()
    print(sorter)


if __name__ == "__main__":
    main()
