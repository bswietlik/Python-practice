# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}


# test function by updating damages for float
def updated_damages(lst):
    float_damages = []
    for damage in lst:
        if damage[-1] == "B":
            float_damages.append(float(damage.strip("B")) * 1000000000)
        elif damage[-1] == "M":
            float_damages.append(float(damage.strip("M")) * 1000000)
        else:
            float_damages.append(damage)
    return float_damages


float_damages=updated_damages(damages)

# Dictionary : key is name of hurricane, value is name and other information
def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i],
                                'Max Sustained Wind': max_sustained_winds[i],
                                'Areas Affected': areas_affected[i],
                                'Damage': float_damages[i], 'Death': deaths[i]}
    return hurricanes


hurricanes = hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, deaths)


# print(hurricanes["Bahamas"])


# 4. Convert dictionary with hurricane name as key to a new dictionary with hurricane year as the key and return new dictionary.
def hurricane_by_year_dictionary(year):
    hurricane_by_year = []
    for name in hurricanes:
        if hurricanes[name]['Year'] == year:
            hurricane_by_year.append(hurricanes[name])
    return hurricane_by_year


# print(hurricane_by_year_dictionary(1932))
# print(hurricane_by_year_dictionary(2018))

# function that counts how often each area is listed as an affected area of a hurricane.

areas_affected = {}


def count_affected_areas(hurricanes):
    for name in hurricanes:
        for area in hurricanes[name]['Areas Affected']:
            if area in areas_affected:
                areas_affected[area] += 1
            else:
                areas_affected[area] = 1
    return areas_affected


print(count_affected_areas(hurricanes))


# function that find the area affected by the most hurricane

def find_area_affected(areas_affected):
    max_area = ""
    max_area_count = 0
    for area in areas_affected:
        if max_area_count < areas_affected[area]:
            max_area = area
            max_area_count = areas_affected[area]
    return max_area, max_area_count


max_area, max_area_count = find_area_affected(areas_affected)
print(max_area, max_area_count)


# Find the highest mortality hurricane and the number of deaths it caused.
def find_max_mortality(hurricanes):
    max_mortality_cane = ""
    max_mortality = 0
    for hurricane in hurricanes:
        if hurricanes[hurricane]['Death'] > max_mortality:
            max_mortality_cane = hurricane
            max_mortality = hurricanes[hurricane]['Death']
    return max_mortality, max_mortality_cane


max_mortality_cane, max_mortality = find_max_mortality(hurricanes)
print(max_mortality_cane, max_mortality)

# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}


def create_mortality_rating(hurricanes):
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: []}
    for hurricane in hurricanes:
        deaths = hurricanes[hurricane]['Death']
        if deaths > 0 and deaths <= 100:
            hurricanes_by_mortality[0].append(hurricanes[hurricane]["Name"])
        elif deaths > 100 and deaths <= 500:
            hurricanes_by_mortality[1].append(hurricanes[hurricane]["Name"])
        elif deaths > 500 and deaths <= 1000:
            hurricanes_by_mortality[2].append(hurricanes[hurricane]["Name"])
        elif deaths > 1000 and deaths <= 10000:
            hurricanes_by_mortality[3].append(hurricanes[hurricane]["Name"])
        else:
            hurricanes_by_mortality[4].append(hurricanes[hurricane]["Name"])
    return hurricanes_by_mortality


mortality_rating = create_mortality_rating(hurricanes)
print(mortality_rating)

# 8 Calculating Hurricane Maximum Damage
def find_max_damages(hurricanes):
  max_damages_hurricane = ""
  max_damages = 0
  for hurricane in hurricanes:
      if hurricanes[hurricane]['Damage'] == 'Damages not recorded':
        continue
      if hurricanes[hurricane]['Damage'] > max_damages:
          max_damages_hurricane = hurricane
          max_damages = hurricanes[hurricane]['Damage']
  return max_damages_hurricane, max_damages

max_damages_hurricane, max_damages=find_max_damages(hurricanes)
print(max_damages_hurricane, max_damages)