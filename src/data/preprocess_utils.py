import pandas as pd
import numpy as np

def calc_history_len(x):
    if pd.isna(x) or str(x).strip() == "":
        return 0
    return len(str(x).split(" "))


def split_impressions(impressions_str):
    if pd.isna(impressions_str) or str(impressions_str).strip() == "":
        return []

    result = []
    for item in str(impressions_str).split(" "):
        news_id, label = item.rsplit("-", 1)
        result.append((news_id, int(label)))
    return result


def expand_behaviors(df, max_rows=None):
    rows = []

    if max_rows is not None:
        df = df.head(max_rows).copy()

    for _, row in df.iterrows():
        for news_id, label in split_impressions(row["impressions"]):
            rows.append(
                {
                    "impression_id": row["impression_id"],
                    "user_id": row["user_id"],
                    "time": row["time"],
                    "history": row["history"],
                    "history_len": row.get("history_len", np.nan),
                    "candidate_news_id": news_id,
                    "label": label,
                }
            )

    return pd.DataFrame(rows)