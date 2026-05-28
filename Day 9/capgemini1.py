def main():
    try:
        sem = int(input("Enter no of semester:\n"))
        max_marks = []

        for i in range(1, sem + 1):
            subjects = int(input(f"Enter no of subjects in {i} semester:\n"))
            print(f"Marks obtained in semester {i}:")

            marks = []
            for j in range(subjects):
                mark = int(input())
                if mark < 0 or mark > 100:
                    print("You have entered invalid mark.")
                    return
                marks.append(mark)

            max_marks.append(max(marks))

        for i in range(sem):
            print(f"Maximum mark in {i+1} semester:{max_marks[i]}")

    except ValueError:
        print("You have entered invalid mark.")

if __name__ == "__main__":
    main()