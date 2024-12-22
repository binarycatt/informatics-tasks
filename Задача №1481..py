a, b, n = map(int, input().split())

price_per_item_in_kopecks = a * 100 + b
total_price_in_kopecks = price_per_item_in_kopecks * n
total_rubles = total_price_in_kopecks // 100
total_kopecks = total_price_in_kopecks % 100

print(total_rubles, total_kopecks)