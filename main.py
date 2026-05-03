game_title = "God of War"
release_year = 2018
platform = "PlayStation 4"

physical_availability = 8
digital_availability = 10
hardware_dependency = 8
documentation = 7
community_activity = 9

total_score = (
    physical_availability
    + digital_availability
    + hardware_dependency 
    + documentation
    + community_activity)

max_score = 50

gpi_score = (total_score / max_score) * 100
risk_level = "Low Risk"

print("Game Preservation Index")
print("-----------------------")
print("Game:", game_title)
print("Year:", release_year)
print("Platform:", platform)
print("GPI Score:", gpi_score, "%")
print("Risk Level:", risk_level)    