# hackerrank problem url
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

clouds = [0, 0, 0, 1, 0, 0]


def jumpingOnClouds(c):
    steps = 0
    curr_position = 0
    while curr_position < len(c)-1:
        curr_pos_plus_2 = (curr_position + 2) % (len(c)-1)
        if c[curr_pos_plus_2] != 1:
            curr_position += 2
            steps += 1
        elif c[curr_pos_plus_2] == 1:
            curr_position += 1
            steps += 1
    return steps


print(jumpingOnClouds(clouds))
