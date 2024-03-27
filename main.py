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
        
        # subgraph clusterF1 {
        #     bgcolor=green;
        #     pencolor=black;
        #     label = "void smt1 (ch str, double c)";
        #     labeljust=c;
        #     descr_1 [shape=plaintext label=<
        #     <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
        #           <TR>
        #                 <TD PORT="descr"  BGCOLOR="darkgrey">longlonglonglonglong description<BR/>description<BR/>description</TD>
        #                 <TD PORT="return" BGCOLOR="orange">return</TD>
        #           </TR>
        #     </TABLE>>];        }
        # 
        # subgraph clusterF0 {
        #     bgcolor=green;
        #     pencolor=black;
        #     label = "int smt0 (int pr01, float pr02)";
        #     labeljust=c; 
        #     descr_0 [shape=plaintext label=<
        #     <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
        #           <TR>
        #                 <TD PORT="descr"  BGCOLOR="darkgrey">longlonglonglonglong description<BR/>description<BR/>description</TD>
        #                 <TD PORT="return" BGCOLOR="orange">return</TD>
        #           </TR>
        #     </TABLE>>];
        # }
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

sch21_maze = """
digraph sch21 {
    rankdir=LR;
    graph [newrank = true]; 
    node [shape=box];
          
    subgraph cluster0 {   
        bgcolor=grey;
        node [style=filled fillcolor=red];
        label = "INPUT";
        labeljust=c;
                
        a [shape=plaintext label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                  <TR>
                        <TD PORT="descr" ROWSPAN="6">структура "maze"</TD>
                  </TR> 
                  <TR>
                        <TD PORT="struct">таблица n x m </TD>
                  </TR>
                  <TR>
                        <TD PORT="walls0">стены вокруг самого "maze" есть всегда</TD>
                  </TR>                  
                  <TR>
                        <TD PORT="walls1">стены с правой части каждой клетки (n x m)</TD>
                  </TR>                 
                  <TR>
                        <TD PORT="walls2">стены с нижней части каждой клетки (n x m)</TD>
                  </TR>                
                  <TR>
                        <TD PORT="flaws">возможны недостатки: "isolated areas" и "loop"</TD>
                  </TR>     
                                  
                  <TR>
                        <TD PORT="rules" ROWSPAN="4">правила обхода</TD>
                  </TR>                 
                  <TR>                        
                        <TD PORT="r1">соседняя клетка == шаг 1</TD>
                  </TR>                
                  <TR>
                        <TD PORT="r2">направление={право, лево, верх, вниз}</TD>                        
                  </TR>               
                  <TR>
                        <TD PORT="r3">вход и выход задаются парой <BR/>начальных (x, y) координат</TD>                        
                  </TR>     
            </TABLE>>];
        a0 [label="С чем работать"];
        
        subgraph clusterPart3 {
            bgcolor=red;
            pencolor=black;
            label = "Part 3";
            labeljust=c; 
            
            descr_3 [shape=plaintext label=<
            <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                  <TR>
                        <TD PORT="r1"  BGCOLOR="darkgrey">The user sets the starting and ending points <BR/></TD>
                  </TR>
                  <TR>
                        <TD PORT="r2"  BGCOLOR="darkgrey">The route, which is the solution, must be displayed <BR/>with "a line" 1 character thick, passing through the middle of all the <BR/>cells in the maze through <BR/>which the solution runs</TD>
                  </TR>
                  <TR>
                        <TD PORT="r3"  BGCOLOR="darkgrey">The color of the solution line must be different <BR/>from the color of the walls, and the field</TD>
                  </TR>
                  <TR>
                        <TD PORT="r4"  BGCOLOR="darkgrey">Prepare full coverage of the maze solving <BR/>module with unit-tests</TD>
                  </TR>
            </TABLE>>];
        }               
                            
        subgraph clusterPart2 {
            bgcolor=red;
            pencolor=black;
            label = "Part 2";
            labeljust=c; 
            
            descr_2 [shape=plaintext label=<
            <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                  <TR>
                        <TD PORT="r1"  BGCOLOR="yellow">A maze is considered perfect if it is possible to get from <BR/>each point to any other point in exactly one way.</TD>
                  </TR>
                  <TR>
                        <TD PORT="r2"  BGCOLOR="darkgrey">You must generate the maze according to Eller's algorithm</TD>
                  </TR>
                  <TR>
                        <TD PORT="r3"  BGCOLOR="darkgrey">The generated maze must not have isolations and loops</TD>
                  </TR>
                  <TR>
                        <TD PORT="r4"  BGCOLOR="darkgrey">Prepare full coverage of the perfect maze <BR/>generation module with unit-tests</TD>
                  </TR>
                  <TR>
                        <TD PORT="r5"  BGCOLOR="darkgrey" ALIGN="center">The user enters only the dimensionality of the maze: <BR/>the number of rows and columns</TD>
                  </TR>
                  <TR>
                        <TD PORT="r6"  BGCOLOR="darkgrey" ALIGN="center">The generated maze must be saved <BR/>in the file format described above</TD>
                  </TR>
                  <TR>
                        <TD PORT="r7"  BGCOLOR="darkgrey" ALIGN="center">The created maze should be displayed <BR/>on the screen as specified in the first part</TD>
                  </TR>
            </TABLE>>];
        } 
        
        subgraph clusterPart1 {
            bgcolor=red;
            pencolor=black;
            label = "Part 1";
            URL="https://edu.21-school.ru/project/69103/task";
            labeljust=c; 
            descr_1 [shape=plaintext label=<
            <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                  <TR>
                        <TD PORT="r1"  BGCOLOR="darkgrey">The program should implement a console-based user interface</TD>
                  </TR>
                  <TR>
                        <TD PORT="r2"  BGCOLOR="darkgrey">The program has an option to load the maze from a file</TD>
                  </TR>
                  <TR>
                        <TD PORT="r3"  BGCOLOR="darkgrey">Maximum size of the maze is 50x50</TD>
                  </TR>
                  <TR>
                        <TD PORT="r4"  BGCOLOR="darkgrey">The loaded maze must be rendered on the screen in <BR/>the console in pseudo-graphics</TD>
                  </TR>
                  <TR>
                        <TD PORT="r5"  BGCOLOR="darkgrey" ALIGN="center">The size of the maze cells themselves is calculated so that <BR/>the maze occupies the entire field allotted to it</TD>
                  </TR>
            </TABLE>>];
        }
            
    }
        
    subgraph cluster1 {
        bgcolor=orange;
        node [style=filled fillcolor=green]; 
        rank=same
        label = "MAGIC";
        labeljust=c;
        
        b0 [label="Что тут может происходить"];
        
        # subgraph clusterF1 {
        #     bgcolor=green;
        #     pencolor=black;
        #     label = "void smt1 (ch str, double c)";
        #     labeljust=c;
        #     descr_1 [shape=plaintext label=<
        #     <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
        #           <TR>
        #                 <TD PORT="descr"  BGCOLOR="darkgrey">longlonglonglonglong description<BR/>description<BR/>description</TD>
        #                 <TD PORT="return" BGCOLOR="orange">return</TD>
        #           </TR>
        #     </TABLE>>];        
        # }
        
    }
        
    subgraph cluster2 {
        bgcolor=red;     
        label = "OUTPUT";  
        labeljust=c;              
        node [style=filled fillcolor=grey];
        c0 [label="Результат"]  
    }
    
    0 [label="INPUT" style=filled fillcolor=grey];
    1 [label="MAGIC" style=filled fillcolor=orange];
    2 [label="OUTPUT" style=filled fillcolor=red];

    a0 -> b0 -> c0;
    0 -> 1 -> 2;    
    # {rank=same {descr_1:r1 -> descr_2:r1 -> descr_3:r1 [style=invis]}}
}

"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    graph_viz_save(sch21_maze, "sch21_maze", 0)
