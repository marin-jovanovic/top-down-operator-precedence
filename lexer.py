from nfa.main import driver

MAX_EATER_NUMBER = -1
MAX_EATER_POINTER = -1
SOURCE_CODE = "".join([i for i in open("test_cases/minusLang.in").readlines()])
CURRENT_STATE = "S_pocetno"
OUTPUT = list()
LINE_NUMBER = 1


def f_0(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_pocetno', '\\t|\\_', ['-']]
    if CURRENT_STATE == "S_pocetno":
        print(0)
        t_in = [
            str(SOURCE_CODE),
            ['S_1', 'S_2'],
            "S_0",
            ['S_0', '\t', 'S_1'],
            ['S_0', ' ', 'S_2']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 0

        return t_0.count("|")


def f_1(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_pocetno', '\\n', ['-', 'NOVI_REDAK']]
    if CURRENT_STATE == "S_pocetno":
        print(1)
        t_in = [
            str(SOURCE_CODE),
            ['S_1'],
            "S_0",
            ['S_0', '\n', 'S_1']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            LINE_NUMBER += 1
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 1

        return t_0.count("|")


def f_2(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_pocetno', '#\\|', ['-', 'UDJI_U_STANJE S_komentar']]
    if CURRENT_STATE == "S_pocetno":
        print(2)
        t_in = [
            str(SOURCE_CODE),
            ['S_2'],
            "S_0",
            ['S_0', '#', 'S_1'],
            ['S_1', '|', 'S_2']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            CURRENT_STATE = "S_komentar"
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 2

        return t_0.count("|")


def f_3(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_komentar', '\\|#', ['-', 'UDJI_U_STANJE S_pocetno']]
    if CURRENT_STATE == "S_komentar":
        print(3)
        t_in = [
            str(SOURCE_CODE),
            ['S_2'],
            "S_0",
            ['S_0', '|', 'S_1'],
            ['S_1', '#', 'S_2']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            CURRENT_STATE = "S_pocetno"
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 3

        return t_0.count("|")


def f_4(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_komentar', '\\n', ['-', 'NOVI_REDAK']]
    if CURRENT_STATE == "S_komentar":
        print(4)
        t_in = [
            str(SOURCE_CODE),
            ['S_1'],
            "S_0",
            ['S_0', '\n', 'S_1']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            LINE_NUMBER += 1
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 4

        return t_0.count("|")


def f_5(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_komentar', '(\\(|\\)|\\{|\\}|\\||\\*|\\\\|\\$|\\t|\\n|\\_|!|"|#|%|&|\'|+|,|-|.|/|0|1|2|3|4|5|6|7|8|9|:|;|<|=|>|?|@|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|[|]|^|_|`|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|~)', ['-']]
    if CURRENT_STATE == "S_komentar":
        print(5)
        t_in = [
            str(SOURCE_CODE),
            ['S_194'],
            "S_0",
            ['S_0', '$', 'S_1'],
            ['S_1', '(', 'S_2'],
            ['S_0', '$', 'S_3'],
            ['S_3', ')', 'S_4'],
            ['S_0', '$', 'S_5'],
            ['S_5', '{', 'S_6'],
            ['S_0', '$', 'S_7'],
            ['S_7', '}', 'S_8'],
            ['S_0', '$', 'S_9'],
            ['S_9', '|', 'S_10'],
            ['S_0', '$', 'S_11'],
            ['S_11', '\\*', 'S_12'],
            ['S_0', '$', 'S_13'],
            ['S_13', '\\', 'S_14'],
            ['S_0', '$', 'S_15'],
            ['S_15', '$', 'S_16'],
            ['S_0', '$', 'S_17'],
            ['S_17', '\t', 'S_18'],
            ['S_0', '$', 'S_19'],
            ['S_19', '\n', 'S_20'],
            ['S_0', '$', 'S_21'],
            ['S_21', ' ', 'S_22'],
            ['S_0', '$', 'S_23'],
            ['S_23', '!', 'S_24'],
            ['S_0', '$', 'S_25'],
            ['S_25', '"', 'S_26'],
            ['S_0', '$', 'S_27'],
            ['S_27', '#', 'S_28'],
            ['S_0', '$', 'S_29'],
            ['S_29', '%', 'S_30'],
            ['S_0', '$', 'S_31'],
            ['S_31', '&', 'S_32'],
            ['S_0', '$', 'S_33'],
            ['S_33', "'", 'S_34'],
            ['S_0', '$', 'S_35'],
            ['S_35', '+', 'S_36'],
            ['S_0', '$', 'S_37'],
            ['S_37', ',', 'S_38'],
            ['S_0', '$', 'S_39'],
            ['S_39', '-', 'S_40'],
            ['S_0', '$', 'S_41'],
            ['S_41', '.', 'S_42'],
            ['S_0', '$', 'S_43'],
            ['S_43', '/', 'S_44'],
            ['S_0', '$', 'S_45'],
            ['S_45', '0', 'S_46'],
            ['S_0', '$', 'S_47'],
            ['S_47', '1', 'S_48'],
            ['S_0', '$', 'S_49'],
            ['S_49', '2', 'S_50'],
            ['S_0', '$', 'S_51'],
            ['S_51', '3', 'S_52'],
            ['S_0', '$', 'S_53'],
            ['S_53', '4', 'S_54'],
            ['S_0', '$', 'S_55'],
            ['S_55', '5', 'S_56'],
            ['S_0', '$', 'S_57'],
            ['S_57', '6', 'S_58'],
            ['S_0', '$', 'S_59'],
            ['S_59', '7', 'S_60'],
            ['S_0', '$', 'S_61'],
            ['S_61', '8', 'S_62'],
            ['S_0', '$', 'S_63'],
            ['S_63', '9', 'S_64'],
            ['S_0', '$', 'S_65'],
            ['S_65', ':', 'S_66'],
            ['S_0', '$', 'S_67'],
            ['S_67', ';', 'S_68'],
            ['S_0', '$', 'S_69'],
            ['S_69', '<', 'S_70'],
            ['S_0', '$', 'S_71'],
            ['S_71', '=', 'S_72'],
            ['S_0', '$', 'S_73'],
            ['S_73', '>', 'S_74'],
            ['S_0', '$', 'S_75'],
            ['S_75', '?', 'S_76'],
            ['S_0', '$', 'S_77'],
            ['S_77', '@', 'S_78'],
            ['S_0', '$', 'S_79'],
            ['S_79', 'A', 'S_80'],
            ['S_0', '$', 'S_81'],
            ['S_81', 'B', 'S_82'],
            ['S_0', '$', 'S_83'],
            ['S_83', 'C', 'S_84'],
            ['S_0', '$', 'S_85'],
            ['S_85', 'D', 'S_86'],
            ['S_0', '$', 'S_87'],
            ['S_87', 'E', 'S_88'],
            ['S_0', '$', 'S_89'],
            ['S_89', 'F', 'S_90'],
            ['S_0', '$', 'S_91'],
            ['S_91', 'G', 'S_92'],
            ['S_0', '$', 'S_93'],
            ['S_93', 'H', 'S_94'],
            ['S_0', '$', 'S_95'],
            ['S_95', 'I', 'S_96'],
            ['S_0', '$', 'S_97'],
            ['S_97', 'J', 'S_98'],
            ['S_0', '$', 'S_99'],
            ['S_99', 'K', 'S_100'],
            ['S_0', '$', 'S_101'],
            ['S_101', 'L', 'S_102'],
            ['S_0', '$', 'S_103'],
            ['S_103', 'M', 'S_104'],
            ['S_0', '$', 'S_105'],
            ['S_105', 'N', 'S_106'],
            ['S_0', '$', 'S_107'],
            ['S_107', 'O', 'S_108'],
            ['S_0', '$', 'S_109'],
            ['S_109', 'P', 'S_110'],
            ['S_0', '$', 'S_111'],
            ['S_111', 'Q', 'S_112'],
            ['S_0', '$', 'S_113'],
            ['S_113', 'R', 'S_114'],
            ['S_0', '$', 'S_115'],
            ['S_115', 'S', 'S_116'],
            ['S_0', '$', 'S_117'],
            ['S_117', 'T', 'S_118'],
            ['S_0', '$', 'S_119'],
            ['S_119', 'U', 'S_120'],
            ['S_0', '$', 'S_121'],
            ['S_121', 'V', 'S_122'],
            ['S_0', '$', 'S_123'],
            ['S_123', 'W', 'S_124'],
            ['S_0', '$', 'S_125'],
            ['S_125', 'X', 'S_126'],
            ['S_0', '$', 'S_127'],
            ['S_127', 'Y', 'S_128'],
            ['S_0', '$', 'S_129'],
            ['S_129', 'Z', 'S_130'],
            ['S_0', '$', 'S_131'],
            ['S_131', '[', 'S_132'],
            ['S_0', '$', 'S_133'],
            ['S_133', ']', 'S_134'],
            ['S_0', '$', 'S_135'],
            ['S_135', '^', 'S_136'],
            ['S_0', '$', 'S_137'],
            ['S_137', '_', 'S_138'],
            ['S_0', '$', 'S_139'],
            ['S_139', '`', 'S_140'],
            ['S_0', '$', 'S_141'],
            ['S_141', 'a', 'S_142'],
            ['S_0', '$', 'S_143'],
            ['S_143', 'b', 'S_144'],
            ['S_0', '$', 'S_145'],
            ['S_145', 'c', 'S_146'],
            ['S_0', '$', 'S_147'],
            ['S_147', 'd', 'S_148'],
            ['S_0', '$', 'S_149'],
            ['S_149', 'e', 'S_150'],
            ['S_0', '$', 'S_151'],
            ['S_151', 'f', 'S_152'],
            ['S_0', '$', 'S_153'],
            ['S_153', 'g', 'S_154'],
            ['S_0', '$', 'S_155'],
            ['S_155', 'h', 'S_156'],
            ['S_0', '$', 'S_157'],
            ['S_157', 'i', 'S_158'],
            ['S_0', '$', 'S_159'],
            ['S_159', 'j', 'S_160'],
            ['S_0', '$', 'S_161'],
            ['S_161', 'k', 'S_162'],
            ['S_0', '$', 'S_163'],
            ['S_163', 'l', 'S_164'],
            ['S_0', '$', 'S_165'],
            ['S_165', 'm', 'S_166'],
            ['S_0', '$', 'S_167'],
            ['S_167', 'n', 'S_168'],
            ['S_0', '$', 'S_169'],
            ['S_169', 'o', 'S_170'],
            ['S_0', '$', 'S_171'],
            ['S_171', 'p', 'S_172'],
            ['S_0', '$', 'S_173'],
            ['S_173', 'q', 'S_174'],
            ['S_0', '$', 'S_175'],
            ['S_175', 'r', 'S_176'],
            ['S_0', '$', 'S_177'],
            ['S_177', 's', 'S_178'],
            ['S_0', '$', 'S_179'],
            ['S_179', 't', 'S_180'],
            ['S_0', '$', 'S_181'],
            ['S_181', 'u', 'S_182'],
            ['S_0', '$', 'S_183'],
            ['S_183', 'v', 'S_184'],
            ['S_0', '$', 'S_185'],
            ['S_185', 'w', 'S_186'],
            ['S_0', '$', 'S_187'],
            ['S_187', 'x', 'S_188'],
            ['S_0', '$', 'S_189'],
            ['S_189', 'y', 'S_190'],
            ['S_0', '$', 'S_191'],
            ['S_191', 'z', 'S_192'],
            ['S_0', '$', 'S_193'],
            ['S_2', '$', 'S_194'],
            ['S_4', '$', 'S_194'],
            ['S_6', '$', 'S_194'],
            ['S_8', '$', 'S_194'],
            ['S_10', '$', 'S_194'],
            ['S_12', '$', 'S_194'],
            ['S_14', '$', 'S_194'],
            ['S_16', '$', 'S_194'],
            ['S_18', '$', 'S_194'],
            ['S_20', '$', 'S_194'],
            ['S_22', '$', 'S_194'],
            ['S_24', '$', 'S_194'],
            ['S_26', '$', 'S_194'],
            ['S_28', '$', 'S_194'],
            ['S_30', '$', 'S_194'],
            ['S_32', '$', 'S_194'],
            ['S_34', '$', 'S_194'],
            ['S_36', '$', 'S_194'],
            ['S_38', '$', 'S_194'],
            ['S_40', '$', 'S_194'],
            ['S_42', '$', 'S_194'],
            ['S_44', '$', 'S_194'],
            ['S_46', '$', 'S_194'],
            ['S_48', '$', 'S_194'],
            ['S_50', '$', 'S_194'],
            ['S_52', '$', 'S_194'],
            ['S_54', '$', 'S_194'],
            ['S_56', '$', 'S_194'],
            ['S_58', '$', 'S_194'],
            ['S_60', '$', 'S_194'],
            ['S_62', '$', 'S_194'],
            ['S_64', '$', 'S_194'],
            ['S_66', '$', 'S_194'],
            ['S_68', '$', 'S_194'],
            ['S_70', '$', 'S_194'],
            ['S_72', '$', 'S_194'],
            ['S_74', '$', 'S_194'],
            ['S_76', '$', 'S_194'],
            ['S_78', '$', 'S_194'],
            ['S_80', '$', 'S_194'],
            ['S_82', '$', 'S_194'],
            ['S_84', '$', 'S_194'],
            ['S_86', '$', 'S_194'],
            ['S_88', '$', 'S_194'],
            ['S_90', '$', 'S_194'],
            ['S_92', '$', 'S_194'],
            ['S_94', '$', 'S_194'],
            ['S_96', '$', 'S_194'],
            ['S_98', '$', 'S_194'],
            ['S_100', '$', 'S_194'],
            ['S_102', '$', 'S_194'],
            ['S_104', '$', 'S_194'],
            ['S_106', '$', 'S_194'],
            ['S_108', '$', 'S_194'],
            ['S_110', '$', 'S_194'],
            ['S_112', '$', 'S_194'],
            ['S_114', '$', 'S_194'],
            ['S_116', '$', 'S_194'],
            ['S_118', '$', 'S_194'],
            ['S_120', '$', 'S_194'],
            ['S_122', '$', 'S_194'],
            ['S_124', '$', 'S_194'],
            ['S_126', '$', 'S_194'],
            ['S_128', '$', 'S_194'],
            ['S_130', '$', 'S_194'],
            ['S_132', '$', 'S_194'],
            ['S_134', '$', 'S_194'],
            ['S_136', '$', 'S_194'],
            ['S_138', '$', 'S_194'],
            ['S_140', '$', 'S_194'],
            ['S_142', '$', 'S_194'],
            ['S_144', '$', 'S_194'],
            ['S_146', '$', 'S_194'],
            ['S_148', '$', 'S_194'],
            ['S_150', '$', 'S_194'],
            ['S_152', '$', 'S_194'],
            ['S_154', '$', 'S_194'],
            ['S_156', '$', 'S_194'],
            ['S_158', '$', 'S_194'],
            ['S_160', '$', 'S_194'],
            ['S_162', '$', 'S_194'],
            ['S_164', '$', 'S_194'],
            ['S_166', '$', 'S_194'],
            ['S_168', '$', 'S_194'],
            ['S_170', '$', 'S_194'],
            ['S_172', '$', 'S_194'],
            ['S_174', '$', 'S_194'],
            ['S_176', '$', 'S_194'],
            ['S_178', '$', 'S_194'],
            ['S_180', '$', 'S_194'],
            ['S_182', '$', 'S_194'],
            ['S_184', '$', 'S_194'],
            ['S_186', '$', 'S_194'],
            ['S_188', '$', 'S_194'],
            ['S_190', '$', 'S_194'],
            ['S_192', '$', 'S_194'],
            ['S_193', '$', 'S_194']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 5

        return t_0.count("|")


def f_6(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_pocetno', '((0|1|2|3|4|5|6|7|8|9)(0|1|2|3|4|5|6|7|8|9)*|0x((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D|E|F)((0|1|2|3|4|5|6|7|8|9)|a|b|c|d|e|f|A|B|C|D|E|F)*)', ['OPERAND']]
    if CURRENT_STATE == "S_pocetno":
        print(6)
        t_in = [
            str(SOURCE_CODE),
            ['S_136'],
            "S_0",
            ['S_0', '$', 'S_1'],
            ['S_1', '$', 'S_2'],
            ['S_2', '0', 'S_3'],
            ['S_1', '$', 'S_4'],
            ['S_4', '1', 'S_5'],
            ['S_1', '$', 'S_6'],
            ['S_6', '2', 'S_7'],
            ['S_1', '$', 'S_8'],
            ['S_8', '3', 'S_9'],
            ['S_1', '$', 'S_10'],
            ['S_10', '4', 'S_11'],
            ['S_1', '$', 'S_12'],
            ['S_12', '5', 'S_13'],
            ['S_1', '$', 'S_14'],
            ['S_14', '6', 'S_15'],
            ['S_1', '$', 'S_16'],
            ['S_16', '7', 'S_17'],
            ['S_1', '$', 'S_18'],
            ['S_18', '8', 'S_19'],
            ['S_1', '$', 'S_20'],
            ['S_3', '$', 'S_21'],
            ['S_5', '$', 'S_21'],
            ['S_7', '$', 'S_21'],
            ['S_9', '$', 'S_21'],
            ['S_11', '$', 'S_21'],
            ['S_13', '$', 'S_21'],
            ['S_15', '$', 'S_21'],
            ['S_17', '$', 'S_21'],
            ['S_19', '$', 'S_21'],
            ['S_20', '$', 'S_21'],
            ['S_21', '$', 'S_22'],
            ['S_22', '0', 'S_23'],
            ['S_21', '$', 'S_24'],
            ['S_24', '1', 'S_25'],
            ['S_21', '$', 'S_26'],
            ['S_26', '2', 'S_27'],
            ['S_21', '$', 'S_28'],
            ['S_28', '3', 'S_29'],
            ['S_21', '$', 'S_30'],
            ['S_30', '4', 'S_31'],
            ['S_21', '$', 'S_32'],
            ['S_32', '5', 'S_33'],
            ['S_21', '$', 'S_34'],
            ['S_34', '6', 'S_35'],
            ['S_21', '$', 'S_36'],
            ['S_36', '7', 'S_37'],
            ['S_21', '$', 'S_38'],
            ['S_38', '8', 'S_39'],
            ['S_21', '$', 'S_40'],
            ['S_40', '9', 'S_41'],
            ['S_23', '$', 'S_42'],
            ['S_25', '$', 'S_42'],
            ['S_27', '$', 'S_42'],
            ['S_29', '$', 'S_42'],
            ['S_31', '$', 'S_42'],
            ['S_33', '$', 'S_42'],
            ['S_35', '$', 'S_42'],
            ['S_37', '$', 'S_42'],
            ['S_39', '$', 'S_42'],
            ['S_41', '$', 'S_42'],
            ['S_23', '$', 'S_21'],
            ['S_25', '$', 'S_21'],
            ['S_27', '$', 'S_21'],
            ['S_29', '$', 'S_21'],
            ['S_31', '$', 'S_21'],
            ['S_33', '$', 'S_21'],
            ['S_35', '$', 'S_21'],
            ['S_37', '$', 'S_21'],
            ['S_39', '$', 'S_21'],
            ['S_41', '$', 'S_21'],
            ['S_21', '$', 'S_42'],
            ['S_0', '$', 'S_43'],
            ['S_43', '0', 'S_44'],
            ['S_44', 'x', 'S_45'],
            ['S_45', '$', 'S_46'],
            ['S_46', '$', 'S_47'],
            ['S_47', '0', 'S_48'],
            ['S_46', '$', 'S_49'],
            ['S_49', '1', 'S_50'],
            ['S_46', '$', 'S_51'],
            ['S_51', '2', 'S_52'],
            ['S_46', '$', 'S_53'],
            ['S_53', '3', 'S_54'],
            ['S_46', '$', 'S_55'],
            ['S_55', '4', 'S_56'],
            ['S_46', '$', 'S_57'],
            ['S_57', '5', 'S_58'],
            ['S_46', '$', 'S_59'],
            ['S_59', '6', 'S_60'],
            ['S_46', '$', 'S_61'],
            ['S_61', '7', 'S_62'],
            ['S_46', '$', 'S_63'],
            ['S_63', '8', 'S_64'],
            ['S_46', '$', 'S_65'],
            ['S_48', '$', 'S_66'],
            ['S_50', '$', 'S_66'],
            ['S_52', '$', 'S_66'],
            ['S_54', '$', 'S_66'],
            ['S_56', '$', 'S_66'],
            ['S_58', '$', 'S_66'],
            ['S_60', '$', 'S_66'],
            ['S_62', '$', 'S_66'],
            ['S_64', '$', 'S_66'],
            ['S_65', '$', 'S_66'],
            ['S_45', '$', 'S_67'],
            ['S_67', 'a', 'S_68'],
            ['S_45', '$', 'S_69'],
            ['S_69', 'b', 'S_70'],
            ['S_45', '$', 'S_71'],
            ['S_71', 'c', 'S_72'],
            ['S_45', '$', 'S_73'],
            ['S_73', 'd', 'S_74'],
            ['S_45', '$', 'S_75'],
            ['S_75', 'e', 'S_76'],
            ['S_45', '$', 'S_77'],
            ['S_77', 'f', 'S_78'],
            ['S_45', '$', 'S_79'],
            ['S_79', 'A', 'S_80'],
            ['S_45', '$', 'S_81'],
            ['S_81', 'B', 'S_82'],
            ['S_45', '$', 'S_83'],
            ['S_83', 'C', 'S_84'],
            ['S_45', '$', 'S_85'],
            ['S_85', 'D', 'S_86'],
            ['S_45', '$', 'S_87'],
            ['S_87', 'E', 'S_88'],
            ['S_45', '$', 'S_89'],
            ['S_66', '$', 'S_90'],
            ['S_68', '$', 'S_90'],
            ['S_70', '$', 'S_90'],
            ['S_72', '$', 'S_90'],
            ['S_74', '$', 'S_90'],
            ['S_76', '$', 'S_90'],
            ['S_78', '$', 'S_90'],
            ['S_80', '$', 'S_90'],
            ['S_82', '$', 'S_90'],
            ['S_84', '$', 'S_90'],
            ['S_86', '$', 'S_90'],
            ['S_88', '$', 'S_90'],
            ['S_89', '$', 'S_90'],
            ['S_90', '$', 'S_91'],
            ['S_91', '$', 'S_92'],
            ['S_92', '0', 'S_93'],
            ['S_91', '$', 'S_94'],
            ['S_94', '1', 'S_95'],
            ['S_91', '$', 'S_96'],
            ['S_96', '2', 'S_97'],
            ['S_91', '$', 'S_98'],
            ['S_98', '3', 'S_99'],
            ['S_91', '$', 'S_100'],
            ['S_100', '4', 'S_101'],
            ['S_91', '$', 'S_102'],
            ['S_102', '5', 'S_103'],
            ['S_91', '$', 'S_104'],
            ['S_104', '6', 'S_105'],
            ['S_91', '$', 'S_106'],
            ['S_106', '7', 'S_107'],
            ['S_91', '$', 'S_108'],
            ['S_108', '8', 'S_109'],
            ['S_91', '$', 'S_110'],
            ['S_93', '$', 'S_111'],
            ['S_95', '$', 'S_111'],
            ['S_97', '$', 'S_111'],
            ['S_99', '$', 'S_111'],
            ['S_101', '$', 'S_111'],
            ['S_103', '$', 'S_111'],
            ['S_105', '$', 'S_111'],
            ['S_107', '$', 'S_111'],
            ['S_109', '$', 'S_111'],
            ['S_110', '$', 'S_111'],
            ['S_90', '$', 'S_112'],
            ['S_112', 'a', 'S_113'],
            ['S_90', '$', 'S_114'],
            ['S_114', 'b', 'S_115'],
            ['S_90', '$', 'S_116'],
            ['S_116', 'c', 'S_117'],
            ['S_90', '$', 'S_118'],
            ['S_118', 'd', 'S_119'],
            ['S_90', '$', 'S_120'],
            ['S_120', 'e', 'S_121'],
            ['S_90', '$', 'S_122'],
            ['S_122', 'f', 'S_123'],
            ['S_90', '$', 'S_124'],
            ['S_124', 'A', 'S_125'],
            ['S_90', '$', 'S_126'],
            ['S_126', 'B', 'S_127'],
            ['S_90', '$', 'S_128'],
            ['S_128', 'C', 'S_129'],
            ['S_90', '$', 'S_130'],
            ['S_130', 'D', 'S_131'],
            ['S_90', '$', 'S_132'],
            ['S_132', 'E', 'S_133'],
            ['S_90', '$', 'S_134'],
            ['S_111', '$', 'S_135'],
            ['S_113', '$', 'S_135'],
            ['S_115', '$', 'S_135'],
            ['S_117', '$', 'S_135'],
            ['S_119', '$', 'S_135'],
            ['S_121', '$', 'S_135'],
            ['S_123', '$', 'S_135'],
            ['S_125', '$', 'S_135'],
            ['S_127', '$', 'S_135'],
            ['S_129', '$', 'S_135'],
            ['S_131', '$', 'S_135'],
            ['S_133', '$', 'S_135'],
            ['S_134', '$', 'S_135'],
            ['S_42', '$', 'S_136'],
            ['S_135', '$', 'S_136']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            OUTPUT.append("OPERAND " + str(LINE_NUMBER) + " " + SOURCE_CODE[:MAX_EATER_NUMBER])
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 6

        return t_0.count("|")


def f_7(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_pocetno', '\\(', ['LIJEVA_ZAGRADA']]
    if CURRENT_STATE == "S_pocetno":
        print(7)
        t_in = [
            str(SOURCE_CODE),
            ['S_1'],
            "S_0",
            ['S_0', '(', 'S_1']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            OUTPUT.append("LIJEVA_ZAGRADA " + str(LINE_NUMBER) + " " + SOURCE_CODE[:MAX_EATER_NUMBER])
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 7

        return t_0.count("|")


def f_8(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_pocetno', '\\)', ['DESNA_ZAGRADA']]
    if CURRENT_STATE == "S_pocetno":
        print(8)
        t_in = [
            str(SOURCE_CODE),
            ['S_1'],
            "S_0",
            ['S_0', ')', 'S_1']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            OUTPUT.append("DESNA_ZAGRADA " + str(LINE_NUMBER) + " " + SOURCE_CODE[:MAX_EATER_NUMBER])
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 8

        return t_0.count("|")


def f_9(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_pocetno', '-', ['OP_MINUS']]
    if CURRENT_STATE == "S_pocetno":
        print(9)
        t_in = [
            str(SOURCE_CODE),
            ['S_1'],
            "S_0",
            ['S_0', '-', 'S_1']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            OUTPUT.append("OP_MINUS " + str(LINE_NUMBER) + " " + SOURCE_CODE[:MAX_EATER_NUMBER])
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 9

        return t_0.count("|")


def f_10(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_pocetno', '-(\\t|\\n|\\_)*-', ['OP_MINUS', 'UDJI_U_STANJE S_unarni', 'VRATI_SE 1']]
    if CURRENT_STATE == "S_pocetno":
        print(10)
        t_in = [
            str(SOURCE_CODE),
            ['S_9'],
            "S_0",
            ['S_0', '-', 'S_1'],
            ['S_1', '$', 'S_2'],
            ['S_2', '\t', 'S_3'],
            ['S_1', '$', 'S_4'],
            ['S_4', '\n', 'S_5'],
            ['S_1', '$', 'S_6'],
            ['S_6', ' ', 'S_7'],
            ['S_3', '$', 'S_8'],
            ['S_5', '$', 'S_8'],
            ['S_7', '$', 'S_8'],
            ['S_3', '$', 'S_1'],
            ['S_5', '$', 'S_1'],
            ['S_7', '$', 'S_1'],
            ['S_1', '$', 'S_8'],
            ['S_8', '-', 'S_9']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            CURRENT_STATE = "S_unarni"
            reduction_value = SOURCE_CODE[:1]
            SOURCE_CODE = SOURCE_CODE[1:]
            OUTPUT.append("OP_MINUS " + str(LINE_NUMBER) + " " + SOURCE_CODE[:1])
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 10

        return t_0.count("|")


def f_11(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_pocetno', '\\((\\t|\\n|\\_)*-', ['LIJEVA_ZAGRADA', 'UDJI_U_STANJE S_unarni', 'VRATI_SE 1']]
    if CURRENT_STATE == "S_pocetno":
        print(11)
        t_in = [
            str(SOURCE_CODE),
            ['S_9'],
            "S_0",
            ['S_0', '(', 'S_1'],
            ['S_1', '$', 'S_2'],
            ['S_2', '\t', 'S_3'],
            ['S_1', '$', 'S_4'],
            ['S_4', '\n', 'S_5'],
            ['S_1', '$', 'S_6'],
            ['S_6', ' ', 'S_7'],
            ['S_3', '$', 'S_8'],
            ['S_5', '$', 'S_8'],
            ['S_7', '$', 'S_8'],
            ['S_3', '$', 'S_1'],
            ['S_5', '$', 'S_1'],
            ['S_7', '$', 'S_1'],
            ['S_1', '$', 'S_8'],
            ['S_8', '-', 'S_9']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            CURRENT_STATE = "S_unarni"
            reduction_value = SOURCE_CODE[:1]
            SOURCE_CODE = SOURCE_CODE[1:]
            OUTPUT.append("LIJEVA_ZAGRADA " + str(LINE_NUMBER) + " " + SOURCE_CODE[:1])
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 11

        return t_0.count("|")


def f_12(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_unarni', '\\t|\\_', ['-']]
    if CURRENT_STATE == "S_unarni":
        print(12)
        t_in = [
            str(SOURCE_CODE),
            ['S_1', 'S_2'],
            "S_0",
            ['S_0', '\t', 'S_1'],
            ['S_0', ' ', 'S_2']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 12

        return t_0.count("|")


def f_13(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_unarni', '\\n', ['-', 'NOVI_REDAK']]
    if CURRENT_STATE == "S_unarni":
        print(13)
        t_in = [
            str(SOURCE_CODE),
            ['S_1'],
            "S_0",
            ['S_0', '\n', 'S_1']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            LINE_NUMBER += 1
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 13

        return t_0.count("|")


def f_14(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_unarni', '-', ['UMINUS', 'UDJI_U_STANJE S_pocetno']]
    if CURRENT_STATE == "S_unarni":
        print(14)
        t_in = [
            str(SOURCE_CODE),
            ['S_1'],
            "S_0",
            ['S_0', '-', 'S_1']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            CURRENT_STATE = "S_pocetno"
            OUTPUT.append("UMINUS " + str(LINE_NUMBER) + " " + SOURCE_CODE[:MAX_EATER_NUMBER])
            SOURCE_CODE = SOURCE_CODE[MAX_EATER_NUMBER:]
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 14

        return t_0.count("|")


def f_15(may_i_eat=False):
    global MAX_EATER_NUMBER, MAX_EATER_POINTER, SOURCE_CODE, CURRENT_STATE, OUTPUT
    global LINE_NUMBER

    # ['S_unarni', '-(\\t|\\n|\\_)*-', ['UMINUS', 'VRATI_SE 1']]
    if CURRENT_STATE == "S_unarni":
        print(15)
        t_in = [
            str(SOURCE_CODE),
            ['S_9'],
            "S_0",
            ['S_0', '-', 'S_1'],
            ['S_1', '$', 'S_2'],
            ['S_2', '\t', 'S_3'],
            ['S_1', '$', 'S_4'],
            ['S_4', '\n', 'S_5'],
            ['S_1', '$', 'S_6'],
            ['S_6', ' ', 'S_7'],
            ['S_3', '$', 'S_8'],
            ['S_5', '$', 'S_8'],
            ['S_7', '$', 'S_8'],
            ['S_3', '$', 'S_1'],
            ['S_5', '$', 'S_1'],
            ['S_7', '$', 'S_1'],
            ['S_1', '$', 'S_8'],
            ['S_8', '-', 'S_9']
        ]
        t_0 = driver(t_in)

        if may_i_eat:
            reduction_value = SOURCE_CODE[:1]
            SOURCE_CODE = SOURCE_CODE[1:]
            OUTPUT.append("UMINUS " + str(LINE_NUMBER) + " " + SOURCE_CODE[:1])
        else:

            if t_0.count("|") > MAX_EATER_NUMBER:
                MAX_EATER_NUMBER = t_0.count("|")
                MAX_EATER_POINTER = 15

        return t_0.count("|")


if __name__ == '__main__':
    TTL = 500

    while TTL != 0:
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
        f_8()
        f_9()
        f_10()
        f_11()
        f_12()
        f_13()
        f_14()
        f_15()

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
        elif MAX_EATER_POINTER == 8:
            f_8(True)
        elif MAX_EATER_POINTER == 9:
            f_9(True)
        elif MAX_EATER_POINTER == 10:
            f_10(True)
        elif MAX_EATER_POINTER == 11:
            f_11(True)
        elif MAX_EATER_POINTER == 12:
            f_12(True)
        elif MAX_EATER_POINTER == 13:
            f_13(True)
        elif MAX_EATER_POINTER == 14:
            f_14(True)
        elif MAX_EATER_POINTER == 15:
            f_15(True)
        print(100 * "*")
        print(list(SOURCE_CODE))
        print(SOURCE_CODE)
        [print(i) for i in OUTPUT]
        print(CURRENT_STATE)
    # file = [i[:-1] for i in open("lexer.py").readlines()]
    # [print("lexer_code.append(\"" + str(i) + "\")") for i in file]
    pass
