# KML 3D bar graph generator

It generates kml file which shows 3D bar graph on the earth. You can display it on Google Earth and so on.

<img width="1009" alt="スクリーンショット 2023-08-16 18 14 03" src="https://github.com/atsu7/kml-3D-bar-graph-generator/assets/30950577/71f153de-0162-4296-af70-f99473669b6e">


## Dependencies
- simplekml
- polycircles

you can install them with
```
python3 -m pip install -r requirments.txt
```

## How to use
### Prepare a csv file
Put a csv file in `input/`

The format is 
```
GraphTitle,Color,Ratio,Radius,Margin,Longitude,Latitude
ItemName1, ItemName2, ItemName3
Value1,Value2,Value3
```
`Color` should be indicated as hex rgba

`Ratio` means (The graph height) / (Value).

`Radius` means a radius of one bar.

`Margin` means a distance between bars.

`Longitude` and `Latitude` mean those of a bar on the far left.

This is an example.
```
The price of fruits,00ff00aa,0.5,400,400,40,140
Apple, Banana, Cherry
500,200,300
```

### Run
```
Python3 main.py file_name.csv
```

### Tips
- You can edit color, height, icon, label on Google Earth Pro without coding.
- You can also use this app to make a single cylinder

