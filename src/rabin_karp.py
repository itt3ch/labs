def func_karp(haystack, needle, base=256, prime=31):

    if not haystack or not needle or len(haystack) < len(needle):
        return []

    needle_hash = 0
    haystack_hash = 0
    indices = []


    for i in range(len(needle)):
        needle_hash = (needle_hash * base + ord(needle[i])) % prime
        haystack_hash = (haystack_hash * base + ord(haystack[i])) % prime


    for i in range(len(haystack)- len(needle)+ 1):
        if haystack_hash == needle_hash:
            if haystack[i:i+len(needle)] == needle:
                indices.append(i)
        if i < len(haystack) - len(needle):
            haystack_hash = (base * (haystack_hash - ord(haystack[i]) * (base ** (len(needle) - 1))) + ord(haystack[i + len(needle)])) % prime
            if haystack_hash < 0:
                haystack_hash += prime

    return indices


haystack = "programming program"
needle = "program"
print("Індекси підстрічки:", func_karp(haystack, needle))
