from nfa.main import driver

MAX_EATER_NUMBER = -1
MAX_EATER_POINTER = -1
SOURCE_CODE = "".join([i for i in open("test_cases/java/java.in").readlines()])
CURRENT_STATE = "S_INIT"
OUTPUT = list()
LINE_NUMBER = 1


def f_0(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_INIT', '\\t|\\_', ['-']]
    if CURRENT_STATE == "S_INIT":
        print(0)
        t_in = [
            str(SOURCE_CODE),
            ['S_1', 'S_2'],
            "S_0",
            ['S_0', '\t', 'S_1'],
            ['S_0', ' ', 'S_2']
        ]
        t_0, is_accepted = driver(t_in)

        if may_i_eat:
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        elif is_accepted:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 0

        return t_0.count("|")


def f_1(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_INIT', '\\n', ['-', 'NOVI_REDAK']]
    if CURRENT_STATE == "S_INIT":
        print(1)
        t_in = [
            str(SOURCE_CODE),
            ['S_1'],
            "S_0",
            ['S_0', '\n', 'S_1']
        ]
        t_0, is_accepted = driver(t_in)

        if may_i_eat:
            LINE_NUMBER += 1
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        elif is_accepted:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 1

        return t_0.count("|")


def f_2(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_INIT', '//', ['UDJI_U_STANJE ONE_LINE_COMMENT']]
    if CURRENT_STATE == "S_INIT":
        print(2)
        t_in = [
            str(SOURCE_CODE),
            ['S_2'],
            "S_0",
            ['S_0', '/', 'S_1'],
            ['S_1', '/', 'S_2']
        ]
        t_0, is_accepted = driver(t_in)

        if may_i_eat:
            CURRENT_STATE = "ONE_LINE_COMMENT"
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        elif is_accepted:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 2

        return t_0.count("|")


def f_3(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['ONE_LINE_COMMENT', '\\n', ['UDJI_U_STANJE S_INIT']]
    if CURRENT_STATE == "ONE_LINE_COMMENT":
        print(3)
        t_in = [
            str(SOURCE_CODE),
            ['S_1'],
            "S_0",
            ['S_0', '\n', 'S_1']
        ]
        t_0, is_accepted = driver(t_in)

        if may_i_eat:
            CURRENT_STATE = "S_INIT"
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        elif is_accepted:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 3

        return t_0.count("|")


def f_4(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['ONE_LINE_COMMENT', '(\\(|\\)|\\{|\\}|\\||\\*|\\\\|\\$|\\t|\\n|\\_|!|"|#|%|&|\'|+|,|-|.|/|0|1|2|3|4|5|6|7|8|9|:|;|<|=|>|?|@|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|[|]|^|_|`|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|~)', ['-']]
    if CURRENT_STATE == "ONE_LINE_COMMENT":
        print(4)
        t_in = [
            str(SOURCE_CODE),
            ['S_195'],
            "S_0",
            ['S_0', '__$__', 'S_1'],
            ['S_1', '(', 'S_2'],
            ['S_0', '__$__', 'S_3'],
            ['S_3', ')', 'S_4'],
            ['S_0', '__$__', 'S_5'],
            ['S_5', '{', 'S_6'],
            ['S_0', '__$__', 'S_7'],
            ['S_7', '}', 'S_8'],
            ['S_0', '__$__', 'S_9'],
            ['S_9', '|', 'S_10'],
            ['S_0', '__$__', 'S_11'],
            ['S_11', '*', 'S_12'],
            ['S_0', '__$__', 'S_13'],
            ['S_13', '\\', 'S_14'],
            ['S_0', '__$__', 'S_15'],
            ['S_15', '$', 'S_16'],
            ['S_0', '__$__', 'S_17'],
            ['S_17', '\t', 'S_18'],
            ['S_0', '__$__', 'S_19'],
            ['S_19', '\n', 'S_20'],
            ['S_0', '__$__', 'S_21'],
            ['S_21', ' ', 'S_22'],
            ['S_0', '__$__', 'S_23'],
            ['S_23', '!', 'S_24'],
            ['S_0', '__$__', 'S_25'],
            ['S_25', '"', 'S_26'],
            ['S_0', '__$__', 'S_27'],
            ['S_27', '#', 'S_28'],
            ['S_0', '__$__', 'S_29'],
            ['S_29', '%', 'S_30'],
            ['S_0', '__$__', 'S_31'],
            ['S_31', '&', 'S_32'],
            ['S_0', '__$__', 'S_33'],
            ['S_33', "'", 'S_34'],
            ['S_0', '__$__', 'S_35'],
            ['S_35', '+', 'S_36'],
            ['S_0', '__$__', 'S_37'],
            ['S_37', ',', 'S_38'],
            ['S_0', '__$__', 'S_39'],
            ['S_39', '-', 'S_40'],
            ['S_0', '__$__', 'S_41'],
            ['S_41', '.', 'S_42'],
            ['S_0', '__$__', 'S_43'],
            ['S_43', '/', 'S_44'],
            ['S_0', '__$__', 'S_45'],
            ['S_45', '0', 'S_46'],
            ['S_0', '__$__', 'S_47'],
            ['S_47', '1', 'S_48'],
            ['S_0', '__$__', 'S_49'],
            ['S_49', '2', 'S_50'],
            ['S_0', '__$__', 'S_51'],
            ['S_51', '3', 'S_52'],
            ['S_0', '__$__', 'S_53'],
            ['S_53', '4', 'S_54'],
            ['S_0', '__$__', 'S_55'],
            ['S_55', '5', 'S_56'],
            ['S_0', '__$__', 'S_57'],
            ['S_57', '6', 'S_58'],
            ['S_0', '__$__', 'S_59'],
            ['S_59', '7', 'S_60'],
            ['S_0', '__$__', 'S_61'],
            ['S_61', '8', 'S_62'],
            ['S_0', '__$__', 'S_63'],
            ['S_63', '9', 'S_64'],
            ['S_0', '__$__', 'S_65'],
            ['S_65', ':', 'S_66'],
            ['S_0', '__$__', 'S_67'],
            ['S_67', ';', 'S_68'],
            ['S_0', '__$__', 'S_69'],
            ['S_69', '<', 'S_70'],
            ['S_0', '__$__', 'S_71'],
            ['S_71', '=', 'S_72'],
            ['S_0', '__$__', 'S_73'],
            ['S_73', '>', 'S_74'],
            ['S_0', '__$__', 'S_75'],
            ['S_75', '?', 'S_76'],
            ['S_0', '__$__', 'S_77'],
            ['S_77', '@', 'S_78'],
            ['S_0', '__$__', 'S_79'],
            ['S_79', 'A', 'S_80'],
            ['S_0', '__$__', 'S_81'],
            ['S_81', 'B', 'S_82'],
            ['S_0', '__$__', 'S_83'],
            ['S_83', 'C', 'S_84'],
            ['S_0', '__$__', 'S_85'],
            ['S_85', 'D', 'S_86'],
            ['S_0', '__$__', 'S_87'],
            ['S_87', 'E', 'S_88'],
            ['S_0', '__$__', 'S_89'],
            ['S_89', 'F', 'S_90'],
            ['S_0', '__$__', 'S_91'],
            ['S_91', 'G', 'S_92'],
            ['S_0', '__$__', 'S_93'],
            ['S_93', 'H', 'S_94'],
            ['S_0', '__$__', 'S_95'],
            ['S_95', 'I', 'S_96'],
            ['S_0', '__$__', 'S_97'],
            ['S_97', 'J', 'S_98'],
            ['S_0', '__$__', 'S_99'],
            ['S_99', 'K', 'S_100'],
            ['S_0', '__$__', 'S_101'],
            ['S_101', 'L', 'S_102'],
            ['S_0', '__$__', 'S_103'],
            ['S_103', 'M', 'S_104'],
            ['S_0', '__$__', 'S_105'],
            ['S_105', 'N', 'S_106'],
            ['S_0', '__$__', 'S_107'],
            ['S_107', 'O', 'S_108'],
            ['S_0', '__$__', 'S_109'],
            ['S_109', 'P', 'S_110'],
            ['S_0', '__$__', 'S_111'],
            ['S_111', 'Q', 'S_112'],
            ['S_0', '__$__', 'S_113'],
            ['S_113', 'R', 'S_114'],
            ['S_0', '__$__', 'S_115'],
            ['S_115', 'S', 'S_116'],
            ['S_0', '__$__', 'S_117'],
            ['S_117', 'T', 'S_118'],
            ['S_0', '__$__', 'S_119'],
            ['S_119', 'U', 'S_120'],
            ['S_0', '__$__', 'S_121'],
            ['S_121', 'V', 'S_122'],
            ['S_0', '__$__', 'S_123'],
            ['S_123', 'W', 'S_124'],
            ['S_0', '__$__', 'S_125'],
            ['S_125', 'X', 'S_126'],
            ['S_0', '__$__', 'S_127'],
            ['S_127', 'Y', 'S_128'],
            ['S_0', '__$__', 'S_129'],
            ['S_129', 'Z', 'S_130'],
            ['S_0', '__$__', 'S_131'],
            ['S_131', '[', 'S_132'],
            ['S_0', '__$__', 'S_133'],
            ['S_133', ']', 'S_134'],
            ['S_0', '__$__', 'S_135'],
            ['S_135', '^', 'S_136'],
            ['S_0', '__$__', 'S_137'],
            ['S_137', '_', 'S_138'],
            ['S_0', '__$__', 'S_139'],
            ['S_139', '`', 'S_140'],
            ['S_0', '__$__', 'S_141'],
            ['S_141', 'a', 'S_142'],
            ['S_0', '__$__', 'S_143'],
            ['S_143', 'b', 'S_144'],
            ['S_0', '__$__', 'S_145'],
            ['S_145', 'c', 'S_146'],
            ['S_0', '__$__', 'S_147'],
            ['S_147', 'd', 'S_148'],
            ['S_0', '__$__', 'S_149'],
            ['S_149', 'e', 'S_150'],
            ['S_0', '__$__', 'S_151'],
            ['S_151', 'f', 'S_152'],
            ['S_0', '__$__', 'S_153'],
            ['S_153', 'g', 'S_154'],
            ['S_0', '__$__', 'S_155'],
            ['S_155', 'h', 'S_156'],
            ['S_0', '__$__', 'S_157'],
            ['S_157', 'i', 'S_158'],
            ['S_0', '__$__', 'S_159'],
            ['S_159', 'j', 'S_160'],
            ['S_0', '__$__', 'S_161'],
            ['S_161', 'k', 'S_162'],
            ['S_0', '__$__', 'S_163'],
            ['S_163', 'l', 'S_164'],
            ['S_0', '__$__', 'S_165'],
            ['S_165', 'm', 'S_166'],
            ['S_0', '__$__', 'S_167'],
            ['S_167', 'n', 'S_168'],
            ['S_0', '__$__', 'S_169'],
            ['S_169', 'o', 'S_170'],
            ['S_0', '__$__', 'S_171'],
            ['S_171', 'p', 'S_172'],
            ['S_0', '__$__', 'S_173'],
            ['S_173', 'q', 'S_174'],
            ['S_0', '__$__', 'S_175'],
            ['S_175', 'r', 'S_176'],
            ['S_0', '__$__', 'S_177'],
            ['S_177', 's', 'S_178'],
            ['S_0', '__$__', 'S_179'],
            ['S_179', 't', 'S_180'],
            ['S_0', '__$__', 'S_181'],
            ['S_181', 'u', 'S_182'],
            ['S_0', '__$__', 'S_183'],
            ['S_183', 'v', 'S_184'],
            ['S_0', '__$__', 'S_185'],
            ['S_185', 'w', 'S_186'],
            ['S_0', '__$__', 'S_187'],
            ['S_187', 'x', 'S_188'],
            ['S_0', '__$__', 'S_189'],
            ['S_189', 'y', 'S_190'],
            ['S_0', '__$__', 'S_191'],
            ['S_191', 'z', 'S_192'],
            ['S_0', '__$__', 'S_193'],
            ['S_193', '~', 'S_194'],
            ['S_2', '__$__', 'S_195'],
            ['S_4', '__$__', 'S_195'],
            ['S_6', '__$__', 'S_195'],
            ['S_8', '__$__', 'S_195'],
            ['S_10', '__$__', 'S_195'],
            ['S_12', '__$__', 'S_195'],
            ['S_14', '__$__', 'S_195'],
            ['S_16', '__$__', 'S_195'],
            ['S_18', '__$__', 'S_195'],
            ['S_20', '__$__', 'S_195'],
            ['S_22', '__$__', 'S_195'],
            ['S_24', '__$__', 'S_195'],
            ['S_26', '__$__', 'S_195'],
            ['S_28', '__$__', 'S_195'],
            ['S_30', '__$__', 'S_195'],
            ['S_32', '__$__', 'S_195'],
            ['S_34', '__$__', 'S_195'],
            ['S_36', '__$__', 'S_195'],
            ['S_38', '__$__', 'S_195'],
            ['S_40', '__$__', 'S_195'],
            ['S_42', '__$__', 'S_195'],
            ['S_44', '__$__', 'S_195'],
            ['S_46', '__$__', 'S_195'],
            ['S_48', '__$__', 'S_195'],
            ['S_50', '__$__', 'S_195'],
            ['S_52', '__$__', 'S_195'],
            ['S_54', '__$__', 'S_195'],
            ['S_56', '__$__', 'S_195'],
            ['S_58', '__$__', 'S_195'],
            ['S_60', '__$__', 'S_195'],
            ['S_62', '__$__', 'S_195'],
            ['S_64', '__$__', 'S_195'],
            ['S_66', '__$__', 'S_195'],
            ['S_68', '__$__', 'S_195'],
            ['S_70', '__$__', 'S_195'],
            ['S_72', '__$__', 'S_195'],
            ['S_74', '__$__', 'S_195'],
            ['S_76', '__$__', 'S_195'],
            ['S_78', '__$__', 'S_195'],
            ['S_80', '__$__', 'S_195'],
            ['S_82', '__$__', 'S_195'],
            ['S_84', '__$__', 'S_195'],
            ['S_86', '__$__', 'S_195'],
            ['S_88', '__$__', 'S_195'],
            ['S_90', '__$__', 'S_195'],
            ['S_92', '__$__', 'S_195'],
            ['S_94', '__$__', 'S_195'],
            ['S_96', '__$__', 'S_195'],
            ['S_98', '__$__', 'S_195'],
            ['S_100', '__$__', 'S_195'],
            ['S_102', '__$__', 'S_195'],
            ['S_104', '__$__', 'S_195'],
            ['S_106', '__$__', 'S_195'],
            ['S_108', '__$__', 'S_195'],
            ['S_110', '__$__', 'S_195'],
            ['S_112', '__$__', 'S_195'],
            ['S_114', '__$__', 'S_195'],
            ['S_116', '__$__', 'S_195'],
            ['S_118', '__$__', 'S_195'],
            ['S_120', '__$__', 'S_195'],
            ['S_122', '__$__', 'S_195'],
            ['S_124', '__$__', 'S_195'],
            ['S_126', '__$__', 'S_195'],
            ['S_128', '__$__', 'S_195'],
            ['S_130', '__$__', 'S_195'],
            ['S_132', '__$__', 'S_195'],
            ['S_134', '__$__', 'S_195'],
            ['S_136', '__$__', 'S_195'],
            ['S_138', '__$__', 'S_195'],
            ['S_140', '__$__', 'S_195'],
            ['S_142', '__$__', 'S_195'],
            ['S_144', '__$__', 'S_195'],
            ['S_146', '__$__', 'S_195'],
            ['S_148', '__$__', 'S_195'],
            ['S_150', '__$__', 'S_195'],
            ['S_152', '__$__', 'S_195'],
            ['S_154', '__$__', 'S_195'],
            ['S_156', '__$__', 'S_195'],
            ['S_158', '__$__', 'S_195'],
            ['S_160', '__$__', 'S_195'],
            ['S_162', '__$__', 'S_195'],
            ['S_164', '__$__', 'S_195'],
            ['S_166', '__$__', 'S_195'],
            ['S_168', '__$__', 'S_195'],
            ['S_170', '__$__', 'S_195'],
            ['S_172', '__$__', 'S_195'],
            ['S_174', '__$__', 'S_195'],
            ['S_176', '__$__', 'S_195'],
            ['S_178', '__$__', 'S_195'],
            ['S_180', '__$__', 'S_195'],
            ['S_182', '__$__', 'S_195'],
            ['S_184', '__$__', 'S_195'],
            ['S_186', '__$__', 'S_195'],
            ['S_188', '__$__', 'S_195'],
            ['S_190', '__$__', 'S_195'],
            ['S_192', '__$__', 'S_195'],
            ['S_194', '__$__', 'S_195']
        ]
        t_0, is_accepted = driver(t_in)

        if may_i_eat:
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        elif is_accepted:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 4

        return t_0.count("|")


def f_5(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_INIT', 'package', ['VISIBILITY_MODIFIER']]
    if CURRENT_STATE == "S_INIT":
        print(5)
        t_in = [
            str(SOURCE_CODE),
            ['S_7'],
            "S_0",
            ['S_0', 'p', 'S_1'],
            ['S_1', 'a', 'S_2'],
            ['S_2', 'c', 'S_3'],
            ['S_3', 'k', 'S_4'],
            ['S_4', 'a', 'S_5'],
            ['S_5', 'g', 'S_6'],
            ['S_6', 'e', 'S_7']
        ]
        t_0, is_accepted = driver(t_in)

        if may_i_eat:
            OUTPUT.append("VISIBILITY_MODIFIER " + str(LINE_NUMBER) + " " + SOURCE_CODE[:MAX_EATER_NUMBER])
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        elif is_accepted:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 5

        return t_0.count("|")


def f_6(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_INIT', ';', ['END_OF_INSTRUCTION']]
    if CURRENT_STATE == "S_INIT":
        print(6)
        t_in = [
            str(SOURCE_CODE),
            ['S_1'],
            "S_0",
            ['S_0', ';', 'S_1']
        ]
        t_0, is_accepted = driver(t_in)

        if may_i_eat:
            OUTPUT.append("END_OF_INSTRUCTION " + str(LINE_NUMBER) + " " + SOURCE_CODE[:MAX_EATER_NUMBER])
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        elif is_accepted:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 6

        return t_0.count("|")


def f_7(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_INIT', '(\\(|\\)|\\{|\\}|\\||\\*|\\\\|\\$|\\t|\\n|\\_|!|"|#|%|&|\'|+|,|-|.|/|0|1|2|3|4|5|6|7|8|9|:|;|<|=|>|?|@|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|[|]|^|_|`|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|~)', ['-']]
    if CURRENT_STATE == "S_INIT":
        print(7)
        t_in = [
            str(SOURCE_CODE),
            ['S_195'],
            "S_0",
            ['S_0', '__$__', 'S_1'],
            ['S_1', '(', 'S_2'],
            ['S_0', '__$__', 'S_3'],
            ['S_3', ')', 'S_4'],
            ['S_0', '__$__', 'S_5'],
            ['S_5', '{', 'S_6'],
            ['S_0', '__$__', 'S_7'],
            ['S_7', '}', 'S_8'],
            ['S_0', '__$__', 'S_9'],
            ['S_9', '|', 'S_10'],
            ['S_0', '__$__', 'S_11'],
            ['S_11', '*', 'S_12'],
            ['S_0', '__$__', 'S_13'],
            ['S_13', '\\', 'S_14'],
            ['S_0', '__$__', 'S_15'],
            ['S_15', '$', 'S_16'],
            ['S_0', '__$__', 'S_17'],
            ['S_17', '\t', 'S_18'],
            ['S_0', '__$__', 'S_19'],
            ['S_19', '\n', 'S_20'],
            ['S_0', '__$__', 'S_21'],
            ['S_21', ' ', 'S_22'],
            ['S_0', '__$__', 'S_23'],
            ['S_23', '!', 'S_24'],
            ['S_0', '__$__', 'S_25'],
            ['S_25', '"', 'S_26'],
            ['S_0', '__$__', 'S_27'],
            ['S_27', '#', 'S_28'],
            ['S_0', '__$__', 'S_29'],
            ['S_29', '%', 'S_30'],
            ['S_0', '__$__', 'S_31'],
            ['S_31', '&', 'S_32'],
            ['S_0', '__$__', 'S_33'],
            ['S_33', "'", 'S_34'],
            ['S_0', '__$__', 'S_35'],
            ['S_35', '+', 'S_36'],
            ['S_0', '__$__', 'S_37'],
            ['S_37', ',', 'S_38'],
            ['S_0', '__$__', 'S_39'],
            ['S_39', '-', 'S_40'],
            ['S_0', '__$__', 'S_41'],
            ['S_41', '.', 'S_42'],
            ['S_0', '__$__', 'S_43'],
            ['S_43', '/', 'S_44'],
            ['S_0', '__$__', 'S_45'],
            ['S_45', '0', 'S_46'],
            ['S_0', '__$__', 'S_47'],
            ['S_47', '1', 'S_48'],
            ['S_0', '__$__', 'S_49'],
            ['S_49', '2', 'S_50'],
            ['S_0', '__$__', 'S_51'],
            ['S_51', '3', 'S_52'],
            ['S_0', '__$__', 'S_53'],
            ['S_53', '4', 'S_54'],
            ['S_0', '__$__', 'S_55'],
            ['S_55', '5', 'S_56'],
            ['S_0', '__$__', 'S_57'],
            ['S_57', '6', 'S_58'],
            ['S_0', '__$__', 'S_59'],
            ['S_59', '7', 'S_60'],
            ['S_0', '__$__', 'S_61'],
            ['S_61', '8', 'S_62'],
            ['S_0', '__$__', 'S_63'],
            ['S_63', '9', 'S_64'],
            ['S_0', '__$__', 'S_65'],
            ['S_65', ':', 'S_66'],
            ['S_0', '__$__', 'S_67'],
            ['S_67', ';', 'S_68'],
            ['S_0', '__$__', 'S_69'],
            ['S_69', '<', 'S_70'],
            ['S_0', '__$__', 'S_71'],
            ['S_71', '=', 'S_72'],
            ['S_0', '__$__', 'S_73'],
            ['S_73', '>', 'S_74'],
            ['S_0', '__$__', 'S_75'],
            ['S_75', '?', 'S_76'],
            ['S_0', '__$__', 'S_77'],
            ['S_77', '@', 'S_78'],
            ['S_0', '__$__', 'S_79'],
            ['S_79', 'A', 'S_80'],
            ['S_0', '__$__', 'S_81'],
            ['S_81', 'B', 'S_82'],
            ['S_0', '__$__', 'S_83'],
            ['S_83', 'C', 'S_84'],
            ['S_0', '__$__', 'S_85'],
            ['S_85', 'D', 'S_86'],
            ['S_0', '__$__', 'S_87'],
            ['S_87', 'E', 'S_88'],
            ['S_0', '__$__', 'S_89'],
            ['S_89', 'F', 'S_90'],
            ['S_0', '__$__', 'S_91'],
            ['S_91', 'G', 'S_92'],
            ['S_0', '__$__', 'S_93'],
            ['S_93', 'H', 'S_94'],
            ['S_0', '__$__', 'S_95'],
            ['S_95', 'I', 'S_96'],
            ['S_0', '__$__', 'S_97'],
            ['S_97', 'J', 'S_98'],
            ['S_0', '__$__', 'S_99'],
            ['S_99', 'K', 'S_100'],
            ['S_0', '__$__', 'S_101'],
            ['S_101', 'L', 'S_102'],
            ['S_0', '__$__', 'S_103'],
            ['S_103', 'M', 'S_104'],
            ['S_0', '__$__', 'S_105'],
            ['S_105', 'N', 'S_106'],
            ['S_0', '__$__', 'S_107'],
            ['S_107', 'O', 'S_108'],
            ['S_0', '__$__', 'S_109'],
            ['S_109', 'P', 'S_110'],
            ['S_0', '__$__', 'S_111'],
            ['S_111', 'Q', 'S_112'],
            ['S_0', '__$__', 'S_113'],
            ['S_113', 'R', 'S_114'],
            ['S_0', '__$__', 'S_115'],
            ['S_115', 'S', 'S_116'],
            ['S_0', '__$__', 'S_117'],
            ['S_117', 'T', 'S_118'],
            ['S_0', '__$__', 'S_119'],
            ['S_119', 'U', 'S_120'],
            ['S_0', '__$__', 'S_121'],
            ['S_121', 'V', 'S_122'],
            ['S_0', '__$__', 'S_123'],
            ['S_123', 'W', 'S_124'],
            ['S_0', '__$__', 'S_125'],
            ['S_125', 'X', 'S_126'],
            ['S_0', '__$__', 'S_127'],
            ['S_127', 'Y', 'S_128'],
            ['S_0', '__$__', 'S_129'],
            ['S_129', 'Z', 'S_130'],
            ['S_0', '__$__', 'S_131'],
            ['S_131', '[', 'S_132'],
            ['S_0', '__$__', 'S_133'],
            ['S_133', ']', 'S_134'],
            ['S_0', '__$__', 'S_135'],
            ['S_135', '^', 'S_136'],
            ['S_0', '__$__', 'S_137'],
            ['S_137', '_', 'S_138'],
            ['S_0', '__$__', 'S_139'],
            ['S_139', '`', 'S_140'],
            ['S_0', '__$__', 'S_141'],
            ['S_141', 'a', 'S_142'],
            ['S_0', '__$__', 'S_143'],
            ['S_143', 'b', 'S_144'],
            ['S_0', '__$__', 'S_145'],
            ['S_145', 'c', 'S_146'],
            ['S_0', '__$__', 'S_147'],
            ['S_147', 'd', 'S_148'],
            ['S_0', '__$__', 'S_149'],
            ['S_149', 'e', 'S_150'],
            ['S_0', '__$__', 'S_151'],
            ['S_151', 'f', 'S_152'],
            ['S_0', '__$__', 'S_153'],
            ['S_153', 'g', 'S_154'],
            ['S_0', '__$__', 'S_155'],
            ['S_155', 'h', 'S_156'],
            ['S_0', '__$__', 'S_157'],
            ['S_157', 'i', 'S_158'],
            ['S_0', '__$__', 'S_159'],
            ['S_159', 'j', 'S_160'],
            ['S_0', '__$__', 'S_161'],
            ['S_161', 'k', 'S_162'],
            ['S_0', '__$__', 'S_163'],
            ['S_163', 'l', 'S_164'],
            ['S_0', '__$__', 'S_165'],
            ['S_165', 'm', 'S_166'],
            ['S_0', '__$__', 'S_167'],
            ['S_167', 'n', 'S_168'],
            ['S_0', '__$__', 'S_169'],
            ['S_169', 'o', 'S_170'],
            ['S_0', '__$__', 'S_171'],
            ['S_171', 'p', 'S_172'],
            ['S_0', '__$__', 'S_173'],
            ['S_173', 'q', 'S_174'],
            ['S_0', '__$__', 'S_175'],
            ['S_175', 'r', 'S_176'],
            ['S_0', '__$__', 'S_177'],
            ['S_177', 's', 'S_178'],
            ['S_0', '__$__', 'S_179'],
            ['S_179', 't', 'S_180'],
            ['S_0', '__$__', 'S_181'],
            ['S_181', 'u', 'S_182'],
            ['S_0', '__$__', 'S_183'],
            ['S_183', 'v', 'S_184'],
            ['S_0', '__$__', 'S_185'],
            ['S_185', 'w', 'S_186'],
            ['S_0', '__$__', 'S_187'],
            ['S_187', 'x', 'S_188'],
            ['S_0', '__$__', 'S_189'],
            ['S_189', 'y', 'S_190'],
            ['S_0', '__$__', 'S_191'],
            ['S_191', 'z', 'S_192'],
            ['S_0', '__$__', 'S_193'],
            ['S_193', '~', 'S_194'],
            ['S_2', '__$__', 'S_195'],
            ['S_4', '__$__', 'S_195'],
            ['S_6', '__$__', 'S_195'],
            ['S_8', '__$__', 'S_195'],
            ['S_10', '__$__', 'S_195'],
            ['S_12', '__$__', 'S_195'],
            ['S_14', '__$__', 'S_195'],
            ['S_16', '__$__', 'S_195'],
            ['S_18', '__$__', 'S_195'],
            ['S_20', '__$__', 'S_195'],
            ['S_22', '__$__', 'S_195'],
            ['S_24', '__$__', 'S_195'],
            ['S_26', '__$__', 'S_195'],
            ['S_28', '__$__', 'S_195'],
            ['S_30', '__$__', 'S_195'],
            ['S_32', '__$__', 'S_195'],
            ['S_34', '__$__', 'S_195'],
            ['S_36', '__$__', 'S_195'],
            ['S_38', '__$__', 'S_195'],
            ['S_40', '__$__', 'S_195'],
            ['S_42', '__$__', 'S_195'],
            ['S_44', '__$__', 'S_195'],
            ['S_46', '__$__', 'S_195'],
            ['S_48', '__$__', 'S_195'],
            ['S_50', '__$__', 'S_195'],
            ['S_52', '__$__', 'S_195'],
            ['S_54', '__$__', 'S_195'],
            ['S_56', '__$__', 'S_195'],
            ['S_58', '__$__', 'S_195'],
            ['S_60', '__$__', 'S_195'],
            ['S_62', '__$__', 'S_195'],
            ['S_64', '__$__', 'S_195'],
            ['S_66', '__$__', 'S_195'],
            ['S_68', '__$__', 'S_195'],
            ['S_70', '__$__', 'S_195'],
            ['S_72', '__$__', 'S_195'],
            ['S_74', '__$__', 'S_195'],
            ['S_76', '__$__', 'S_195'],
            ['S_78', '__$__', 'S_195'],
            ['S_80', '__$__', 'S_195'],
            ['S_82', '__$__', 'S_195'],
            ['S_84', '__$__', 'S_195'],
            ['S_86', '__$__', 'S_195'],
            ['S_88', '__$__', 'S_195'],
            ['S_90', '__$__', 'S_195'],
            ['S_92', '__$__', 'S_195'],
            ['S_94', '__$__', 'S_195'],
            ['S_96', '__$__', 'S_195'],
            ['S_98', '__$__', 'S_195'],
            ['S_100', '__$__', 'S_195'],
            ['S_102', '__$__', 'S_195'],
            ['S_104', '__$__', 'S_195'],
            ['S_106', '__$__', 'S_195'],
            ['S_108', '__$__', 'S_195'],
            ['S_110', '__$__', 'S_195'],
            ['S_112', '__$__', 'S_195'],
            ['S_114', '__$__', 'S_195'],
            ['S_116', '__$__', 'S_195'],
            ['S_118', '__$__', 'S_195'],
            ['S_120', '__$__', 'S_195'],
            ['S_122', '__$__', 'S_195'],
            ['S_124', '__$__', 'S_195'],
            ['S_126', '__$__', 'S_195'],
            ['S_128', '__$__', 'S_195'],
            ['S_130', '__$__', 'S_195'],
            ['S_132', '__$__', 'S_195'],
            ['S_134', '__$__', 'S_195'],
            ['S_136', '__$__', 'S_195'],
            ['S_138', '__$__', 'S_195'],
            ['S_140', '__$__', 'S_195'],
            ['S_142', '__$__', 'S_195'],
            ['S_144', '__$__', 'S_195'],
            ['S_146', '__$__', 'S_195'],
            ['S_148', '__$__', 'S_195'],
            ['S_150', '__$__', 'S_195'],
            ['S_152', '__$__', 'S_195'],
            ['S_154', '__$__', 'S_195'],
            ['S_156', '__$__', 'S_195'],
            ['S_158', '__$__', 'S_195'],
            ['S_160', '__$__', 'S_195'],
            ['S_162', '__$__', 'S_195'],
            ['S_164', '__$__', 'S_195'],
            ['S_166', '__$__', 'S_195'],
            ['S_168', '__$__', 'S_195'],
            ['S_170', '__$__', 'S_195'],
            ['S_172', '__$__', 'S_195'],
            ['S_174', '__$__', 'S_195'],
            ['S_176', '__$__', 'S_195'],
            ['S_178', '__$__', 'S_195'],
            ['S_180', '__$__', 'S_195'],
            ['S_182', '__$__', 'S_195'],
            ['S_184', '__$__', 'S_195'],
            ['S_186', '__$__', 'S_195'],
            ['S_188', '__$__', 'S_195'],
            ['S_190', '__$__', 'S_195'],
            ['S_192', '__$__', 'S_195'],
            ['S_194', '__$__', 'S_195']
        ]
        t_0, is_accepted = driver(t_in)

        if may_i_eat:
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        elif is_accepted:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 7

        return t_0.count("|")


if __name__ == '__main__':
    TTL = 15

    while SOURCE_CODE != "":
        TTL -= 1
        MAX_EATER_NUMBER -= 1
        MAX_EATER_POINTER = -1

        f_0()
        f_1()
        f_2()
        f_3()
        f_4()
        f_5()
        f_6()
        f_7()

        print("MAX_EATER_NUMBER", MAX_EATER_NUMBER)
        if MAX_EATER_POINTER == 0:
            f_0(True)
        elif MAX_EATER_POINTER == 1:
            f_1(True)
        elif MAX_EATER_POINTER == 2:
            f_2(True)
        elif MAX_EATER_POINTER == 3:
            f_3(True)
        elif MAX_EATER_POINTER == 4:
            f_4(True)
        elif MAX_EATER_POINTER == 5:
            f_5(True)
        elif MAX_EATER_POINTER == 6:
            f_6(True)
        elif MAX_EATER_POINTER == 7:
            f_7(True)
        print(100 * "*")
        print(list(SOURCE_CODE))
        print(SOURCE_CODE)
        [print(i) for i in OUTPUT]
        print(CURRENT_STATE)
        if MAX_EATER_NUMBER < 0:
            SOURCE_CODE = SOURCE_CODE[1:]
    # file = [i[:-1] for i in open("lexer.py").readlines()]
    # [print("lexer_code.append(\"" + str(i) + "\")") for i in file]
    pass
