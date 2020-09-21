import sys

_frame = sys._getframe()
_frame.f_back.f_code.co_filename # 调用该函数的文件名
_frame.f_back.f_lineno # 行号
_frame.f_back.f_code.co_name # 调用函数名
