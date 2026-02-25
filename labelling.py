def label_features(feature_rows, run_type):
    """
    run_type: 'normal' or 'brute'
    """
    label = 1 if run_type == "brute" else 0

    for row in feature_rows:
        row["label"] = label

    return feature_rows
