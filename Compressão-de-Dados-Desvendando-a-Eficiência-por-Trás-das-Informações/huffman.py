import heapq
from collections import defaultdict


def build_frequency_table(data):
    frequency_table = defaultdict(int)
    for symbol in data:
        frequency_table[symbol] += 1
    return frequency_table


def build_huffman_tree(frequency_table):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequency_table.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]


def build_huffman_codes(tree):
    codes = {}
    for symbol, code in tree[1:]:
        codes[symbol] = code
    return codes


def compress(data, codes):
    compressed_data = ""
    for symbol in data:
        compressed_data += codes[symbol]
    return compressed_data


def decompress(compressed_data, tree):
    decompressed_data = ""
    current_node = tree
    for bit in compressed_data:
        if bit == '0':
            current_node = current_node[1]
        else:
            current_node = current_node[2]
        if isinstance(current_node[0], str):
            decompressed_data += current_node[0]
            current_node = tree
    return decompressed_data


# Exemplo de uso:
data = "exemplo de texto a ser comprimido"
frequency_table = build_frequency_table(data)
huffman_tree = build_huffman_tree(frequency_table)
huffman_codes = build_huffman_codes(huffman_tree)
compressed_data = compress(data, huffman_codes)
decompressed_data = decompress(compressed_data, huffman_tree)


print("Texto original:", data)
print("Texto comprimido:", compressed_data)
print("Texto descomprimido:", decompressed_data)
