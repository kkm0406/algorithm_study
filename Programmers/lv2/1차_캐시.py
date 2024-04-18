from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    time = 0
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if not cache:  # miss
            cache.append(city)
            time += 5
        else:
            if city in cache:  # hit
                time += 1
                cache.remove(city)
                cache.append(city)
            else:  # miss
                time += 5
                if len(cache) < cacheSize:
                    cache.append(city)
                elif len(cache) == cacheSize:
                    cache.popleft()
                    cache.append(city)

    return time