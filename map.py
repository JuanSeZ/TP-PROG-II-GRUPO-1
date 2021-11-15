from monitoring import Pilar, Tigre, Escobar, San_Isidro, Ranking_In_Zone
zone_list = [Pilar, Tigre, Escobar, San_Isidro]
import pip
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Map:

    def build_map(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for zone in zone_list:
            for event in Ranking_In_Zone.get_ranking():
                ax.scatter(x=event[1].get_coordinates()[0],y=event[1].get_coordinates()[1], linewidth=event[0])
                origin_point = zone.get_center_of_point()
                widht = zone.get_width()
                ax.add_patch(
                    patches.Rectangle(
                        xy=origin_point,
                        width=widht,
                        height=widht,
                        linewidth=1,
                        color='green',
                        fill=False))
        plt.show()

Map = Map()
Map.build_map()
