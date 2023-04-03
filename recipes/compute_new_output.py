# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
output = dataiku.Dataset("output")
output_df = output.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

new_output_df = output_df # For this sample code, simply copy input to output


# Write recipe outputs
new_output = dataiku.Dataset("new_output")
new_output.write_with_schema(new_output_df)
