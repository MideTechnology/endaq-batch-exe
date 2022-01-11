import glob
import os
import inspect

import fire
import ebmlite.core
import endaq.batch


def self_path():
    """Get the current working directory for this file."""
    locally_defined_obj = lambda: None
    return os.path.abspath(inspect.getsourcefile(locally_defined_obj))


ebmlite.core.SCHEMA_PATH.append(os.path.dirname(self_path()))


class CliGetDataBuilder(endaq.batch.GetDataBuilder):
    def aggregate_data(self, *file_patterns):
        """
        Compile configured data from the given files into a dataframe.

        :param filenames: a sequence of unix-style file patterns that match
            recording files to process
        """
        filenames = [
            filename
            for file_pattern in file_patterns
            for filename in glob.iglob(file_pattern, recursive=True)
        ]

        return super().aggregate_data(filenames)


if __name__ == "__main__":
    fire.Fire(CliGetDataBuilder)
