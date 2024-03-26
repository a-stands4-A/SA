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


raw0 = """
digraph G{
 rankdir=LR;
 node[color="red",fontsize=14];
 edge[color="darkgreen",fontcolor="blue",fontsize=12];
 OPEN[shape="rectangle",style="filled",fillcolor="lightgrey"];
 CLOSED[shape="octagon",label="Финиш"];
 VERIFIED[shape="rectangle",style="rounded"];
 OPEN->RESOLVED->VERIFIED->CLOSED;
 OPEN->CLOSED[style="bold"];
 VERIFIED->OPEN[label="обнаружены ошибки",style="dashed",arrowhead="dot", URL="http://www.google.com"];
 VERIFIED->OPEN[label="обнаружены ошибкDDDD",style="dashed",arrowhead="dot", URL="http://lib.custis.ru/Graphviz"];
}
"""

raw1 = """
 digraph G{
   node[fontsize=9];
   { /* шкала месяцев*/
     node[shape=plaintext]; /* что бы не было видно рамок */
     edge[color=white] /* что бы не было видно стрелок */
     "март" ->  "июнь" -> "сентябрь" -> "декабрь"; 
   }
   { rank = same; "март"; "весна"; "a"; }
   { rank = same; "июнь"; "лето";}
   { rank = same; "сентябрь"; "осень"; "d"; }
   { rank = same; "декабрь"; "зима"; "e"}
   "весна" -> "лето" -> "осень" -> "зима" -> "весна"
   "a" -> "b" -> "c" -> "d" -> "e" ;
 }
"""

raw2 = """
 digraph G {
  rankdir=LR;
  subgraph cluster0 {
       node [style=filled,color=white];
       style=filled;
       color=lightgrey;
       a0;
       a1
       label = "process #1";
  }
  subgraph cluster1 {
       node [style=filled];
       b0;
       label = "process #2";
       color=blue
  }
  start -> a0;
  start -> b0;
  a0 -> a1 -> end;
  b0 -> end;
 }
"""

raw3 = """
digraph structs {
  rankdir=LR;
  first [shape=record,label="  x1\n all | { x21 | <f0> x22| x23} | x3" ];
  second [shape=record,label=" x22_1 | x22_2 | x22_3"];
  first:<f0> -> second [label="asdasd", URL="http://lib.custis.ru/Graphviz"];
}
"""

SA_init = """
digraph BB {
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
        bgcolor=green;
        node [style=filled fillcolor=orange]; 
        rank=same
        label = "MAGIC";
        labeljust=c;
        
        b [label="Что тут может происходить"];
        
        subgraph clusterF1 {
            bgcolor=orange;
            pencolor=black;
            label = "void smt1 (ch str, double c)";
            labeljust=c;
            # pr11 [label="ch str"]
            # pr12 [label="double c"]
            # return_f1 [label="return"];
            # descr_1 [label="qweqw"];
            descr_1 [shape=plaintext label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                  <TR>
                        <TD PORT="descr"  BGCOLOR="lightgrey">longlonglonglonglong description<BR/>description<BR/>description</TD>
                        <TD PORT="return" BGCOLOR="green">return</TD>
                  </TR>
            </TABLE>>];        }
        
        subgraph clusterF0 {
            bgcolor=orange;
            pencolor=black;
            label = "int smt0 (int pr01, float pr02)";
            labeljust=c; 
            descr_0 [shape=plaintext label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                  <TR>
                        <TD PORT="descr"  BGCOLOR="lightgrey">longlonglonglonglong description<BR/>description<BR/>description</TD>
                        <TD PORT="return" BGCOLOR="green">return</TD>
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
    graph_viz_save(SA_init, "SA_init", 1)
    # graph_viz_save(raw3, "raw1", 1)


