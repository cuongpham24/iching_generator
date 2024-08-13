heavenlyStems = ["giáp", "ất", "bính", "đinh", "mậu", "kỷ", "canh", "tân", "nhâm", "quý"]
heavenlyStemsElement = ["mộc", "mộc", "hỏa", "hỏa", "thổ", "thổ", "kim", "kim", "thủy", "thủy"]

earthlyBranches = ["tý", "sửu", "dần", "mão", "thìn", "tỵ", "ngọ", "mùi", "thân", "dậu", "tuất", "hợi"]
earthlyBranchesElement = ["thủy", "thổ", "mộc", "mộc", "thổ", "hỏa", "hỏa", "thổ", "kim", "kim", "thổ", "thủy"]

numHeaven = len(heavenlyStems)
numEarth = len(earthlyBranches)

elements = {
    "kim": 1,
    "thủy": 2,
    "mộc": 3,
    "hỏa": 4,
    "thổ": 5
}

elementGeneratingCycle = {
    2: 3,
    3: 4,
    4: 5,
    5: 1,
    1: 2
}

elementControllingCycle = {
    2: 4,
    4: 1,
    1: 3,
    3: 5,
    5: 2
}

