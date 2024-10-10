#!/usr/bin/env python3
'''takes a mixed list of integers and
floats and returns their sum as a float'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''sum'''
    return float(sum(mxd_lst))
