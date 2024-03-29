from .alignment import Alignment
from .algorithm import *

class AlgorithmGreedy(Algorithm):
    def run(self, aln:Alignment, max_steps:int):
        """
        Run at most `max_steps` steps of the greedy algorithm, or until it finds the solution.
        At the end of the run a tree representing a state of the algorithm is produced and can be
        graphycally represented.
        """
        # reset the alignment before starting
        aln.reset()

        solution = None
        expanded = aln

        if max_steps == 0:
            i = 0
        else:
            for i in range(max_steps):
                # get the __best__ non expanded node so far
                expanded = aln.get_best_node_to_expand()
                
                if expanded:
                    expanded.expand()
    
                # check if a solution was found (GREEDY)
                solution = aln.get_solution()
    
                if solution:
                    # if a solution was found it's done!
                    break
            i += 1
    
        if expanded:
            # colour green the latest expanded node
            expanded.color = COLOR_EXPANDED_BOX
    
        if solution:
            # colour blue the solution if any was found
            solution.color = COLOR_SOLUTION_BOX
        else:
            # colour red the best unexplored node so far
            # which will be the green box in the a step
            best_non_expanded = aln.get_best_node_to_expand()

            if best_non_expanded:
                best_non_expanded.color = COLOR_BEST_BOX

        return solution is not None, i
