def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0
    l = len(needle)
    for i in range(len(haystack) - l + 1):
        if haystack[i:i + l] == needle:
            return i

strStr("haystack", "st")
