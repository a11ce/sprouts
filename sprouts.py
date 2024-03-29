import collections

Loop = collections.namedtuple('Loop', 'outer inner')
Graph = collections.namedtuple('Graph', 'loops singleEdges')

def isPath(path, graph):
    loops = graph.loops
    exposed = exposedPoints(graph) 
    if path[0] in exposed and path[1] in exposed:
        return True
    for loop in loops:
        if  ( 
                (
                    (path[0] in loop.inner and path[1] not in loop.outer) 
                    or 
                    (path[1] in loop.inner and path[0] not in loop.outer)
                )
                and not
                (
                    (path[0] in loop.inner and path[1] in loop.inner)
                )
            ):
            print(loop)
            return False
    return True

def exposedPoints(graph):
    loops = graph.loops
    exposed = []
    for loop in loops:
        exposed.extend(loop.outer)
    for loop in loops:
        if loop.outer:
            for point in loop.inner:
                try:
                    exposed.remove(point)
                except:
                    pass
        else:
            exposed.extend(loop.inner)
    return exposed

def connectionsTo(point, graph):
    count=0
    for loop in graph.loops:
        if point in loop.outer:
            count += 2
    for edge in graph.singleEdges:
        if point in edge:
            count += 1
    return count

def pointsInGraph(graph):
    points = []
    for loop in graph.loops:
        points.extend(loop.outer + loop.inner)
    for edge in graph.singleEdges:
        points.extend(edge)
    return list(set(points))

#def existingEdges(graph):
 #   edges = []
  #  for loop in graph.loops:
        

def possibleMoves(graph):
    possible = []
    points = pointsInGraph(graph)
    for i in range(len(points)):
        startPoint = points[i]
        if connectionsTo(startPoint, graph) < 3:
            possTarg = points[i+1:]
            for targ in possTarg:
                if isPath( (startPoint,targ), graph) and connectionsTo(targ, graph) < 3:
                    possible.append( {startPoint,targ})
    return possible

def main():

    turn3 = Graph(
            [
            Loop([1,6],[2,5,7,8]),
            Loop([2,5,7],[8]),
            ],
            [
            [5,6],
            [2,8]
            ]
            )
            
    turn5 = Graph(
            [ 
            Loop([1,6],[2,3,4,5]),
            Loop([2,4,5], [3]),
            Loop([], [7]),
            ],
            [
            [2,3],
            [3,4],
            [5,6],      
            ]
            )
    
    
    print(exposedPoints(turn3))
    print(isPath( (8,7) ,turn3) )
    print(connectionsTo(7, turn3))
    #print(pointsInGraph(testGraph))
    print(possibleMoves(turn3))
if __name__ == "__main__":
    main()