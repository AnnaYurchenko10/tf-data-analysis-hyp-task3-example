import pandas as pd
import numpy as np


chat_id = 762047857 # Ваш chat ID, не меняйте название переменной

def solution(...) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Установленный порог затрат
    threshold = 300
    
    # Уровень значимости
    level = 0.1
    
    # Проведение одновыборочного t-теста
    t_statistic, p_value = stats.ttest_1samp(..., popmean=threshold)
    
    # Возвращаем True, если нулевая гипотеза отклоняется
    return (p_value / 2 < level) and (t_statistic < 0)
