def count_words_in_line(line, keyword):
    count = 0
    words = line.split()
    for word in words:
        if word == keyword:
            count += 1
    return count


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
