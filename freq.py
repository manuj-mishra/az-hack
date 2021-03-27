def open_file(file_name):
    f = open(file_name)
    lines = []
    for line in f:
        lines.append(line.lower())
    return lines


def find_most_frequent_word(data, window_size, keyword):
    most_frequent_window = -3
    count_max = 0
    for i in range(0, len(data), window_size):
        curr_count = 0
        for j in range(i, min(i+window_size, len(data))):
            curr_count += data[j].count(keyword)
            # do all the counting here
        if count_max < curr_count:
            count_max = curr_count
            most_frequent_window = i+2

    return most_frequent_window


if __name__ == "__main__":
    file_data = open_file("data.txt")
    print(find_most_frequent_word(file_data, 5, "vaccine efficacy"))
