'''
Helper file for running AggregateDeepProfiler
'''

import os
import numpy as np
import pandas as pd

from pycytominer.cyto_utils.DeepProfiler_processing import AggregateDeepProfiler

project_dir = '/local_group_storage/broad_data/michael/training'
experiment = '730_profile'

profile_dir = os.path.join(project_dir, "outputs", experiment, "features")

index_file = os.path.join(project_dir, "inputs", "metadata", "sub_index.csv")

output_folder = os.path.join(project_dir, 'outputs', experiment, 'aggregated')

well_class = AggregateDeepProfiler(
    index_file=index_file,
    profile_dir=profile_dir,
    aggregate_operation="median",
    aggregate_on="well",
    output_file=output_folder,
)
df_well = well_class.aggregate_deep()

df_well.to_csv('/local_group_storage/broad_data/michael/730_aggregated_median.csv')