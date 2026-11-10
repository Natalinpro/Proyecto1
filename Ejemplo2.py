# AP para {a^i b^j c^k | i = j-k}. "" representa ε

# A) acepta con pila vacía (F no se usa)
K_a = {"q0", "q1", "q2"}
sigma_a = {"a", "b", "c"}
gamma_a = {"a", "b"}
s_a = "q0"
F_a = set()
delta_a = [
    (("q0", "a", ""), ("q0", "a")),
    (("q0", "b", "a"), ("q1", "")),
    (("q0", "b", ""), ("q1", "b")),
    (("q1", "b", "a"), ("q1", "")),
    (("q1", "b", ""), ("q1", "b")),
    (("q1", "c", "b"), ("q2", "")),
    (("q2", "c", "b"), ("q2", "")),
]
ap_a = (K_a, sigma_a, gamma_a, delta_a, s_a, F_a)

# B) acepta por estado final, sin vaciar la pila (Z marca el fondo)
K_b = {"q0", "q1", "q2", "q3", "qf"}
sigma_b = {"a", "b", "c"}
gamma_b = {"a", "b", "Z"}
s_b = "q0"
F_b = {"qf"}
delta_b = [
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
ap_b = (K_b, sigma_b, gamma_b, delta_b, s_b, F_b)


def acepta(w, ap, vac, tr=False):
    K, sigma, gamma, delta, s, F = ap
    if any(c not in sigma for c in w):
        return False
    ini = (s, w, "")
    stk = [(ini, [ini])]
    vis = set()
    while stk:
        cfg, cam = stk.pop()
        if cfg in vis:
            continue
        vis.add(cfg)
        e, r, p = cfg
        if not r and ((not p) if vac else e in F):
            if tr:
                mostrar(cam)
            return True
        for (e1, lee, sac), (e2, met) in delta:
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
    acepta("abbc", ap_a, True, tr=True)
    print("\nB) estado final, 'abbc':")
    acepta("abbc", ap_b, False, tr=True)
    print()
    #Ejemplos para poner a prueba 
    for w in ["", "ab", "bc", "abbc", "aabbb", "aabbbc", "abc", "aabb", "abcc", "ba", "c"]:
        ra = acepta(w, ap_a, True)
        rb = acepta(w, ap_b, False)
        print(f"{w or 'ε':<8}A:{'SI' if ra else 'NO':<4}B:{'SI' if rb else 'NO'}")
