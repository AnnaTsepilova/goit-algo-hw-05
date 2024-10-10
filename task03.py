import timeit


def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0:
        return 0

    skip = {}
    for k in range(m - 1):
        skip[pattern[k]] = m - k - 1
    skip = skip.get

    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1
        k += skip(text[k], m)
    return -1


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = [0] * m
    j = 0  # індекс для шаблону
    compute_lps(pattern, m, lps)

    i = 0  # індекс для тексту
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j  # знайдено збіг
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def compute_lps(pattern, m, lps):
    length = 0
    lps[0] = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def rabin_karp(text, pattern, d=256, q=101):
    n = len(text)
    m = len(pattern)
    p = 0  # хеш шаблону
    t = 0  # хеш підрядка
    h = 1

    # Значення h буде "d^(m-1) % q"
    for i in range(m-1):
        h = (h * d) % q

    # Обчислення початкового хешу для шаблону та першого вікна тексту
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i+m] == pattern:
                return i

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return -1


# Функція для вимірювання часу виконання пошуку
def measure_time(search_function, text, pattern):
    return timeit.timeit(lambda: search_function(text, pattern), number=1)


# Завантажуємо текстові файли
text1 = open("text1.txt", "r", encoding='windows-1251').read()

text2 = open("text2.txt", "r", encoding='utf-8').read()

# Вибираємо шаблони для тестування
existing_substring = "алгоритм"  # підрядок, який існує в тексті
non_existing_substring = "невідомий"  # вигаданий підрядок

# Вимірюємо час для text1
time_bm_existing_text1 = measure_time(boyer_moore, text1, existing_substring)
time_kmp_existing_text1 = measure_time(kmp_search, text1, existing_substring)
time_rk_existing_text1 = measure_time(rabin_karp, text1, existing_substring)

time_bm_non_existing_text1 = measure_time(boyer_moore, text1, non_existing_substring)
time_kmp_non_existing_text1 = measure_time(kmp_search, text1, non_existing_substring)
time_rk_non_existing_text1 = measure_time(rabin_karp, text1, non_existing_substring)

# Вимірюємо час для text2
time_bm_existing_text2 = measure_time(boyer_moore, text2, existing_substring)
time_kmp_existing_text2 = measure_time(kmp_search, text2, existing_substring)
time_rk_existing_text2 = measure_time(rabin_karp, text2, existing_substring)

time_bm_non_existing_text2 = measure_time(boyer_moore, text2, non_existing_substring)
time_kmp_non_existing_text2 = measure_time(kmp_search, text2, non_existing_substring)
time_rk_non_existing_text2 = measure_time(rabin_karp, text2, non_existing_substring)

# Виводимо результати
print("Text 1, existing substring:")
print(f"Boyer-Moore: {time_bm_existing_text1}")
print(f"KMP: {time_kmp_existing_text1}")
print(f"Rabin-Karp: {time_rk_existing_text1}")

print("Text 1, non-existing substring:")
print(f"Boyer-Moore: {time_bm_non_existing_text1}")
print(f"KMP: {time_kmp_non_existing_text1}")
print(f"Rabin-Karp: {time_rk_non_existing_text1}")

print("Text 2, existing substring:")
print(f"Boyer-Moore: {time_bm_existing_text2}")
print(f"KMP: {time_kmp_existing_text2}")
print(f"Rabin-Karp: {time_rk_existing_text2}")

print("Text 2, non-existing substring:")
print(f"Boyer-Moore: {time_bm_non_existing_text2}")
print(f"KMP: {time_kmp_non_existing_text2}")
print(f"Rabin-Karp: {time_rk_non_existing_text2}")
