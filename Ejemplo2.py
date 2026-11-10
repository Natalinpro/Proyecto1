# AP para {a^i b^j c^k | i = j-k}. "" representa ε
# ((estado, leer, sacar), (estado_nuevo, meter))

# A) acepta con pila vacía
DA = [
    (("q0", "a", ""), ("q0", "a")),
    (("q0", "b", "a"), ("q1", "")),
    (("q0", "b", ""), ("q1", "b")),
    (("q1", "b", "a"), ("q1", "")),
    (("q1", "b", ""), ("q1", "b")),
    (("q1", "c", "b"), ("q2", "")),
    (("q2", "c", "b"), ("q2", "")),
]

# B) acepta por estado final (sin vaciar la pila), Z marca el fondo
DB = [
    (("q0", "", ""), ("q1", "Z")),
    (("q1", "a", ""), ("q1", "a")),
    (("q1", "b", "a"), ("q2", "")),
    (("q1", "b", ""), ("q2", "b")),
    (("q2", "b", "a"), ("q2", "")),
    (("q2", "b", ""), ("q2", "b")),
    (("q2", "c", "b"), ("q3", "")),
    (("q3", "c", "b"), ("q3", "")),
    (("q1", "", "Z"), ("qf", "Z")),
    (("q2", "", "Z"), ("qf", "Z")),
    (("q3", "", "Z"), ("qf", "Z")),
]
FB = {"qf"}


def acepta(w, dl, vac, fn=(), tr=False):
    ini = ("q0", w, "")
    stk = [(ini, [ini])]
    vis = set()
    while stk:
        cfg, cam = stk.pop()
        if cfg in vis:
            continue
        vis.add(cfg)
        e, r, p = cfg
        if not r and ((not p) if vac else e in fn):
            if tr:
                mostrar(cam)
            return True
        for (e1, lee, sac), (e2, met) in dl:
            if e1 == e and r.startswith(lee) and p.endswith(sac):
                nv = (e2, r[len(lee):], p[:len(p) - len(sac)] + met)
                stk.append((nv, cam + [nv]))
    return False


def mostrar(cam):
    print(f"{'Estado':<8}{'Por leer':<10}Pila")
    for e, r, p in cam:
        print(f"{e:<8}{r or 'ε':<10}{p or 'ε'}")


if __name__ == "__main__":
    print("A) pila vacía, 'abbc':")
    acepta("abbc", DA, True, tr=True)
    print("\nB) estado final, 'abbc':")
    acepta("abbc", DB, False, FB, tr=True)
    print()
    for w in ["", "ab", "bc", "abbc", "aabbb", "aabbbc", "abc", "aabb", "abcc", "ba", "c"]:
        ra = acepta(w, DA, True)
        rb = acepta(w, DB, False, FB)
        print(f"{w or 'ε':<8}A:{'SI' if ra else 'NO':<4}B:{'SI' if rb else 'NO'}")
