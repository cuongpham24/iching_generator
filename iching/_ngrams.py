from ._constant import earthlyBranches

trigrams = {
    1: "111",
    2: "110",
    3: "101",
    4: "100",
    5: "011",
    6: "010",
    7: "001",
    8: "000"
}

trigramsNames = {
    1: "càn",
    2: "đoài",
    3: "ly",
    4: "chấn",
    5: "tốn",
    6: "khảm",
    7: "cấn",
    8: "khôn"
}

trigramsMeaning = {
    "thiên": 1,
    "trạch": 2,
    "hỏa": 3,
    "lôi": 4,
    "phong": 5,
    "thủy": 6,
    "sơn": 7,
    "địa": 8
}

trigramsElements = {
    1: "kim",
    2: "kim",
    3: "hỏa",
    4: "mộc",
    5: "mộc",
    6: "thủy",
    7: "thổ",
    8: "thổ"
}

trigramsPros = {
    1: "+",
    2: "+",
    3: "+",
    4: "+",
    5: "-",
    6: "-",
    7: "-",
    8: "-"
}

trigramsBranchStart = {
    "càn": "tý",
    "đoài": "tỵ",
    "ly": "mão",
    "chấn": "tý",
    "tốn": "sửu",
    "khảm": "dần",
    "cấn": "thìn",
    "khôn": "mùi"
}

hexagramsNames = {
    1: "Thuần Càn",
    2: "Thuần Khôn",
    3: "Thủy Lôi Truân",
    4: "Sơn Thủy Mông",
    5: "Thủy Thiên Nhu",
    6: "Thiên Thủy Tụng",
    7: "Địa Thủy Sư",
    8: "Thủy Địa Tỷ",
    9: "Phong Thiên Tiểu Súc",
    10: "Thiên Trạch Lý",
    11: "Địa Thiên Thái",
    12: "Thiên Địa Bĩ",
    13: "Thiên Hỏa Đồng Nhân",
    14: "Hỏa Thiên Đại Hữu",
    15: "Địa Sơn Khiêm",
    16: "Lôi Địa Dự",
    17: "Trạch Lôi Tùy",
    18: "Sơn Phong Cổ",
    19: "Địa Trạch Lâm",
    20: "Phong Địa Quan",
    21: "Hỏa Lôi Phệ Hạp",
    22: "Sơn Hỏa Bí",
    23: "Sơn Địa Bác",
    24: "Địa Lôi Phục",
    25: "Thiên Lôi Vô Vọng",
    26: "Sơn Thiên Đại Súc",
    27: "Sơn Lôi Di",
    28: "Trạch Phong Đại Quá",
    29: "Thuần Khảm",
    30: "Thuần Ly",
    31: "Trạch Sơn Hàm",
    32: "Lôi Phong Hằng",
    33: "Thiên Sơn Độn",
    34: "Lôi Thiên Đại Tráng",
    35: "Hỏa Địa Tấn",
    36: "Địa Hỏa Minh Di",
    37: "Phong Hỏa Gia Nhân",
    38: "Hỏa Trạch Khuê",
    39: "Thủy Sơn Kiển",
    40: "Lôi Thủy Giải",
    41: "Sơn Trạch Tổn",
    42: "Phong Lôi Ích",
    43: "Trạch Thiên Quải",
    44: "Thiên Phong Cấu",
    45: "Trạch Địa Tụy",
    46: "Địa Phong Thăng",
    47: "Trạch Thủy Khốn",
    48: "Thủy Phong Tỉnh",
    49: "Trạch Hỏa Cách",
    50: "Hỏa Phong Đỉnh",
    51: "Thuần Chấn",
    52: "Thuần Cấn",
    53: "Phong Sơn Tiệm",
    54: "Lôi Trạch Quy Muội",
    55: "Lôi Hỏa Phong",
    56: "Hỏa Sơn Lữ",
    57: "Thuần Tốn",
    58: "Thuần Đoài",
    59: "Phong Thủy Hoán",
    60: "Thủy Trạch Tiết",
    61: "Phong Trạch Trung Phu",
    62: "Lôi Sơn Tiểu Quá",
    63: "Thủy Hỏa Ký Tế",
    64: "Hỏa Thủy Vị Tế"
}

hexagramsFamily = {
    1: [1, 44, 33, 12, 20, 23, 35, 14],
    2: [58, 47, 45, 31, 39, 15, 62, 54],
    3: [4, 6, 13, 30, 50, 56, 59, 64],
    4: [51, 16, 40, 32, 46, 48, 28, 17],
    5: [57, 9, 37, 42, 25, 21, 27, 18],
    6: [29, 60, 3, 63, 49, 55, 36, 7],
    7: [52, 22, 26, 41, 38, 10, 61, 53],
    8: [2, 24, 19, 11, 34, 43, 5, 8],
}

hexagramsStructure = {
    (1, 1): 1,
    (8, 8): 2,
    (6, 4): 3,
    (7, 6): 4,
    (6, 1): 5,
    (1, 6): 6,
    (8, 6): 7,
    (6, 8): 8,
    (5, 1): 9,
    (1, 2): 10,
    (8, 1): 11,
    (1, 8): 12,
    (1, 3): 13,
    (3, 1): 14,
    (8, 7): 15,
    (4, 8): 16,
    (2, 4): 17,
    (7, 5): 18,
    (8, 2): 19,
    (5, 8): 20,
    (3, 4): 21,
    (7, 3): 22,
    (7, 8): 23,
    (8, 4): 24,
    (1, 4): 25,
    (7, 1): 26,
    (7, 4): 27,
    (2, 5): 28,
    (6, 6): 29,
    (3, 3): 30,
    (2, 7): 31,
    (4, 5): 32,
    (1, 7): 33,
    (4, 1): 34,
    (3, 8): 35,
    (8, 3): 36,
    (5, 3): 37,
    (3, 2): 38,
    (6, 7): 39,
    (4, 6): 40,
    (7, 2): 41,
    (5, 4): 42,
    (2, 1): 43,
    (1, 5): 44,
    (2, 8): 45,
    (8, 5): 46,
    (2, 6): 47,
    (6, 5): 48,
    (2, 3): 49,
    (3, 5): 50,
    (4, 4): 51,
    (7, 7): 52,
    (5, 7): 53,
    (4, 2): 54,
    (4, 3): 55,
    (3, 7): 56,
    (5, 5): 57,
    (2, 2): 58,
    (5, 6): 59,
    (6, 2): 60,
    (5, 2): 61,
    (4, 7): 62,
    (6, 3): 63,
    (3, 6): 64
}

basicHexagramsBranches = {
    # 1: ['tý', 'dần', 'thìn', 'ngọ', 'thân', 'tuất'],
    # 2: ['tỵ', 'mão', 'sửu', 'hợi', 'dậu', 'mùi'],
    # 3: ['mão', 'sửu', 'hợi', 'dậu', 'mùi', 'tỵ'],
    # 4: ['tý', 'dần', 'thìn', 'ngọ', 'thân', 'tuất'],
    # 5: ['sửu', 'hợi', 'dậu', 'mùi', 'tỵ', 'mão'],
    # 6: ['dần', 'thìn', 'ngọ', 'thân', 'tuất', 'tý'],
    # 7: ['thìn', 'ngọ', 'thân', 'tuất', 'tý', 'dần'],
    # 8: ['mùi', 'tỵ', 'mão', 'sửu', 'hợi', 'dậu']
    1: [0, 2, 4, 6, 8, 10], 
    2: [5, 3, 1, 11, 9, 7],
    3: [3, 1, 11, 9, 7, 5],
    4: [0, 2, 4, 6, 8, 10],
    5: [1, 11, 9, 7, 5, 3],
    6: [2, 4, 6, 8, 10, 0],
    7: [4, 6, 8, 10, 0, 2],
    8: [7, 5, 3, 1, 11, 9]
}

hexSixRelatives = {
    "huynh đệ": 1,
    "tử tôn": 2,
    "thê tài": 3,
    "quan quỷ": 4,
    "phụ mẫu": 5
}

sixRelativesGeneratingCycle = {
    1: 2,
    2: 3,
    3: 4,
    4: 5,
    5: 1
}

sixRelativesControllingCycle = {
    1: 3,
    2: 4,
    3: 5,
    4: 1,
    5: 2
}

if __name__=="__init__":

    # Generate hexagram structure
    hexagramsStructure = {}
    for que in hexagramsNames:
        thuong, ha, *arg = hexagramsNames[que].lower().split()
        thuong, ha = trigramsMeaning[thuong], trigramsMeaning[ha]
        hexagramsStructure[(thuong, ha)] = que

    # Generate the basic hexagram earthly branches
    basicHexagramsBranches = {}
    for que in range(1, 9):
        start = earthlyBranches.index(trigramsBranchStart[trigramsNames[que]])
        branches = []
        for i in range(6):
            if trigramsPros[que] == "+":
                branches.append(earthlyBranches[(start + i * 2) % 12])
            else:
                branches.append(earthlyBranches[(start - i * 2) % 12])
        basicHexagramsBranches[que] = branches