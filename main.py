import glob

import fire
import endaq.batch


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
