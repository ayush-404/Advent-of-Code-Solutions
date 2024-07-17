checks = [
    "seeds:",
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]

with open('input.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        if line.strip() in checks:
            checks.find(line.strip())