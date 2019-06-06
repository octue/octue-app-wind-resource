

def wind_speed_comparison():
    """ Reproduce Table 3 and Figure 5 from Westerhellweg.
    NB in our case we only have two rows in the table, as there are only two heights

    Inputs:
        - Averaged wind speeds from cups, at both heights
        - Averaged wind speeds from LiDAR, taken at the two cup heights

    Procedure - see paper Westerhellweg

    Outputs:
        - Save table to csv or print() results
        - Plot figure

    """

    # Table 3 -
    pass


def wind_direction_comparison():
    """ Reproduce Table 5 and Figure 9 from Westerhellweg
    NB in our case we have only one height because there's only one wind vane on the mast

    Inputs:
        - Averaged wind direction from mast vanes
        - Averaged wind directions from LiDAR, at the height of the vanes

    Procedure: - see paper westerhellweg

    Outputs:
        - Save table to CSV or print() results
        - Plot figure

    """
    pass


def standard_deviation_iec_error():
    """ Get the pink error curve from Westerhellewg Figure 6, gives us a lookup table to compare

    Inputs:
        - Cup type and height, boom length
        - Average wind speeds at which to assess error, e.g. [1, 2, 3, 4, 5, 6, 7 ..., 25]

    Procedure:
        - Find IEC61400-121 for the procedure
        - Save the file if you can (don't commit to repository - just email it!)

    Outputs:
        - [25 x 2] max and min error bounds for standard deviation of speed measurements from a cup anemomenter

    """
    pass
