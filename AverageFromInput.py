# CS175L-01
# Bryn Bijur
# AverageFromInput.py
def main():
    # Open a file named philosophers.txt.
    infile = open('numbers.txt', 'r')

    # Read three lines from the file
    line1 = float(infile.readline())
    line2 = float(infile.readline())
    line3 = float(infile.readline())

    # Close the file.
    infile.close()

    # Print the data that was read into
    # memory.
    count = 1
    total = 0
    total += line1
    print("I read in", count, "number(s) Current number is:", line1, "Total is:", total)
    count += 1
    total += line2
    print("I read in", count, "number(s) Current number is:", line2, "Total is:", total)
    count += 1
    total += line3
    print("I read in", count, "number(s) Current number is:", line3, "Total is:", total)
    average = total / count
    print("Average:", average)


# Call the main function.
if __name__ == '__main__':
    main()
