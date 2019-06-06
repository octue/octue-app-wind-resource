import pandas as pd
from octue import analysis


def get_input_dataframe(file_sequence):
    """ Creates a pandas dataframe for our input met mast dataset
    """
    df_from_each_file = []
    for file in file_sequence:

        # TODO @thclark Update the manifest to include the file path, and unbotch this
        # TODO @thclark putting this as an inline creates a generator for reduced meory usage

        full_file_name = '{}/set-orec-metmast/SALE Project met mast/{}'.format(analysis.input_dir, file.data_file['name'])
        print('Reading CSV file:', full_file_name)
        data = pd.read_csv(full_file_name)
        df_from_each_file.append(data)

    df = pd.concat(df_from_each_file, ignore_index=True)

    return df
