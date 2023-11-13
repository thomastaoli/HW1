#Thomas Li
#10/04/2023
#Homework 2

from datetime import datetime

#Ask User's Birth Date
birth_date_str = input("When was your birth date? (YYYY-MM-DD): ")

# Convert the string into a datetime
birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
current_date = datetime.now() 
if birth_date >= datetime.now():
    print("You seem to have entered a birth date in the future. Please try again.")
else:
    age_years = current_date.year - birth_date.year

# Calculate the difference between today and user's birth date
age_days = (current_date - birth_date).days

# Adjust the age if the birthday hasn't come yet this year
if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
    age_years -= 1

# Calculate heartbeats
human_heartbeats = age_days * 100000
blue_whale_heartbeats = age_days * 47520
rabbit_heartbeats = age_days * 194400

# If heartbeats if over a billion
if rabbit_heartbeats >= 1e9:
    rabbit_heartbeats_str = "{:.3f} billion".format(rabbit_heartbeats / 1e9)
else:
    rabbit_heartbeats_str = "{:,}".format(rabbit_heartbeats)

# Determine if the user is older, younger, or the same age as me
age_comparison = "the same age as"
years_difference = 22 - age_years
if age_years < 22:
    age_comparison = "younger than"
elif age_years > 22:
    age_comparison = "older than"

# Determine if the birth year is even or odd
even_or_odd = "even" if birth_date.year % 2 == 0 else "odd"

# Count Democratic presidents in office since birth
presidents = {
    1977: "Jimmy Carter",
    1981: "Ronald Reagan",
    1989: "George H. W. Bush",
    1993: "Bill Clinton",
    2001: "George W. Bush",
    2009: "Barack Obama",
    2017: "Donald Trump",
    2021: "Joe Biden",
}

democratic_presidents = {
    "Jimmy Carter": 1977,
    "Bill Clinton": 1993,
    "Barack Obama": 2009,
    "Joe Biden": 2021,
}

def count_dem_presidents(year):
    count = 0
    for term_year in democratic_presidents.values():
        if year <= term_year <= current_date.year:
            count += 1
    return count

dem_presidents_count = count_dem_presidents(birth_date.year)

# Determine which president was in office when the user was born
def president_when_born(year):
    for term_year, president in sorted(presidents.items(), reverse=True):
        if year >= term_year:
            return president
    return "Not available"

president_at_birth = president_when_born(birth_date.year)

# Print results
print(f"You are {age_years} years old.")
print(f"You have been alive for {age_days} days.")
print(f"Your heart has beaten approximately {human_heartbeats:,} times.")
print(f"A blue whale's heart would have beaten approximately {blue_whale_heartbeats:,} times.")
print(f"A rabbit's heart would have beaten approximately {rabbit_heartbeats_str} times.")
print(f"You are {age_comparison} me. Congratulations! We're young.")
if age_years != 22:
    print(f"That's a {abs(years_difference)} year difference.")
print(f"You were born in an {even_or_odd} year.")
print(f"There have been {dem_presidents_count} Democratic presidents in office since you were born.")
print(f"The U.S. President in office when you were born was {president_at_birth}.")

#Question 5: Other ways to display numbers
# 1. Use +
# print('You are ' + str(age_years) + ' years old.')
# Pro: Easier for beginners. Con: You must manually convert numbers to strings.

#Question 7
#democratic_presidents_start_years = [1977, 1993, 2009, 2021]
#def count_dem_presidents_since_birth(birth_year):
    #return sum(birth_year <= term_start_year <= datetime.now().year for term_start_year in democratic_presidents_start_years)
#dem_presidents_count = count_dem_presidents_since_birth(birth_date.year)