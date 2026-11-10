# AP para a^n b^n (n >= 1). "" representa ε
K = {"q1", "q2"}
sigma = {"a", "b"}
gamma = {"a"}
s = "q1"
F = {"q2"}
delta = [
    (("q1", "a", ""), ("q1", "a")),
    (("q1", "b", "a"), ("q2", "")),
    (("q2", "b", "a"), ("q2", "")),
]
ap = (K, sigma, gamma, delta, s, F)


def acepta(w, ap, tr=False):
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
        if e in F and not r and not p:
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

# Diferentes ejemplos para ponerlo a prueba 
if __name__ == "__main__":
    acepta("aabb", ap, tr=True)
    print()
    for w in ["ab", "aabb", "aaabbb", "abab", "aab", "abb", "ba", "", "a", "b", "abc"]:
        print(f"{w or 'ε':<8}{'ACEPTA' if acepta(w, ap) else 'RECHAZA'}")
