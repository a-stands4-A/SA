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
            label = "void smt1 (ch* str, double c)";
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

sch21_maze = """
digraph sch21 {
    rankdir=LR;    
    # graph [nodesep=0.05 newrank = true splines=spline]; 
    graph [nodesep=0.05 ranksep=2 newrank = true concentrate=true]; 
    node [shape=box];
    label="Black Box solving ???";
              
    subgraph clusterINPUT {   
        rank=same;
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
                        <TD PORT="r2"  BGCOLOR="darkgrey">
The route, which is the solution, must be displayed <BR/>
    with "a line" 1 character thick, passing through the middle of all the <BR/>
    cells in the maze through which the solution runs
                        </TD>
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
        
    subgraph clusterMAGIC {
        bgcolor=orange;
        node [style=filled fillcolor=green]; 
        rank=same
        label = "MAGIC";
        labeljust=c;
        
        b0 [label="Что тут может происходить"];
                
        subgraph clusterPart3_sol {
            bgcolor=green;
            pencolor=black;
            label = "Part 3";
            labeljust=c;
            solPart3 [shape=plaintext label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4"> 
                <TR> 
                    <TD PORT="findSolution" BGCOLOR="darkgrey" BALIGN="LEFT" ROWSPAN="3">struct *maze findSolution(const struct *maze)</TD>
                </TR>
                <TR> 
                    <TD PORT="findSolution1" BGCOLOR="darkgrey" BALIGN="LEFT" HREF="https://habr.com/ru/articles/578110/">Aлгоритм отрисовки линий Брезенхэма</TD>
                </TR>  
                <TR> 
                    <TD PORT="findSolution2" BGCOLOR="darkgrey" BALIGN="LEFT" HREF="https://habr.com/ru/companies/otus/articles/748470/">Алгоритм Дейкстры и А*</TD>
                </TR>     
                <TR>
                    <TD BGCOLOR="darkgrey" PORT="solutionTest" COLSPAN="2" >write tests for solution of maze</TD>
                </TR> 
            </TABLE>>]; 
            # findSolution1 [label="Aлгоритм отрисовки линий Брезенхэма" URL="https://habr.com/ru/articles/578110/" fillcolor=darkgrey]
            # findSolution2 [label="Алгоритм Дейкстры и А*" URL="https://habr.com/ru/companies/otus/articles/748470/" fillcolor=darkgrey]
        } 
        
        subgraph clusterPart2_sol {
            bgcolor=green;
            pencolor=black;
            label = "Part 2";
            labeljust=c;
            solPart2 [shape=plaintext label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                 <TR>
                       <TD BGCOLOR="darkgrey" PORT="info" HREF="https://habr.com/ru/articles/176671/">habr info</TD>
                       <TD BGCOLOR="darkgrey" HREF="https://tproger.ru/articles/maze-generators">tproger info</TD>
                       <TD BGCOLOR="darkgrey" HREF="https://www.educative.io/courses/mazes-for-programmers/understanding-ellers-algorithm">educative info</TD>
                 </TR>
                 <TR>
                       <TD BGCOLOR="darkgrey" PORT="checkMaze" COLSPAN="3" BALIGN="LEFT">int checkMaze(const struct *maze)<BR/>     
    # тут использовать маску для "loop" <BR/>     
    # для "isolated areas" мб найти клетки с тремя  <BR/>     
    # границами и как-то найти, что область замкнута                  
                       </TD>
                 </TR>
                 <TR>
                       <TD BGCOLOR="darkgrey" PORT="genTest" COLSPAN="3">write tests for generationg of maze</TD>
                 </TR>                 
                 <TR>
                       <TD PORT="mazeSave"  BGCOLOR="darkgrey" BALIGN="LEFT" COLSPAN="3">int mazeSave(ch* path/to/file, const struct *maze)</TD>
                 </TR>
            </TABLE>>];        
        }        
        
        subgraph clusterPart1_sol {
            bgcolor=green;
            pencolor=black;
            label = "Part 1";
            labeljust=c;
            solPart1 [shape=plaintext label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                  <TR>
                        <TD PORT="struct"  BGCOLOR="darkgrey" BALIGN="LEFT">struct maze {int n_M, m_M, n, m; <BR/>int** hBorders; int** vBorders;}</TD>
                  </TR>
                  <TR>
                        <TD PORT="gui"  BGCOLOR="darkgrey">int main(int argv, ch* argc)</TD>
                  </TR>
                  <TR>
                        <TD PORT="initMaze"  BGCOLOR="darkgrey" BALIGN="LEFT">int initMaze(ch* path/to/file, n, m):<BR/>
    int rez=0;<BR/>
    if (!path/to/file) generateMaze(n, m);<BR/>
    else (loadFile(path/to/file) = rez);<BR/>
    return rez;
                        </TD>
                  </TR>
                  <TR>
                        <TD PORT="loadFile"  BGCOLOR="darkgrey" BALIGN="LEFT">
int loadFile(ch* path/to/file)<BR/>
        # load in 'r' mode</TD>
                  </TR>
                  <TR>
                        <TD PORT="generateMaze"  BGCOLOR="darkgrey" BALIGN="LEFT">
struct *maze generateMaze(int n, int m)<BR/>
        # load in 'r' mode</TD>
                  </TR>
                  <TR>
                        <TD PORT="checkSize"  BGCOLOR="darkgrey" BALIGN="LEFT">int checkSize(const struct *maze):<BR/>
    if (*maze.n &gt; *maze.n_M || <BR/>         *maze.m &gt; *maze.m_M):<BR/>     
    return ERROR;
                        </TD>
                  </TR>
                  <TR>
                        <TD PORT="renderMaze"  BGCOLOR="darkgrey" HREF="https://clubmate.fi/using-pseudographics-in-blogposts-drawing-ascii-diagrams-and-boxes" BALIGN="LEFT">
int render4090RTX(const struct *maze,<BR/>
    const float* pathC[3],<BR/>
    const float* edgeC[3])<BR/>
    const float* fieldC[3])<BR/>
    #МБ [|-\] - набор символов
                        </TD>
                  </TR>
                  <TR>
                        <TD PORT="wtf"  BGCOLOR="darkgrey">не понял условие</TD>
                  </TR>
            </TABLE>>];        
        }
    }
        
    subgraph clusterOUTPUT {
        bgcolor=red;     
        label = "OUTPUT";  
        labeljust=c;              
        node [style=filled fillcolor=grey];
        c0 [label="Результат"]  
        c1 [label="Проект на 100%"] 
    }
    
    0 [label="INPUT" style=filled fillcolor=grey];
    1 [label="MAGIC" style=filled fillcolor=orange];
    2 [label="OUTPUT" style=filled fillcolor=red];

    0 -> 1 -> 2;
    {rank=same {2 -> c1 -> c0 [style=invis]}}         
    
    solPart1:initMaze     :e -> solPart1:gui:e      [arrowhead=diamond penwidth=2];
    solPart1:checkSize    :e -> solPart1:gui:e      [arrowhead=diamond penwidth=2];
    solPart1:wtf          :e -> solPart1:gui:e      [arrowhead=diamond penwidth=2]; 
    solPart1:loadFile     :e -> solPart1:initMaze:e [arrowhead=diamond penwidth=2 color="blue"]; 
    solPart1:generateMaze :e -> solPart1:initMaze:e [arrowhead=diamond penwidth=2 color="blue"]; 
    solPart2:checkMaze    :e -> solPart1:gui:e      [arrowhead=diamond penwidth=2];
    solPart2:mazeSave     :e -> solPart1:gui:e      [arrowhead=diamond penwidth=2];
    solPart1:renderMaze   :e -> solPart1:gui:e      [arrowhead=diamond penwidth=2];    
    solPart3:findSolution1:se -> solPart1:gui:e      [arrowhead=diamond penwidth=2];
    
    descr_3:r1            -> solPart1:gui        [arrowhead=diamond penwidth=2]; 
    descr_3:r2            -> solPart1:renderMaze [arrowhead=diamond penwidth=2]; 
    descr_3:r3            -> solPart1:renderMaze [arrowhead=diamond penwidth=2]; 
    descr_3:r4            -> solPart3:solutionTest [arrowhead=diamond penwidth=2]; 
     
    descr_1:r1            -> solPart1:gui        [arrowhead=diamond penwidth=2]; 
    descr_2:r5            -> solPart1:initMaze        [arrowhead=diamond penwidth=2];  
    descr_2:r6            -> solPart2:mazeSave   [arrowhead=diamond penwidth=2];  
    
    descr_2:r2:e -> solPart2:info:w        [arrowhead=diamond penwidth=2];     
    descr_2:r3:w -> a:flaws:w             [arrowhead=diamond penwidth=2];
    descr_2:r7:w -> descr_1:r4:w          [arrowhead=diamond penwidth=2];
    descr_2:r3:e -> solPart2:checkMaze:w  [arrowhead=diamond penwidth=2];
    descr_2:r4:e -> solPart2:genTest:w    [arrowhead=diamond penwidth=2];
    
    descr_1:r2 -> solPart1:loadFile  [arrowhead=diamond penwidth=2];
    descr_1:r3 -> solPart1:checkSize [arrowhead=diamond penwidth=2];
    descr_1:r4 -> solPart1:renderMaze    [arrowhead=diamond penwidth=2];
    descr_1:r5 -> solPart1:wtf       [arrowhead=diamond penwidth=2];
}

"""

hand_breaker = """
digraph hand_breaker {
    label="hand_breaker"
    labeljust=t;
    rankdir=LR;    
    # splines="line"; // Force edges to be straight, no curves or angles
    # splines="ortho"; // Force edges to be straight, no curves or angles
    
    graph [newrank=true nodesep=0.05 ranksep=0.05 concentrate=true]; 
    node [shape=box];
    # packmode="graph";
    
    subgraph esp32 {
        rank=same;
        cluster=true;
        label="ESP32_DEV
FREENOVE
ESP32 S3";
        labeljust=t;  
        href="https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf";   
                
        i2c [shape=plaintext labelloc="t" label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                <TR>
                    <TD PORT="I2C" ROWSPAN="2">I2C</TD>          
                </TR>
                <TR>
                    <TD PORT="I2C_chnl">SDA<BR/>SCL<BR/></TD>          
                </TR>                                
            </TABLE>>
            width=1.5
        ];  
        
        pwr [shape=plaintext labelloc="t" label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                <TR>
                    <TD PORT="pwr">pwr</TD>          
                </TR>                               
            </TABLE>>
            width=1.5
        ];  
        
        interrupt [label="Interrupt PIN 19" width=1.5]
        
        GPIO [shape=plaintext labelloc="t" label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                <TR>
                    <TD PORT="FS" ROWSPAN="14" VALIGN="TOP">flex_sensors</TD>              
                </TR>
                <TR>
                    <TD>GPIO 36<BR/>
GPIO 39<BR/>
GPIO 34<BR/>
GPIO 35<BR/>
GPIO 32<BR/>
GPIO 33<BR/>
GPIO 25<BR/>
GPIO 26<BR/>
GPIO 27<BR/>
GPIO 14<BR/>
GPIO 13<BR/>
GPIO 12<BR/>
GPIO 23<BR/>
</TD>             
                </TR>            
            </TABLE>>        
        # height=3 width=1.5
        ];                      
    }   
    
    subgraph TCA9548A {
        cluster=true;
        label=TCA9548A;
        labeljust=t;
        TCA [shape=plaintext labelloc="t" label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4"> 
                <TR>
                    <TD PORT="TCA_chnl">SDA_TCA<BR/>SCL_TCA</TD>
                </TR>  
            </TABLE>>
            width=1.5
         ];
    }
    
    subgraph I2C_slaves {
        cluster=true;
        label=I2C_slaves;
        labeljust=t;
        
        I2C_slaves [shape=plaintext labelloc="t" label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
                <TR>
                    <TD PORT="MPU_0" rowspan="3">MPU_0</TD>
                </TR>  
                <TR>
                    <TD>SDA_SL_0<BR/>SCL_SL_0</TD>
                </TR>
                <TR>
                    <TD PORT="Interrupt">Interrupt</TD>
                </TR>
                <TR>
                    <TD PORT="MPU_1" rowspan="2">MPU_1</TD>
                </TR>  
                <TR>
                    <TD>SDA_SL_1<BR/>SCL_SL_1</TD>
                </TR>
                <TR>
                    <TD PORT="MPU_2" rowspan="2">MPU_2</TD>
                </TR>  
                <TR>
                    <TD>SDA_SL_2<BR/>SCL_SL_2</TD>
                </TR>  
                <TR>
                    <TD PORT="MPU_3" rowspan="2">MPU_3</TD>
                </TR>  
                <TR>
                    <TD>SDA_SL_3<BR/>SCL_SL_3</TD>
                </TR>    
                <TR>
                    <TD PORT="MPU_4" rowspan="2">MPU_4</TD>
                </TR>  
                <TR>
                    <TD>SDA_SL_4<BR/>SCL_SL_4</TD>
                </TR>  
                <TR>
                    <TD PORT="MPU_5" rowspan="2">MPU_5</TD>
                </TR>  
                <TR>
                    <TD>SDA_SL_5<BR/>SCL_SL_5</TD>
                </TR>  
                <TR>
                    <TD PORT="MPU_6" rowspan="2">MPU_6</TD>
                </TR>  
                <TR>
                    <TD>SDA_SL_6<BR/>SCL_SL_6</TD>
                </TR> 
                <TR>
                    <TD PORT="MPU_7" rowspan="2">MPU_7</TD>
                </TR>  
                <TR>
                    <TD>SDA_SL_7<BR/>SCL_SL_7</TD>
                </TR>  
            </TABLE>>
            width=1.5
         ];
    }    
    
    subgraph TP4056_cl {
        # rank=same;
        cluster=true;
        label=TP4056;
        labeljust=t;
        
        TP4056 [shape=plaintext labelloc="t" label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4"> 
                <TR>
                    <TD PORT="TP4056" rowspan="4">BAZA</TD>
                </TR>   
                <TR>
                    <TD PORT="B_plus">B+</TD>
                </TR>
                <TR>
                    <TD PORT="TP4056_EDIT">
                        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">                  
                            <TR>
                                <TD PORT="EDIT" rowspan="3">EDIT</TD>
                            </TR>                
                            <TR>
                                <TD>PMOSFET Vg&lt;0.4V</TD>
                            </TR>  
                            <TR>
                                <TD>Pull-down gate R=10kOm</TD>
                            </TR>
                        </TABLE>
                    </TD>
                </TR>  
                <TR>
                    <TD PORT="OUT_plus">OUT+</TD>
                </TR>                     
            </TABLE>>
            width=1.5
        ];
    } 
    
    subgraph buck_boost_DC_DC {
        cluster=true;
        label="buck-boost DC-DC";
        labeljust=t;
        
         STBB1[shape=plaintext labelloc="t" label=<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4"> 
                <TR>
                    <TD PORT="STBB1">STBB1-APUR</TD>
                </TR>                 
            </TABLE>>
            width=1.5
        ];
    } 
    
    i2c:I2C_chnl              ->       TCA:TCA_chnl     [label="2x{10k, 4.7k, 2.2k}" arrowhead=dot penwidth=1];
    TCA:TCA_chnl:e            ->       I2C_slaves:MPU_0 [label="2x{10k, 4.7k, 2.2k}" arrowhead=dot penwidth=1];
    interrupt:e               ->       I2C_slaves:Interrupt:w [arrowhead=dot penwidth=1];
    TCA:TCA_chnl:e            ->       I2C_slaves:MPU_1 [label="2x{10k, 4.7k, 2.2k}" arrowhead=dot penwidth=1];
    TCA:TCA_chnl:e            ->       I2C_slaves:MPU_2 [label="2x{10k, 4.7k, 2.2k}" arrowhead=dot penwidth=1];
    TCA:TCA_chnl:e            ->       I2C_slaves:MPU_3 [label="2x{10k, 4.7k, 2.2k}" arrowhead=dot penwidth=1];
    TCA:TCA_chnl:e            ->       I2C_slaves:MPU_4 [label="2x{10k, 4.7k, 2.2k}" arrowhead=dot penwidth=1];
    TCA:TCA_chnl:e            ->       I2C_slaves:MPU_5 [label="2x{10k, 4.7k, 2.2k}" arrowhead=dot penwidth=1];
    TCA:TCA_chnl:e            ->       I2C_slaves:MPU_6 [label="2x{10k, 4.7k, 2.2k}" arrowhead=dot penwidth=1];
    TCA:TCA_chnl:e            ->       I2C_slaves:MPU_7 [label="2x{10k, 4.7k, 2.2k}" arrowhead=dot penwidth=1];
 
    TP4056                    -> STBB1          -> pwr:pwr   [arrowhead=dot penwidth=1];      
    
    {rank=same  {GPIO -> interrupt -> i2c [style=invis]}}
    {rank=same  {TP4056 -> STBB1 [style=invis]}}    
}
"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    graph_viz_save(hand_breaker, "hand_breaker", 1)
