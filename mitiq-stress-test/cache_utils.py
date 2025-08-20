import pandas as pd
import os


# function to write out the result into a CSV file
def save_result(cache_res, file_name="results/cached_results.csv"):
    if not os.path.exists(file_name):
        df = pd.DataFrame(
            columns=[
                "circuit",
                "backend",
                "result",
                "degree",
                "fold_multiplier",
                "num_chunks",
                "time",
            ]
        )
        df.to_csv(file_name, index=False)
    df = pd.read_csv(file_name)
    df.loc[len(df)] = cache_res
    df = df.sort_values(by=["circuit", "backend", "fold_multiplier"])
    df.to_csv(file_name, index=False)
