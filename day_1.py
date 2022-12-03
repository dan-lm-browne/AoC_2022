
from get_input import get_input_string, get_raw_input_string, get_input_list


def main():
    test_input = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
    input = get_input_string(1, 2022)
    test_part_1(test_input, input)
    test_part_2(test_input, input)


def test_part_1(test_input, input):
    test_solution = day1_algorithm(test_input)
    if test_solution == 24000:
        print("Algorithm is correct!")
        day1_algorithm(input)


def test_part_2(test_input, input):
    test_solution = day1_algorithm_pt2(test_input)
    if test_solution == 45000:
        print("Algorithm is correct!")
        day1_algorithm_pt2(input)


def day1_algorithm(input):
    calories_per_elf = get_calories_per_elf(input)
    print(max(calories_per_elf))
    return max(calories_per_elf)


def day1_algorithm_pt2(input):
    calories_per_elf = get_calories_per_elf(input)
    sorted_list = sorted(calories_per_elf, reverse=True)
    print(sum(sorted_list[:3]))
    return sum(sorted_list[:3])


def get_calories_per_elf(input):
    per_elf_input = input.split("\n\n")
    calories_per_elf = []
    for elf_snacks in per_elf_input:
        elf_calories = elf_snacks.split("\n")
        elf_calories = [int(a) for a in elf_calories]
        total_calories = sum(elf_calories)
        calories_per_elf.append(total_calories)
    return calories_per_elf


if __name__ == '__main__':
    main()

