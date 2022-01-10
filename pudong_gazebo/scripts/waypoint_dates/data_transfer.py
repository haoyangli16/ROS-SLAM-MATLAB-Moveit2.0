import csv


def data_transfer():
    filename = 'data1.csv'
    dates = []
    with open(filename, 'r') as waypoints:
        reader = csv.reader(waypoints)
        for i, row in enumerate(reader):
            dates.append(row)

    joint_value = [0.0, 0.0, 0.0, 0.0]
    joint_value_list = []

    for data in dates:
        for i in range(0, 4):
            joint_value[i] = float(data[i].strip())
        joint_value_transfer = joint_value[:]
        joint_value_list.append(joint_value_transfer)

    print(joint_value_list)


if __name__ == '__main__':
    data_transfer()
