f = open('input','r+')

seeds = list(f.readline().split())
seeds.pop(0)
print("Seeds are", seeds)

locations = []

file = f.readlines()


for seed in seeds:
    print("=== Seed", seed)
    source = int(seed)
    dest = int(seed)
    for line in file:
        if line != "\n":
            # print(line.split())

            if "map:" in line:
                source = dest
                # print("Source is now", dest)
            else:
                dest_id, source_id, conv_range = [int(value) for value in line.split()]
                if source_id <= source and source_id+conv_range > source:
                    # print("Almanach line is ", line.split())
                    dest = source + (dest_id-source_id)
    # print("Destination is", dest)
    locations.append(dest)

print("locations are", locations)
print("Min location =", min(locations))