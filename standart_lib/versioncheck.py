import sys, warnings
if sys.version_info[0] < 4:
    warnings.warn("Необходима версия Python 4.0 или выше", RuntimeWarning)
else:
    print('Нормальное предложение')