import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': './chicago.csv',
              'new york city': './new_york_city.csv',
              'washington': './washington.csv' }

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
    while True:
        city = str(input('Chicago - New York City - Washington\nEnter the City: ')).lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('--- INVALID CHOICE ---\nPlease follow the above mentioned criteria.')
            continue
        else:
            break
    
# TO DO: get user input for month (all, january, february, ... , june)
    while True:
        print('Jan - Feb - Mar -  ... etc.')
        month = str(input('Enter first 3 letters of a month or \'all\': ')).lower()
        
        if month not in ('jan','feb', 'mar', 'apr', 'may' ,'jun', 'all'):
            print('--- INVALID CHOICE ---\nPlease follow the above mentioned criteria.')
            continue
        else:
            break

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday) 
    while True:
        print('Sat - Sun - Mon -  ... etc.')
        day = str(input('Enter first 3 letters of a weekday or \'all\': ')).lower()
        
        if day not in ('sun','mon', 'tue', 'wed', 'thu' ,'fri', 'sat','all'):
            print('--- INVALID CHOICE ---\nPlease follow the above mentioned criteria.')
            continue
        else:
            break   
       
        print('{},{} & {} are your choices'.format(city,month,day))
    
    print('-'*40)
    return city, month, day

#TestHere# city, month, day = get_filters()

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
    
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['Months']= df['Start Time'].dt.month
    df['Days']= df['Start Time'].dt.day_name().str.lower().map(lambda x: str(x)[0:3])
    
    if month != 'all':
        mth_lst = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = mth_lst.index(month)+1
        df = df[df['Months'] == month]
    
    if day != 'all':
        df = df[df['Days'] == day]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("Most Common Month: ", df['Months'].mode()[0])

    # display the most common day of week
    print("Most Common Day: ", df['Days'].mode()[0].title())

    # display the most common start hour
    x = df['Start Time'].dt.hour.mode()[0]
    if x == 12:
        print("Most Common Start Hour: 12 PM")
    elif x > 12:
        x -= 12
        print("Most Common Start Hour: ", x," PM")
    else:
        print("Most Common Start Hour: ", df['Start Time'].dt.hour.mode()[0], ' AM')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most Common Start Station: ", df['Start Station'].mode()[0])


    # display most commonly used end station
    print("Most Common End Station: ", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " to " + df['End Station']
    print("Most Common Trips: from", df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['totaltraveltime']= pd.to_datetime(df['End Time'])-pd.to_datetime(df['Start Time'])
    print('Total Travel Time: ', df['totaltraveltime'].sum())

    # display mean travel time
    print('Average Trip Time: ', df['totaltraveltime'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Count of User Types: ', df['User Type'].nunique(), ' Categories')
    print(df['User Type'].value_counts().to_string())

    # Display counts of gender
    print('\nGender Count: ', df['Gender'].nunique(), ' Categories')
    print(df['Gender'].value_counts().to_string())

    # Display earliest, most recent, and most common year of birth
    earliest, recent, common = df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode()[0]
    print("\nRegarding birth years of users ... \n \n{} is the earliest \n{} is the most recent \n{} is the most common".format(int(earliest),int(recent),int(common)))

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()