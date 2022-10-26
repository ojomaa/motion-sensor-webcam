from webcam_control import df
from bokeh.plotting import output_file, show, figure
from bokeh.models import HoverTool, ColumnDataSource

#ColumnDataSource() was used to pull the information from df in the webcam_control file and use it here
cds = ColumnDataSource(df)

#figure() is used to design the actual graph and the way it looks. so adding titles, width, height, color, etc.
f= figure(
    x_axis_type = 'datetime',
    width = 500,
    height = 250,
    sizing_mode = 'stretch_both',
    title = "Motion Graph"
    )

#minor_tick_line_color was to remove the small ticks on the y axis
#desired_num_ticks was to remove the grid lines in the actual graph
f.yaxis.minor_tick_line_color = None
f.yaxis[0].ticker.desired_num_ticks= 1

#HoverTool()is used to create a hover over the data so that its readable
#tooltips was to adjust the information pulled from the Times.csv into Year-Month-Day Hour:Minute:Second
#formatters made sure to use the datetime function
hover = HoverTool(
    tooltips=[
        ('Start','@Start{%Y-%m-%d %H:%M:%S}'),
        ('End', '@End{%Y-%m-%d %H:%M:%S}')
    ],
    formatters= {
        '@Start': 'datetime',
        '@End': 'datetime'
    }
)
#add_tools was to add the hover function we created into the graph
f.add_tools(hover)

#quad() was used to make sure the graph was represented in big quadrants instead of a line graph or scatter plot
#the customizers inside are just to adjust the physical appearance of the quadrants
f.quad(
    left ='Start',
    right ='End',
    top = 1,
    bottom = 0,
    color = "gray",
    source = cds
    )

#output_file() is to export all the info into an html file to be used and show() is just to show the info in the output_file
output_file("motion_graph.html")
show(f)