file = open('input','r+')
seeds = list(file.readline().split())
seeds.pop(0)
print("Seeds are", seeds)
locations = []
almanach = file.readlines()

for seed in seeds:
    # OK, pour la 2eme deuxième on voit bien que l'ordre de grandeur de cette liste est en
    # roue libre. est-ce qu'il faut faire pareil avec des plages ?
    # Oskour

    print("- Seed", seed)
    source = int(seed)
    dest = int(seed)
    for line in almanach:
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