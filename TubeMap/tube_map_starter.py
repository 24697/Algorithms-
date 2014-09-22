import networkx as nx
import matplotlib.pyplot as plt
import numpy
import csv

class TubeMap:
    def __init__(self,file_name):
        self.map = None
        self.file_name = file_name

    def get_stations(self):
        with open(self.file_name, newline='') as csv_file:
            map_reader = csv.reader(csv_file, delimiter = ' ', quotechar = '|')
            for row in map_reader:
                print(row)

    def generate_edge_colours(self,current_map):
        return edge_colours

    def create_graph_plot(self,current_map):
        pass

    def display_full_map(self):
        pass

    def display_travel_map(self,start,end):
        pass

    def get_directions(self,start,end):
        return directions

if __name__ == "__main__":
    new_map = TubeMap('tube.csv')
    new_map.get_stations()
    
