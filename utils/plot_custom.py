import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from data import get_num_learning_labels, get_names_learning

dataset = "SemanticUSL" # "SemanticKITTI"  # "SemanticUSL"


def show_data():
    vals = np.genfromtxt('../figures_sem_kitti/total_points_per_label.csv' if dataset == "SemanticKITTI" else
                         '../figures/total_points_per_label.csv', delimiter=',')  # kitti
    distr_dict = dict(zip(get_names_learning()[0], vals))
    distr_dict = dict(sorted(distr_dict.items(), key=lambda item: item[1], reverse=True))
    distr_dict.pop("unlabeled")
    plot_barplot(distr_dict, name_to_save=f"./sns_barplot_all_{dataset}.png")


def plot_barplot(dict, name_to_save="fig.png"):
    total_sum = sum(dict.values())
    print(f"TOTAL NUM OF POINTS: {total_sum}")
    print(dict)

    sns.set(rc={'figure.figsize': (9, 5)})
    ax = sns.barplot(x=list(dict.keys()), y=[int(i) for i in dict.values()])
    percentage = [v / total_sum * 100 for v in dict.values()]
    patches = ax.patches
    for i in range(len(patches)):
        x = patches[i].get_x() + patches[i].get_width() / 2
        y = patches[i].get_height() + .06
        ax.annotate('{:.1f}%'.format(percentage[i]), (x, y), ha='center')

    plt.xticks(rotation=45)
    plt.ylabel("Number of points")
    plt.xlabel("Object classes")
    plt.tight_layout()
    plt.title(dataset)
    plt.savefig(name_to_save, bbox_inches="tight", dpi=300)
    plt.show()


show_data()
