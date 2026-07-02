def extract_winner(judge_output):

    text = judge_output.upper()

    if "WINNER: PRO" in text:
        return "PRO"

    elif "WINNER: ANTI" in text:
        return "ANTI"

    else:
        return "UNKNOWN"