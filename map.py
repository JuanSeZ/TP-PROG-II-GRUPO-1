from monitoring import ranking_list

import pip
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Map:

    def build_map(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for ranking in ranking_list:
            for event in ranking.get_ranking():
                x = event.get_coordinates()[0]
                y = event.get_coordinates()[1]
                ax.scatter(x, y, linewidth=event.concurrence, color="red")
                plt.text(x, y + 0.8, event.get_type(), fontsize=10, horizontalalignment='center', verticalalignment='center')
            origin_point = ranking.zone.get_center_of_point()
            width = ranking.zone.get_width()
            plt.text(ranking.zone.get_center_of_point()[0], ranking.zone.get_center_of_point()[1], ranking.zone.get_descprition())
            ax.add_patch(
                patches.Rectangle(
                    xy=origin_point,
                    width=width,
                    height=width,
                    linewidth=1,
                    color='green',
                    fill=False))
        ax.set_title("Map")
        plt.show()


map = Map()
#map.build_map()
