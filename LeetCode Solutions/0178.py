import pandas as pd
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    if 'score' not in scores.columns:
        raise ValueError("DataFrame must contain a 'score' column")
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    sorted_scores = scores.sort_values(by='score', ascending=False)
    sorted_scores['rank'] = sorted_scores['rank'].astype(int)
    result = sorted_scores[['score', 'rank']]
    return result

