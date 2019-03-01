from octue import octue_app, analysis
import wind_resource
import os, sys


@octue_app.command()
def run():
    """ Runs the application
    """
    wind_resource.run_app()


@octue_app.command()
def version():
    """ Returns the version number of the application
    """

    # Top Tip:
    # For all Octue internal apps, we simply return the git revision of the code.
    # Every single commit creates a new version, we can always check out the exact version of the code that ran, and we
    # can quickly look up the version state and history on github when we have to debug an app. Sweet!
    version_no = os.system('git rev-parse HEAD')

    # Return the version number as a string
    return version_no


# If running from an IDE or test console, you won't be using the command line... just run this file
if __name__ == '__main__':

    # Manual setup
    data_dir = sys.argv[2] if len(sys.argv) > 1 else 'example_data'
    print(data_dir)
    analysis.setup(
        id=None,
        data_dir=data_dir
    )
    # TODO use the clicks test runner to actually invoke run() insead of duplicating the code in run()
    wind_resource.run_app()
