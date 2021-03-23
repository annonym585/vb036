"""
1. Copy your whole ROPOT into text file "ropot.txt" starting with "1."
2. Run vb036.py in your cmd
"""


def find_in_results(question: str, filename: str) -> str:
    answer_found = False
    last = ""
    with open(filename, "r") as results:
        for line in results:
            if question in line:
                answer_found = True
            if answer_found:
                if "\"" in line:
                    my_split = line.split("\"")
                    if len(my_split) >= 4:
                        last = my_split[3]
                if "true" in line:
                    return last
        return "error"


def anj_solver(results: str, file: str) -> None:
    next_is_copy = False
    with open(file, "r") as my_file:
        for line in my_file:
            if not next_is_copy and line[:-2].isnumeric():
                print(line[:-1], end="")
                next_is_copy = True
            elif next_is_copy:
                next_is_copy = False
                print(find_in_results(line[:-1], results))


def main() -> None:
    anj_solver("results.txt", "ropot.txt")


if __name__ == '__main__':
    main()
