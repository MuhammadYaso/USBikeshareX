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
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Which city data you want to explore? ( chicago - new york city - washington): \n').lower()
            if city in ['chicago','new york city','washington']:
                break
            else:
                print('\nSorry, enter one of the 3 avaliable cities.\n')
        except:
            print('\nSorry, your answer is not valid,Try again!\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('\nDo you want to filter with months?\nIf yes please choose one: ( january - february - march - april - may - june )\nIf no filters needed please type (no) :\n').lower()
            if month in ['january','february','march','april','may','june','no']:
                break
            else:
                print('\nSorry, enter one of the 6 avaliable months.\n')
        except:
            print('\nSorry, your answer is not valid,Try again!\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('\nDo you want to filter with days?\nIf yes please choose one: ( monday - tuesday - wednesday - thursday - friday - saturday - sunday )\nIf no filters needed please type (no):\n').title()
            if day in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','No']:
                break
            else:
                print('\nSorry, check the spelling of your answer.\n')
        except:
            print('\nSorry, your answer is not valid,Try again!\n')

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])  #converting 'Start Time' column to datetime object
    df['Hour'] = df['Start Time'].dt.hour   #creating 'Hour' column out of 'Start Time'
    df['Month'] = df['Start Time'].dt.month   #creating 'Month' column out of 'Start Time'
    df['Day of week'] = df['Start Time'].dt.day_name()   #creating 'Day of week' column out of 'Start Time'

    #filtering by the month depending on user input
    if month != 'no':
        months = ['january','february','march','april','may','june','no']
        month = months.index(month) + 1
        df = df[df['Month']==month]
    #filtering by the day depending on user input
    if day != 'No':
        df = df[df['Day of week']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    x = df['Month'].mode()[0]
    print('The most common month is : {}\n'.format(x))

    # TO DO: display the most common day of week
    y = df['Day of week'].mode()[0]
    print('The most common day of week is : {}\n'.format(y))
    # TO DO: display the most common start hour
    z = df['Hour'].mode()[0]
    print('The most common hour is : {}\n'.format(z))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    x = df['Start Station'].mode()[0]
    print('The most common start station is : {}\n'.format(x))

    # TO DO: display most commonly used end station
    y = df['End Station'].mode()[0]
    print('The most common end station is : {}\n'.format(y))

    # TO DO: display most frequent combination of start station and end station trip
    #filtering by the most common Start Station & saving it in z
    z = df[(df['Start Station'])==(df['Start Station'].mode()[0])]
    #extracting the most common End Station in z & saving it in w
    w = z[(z['End Station'])==(z['End Station'].mode()[0])]['End Station'].mode()[0]

    print('The most common trip is from station ({}) to station ({})\n'.format(x,w))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    x = df['Trip Duration'].sum()
    print('The total time travelled : {}\n'.format(x))

    # TO DO: display mean travel time
    y = df['Trip Duration'].mean()
    print('The Average travel time : {}\n'.format(y))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_type(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    x = df['User Type'].value_counts()
    print('The count of user types:\n {}\n'.format(x))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating more User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of gender
    y = df['Gender'].value_counts()
    print('The count of genders:\n {}\n'.format(y))

    # TO DO: Display earliest, most recent, and most common year of birth
    z = df['Birth Year'].min()
    print('The earlist year of birth is : {}\n'.format(z))
    w = df['Birth Year'].max()
    print('The most recent year of birth is : {}\n'.format(w))
    o = df['Birth Year'].mode()[0]
    print('The most common year of birth is : {}\n'.format(o))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    while True:
        try:
            x = input('\nWould you like to display the first 5 rows of the data? (y/n)\n')
            if x in ['y','n']:
                break
            else:
                print('\nPlease answer with y for yes & n for no!\n')
        except:
            print('\nPlease answer with y for yes & n for no!\n')
    if x == 'y':
        a = 0
        b = 5
        y = 'y'
        while y == 'y':
            print(df.iloc[a:b])
            while True:
                try:
                    y = input('\nWould you like to disply the next 5 rows? (y/n)\n')
                    if y in ['y','n']:
                        break
                    else:
                        print('\nPlease answer with y for yes & n for no!\n')
                except:
                    print('\nPlease answer with y for yes & n for no!\n')
            a += 5
            b += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_type(df)
        if city != 'washington':
            user_stats(df)
        else:
            print('\nWashington city does not provide data for genders & birth year of users\n')
            print('-'*40)

        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
