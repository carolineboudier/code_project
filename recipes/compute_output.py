# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.
data={'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}
output_df = pd.DataFrame.from_dict(data, orient='index') # Compute a Pandas dataframe to write into output


# Write recipe outputs
output = dataiku.Dataset("output")
output.write_with_schema(output_df)
