"""
Bikeshare Data Analysis Script
This script allows users to explore US bikeshare data for Chicago, New York City, and Washington.
Users can filter data by city, month, and day of the week, and view various statistics. 
"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def display_raw_data(df):
    """
    Displays raw data 5 rows at a time upon user request.
    It will give options to continue viewing more data until the user opts out.
    """
    row_index = 0

    while True:
        show_data = input(
            "\nWould you like to see 5 lines of raw data? Enter yes or no: "
        ).strip().lower()

        if show_data != 'yes':
            break

        if row_index >= len(df):
            print("\nNo more raw data to display.")
            break

        print(df.iloc[row_index:row_index + 5])
        row_index += 5

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Get city
    while True:
        city = input(
            "Enter city (Chicago, New York City, Washington): "
        ).strip().lower()

        if city in CITY_DATA:
            break
        else:
            print("❌ Invalid city. Please try again.")

    # TO DO: get user input for month (all, january, february, ... , june)
    # Get month
    # check if month is valid or not
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input(
            "Enter month (all, January, February, ... June): "
        ).strip().lower()

        if month in months:
            break
        else:
            print("❌ Invalid month. Please try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Get day
    # check if day is valid or not
    days = ['all', 'monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input(
            "Enter day (all, Monday, Tuesday, ... Sunday): "
        ).strip().lower()

        if day in days:
            break
        else:
            print("❌ Invalid day. Please try again.")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # Convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # Filter by month
    if month != 'all':
        month_index = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['month'] == month_index]
     # Filter by day
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most Common Month:", df['month'].mode()[0])
    
    # TO DO: display the most common day of week
    print("Most Common Day of Week:", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("Most Common Start Hour:", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most Common Start Station:", df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print("Most Common End Station:", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + " -> " + df['End Station']
    print("Most Frequent Trip:", df['trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Travel Time:", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Mean Travel Time:", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nUser Types:")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("\nGender:")
        print(df['Gender'].value_counts())
    else:
        print("\nGender data not available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("\nEarliest Birth Year:", int(df['Birth Year'].min()))
        print("Most Recent Birth Year:", int(df['Birth Year'].max()))
        print("Most Common Birth Year:", int(df['Birth Year'].mode()[0]))
    else:
        print("\nBirth Year data not available.")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        pd.set_option('display.max_columns', None)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
