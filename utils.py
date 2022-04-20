from api_load import api

candidate_api = api()


def load_candidates_from_json():
    return api()


def get_candidate(candidate_id):
    candidate = []
    for candidates in range(len(candidate_api)):
        if candidate_api[candidates]["id"] == candidate_id:
            candidate.append(candidate_api[candidates])
        elif candidate_id > len(candidate_api):
            return "Данный пользователь не найден"
    return candidate


def get_candidates_by_name(candidate_name):
    candidate = []
    for candidates in candidate_api:
        list_name = candidates.get("name").split(" ")
        if candidate_name in list_name:
            print(candidate_name)
            candidate.append(candidates)
    return candidate


def get_candidates_by_skill(skill_name="NO"):
    candidate = []
    for candidates in candidate_api:
        list_skill = candidates.get("skills").lower().split(",")
        if skill_name in list_skill:
            candidate.append(candidates)
    return candidate


