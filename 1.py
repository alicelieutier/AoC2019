import sys

def get_lines_as_number(filename):
    f = open(filename)
    return [int(line.strip()) for line in f.readlines()]

def fuel_from_mass(mass):
    return mass // 3 - 2

def sum_fuel_from_masses(masses, callback):
    return sum((callback(mass) for mass in masses))

# part 2
def total_fuel_from_mass(mass):
    total_fuel = 0
    fuel = fuel_from_mass(mass)
    while fuel > 0:
        total_fuel += fuel
        fuel = fuel_from_mass(fuel)
    return total_fuel

if len(sys.argv) > 1:
    # part 1
    masses = get_lines_as_number(sys.argv[1])
    print(sum_fuel_from_masses(masses, fuel_from_mass))

    # part 2
    print(sum_fuel_from_masses(masses, total_fuel_from_mass))


# tests 
if __name__ == "__main__":
    # part 1
    assert(fuel_from_mass(12) == 2)
    assert(fuel_from_mass(14) == 2)
    assert(fuel_from_mass(1969) == 654)
    assert(fuel_from_mass(100756) == 33583)

    # 2 + 2 + 654 + 33583 = 34241
    test_masses = [12,14,1969,100756]
    assert(sum_fuel_from_masses(test_masses, fuel_from_mass) == 34241)

    # part 2
    assert(total_fuel_from_mass(14) == 2)
    assert(total_fuel_from_mass(1969) == 966)
    assert(total_fuel_from_mass(100756) == 50346)
    