import matplotlib.pyplot as plt

def plot_punnet_square(punnet_square, gp1, gp2):

    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    ax.matshow(punnet_square, alpha=0.7)

    plt.title(f"Punnet Square {gp1}*{gp2}")
    plt.show()


plot_punnet_square([[0, 0, 0], [0, 0, 0], [0, 0, 0]], "AaBB", "aaBb")