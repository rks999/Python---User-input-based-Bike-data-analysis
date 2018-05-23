import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! You can choose between Chicago, New York City and Washington')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Select the city you would like to analyze: ').lower()
        if city.lower() == 'chicago':
            break
        elif city.lower() == "new york city":
            break
        elif city.lower() == "washington":
            break
        else:
            print('That is no valid input. Please mind your spelling!')
            continue
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Select the month you would like to look at! Type in "all"to set no filter: ').lower()
        if month.lower() == 'january':
            break
        elif month.lower() == 'february':
            break
        elif month.lower() == 'march':
            break
        elif month.lower() == 'april':
            break
        elif month.lower() == 'may':
            break
        elif month.lower() == 'june':
            break
        elif month.lower() == 'all':
            break
        else:
            print('That is no valid input. Please mind your spelling!')
            continue
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Select the day you would like to look at! Again, type in "all" to set no filter: ').lower()
        if day.lower() == 'monday':
            break
        elif day.lower() == 'tuesday':
            break
        elif day.lower() == 'wednesday':
            break
        elif day.lower() == 'thursday':
            break
        elif day.lower() == 'friday':
            break
        elif day.lower() == 'saturday':
            break
        elif day.lower() == 'sunday':
            break
        elif day.lower() == 'all':
            break
        else:
            print('That is not a valid input. Please check your spelling!')
            continue

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
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode() [0]
    print('most common month:', common_month)
    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode() [0]
    print('most common day of the week:', common_day_of_week)

    # display the most common start hour
    common_hour = df['hour'].mode() [0]
    print('most common hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode() [0]
    print('most common start station:', common_start)

    # display most commonly used end station [STIMMT SO NOCH NICHT]
    common_end = df['End Station'].mode() [0]
    print('most common end station:', common_end)

    # display most frequent combination of start station and end station trip
    common_trip = (df['Start Station']+df['End Station']).mode()[0]
    print(common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Total travel time: ", total_travel)
    print("mean travel time: ", mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    # Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print(count_gender)
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birthdate = df['Birth Year'].min()
        most_recent_birthdate = df['Birth Year'].max()
        most_common_birthdate = df['Birth Year'].mode()
        print("Earliest birthdate: ", earliest_birthdate)
        print('-'*40)
        print("Most recent birthdate: ", most_recent_birthdate)
        print('-'*40)
        print("Most common birthdate: ", most_common_birthdate)
        print('-'*40)
    print(user_types)
    print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Displays the data used to compute the stats
    Input:
        the dataframe with all the bikeshare data
    Returns:
       none
    """

    #leave out auxiliary columns created for calculation purpose before showing raw data
    df = df.drop(['month', 'day_of_week', 'hour'], axis = 1)

    rowIndex = 0

    showmore = input("\n Would you like to see rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()

    while True:

        if showmore == 'no':
            return

        if showmore == 'yes':
            print(df[rowIndex: rowIndex + 5])
            rowIndex = rowIndex + 5


        showmore = input("\n Would you like to see five more rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
