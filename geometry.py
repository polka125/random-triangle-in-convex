import math

def scal(xs, ys):
    """Cкалярное произведение двух векторов. 
       В случае len(xs) == len(ys) == 2 это произведение
       вектора (xs[0], ys[0]) на (xs[1], ys[1]).
       В случае len(xs) == len(ys) == 4 это произведение
       вектора (xs[1] - xs[0], ys[1] - ys[0]) на (xs[3] - xs[2], ys[3] - ys[2])
    """
    if len(xs) == 2:
        return xs[0] * xs[1] + ys[0] * ys[1]
    if len(xs) == 4:
        xs_2 = [xs[1] - xs[0], xs[3] - xs[2]]
        ys_2 = [ys[1] - ys[0], ys[3] - ys[2]]
        return scal(xs_2, ys_2)

def vec(xs, ys):
    """Векторное произведение двух векторов. 
       В случае len(xs) == len(ys) == 2 это произведение
       вектора (xs[0], ys[0]) на (xs[1], ys[1]).
       В случае len(xs) == len(ys) == 4 это произведение
       вектора (xs[1] - xs[0], ys[1] - ys[0]) на (xs[3] - xs[2], ys[3] - ys[2])
    """
    if len(xs) == 2:
        return xs[0] * ys[1] - xs[1] * ys[0]
    if len(xs) == 4:
        xs_2 = [xs[1] - xs[0], xs[3] - xs[2]]
        ys_2 = [ys[1] - ys[0], ys[3] - ys[2]]
        return vec(xs_2, ys_2)
    raise Exception("illegal arguments")


def area(xs, ys):
    """Абсолютная площать многоугольника, заданного вектором х и у координат вершин"""
    n = len(xs) #number of sides
    ans = 0.0
    for i in range(n - 1):
        ans += vec(xs[i:i+2], ys[i:i+2])
    ans += vec([xs[-1], xs[0]], [ys[-1], ys[0]])
    ans /= 2.0
    return abs(ans)
    

def vec_len(xs, ys):
    if len(xs) == 1:
        return math.hypot(xs[0], ys[0])
    if len(xs) == 2:
        return vec_len([xs[1] - xs[0]], [ys[1] - ys[0]])


def grind_to_eps(xs, ys, eps=0.001):
    """измельчает отрезок на отрезки длины @param eps"""
    section_len = vec_len(xs, ys)
    
    point_number = math.ceil(section_len / eps)
    
    dx = scal([xs[0], xs[1], 0, 1], 
                  [ys[0], ys[1], 0, 0]) / section_len
    dy = scal([xs[0], xs[1], 0, 0], 
                  [ys[0], ys[1], 0, 1]) / section_len
    
    ans_x, ans_y = [], []
    for i in range(point_number):
        ans_x.append(xs[0] + dx * eps * i)
        ans_y.append(ys[0] + dy * eps * i)
    return ans_x, ans_y

def grind_polygon(xs, ys, eps=0.01):
    """измельчает каждую сторону многоугольника"""
    n = len(xs)
    xs_ans = []
    ys_ans = []
    for i in range(n - 1):
        xs_sec, ys_sec = grind_to_eps(xs[i:i+2], ys[i:i+2], eps)
        xs_ans.extend(xs_sec)
        ys_ans.extend(ys_sec)
    xs_sec, ys_sec = grind_to_eps([xs[-1], xs[0]], [ys[-1], ys[0]], eps)
    xs_ans.extend(xs_sec)
    ys_ans.extend(ys_sec)
    
    return xs_ans, ys_ans
    

if __name__ == "__main__":
    from cnvx_provider import polygon
    xs, ys = polygon(100000)
    print(area(xs, ys)) # 3.1415612355921883
    
    
#    print(*zip(*grind_to_eps([0, -1], 
#                       [0, 1])))
                       
    print(*zip(*grind_polygon([1, -1, -1, 1], 
                        [1, 1, -1, -1], 0.5)))
                        
                        
    xs = [0.84, 0.22, 0.63]
    ys = [0.21, 0.92, -0.5]
    print(area(xs, ya))