heavenlyStems = ["giáp", "ất", "bính", "đinh", "mậu", "kỷ", "canh", "tân", "nhâm", "quý"]
heavenlyStemsElement = ["mộc", "mộc", "hỏa", "hỏa", "thổ", "thổ", "kim", "kim", "thủy", "thủy"]

earthlyBranches = ["tý", "sửu", "dần", "mão", "thìn", "tỵ", "ngọ", "mùi", "thân", "dậu", "tuất", "hợi"]
earthlyBranchesElement = ["thủy", "thổ", "mộc", "mộc", "thổ", "hỏa", "hỏa", "thổ", "kim", "kim", "thổ", "thủy"]
earthlyBranchesNo = {"tý": 1, "sửu": 2, "dần": 3, "mão": 4, "thìn": 5, "tỵ": 6, "ngọ": 7, "mùi": 8, "thân": 9, "dậu": 10, "tuất": 11, "hợi": 12}

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

timeBranches = {
    "tý": [23, 1],
    "sửu": [1, 3],
    "dần": [3, 5],
    "mão": [5, 7],
    "thìn": [7, 9],
    "tỵ": [9, 11],
    "ngọ": [11, 13],
    "mùi": [13, 15],
    "thân": [15, 17],
    "dậu": [17, 19],
    "tuất": [19, 21],
    "hợi": [21, 23]
}