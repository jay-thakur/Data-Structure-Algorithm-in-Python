import heapq

q = []

heapq.heappush(q, (2, 'whatsapp'))
heapq.heappush(q, (0, 'facebook'))
heapq.heappush(q, (1, 'twitter'))
heapq.heappush(q, (3, 'linkedin'))

while q:
    next_item = heapq.heappop(q)
    print(next_item)
    