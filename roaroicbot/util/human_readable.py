# ─────────────────────────────────────────────
# Powered by Roaroic | Developer Channel: @roaroic0
# https://t.me/roaroic0
# ─────────────────────────────────────────────
#Thanks @roaroic0 for helping in this journey 
def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'
