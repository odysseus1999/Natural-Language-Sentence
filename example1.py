import geograpy
url='https://en.wikipedia.org/wiki/2012_Summer_Olympics_torch_relay'
places = geograpy.get_geoPlace_context(url = url)
print(places)


#UPDATED

# import geograpy
# import pandas as pd

# url = 'https://en.wikipedia.org/wiki/2012_Summer_Olympics_torch_relay'
# places = geograpy.get_geoPlace_context(url=url)

# # Extracting data into lists
# countries = places.countries if places.countries else []
# regions = places.regions if places.regions else []
# cities = places.cities if places.cities else []
# other = places.other if places.other else []

# # Ensure all lists have the same length by padding with empty strings
# max_length = max(len(countries), len(regions), len(cities), len(other))
# countries += [''] * (max_length - len(countries))
# regions += [''] * (max_length - len(regions))
# cities += [''] * (max_length - len(cities))
# other += [''] * (max_length - len(other))

# # Create DataFrame
# data = {
#     'Countries': countries,
#     'Regions': regions,
#     'Cities': cities,
#     'Other': other
# }
# df = pd.DataFrame(data)

# # Export to Excel
# excel_file = 'geography_places.xlsx'
# df.to_excel(excel_file, index=False)
# print(f"Data exported to {excel_file}")
