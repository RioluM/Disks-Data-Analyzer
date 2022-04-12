
def count_disks_per_datacenter(datacenter_occurrence):
    return {datacenter: datacenter_occurrence.count(datacenter) for datacenter in set(datacenter_occurrence)}


def convert_to_days(seconds):
    return int(seconds/60/60/24)


def calculate_datacenters_age_avg(datacenter_age_sum, datacenter_quantity):
    return {datacenter: convert_to_days(datacenter_age_sum[datacenter] / datacenter_quantity[datacenter])
            for datacenter in datacenter_quantity}


def get_broken_disks(data_separated):
    return {disk_row[2]: int(disk_row[7]) + int(disk_row[8])
            for disk_row in data_separated
            if int(disk_row[7]) > 0 or int(disk_row[8]) > 0}


with open("data.raw", "r") as f:
    data = f.readlines()
data_separated = [row.replace("\n", "").split(";") for row in data]

# 1
print(f"Total disks: {len(data_separated)}")
datacenter_occurrence = [disk_row[0] for disk_row in data_separated]
datacenter_quantity = count_disks_per_datacenter(datacenter_occurrence)
print(f"Disks in every datacenter: {datacenter_quantity}")

# 2
age_occurrence = [int(disk_row[3]) for disk_row in data_separated]
min_age = min(age_occurrence)
youngest_disk_index = age_occurrence.index(min_age)
max_age = max(age_occurrence)
oldest_disk_index = age_occurrence.index(max_age)
print(f"Youngest disk: {data_separated[youngest_disk_index][2]}, "
      f"age: {convert_to_days(min_age)}. "
      f"Oldest disk: {data_separated[oldest_disk_index][2]}, "
      f"age: {convert_to_days(max_age)}")

# 3
datacenter_age_sum = {datacenter: 0 for datacenter in datacenter_quantity}
for disk_row in data_separated:
    datacenter_age_sum[disk_row[0]] += int(disk_row[3])
datacenters_age_avg = calculate_datacenters_age_avg(datacenter_age_sum, datacenter_quantity)
print(f"Disk age per datacenter: {datacenters_age_avg}")

# 4
read_averages = [int(disk_row[4])/int(disk_row[3]) for disk_row in data_separated]
write_averages = [int(disk_row[5])/int(disk_row[3]) for disk_row in data_separated]
print(f"IO/s disks read average {sum(read_averages)/len(data_separated)}")
print(f"IO/s disks write average {sum(write_averages)/len(data_separated)}")

# 5
io_average = list(map(lambda x, y: x+y, read_averages, write_averages))
io_average = [[io_average[disk_index], data_separated[disk_index][2]] for disk_index in range(len(io_average))]
io_average.sort(key=lambda x: x[0])
print("Top 5 lowest average IO/s:")
[print(disk_average[0], disk_average[1]) for disk_average in io_average[:5]]
print("Top 5 highest average IO/s:")
[print(disk_average[0], disk_average[1]) for disk_average in io_average[-5:]]

# 6
broken_disks = get_broken_disks(data_separated)
print(f"Broken disks and number of errors: {broken_disks}")

