def length_of_last_word(s):
    s_striped = s.strip()
    last_space_index = s_striped.rfind(' ')
    return len(s_striped)- (last_space_index + 1)
