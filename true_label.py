# features.py or a new script like prepare_data.py

from features import feature_rows
from labelling import label_features   # or same file

# YOU decide this based on how traffic was generated
RUN_TYPE = "brute"   # or "brute"

labeled_data = label_features(feature_rows, RUN_TYPE)

print(labeled_data)
