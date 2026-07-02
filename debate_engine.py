from prompts import *
from agents import run_agent_stream
from winner import extract_winner


def run_debate(query):

    history = ""

    # ROUND 1
    pro_prompt = PRO_AGENT_PROMPT.format(
        query=query,
        history="No conversation yet."
    )

    pro_response = run_agent_stream(
        pro_prompt,
        stream_output=True
    )

    if "[Agent failed" not in pro_response:
        history += f"\nPRO: {pro_response}\n"


    # ROUND 2
    anti_prompt = ANTI_AGENT_PROMPT.format(
        query=query,
        history=history
    )

    anti_response = run_agent_stream(
        anti_prompt,
        stream_output=True
    )

    if "[Agent failed" not in anti_response:
        history += f"\nANTI: {anti_response}\n"


    # ROUND 3
    pro_prompt = PRO_AGENT_PROMPT.format(
        query=query,
        history=history
    )

    pro_response = run_agent_stream(
        pro_prompt,
        stream_output=True
    )

    if "[Agent failed" not in pro_response:
        history += f"\nPRO: {pro_response}\n"


    # ROUND 4
    anti_prompt = ANTI_AGENT_PROMPT.format(
        query=query,
        history=history
    )

    anti_response = run_agent_stream(
        anti_prompt,
        stream_output=True
    )

    if "[Agent failed" not in anti_response:
        history += f"\nANTI: {anti_response}\n"


    # JUDGES
    logic_prompt = LOGIC_JUDGE_PROMPT.format(
        debate=history
    )

    logic_result = run_agent_stream(
        logic_prompt,
        stream_output=True
    )


    evidence_prompt = EVIDENCE_JUDGE_PROMPT.format(
        debate=history
    )

    evidence_result = run_agent_stream(
        evidence_prompt,
        stream_output=True
    )


    practicality_prompt = PRACTICALITY_JUDGE_PROMPT.format(
        debate=history
    )

    practicality_result = run_agent_stream(
        practicality_prompt,
        stream_output=True
    )


    # VOTES
    logic_vote = extract_winner(logic_result)
    evidence_vote = extract_winner(evidence_result)
    practicality_vote = extract_winner(practicality_result)

    votes = []

    if logic_vote != "UNKNOWN":
        votes.append(logic_vote)

    if evidence_vote != "UNKNOWN":
        votes.append(evidence_vote)

    if practicality_vote != "UNKNOWN":
        votes.append(practicality_vote)

    pro_votes = votes.count("PRO")
    anti_votes = votes.count("ANTI")

    if pro_votes > anti_votes:
        final_winner = "PRO"

    elif anti_votes > pro_votes:
        final_winner = "ANTI"

    else:
        final_winner = "DRAW"


    # ANALYZER
    analyzer_prompt = ANALYZER_PROMPT.format(
        debate=history
    )

    analysis_result = run_agent_stream(
        analyzer_prompt,
        stream_output=True
    )

    judge_summary = f"""
Logic Judge: {logic_vote}

Evidence Judge: {evidence_vote}

Practicality Judge: {practicality_vote}
"""

    return {
        "history": history,
        "judges": judge_summary,
        "winner": final_winner,
        "analysis": analysis_result
    }