# CSE 280 Prove 6

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**: Hunter Heuser

**Section**: 02

**Teacher**: Brother Macbeth

## Question 1 (5 points)

Fill in the adjacency table below for the graph below:

![](prove06_graph1.png)

|Vertex|Adjacent Verticies|
|:-:|:-:|
|0|4|
|1|4|
|2|3|
|3|4|
|4|3|

## Question 2 (4 points)

The list of 9 graphs below have 4 pairs of isomorphic graphs.  Find the 4 pairs.  Note that one of the graphs does not have a match.

![](prove06_graph2.png)

|#|Isomorphic Pairs|
|:-:|:-:|
|1st Pair|G & C|
|2nd Pair|B and I|
|3rd Pair|A and F|
|4th Pair|D and E|

Source: Question adapted from Applied Discrete Structures by Alan Doerr & Kenneth Levasseur which is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License.

## Question 3 (15 points)

Write python code to create an adjacency table for the undirected graph below.  Second, implement the `find_neighbors` function which will take as input vertex and the adjaceny table and returns a list of verticies that are adjacent to the input vertex.  Finally, implement the `is_neighbor` which takes two verticies and the adjaceny table and returns True if they are adjacent; False otherwise.

![](prove06_graph3.png)

```python
adjacency_table =     'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
    'D': ['C', 'E', 'F'],
    'E': ['D'],
    'F': ['D']

def find_neighbors(vertex, adjaceny_table):
    if vertex in adjacency_table:
        return adjacency_table[vertex]
    else:
        return []


def is_neighbor(vertex1, vertex2, adjacency_table):
    return vertex2 in adjacency_table.get(vertex1, [])

print(find_neighbors('A', adjacency_table)) # should print ['B', 'C']
print(find_neighbors('D', adjacency_table)) # should print ['C', 'E', 'F']

print(is_neighbor('A','B',adjacency_table)) # True
print(is_neighbor('D','F',adjacency_table)) # True
print(is_neighbor('C','F',adjacency_table)) # False
```

## Question 4 (6 points)

Determine if the graph below has an Euler Circuit.  If it does, then write down the sequence of verticies that make up the Euler Circuit.  If it does not, then write "No Euler Cycle"

|Graph|Euler Cycle|
|:-:|:-:|
|![](prove06_graph4.png)|No Euler Cycle|
|![](prove06_graph5.png)|$\lbrace 1,2,3,4,5,1,4,6,1\rbrace$|
|![](prove06_graph6.png)|No Euler Cycle|

## Question 5 (20 points)

Complete the tables below to identify the final state (per the FSM diagram) and whether that final state was an accepting state for each of the inputs.   

**Part 1**

![](prove06_graph7.png)

|Input|Final State|Accepting (Yes/No)|
|:-:|:-:|:-:|
|00101|D|Yes|
|011100|C|No|
|01111|B|No|
|0101|D|Yes|
|00000|C|No|
|11111|D|Yes|
|11100|D|Yes|
|10011|D|No|

**Part 2**

![](prove06_graph8.png)

|Input|Final State|Accepting (Yes/No)|
|:-:|:-:|:-:|
|00101|S5|Yes|
|011100|S2|Yes|
|01111|S4|No|
|0101|S3|Yes|
|00000|S5|No|
|11111|S4|No|
|11100|S2|Yes|
|10011|S4|No|

## Question 6

Describe the bit string recognized/accepted by the following FSM:

![](prove06_graph9.png)

Answer: 01
0101
010101
01010101 and any that deviate from this will not work.