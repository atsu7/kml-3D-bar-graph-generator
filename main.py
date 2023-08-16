import sys
import math
import csv
import simplekml
from polycircles import polycircles


def make_bar(lat, lon, radius, height, kml, legend, color):
    polycircle = polycircles.Polycircle(latitude=lat, longitude=lon, radius=radius, number_of_vertices=36)
    cords = []
    for dict in polycircle:
        cords.append((dict['lon'], dict['lat'], height))
    
    pol = kml.newpolygon(name=legend+"_polygon", outerboundaryis=cords)
    pol.style.polystyle.color = simplekml.Color.hexa(color)
    pol.altitudemode = simplekml.AltitudeMode.absolute
    pol.style.linestyle.width = 0
    pol.extrude = True

def make_label(lat, lon, height, kml, legend, value, legend_height=1000):
    value_label = kml.newpoint(name=int(value), coords=[(lon, lat, height)]) # FIX intをここで指定
    legend_label = kml.newpoint(name=legend, coords=[(lon, lat, legend_height)])
    value_label.altitudemode = simplekml.AltitudeMode.absolute
    value_label.style.iconstyle.icon.href = None
    value_label.style.labelstyle.scale = 3 # FIX ここでフォントサイズを指定
    legend_label.altitudemode = simplekml.AltitudeMode.absolute
    legend_label.style.iconstyle.icon.href = None
    legend_label.style.labelstyle.scale = 3.0 # FIX ここでフォントサイズを指定




def meridian_distance_to_longitude_difference(latitude, distance, radius=6371000.0):
    """
    Convert a distance along a meridian to a difference in longitude at a given latitude.
    
    Parameters:
    latitude (float): Latitude in degrees.
    distance (float): Distance along the meridian in the same unit as the radius.
    radius (float): Radius of the sphere (default is Earth's radius in kilometers).
    
    Returns:
    float: Difference in longitude in degrees.
    """
    latitude_radians = math.radians(latitude)
    meridian_length = 2 * math.pi * radius * math.cos(latitude_radians)
    degrees_per_meridian = 360.0
    longitude_difference = (distance / meridian_length) * degrees_per_meridian
    return longitude_difference


def main():
    csv_name = sys.argv[1]
    with open("input/"+csv_name, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        first_row = next(csvreader)

        graph_title = first_row[0]
        color = first_row[1]

        ratio = first_row[2]
        try:
            ratio = float(ratio)
        except ValueError:
            print("Error: Ratio is not a number")

        radius = first_row[3]
        try:
            radius = float(radius)
        except ValueError:
            print("Error: Radius is not a number")
        
        margin = first_row[4]
        try:
            margin = float(margin)
        except ValueError:
            print("Error: Margin is not a number")

        first_lat = first_row[5]
        try:
            first_lat = float(first_lat)
        except ValueError:
            print("Error: First latitude is not a number")
        first_lon = first_row[6]
        try:
            first_lon = float(first_lon)
        except ValueError:
            print("Error: First longitude is not a number")
        

        second_row = next(csvreader)
        legends_list = []
        for i in range(0, len(second_row)):
            
            legends_list.append(second_row[i])
        
        third_row = next(csvreader)
        values_list = []
        for i in range(0, len(third_row)):
            try:
                value = float(third_row[i])
                values_list.append(value)
            except ValueError:
                print("Error: Value is not a number")

    if len(legends_list) != len(values_list):
        print("Error: Number of legends and values are not equal")
        return
    
    kml = simplekml.Kml()

    for i in range(0, len(legends_list)):
        lat = first_lat
        lon = first_lon + (i)*meridian_distance_to_longitude_difference(first_lat,margin+2*radius)
        make_bar(lat, lon, radius, values_list[i]*ratio, kml, legends_list[i],color)
        make_label(lat, lon, values_list[i]*ratio, kml, legends_list[i], values_list[i])            

    kml.save("output/"+csv_name.split('.')[0]+".kml")
        
        

if __name__ == '__main__':
    main()