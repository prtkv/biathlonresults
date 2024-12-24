from enum import Enum, IntEnum


class LevelType(IntEnum):
    ALL_LEVELS = -1  # includes all levels (1-6)
    ALL = 0  # includes levels 1-4
    BMW_IBU_WC = 1  # world cup, that's what you need
    IBU_CUP = 2
    JR_CUP = 3
    OTH = 4
    REG = 5
    PARA = 6


class AnalysisType(Enum):
    TOTAL_COURSE_TIME = "CRST"
    TOTAL_RANGE_TIME = "RNGT"
    TOTAL_SHOOTING_TIME = "STTM"
    SKI_TIME = "SKIT"
    PURSUIT_TIME = "PURS"
    BEST_WOMEN = "BSTW"
    BEST_MEN = "BSTM"
    RESULTS_LEG_1 = "FI1L"
    RESULTS_LEG_2 = "FI2L"
    RESULTS_LEG_3 = "FI3L"
    RESULTS_LEG_4 = "FI4L"
    COURSE_TIME_LEG_1 = "CRST1"
    COURSE_TIME_LEG_2 = "CRST2"
    COURSE_TIME_LEG_3 = "CRST3"
    COURSE_TIME_LEG_4 = "CRST4"
    RANGE_TIME_LEG_1 = "RNGT1"
    RANGE_TIME_LEG_2 = "RNGT2"
    RANGE_TIME_LEG_3 = "RNGT3"
    RANGE_TIME_LEG_4 = "RNGT4"
    COURSE_TIME_LAP_1 = "CRS1"
    COURSE_TIME_LAP_2 = "CRS2"
    COURSE_TIME_LAP_3 = "CRS3"
    COURSE_TIME_LAP_4 = "CRS4"
    COURSE_TIME_LAP_5 = "CRS5"
    COURSE_TIME_LAP_6 = "CRS6"
    COURSE_TIME_LAP_7 = "CRS7"
    COURSE_TIME_LAP_8 = "CRS8"
    COURSE_TIME_LAP_9 = "CRS9"
    COURSE_TIME_LAP_10 = "CRS10"
    COURSE_TIME_LAP_11 = "CRS11"
    COURSE_TIME_LAP_12 = "CRS12"
    RANGE_TIME_1 = "RNG1"
    RANGE_TIME_2 = "RNG2"
    RANGE_TIME_3 = "RNG3"
    RANGE_TIME_4 = "RNG4"
    RANGE_TIME_5 = "RNG5"
    RANGE_TIME_6 = "RNG6"
    RANGE_TIME_7 = "RNG7"
    RANGE_TIME_8 = "RNG8"
    SHOOTING_TIME_1 = "S1TM"
    SHOOTING_TIME_2 = "S2TM"
    SHOOTING_TIME_3 = "S3TM"
    SHOOTING_TIME_4 = "S4TM"
    SHOOTING_TIME_5 = "S5TM"
    SHOOTING_TIME_6 = "S6TM"
    SHOOTING_TIME_7 = "S7TM"
    SHOOTING_TIME_8 = "S8TM"
