import pandas as pd
import numpy as np
from scipy import stats


chat_id = 700385968 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    pval = stats.ttest_ind(x, y, equal_var=False).pvalue
    if (pval < 0.05):
      ans = True
    else:
      ans = False
    return ans
