#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    It`s my fucking project, guys!!!!!!!!
"""


def parse_field_info():
    """
    Gives information about field shape
    """
    field_info = input()
    field_info = field_info.split(' ')[1:]
    result = (int(field_info[0]), int(field_info[1][:-1]))
    return result


def parse_field(info_about_field):
    """
    Gives additional information about all figure's rows
    """
    lines_from_file = []
    local_none = input()         # for scope information
    for position in range(info_about_field[0]):
        local_row = input()[4:]
        local_pos = []
        for elements in local_row:
            local_pos.append(elements)
        lines_from_file.append(local_pos)
    return lines_from_file


def parse_figure():
    """
    Parse the figure.

    The function parses the height of the figure (maybe the width would be
    useful as well), and then reads it.
    It would be nice to save it and return for further usage.
    The input may look like this:

    Piece 2 2:
    **
    ..
    """
    info = input()
    height = int(info.split()[1])
    rows = []
    for _ in range(height):
        row = input()
        conclusion_row = []
        for places in range(len(row)):
            conclusion_row.append(row[places])
        rows.append(conclusion_row)
    left_board = len(rows[0])
    right_board = 0
    upper_board = 0
    for row in rows:
        if '*' not in row:
            upper_board += 1
        else:
            break
    rows = rows[upper_board:]
    for row in rows:
        for pos in range(len(row)):
            if '*' in row[pos]:
                left_board = min(left_board, pos)
                right_board = max(right_board, pos)
    rows = [row[left_board:right_board+1] for row in rows]
    conclusion_row = []
    for place in rows:
        if '*' in place:
            conclusion_row.append(place)
    additional_information_about_board = [upper_board, left_board]
    result = [len(conclusion_row), len(conclusion_row[0])] + additional_information_about_board
    return result, conclusion_row


def step(field, info_figure, size, shape_of_figure, player):
    """
    Makes our function work
    """
    height_figure = shape_of_figure[0]
    width_figure = shape_of_figure[1]
    current_height = size[0] + 1
    current_width = size[1] + 1
    additional_pos = shape_of_figure[2]
    additional_width = shape_of_figure[3]
    for rows in range(0, current_height - height_figure):
        for columns in range(0, current_width - width_figure):
            count = 0
            notion = 0
            for row in range(0, height_figure):
                for col in range(0, width_figure):
                    field_position = field[rows + row][columns + col]
                    figure_position = info_figure[row][col]
                    if figure_position != '.':
                        if field_position != '.':
                            if player == 1:
                                letter = 'O'
                            else:
                                letter = 'X'
                            if field_position.upper() == letter:
                                count += 1
                            else:
                                notion = True
                                break
                        else:
                            continue
                if notion:
                    break
            if count == 1 and not notion:
                pos_x = rows - additional_pos
                pos_y = columns - additional_width
                return (pos_x, pos_y)


def move(player: int):
    """
    Concatenate all main function
    """
    field_info = parse_field_info()
    field = parse_field(field_info)
    figure_info = parse_figure()
    figure_size = figure_info[0]
    figure = figure_info[1]
    coordinate = step(field, figure, field_info, figure_size, player)
    if coordinate:
        result = (coordinate[0], coordinate[1])
        return result


def play(player):
    """
    Operates  main action
    """

    while True:
        our_move = move(player)
        try:
            print(*our_move)
        except:
            break


def parse_info_about_player():
    """
    Returns information about player
    """

    i = input()
    return 1 if "p1 :" in i else 2


def main():
    """
    Do all main actions
    """
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        return(None)


if __name__ == "__main__":
    main()
