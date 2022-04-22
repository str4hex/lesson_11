import json

with open("candidates.json", "r", encoding="utf8") as candidate:
    candidate_json = json.load(candidate)


def get_candidate(candidate_id):
    for candidates in candidate_json:
        if candidates["id"] == candidate_id:
            return candidates


def get_candidates_by_name(candidate_name):
    candidate = []
    for candidates in candidate_json:
        list_name = candidates.get("name").split(" ")
        if candidate_name in list_name:
            candidate.append(candidates)
    return candidate


def get_candidates_by_skill(skill_name="NO"):
    candidate = []
    for candidates in candidate_json:
        list_skill = candidates.get("skills").lower().split(", ")
        if skill_name.lower() in list_skill:
            candidate.append(candidates)
    return candidate
