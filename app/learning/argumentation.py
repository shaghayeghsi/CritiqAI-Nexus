def analyze_argument(claim,argument,evidence):
    t=argument.lower(); ev=evidence.strip()
    indicators={
      "has_reasoning_connectors":any(w in t for w in ["because","therefore","since","زیرا","بنابراین"]),
      "has_counterargument":any(w in t for w in ["however","although","counter","با این حال","اگرچه"]),
      "evidence_provided":len(ev)>=20,
      "claim_is_specific":len(claim.split())>=5}
    score=round(100*sum(indicators.values())/len(indicators)); feedback=[]
    if not indicators["has_reasoning_connectors"]: feedback.append("Make the logical link between reasons and the claim explicit.")
    if not indicators["has_counterargument"]: feedback.append("Consider a plausible counterargument.")
    if not indicators["evidence_provided"]: feedback.append("Add specific, verifiable evidence.")
    if not indicators["claim_is_specific"]: feedback.append("Narrow the claim so it can be evaluated.")
    if not feedback: feedback.append("Several argument components are present; verify that the evidence directly supports the claim.")
    return {"rubric_score":score,"indicators":indicators,"feedback":feedback,
            "next_question":"What evidence would most strongly challenge your current conclusion?"}
