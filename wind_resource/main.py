import numpy as np
from octue import analysis


def run_app():
    """ A function that does some analysis, and saves the result to a data file.
    Can be a legacy module - note the complete lack of octue dependencies.
    """

    # Get the relevant files in each data set, sorted in sequence
    met_mast_data = analysis.input_manifest.from_dataset(
        method='name_icontains',
        filter_value='met'
    )
    lidar_data = analysis.input_manifest.from_dataset(
        method='name_icontains',
        filter_value='lidar'
    )
    print('There are ', len(lidar_data.files), 'files in the lidar dataset.')
    print('There are ', len(met_mast_data.files), 'files in the met mast dataset.')
    scan_files = lidar_data.get_file_sequence(
        method='name_endswith',
        filter_value='.scn'
    )
    mast_csv_files = met_mast_data.get_file_sequence(
        method='name_endswith',
        filter_value='.csv'
    )
    print('There are', len(scan_files), ' scan files from the lidar, sorted sequentially')
    print('There are', len(mast_csv_files), ' csv files from the met mast, sorted in sequentially')
