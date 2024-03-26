# https://graphviz.readthedocs.io/en/stable/manual.html
# http://lib.custis.ru/Graphviz

import pandas as pd
import numpy as np
import graphviz

"""
https://bioweb.pasteur.fr/docs/modules/graphviz/2.38.0/info/attrs.html#d:fillcolor
"""


def print_hi(name: str) -> None:
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def graph_viz_frmt(rraw:str, t: int = 0) -> graphviz.Source:
    src = graphviz.Source(rraw)
    if 0 == t:
        src.format = 'png'
    elif 1 == t:
        src.format = 'svg'
    else:
        src.format = 'pdf'
    return src


def graph_viz_save(rraw:str, name:str, t: int = 0) -> None:
    src = graph_viz_frmt(rraw, t)
    src.engine = 'dot'  # neato # dot
    src.render(f'{name}/{name}.gv', view=True, cleanup=True).replace('\\', '/')


sch21 = """
digraph sch21 {
    rankdir=LR;
    graph [newrank = true]; 
    node [shape=box];
          
    subgraph cluster0 {   
        bgcolor=grey;
        node [style=filled fillcolor=red];
        label = "INPUT";
        labeljust=c;
        
        a [label="С чем работать"];
    }
        
    subgraph cluster1 {
        bgcolor=orange;
        node [style=filled fillcolor=green]; 
        rank=same
        label = "MAGIC";
        labeljust=c;
        
        b [label="Что тут может происходить"];
        
        subgraph clusterF1 {
            bgcolor=green;
            pencolor=black;
            label = "void smt1 (ch str, double c)";
            labeljust=c;
            descr_1 [shape=plaintext label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                  <TR>
                        <TD PORT="descr"  BGCOLOR="darkgrey">longlonglonglonglong description<BR/>description<BR/>description</TD>
                        <TD PORT="return" BGCOLOR="orange">return</TD>
                  </TR>
            </TABLE>>];        }
        
        subgraph clusterF0 {
            bgcolor=green;
            pencolor=black;
            label = "int smt0 (int pr01, float pr02)";
            labeljust=c; 
            descr_0 [shape=plaintext label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                  <TR>
                        <TD PORT="descr"  BGCOLOR="darkgrey">longlonglonglonglong description<BR/>description<BR/>description</TD>
                        <TD PORT="return" BGCOLOR="orange">return</TD>
                  </TR>
            </TABLE>>];
        }
    }
        
    subgraph cluster2 {
        bgcolor=red;     
        label = "OUTPUT";  
        labeljust=c;              
        node [style=filled fillcolor=grey];
        c [label="Результат"]  
    }
    
    0 [label="INPUT" style=filled fillcolor=grey];
    1 [label="MAGIC" style=filled fillcolor=orange];
    2 [label="OUTPUT" style=filled fillcolor=red];

    a -> b -> c;
    0 -> 1 -> 2;            
    descr_0:return -> descr_1:return; 
}

"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    graph_viz_save(sch21, "sch21", 1)


