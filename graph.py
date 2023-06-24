# we'll import a file exported in linkedin to create a network graph from the connections listed in the exported file

# import plotly for network graph
import plotly.graph_objects as go
import pandas as pd
import os

# import the csv file

def import_csv(file):
    # delete the first 3 rows of the csv file
    with open(file, 'r') as fin:
        data = fin.read().splitlines(True)
    with open("source/temp.csv", 'w') as fout:
        fout.writelines(data[3:])
    df = pd.read_csv("source/temp.csv")
    # add "me" to the first row
    df.loc[-1] = ['Valentin', 'Fröhlich', 'https://www.linkedin.com/in/valentin-fr%C3%B6hlich-3b5662275/', '', 'ETHZ', 'Student', '']
    # delete the temp file
    os.remove("source/temp.csv")
    print(df)
    return df

def create_graph(df):
    # create the graph
    fig = go.Figure(data=[go.Sankey(
        node = dict(
            pad = 15,
            thickness = 20,
            line = dict(color = "black", width = 0.5),
            label = df['First Name'],
        ),
        link = dict(
            source = df['Source'],
            target = df['Target'],
        )
    )])
    # save the graph
    fig.write_html('graph.html', auto_open=True)

def main():
    df = import_csv('source/Connections.csv')
    print(df)
    create_graph(df)
    
    
if __name__ == "__main__":
    main()