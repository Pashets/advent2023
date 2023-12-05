import re
from collections import defaultdict


def parse(rows):
    is_seeds = True
    is_seed_to_soil = False
    is_soil_to_fertilizer = False
    is_fertilizer_to_water = False
    is_water_to_light = False
    is_light_to_temperature = False
    is_temperature_to_humidity = False
    is_humidity_to_location = False
    seeds = []
    seed_to_soil = defaultdict(range)
    soil_to_fertilizer = defaultdict(range)
    fertilizer_to_water = defaultdict(range)
    water_to_light = defaultdict(range)
    light_to_temperature = defaultdict(range)
    temperature_to_humidity = defaultdict(range)
    humidity_to_location = defaultdict(range)

    def check_and_change(check, change, row):
        if check:
            destination, source, range_len = map(int, row.split())
            change[range(source, source + range_len)] = (
                range(destination, destination + range_len)
            )

    for row in rows:
        if row == '\n':
            is_seeds = False
            is_seed_to_soil = False
            is_soil_to_fertilizer = False
            is_fertilizer_to_water = False
            is_water_to_light = False
            is_light_to_temperature = False
            is_temperature_to_humidity = False
            is_humidity_to_location = False
        if 'seed-to-soil map:' in row:
            is_seed_to_soil = True
            continue
        if 'soil-to-fertilizer map:' in row:
            is_soil_to_fertilizer = True
            continue
        if 'fertilizer-to-water map:' in row:
            is_fertilizer_to_water = True
            continue
        if 'water-to-light map' in row:
            is_water_to_light = True
            continue
        if 'light-to-temperature' in row:
            is_light_to_temperature = True
            continue
        if 'temperature-to-humidity' in row:
            is_temperature_to_humidity = True
            continue
        if 'humidity-to-location' in row:
            is_humidity_to_location = True
            continue
        if is_seeds:
            seeds = [*map(int, re.findall(r'\d+', row.split(':')[1]))]
        check_and_change(is_seed_to_soil, seed_to_soil, row)
        check_and_change(is_soil_to_fertilizer, soil_to_fertilizer, row)
        check_and_change(is_fertilizer_to_water, fertilizer_to_water, row)
        check_and_change(is_water_to_light, water_to_light, row)
        check_and_change(is_light_to_temperature, light_to_temperature, row)
        check_and_change(is_temperature_to_humidity, temperature_to_humidity,
                         row)
        check_and_change(is_humidity_to_location, humidity_to_location, row)
    return seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location


def get_destination(range_map, source):
    for src_range in range_map:
        if src_range.start <= source < src_range.stop:
            return range_map[src_range].start + source - src_range.start
    return source


def get_range_source(sort_ranges, source):
    for src_range in sort_ranges:
        if src_range.start <= source < src_range.stop:
            return src_range
    if source < sort_ranges[0].start:
        return range(0, sort_ranges[0].start)
    if source >= sort_ranges[-1].stop:
        return range(sort_ranges[-1].stop, source)
    for range_index in range(1, len(sort_ranges)):
        if (
                sort_ranges[range_index - 1].stop <=
                source <
                sort_ranges[range_index].start
        ):
            return range(
                sort_ranges[range_index - 1].stop,
                sort_ranges[range_index].start
            )


def task_1(rows):
    seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = parse(
        rows
    )

    locations = []
    for seed in seeds:
        soil = get_destination(seed_to_soil, seed)
        fertilizer = get_destination(soil_to_fertilizer, soil)
        water = get_destination(fertilizer_to_water, fertilizer)
        light = get_destination(water_to_light, water)
        temperature = get_destination(light_to_temperature, light)
        humidity = get_destination(temperature_to_humidity, temperature)
        location = get_destination(humidity_to_location, humidity)
        locations.append(location)
    return sorted(locations)[0]


def sorted_ranges(ranges):
    return sorted(list(ranges), key=lambda i: i.start)


def get_ranges_for_range(range_map, range_source):
    ranges = sorted_ranges(range_map)
    range_for_start = get_range_source(ranges, range_source.start)
    destination_ranges = [range(range_source.start, range_for_start.stop)]
    range_for_end = get_range_source(ranges, range_source.stop - 1)
    if range_for_end == range_for_start:
        return [range_source]
    destination_ranges.append(range(range_for_end.start, range_source.stop))
    if range_for_end.start == range_for_start.stop:
        return destination_ranges
    else:
        range_source = range(range_for_start.stop, range_for_end.start)
        destination_ranges.extend(get_ranges_for_range(ranges, range_source))
        return sorted_ranges(set(destination_ranges))


def get_destination_ranges(range_map, source_ranges):
    split_source_ranges = []
    for source_range in source_ranges:
        split_source_ranges.extend(
            get_ranges_for_range(range_map, source_range)
        )
    destination_ranges = sorted_ranges([
        range(
            get_destination(range_map, split_source_range.start),
            get_destination(range_map, split_source_range.stop - 1)
        ) for split_source_range in split_source_ranges
    ])
    return destination_ranges


def task_2(rows):
    seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = parse(
        rows
    )
    seeds_ranges = []
    for i in range(0, len(seeds), 2):
        seeds_ranges.append(range(seeds[i], seeds[i] + seeds[i + 1]))
    min_locations = []
    for seeds_range in seeds_ranges:
        seed_ranges = get_ranges_for_range(seed_to_soil, seeds_range)
        soil_ranges = sorted_ranges([
            range(
                get_destination(seed_to_soil, source_range.start),
                get_destination(seed_to_soil, source_range.stop - 1)
            ) for source_range in seed_ranges
        ])
        fertilizer_ranges = get_destination_ranges(
            soil_to_fertilizer, soil_ranges
        )
        water_ranges = get_destination_ranges(
            fertilizer_to_water, fertilizer_ranges
        )
        light_ranges = get_destination_ranges(
            water_to_light, water_ranges
        )
        temperature_ranges = get_destination_ranges(
            light_to_temperature, light_ranges
        )
        humidity_ranges = get_destination_ranges(
            temperature_to_humidity, temperature_ranges
        )
        location_ranges = get_destination_ranges(
            humidity_to_location, humidity_ranges
        )
        location_ranges = sorted_ranges(location_ranges)
        min_locations.append(location_ranges[0].start)
    return sorted(min_locations)[0]


with open('input.txt') as f:
    lines = f.readlines()
    print(task_1(lines))
    print(task_2(lines))
