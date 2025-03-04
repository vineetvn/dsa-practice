def longestCommonPrefix(strs):
    pref = strs[0]
    pref_len = len(pref)

    for s in strs[1:]:
        while pref != s[0:pref_len]:
            pref_len -= 1
            if pref_len == 0:
                return ""

            pref = pref[0:pref_len]

    return pref


print(longestCommonPrefix(["flower", "flow", "flight"]))
