import numpy as np
import pandas as pd


def average_wind_direction(mast_input_dataframe, mast_average_dataframe):
    """ Get wind direction from met mast vanes, get mast shadow on itself, add them to mast_average_dataframe

    Inputs:
        - Geometric parameters for vane height and orientation
        - NB Both vanes at same height
        - Window timestamps and indices
                [0 20171106T00:00:00.0000Z,
                 1 20171106T00:10:00.0000Z,
                 2 20171106T00:20:00.0000Z,
                 ... ]
        - WindVane_2 and WindVane_1 signals from the csv data

    Procedure:
        - Split the wind vane data into the windows. For each window, take an average for each windvane.
        - Plot a timeseries for each wind vane to check.
        - Figure out what vane offsets are
        - Correct vanes for offset
        - Determine which vane (A or B) to use (which side of mast is most valid)
        - Combine into a single series of wind direction
        - Plot a timeseries to check. It should be nice and smooth, because the wind doesn't suddenly change direction
        - Return the results

    Outputs:
        - Update column 'average_wind_direction' with 10-minute average wind direction at the height of the vanes, [nWindows x 1]
        - Update column 'mast_side' with which side of met mast should be used (A=true, B=false), [nWindows x 1]

    """
    pass


def wind_speed(mast_input_dataframe, mast_average_dataframe, mast_high_res_dataframe):
    """ Get the high resolution wind speed data for the two heights

    Inputs:
        - High res data (from the input datastore) [nSamples x ...] with timestamps and data from anemometers 1-4
        - 'mast_side' column with which side of met mast should be used (A=true, B=false), [nWindows x 1]

    Procedure:
        - Use the A/B direction array to look up, for each entry in the high res input, which side of the mast to use A or B
        - Merge from the two sides of the mast into a single wind speed timeseries from each eight, selecting from each side of the mast based on A/B
        - Plot a timeseries to check. It should be nice and smooth, because the wind doesn't suddenly change direction.
            Plot only for a day at a time, because the whole timeseries will probably crash your computer.
            Plot both the inputs and the output so you can see which signal is being used.

    Outputs:
        - Update columns 'wind_speed_upper' and 'wind_speed_lower' in 'mast_high_res_dataframe' with wind speeds [nSamples x 2] where first column is the low height, second column is the high one.

    """
    pass


def average_wind_speed(mast_high_res_dataframe, mast_average_dataframe):
    """ Get the average wind speed for each window at each cup height

    Inputs:
        - High res data (from the input datastore) [nSamples x ...] with timestamps
        - Array of wind speeds [nSamples x 2] where first column is the low height, second column is the high one.
        - Window timestamps and indices
                [0 20171106T00:00:00.0000Z,
                 1 20171106T00:10:00.0000Z,
                 2 20171106T00:20:00.0000Z,
                 ... ]

    Procedure:
        - Similar to the averaging process for wind direction, select samples that occur within a given window and average them
        - Plot full timeseries to check

    Outputs:
        - Update column 'average_wind_speed_upper' and 'average_wind_speed_lower' with  10-minute average wind speeds [nWindows x 2] where first column is the low height, second column is the high one

    """
    pass


def average_wind_speed_filter(mast_average_dataframe, cut_in_speed, cut_out_speed):
    """ Get a boolean array, true where the 10 minute window is valid, false where invalid

    Inputs:
        - Columns 'average_wind_speed_upper' 10-minute average wind speeds [nWindows x 1] from the upper cup
        - Cut in and out speeds in m/s

    Procedure:
        - Use only the high one, because the wind turbine cutin/out will be based on anemometer at hub height
        - If greater than cut out speed, or lower than cutin speed, then output is false, otherwise true
        - Plot on top of wind speed as a timeseries, to check that its true at the right points

    Output:
        - Update column 'average_wind_speed_filter' with Boolean array [nWindows x 1], true where wind speed is in range

    """


def average_wind_direction_filter(mast_average_dataframe, range):
    """ Get a boolean array, true where wind direction is in a specified range

    Inputs:
        - Column 'average_wind_direction' of 10-minute average wind directions [nWindows x 1]
        - Specified range [2 x 1], to get this, look at google maps and determine a direction range where wind comes from offshore and does not go over land.
            (directions from earlsferry to kingshorn ar considered to be 'from offshore')

    Procedure:
        - If wind direction in the given range, the corresponding result is true, otherwise false

    Output:
        - Update column 'average_wind_direction_filter' with Boolean array [nWindows x 1], true where wind speed is in the specified direction range

    """
    pass


def rain_filter():
    """ IGNORE. We're not filtering rain.
    :return:
    """
    pass


def mast_shadow_on_lidar():
    """ IGNORE. Only affects one bin in up to two beams in a conic scan. The lidar analysis is based on a robust fit
     across the vertical profile in addition to the robust VAD fit, so it's very unlikely to be sensitive.
     In addition, the mast is extremely slim (unlike the one on FINO1) so is unlikely to exert a major signature

    """
    pass


def turbulent_intensity(mast_average_dataframe, mast_high_res_dataframe):
    """ Compute turbulent intensity TI for each cup height, in each window. Reproduces the blue curve of Figure 8 in
    Westerhellweg

    Inputs:
        - Columns 'wind_speed_upper' and 'wind_speed_lower' and timestamps from the high_res dataframe
        - Columns 'average_wind_speed_upper' and 'average_wind_speed_lower' and timestamps from the average dataframe

    Procedure:
        - There's got to be a standard method to get TI from wind speed. Probably defined in an IEC standard somewhere, or the Wind Energy Hadbook. Find and do it!
        - Plot the timeseries to check

    Outputs:
        - Update columns 'turbulent_intensity_upper' and 'turbulent_intensity_lower' with turbulent intensity values
    """
    pass


def met_mast_analysis(mast_input_dataframe):
    """ Main function to analyse met mast data

    """

    range = np.array([45, 120])
    cut_in_speed = 3.5
    cut_out_speed = 25

    # Create a data frame to store the window-average data
    mast_average_dataframe = pd.DataFrame(columns=[
        'timestamp',
        'average_wind_direction',
        'mast_side',
        'average_wind_speed_lower',
        'average_wind_speed_upper',
        'average_wind_speed_filter',
        'average_wind_direction_filter',
        'turbulent_intensity_upper',
        'turbulent_intensity_lower',
    ])

    # Create a data frame to store the processed, still high-res, data
    mast_high_res_dataframe = pd.DataFrame(columns=[
        'timestamp',
        'wind_speed_lower',
        'wind_speed_upper',
    ])

    # TODO here, assign timestamps columns from the input dataframe to the high_res one, and create timestamps for the averaged dataframe.
    #  NB google or search stackoverflow for how to make regularly spaced time column in pandas / numpy

    # Compute usable wind direction and speed from raw instruments
    average_wind_direction(mast_input_dataframe, mast_average_dataframe)
    wind_speed(mast_input_dataframe, mast_average_dataframe, mast_high_res_dataframe)
    average_wind_speed(mast_high_res_dataframe, mast_average_dataframe)

    # Compute filters based on our criteria
    average_wind_speed_filter(mast_average_dataframe, cut_in_speed, cut_out_speed)
    average_wind_direction_filter(mast_average_dataframe, range)

    # Report 'counts' i.e. the number of 10 minute windows which are valid. e.g. sum(average_wind_speed_filter() && average_wind_direction_filter())

    # Compute turbulent intensity from the met mast
    turbulent_intensity(mast_average_dataframe, mast_high_res_dataframe)


