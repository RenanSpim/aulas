import numpy as np

def calc_me(f, g):
    me = []
    for i in range(f.shape[0]):
        for j in range(f.shape[1]):
            me.append(abs(f[i, j] - g[i, j]))
    return me

def calc_mae(f, g):
    me = calc_me(f, g)
    mae = sum(me) / len(me)
    return mae

def calc_mse(f, g):
    
    me = calc_me(f, g)
    mse = sum([x**2 for x in me]) / len(me)
    return mse

def calc_rmse(f, g):
    mse = calc_mse(f, g)
    rmse = mse ** 0.5
    return rmse

def calc_jaccard(f, g, threshold=128):
    return np.mean(np.abs(f - g) <= threshold)

def main():
    f = np.array([[255, 255, 255], [255, 0, 255], [255, 255, 255]])
    g = np.array([[250, 250, 250], [250, 1, 250], [250, 250, 250]])

    me = calc_me(f, g)
    mae = calc_mae(f, g)
    mse = calc_mse(f, g)
    rmse = calc_rmse(f, g)
    jaccard = calc_jaccard(f, g, 0)
    
    for i in range(f.shape[0]):
        for j in range(f.shape[1]):
            print(f"Pixel ({i}, {j}): f={f[i, j]}, g={g[i, j]}, ME={me[i * f.shape[1] + j]}")
    print(f"MAE: {mae}")
    print(f"MSE: {mse}")
    print(f"RMSE: {rmse}")
    print(f"Coeficiente de Jaccard: {jaccard}")

if __name__ == "__main__":
    main()