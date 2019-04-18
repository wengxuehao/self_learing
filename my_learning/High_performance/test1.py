# 提前结束函数进程执行速度就快一些，减少不必要的循环
def search_fast(haystack,needle):
    for item in haystack:
        if item == needle:
            return True
    return False



def search_slow(haystack,needle):
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
    return return_value

