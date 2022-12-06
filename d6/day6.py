def get_marker(file_name, distinct_char_count):
    with open(file_name) as f:
        input = f.read().strip()

        for i in range(len(input)):
            if(i == len(input) - distinct_char_count):
                break
            else:
                if len(set(input[i:i + distinct_char_count])) == distinct_char_count:
                    return i + distinct_char_count

print(get_marker("./d6/input.txt", 4))
print(get_marker("./d6/input.txt", 14))
