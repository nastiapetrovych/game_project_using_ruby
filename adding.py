field = """...............
...............
.....o.........
.....oo........
....ooo........
.....o.........
.......xxxx....
.......xxxx....
.......xxxx....
..............."""

# ..*
# ***

figures = [
    "..****\n...**.",
    "..*\n***",
    "*\n*"
]


def convert_str_field_into_list(field: str) -> list:
    return [[val for val in row] for row in field.lower().split("\n")]


def convert_list_field_into_str(field: list) -> str:
    return "\n".join(["".join(row) for row in field])


def find_all_player_points(field: str, player: int) -> list:
    player = "x" if player == 1 else "o"
    field = convert_str_field_into_list(field)
    points = []
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == player:
                points.append((i, j))

    return points


def filter_extreme_points(field: str, points: list) -> list:
    field = convert_str_field_into_list(field)
    available_points = []

    for x, y in points:
        neighbors = []
        for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            try:
                if i >= 0 and j >= 0:
                    neighbors.append(field[i][j])
            except IndexError:
                pass

        if neighbors.count(".") > 0:
            available_points.append((x, y))

    return available_points


def get_figure_points(figure: str) -> list:
    figure = convert_str_field_into_list(figure)
    points = []

    for i in range(len(figure)):
        for j in range(len(figure[0])):
            if figure[i][j] == "*":
                points.append((i, j))

    return points


def is_correct_step_for_figure(field: str, figure: str, field_point: tuple, fig_point: tuple, player: int):
    new_field = convert_str_field_into_list(field)
    figure = convert_str_field_into_list(figure)
    player = "x" if player == 1 else "o"

    start_x, start_y = field_point[0] - fig_point[0], field_point[1] - fig_point[1]
    if start_x < 0 or start_y < 0:
        return None

    try:
        for i1, i2 in zip(range(start_x, start_x + len(figure)), range(len(figure))):
            for j1, j2 in zip(range(start_y, start_y + len(figure[0])), range(len(figure[0]))):
                new_field[i1][j1] = figure[i2][j2].replace("*", player)

        new_field = convert_list_field_into_str(new_field)
        opponent = "o" if player == "x" else "x"

        if (field.count(opponent) != new_field.count(opponent) or
                new_field.count(player) != field.count(player) + convert_list_field_into_str(figure).count("*") - 1):
            return None

    except IndexError:
        return None

    return new_field


def main(player: int):
    correct_attempts = []

    figure = figures[1]   # index of the figure!!!
    points = filter_extreme_points(field, find_all_player_points(field, player))
    stars = get_figure_points(figure)

    for point in points:
        for star in stars:
            result = is_correct_step_for_figure(field, figure, point, star, player)
            if result is not None:
                correct_attempts.append((point[0] - star[0], point[1] - star[1]))
                print(result)
                print()

    return correct_attempts


main(0)



