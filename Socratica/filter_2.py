# Map, Filter, and Reduce Functions
# Filter

# Remove missing data

countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "", "Ecuador", "", "", "Venezuela"]

print(list(filter(None, countries)))

# False values
# "", 0, 0.0, 0j, [], (), {}, False, None, instances which signal they are empty
