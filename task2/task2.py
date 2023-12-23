import argparse

def read_circle(file_path):
    with open(file_path, 'r') as file:
        radius = float(file.readline().strip())
        x, y = map(float, file.readline().strip().split())
    return x, y, radius

def read_points(file_path):
    with open(file_path, 'r') as file:
        points = [tuple(map(float, line.strip().split())) for line in file]
    return points

def find_positions(x, y, radius, point_x, point_y):
    distance = (point_x - x)**2 + (point_y - y)**2
    if distance < radius**2:
        return "точка внутри"
    elif distance == radius**2:
        return "точка лежит на окружности"
    else:
        return "точка снаружи"

def main():
    parser = argparse.ArgumentParser(description='Process circle and point data.')
    parser.add_argument('circle_file', help='File with circle data')
    parser.add_argument('point_file', help='File with point data')
    args = parser.parse_args()

    x, y, radius = read_circle(args.circle_file)
    points = read_points(args.point_file)

    for point in points:
        result = find_positions(x, y, radius, *point)
        print(result)

if __name__ == "__main__":
    main()
