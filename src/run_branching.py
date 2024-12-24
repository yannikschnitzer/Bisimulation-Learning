from bisimulation_learning.fintely_branching.experiments import *
from bisimulation_learning.fintely_branching.cegis_solver import *
from bisimulation_learning.shared import *
    

def run_and_show(trs, tem):
    theta, eta = bisimulation_learning(trs, tem, iters=10000, explicit_classes=True)
    gamma = compute_adjacency_matrix(trs, tem, theta)
    draw_quotient(gamma, "Default Name")
    visualize_branching(theta, tem)

def run_and_print(trs, tem: BDTTemplate):
    start_time = time.time()  # Record the start time
    theta, eta = bisimulation_learning(trs, tem, iters=10000, explicit_classes=False)
    end_time = time.time()
    print(f"""
    theta = {theta},
    eta   = {eta} 
    """)
    print("Runtime Learning: " ,(end_time-start_time))

    start_time = time.time()
    gamma = compute_adjacency_matrix(trs, tem, theta)
    end_time = time.time()
    print("Runtime Quotient Extraction: " ,(end_time-start_time))

    for p in range(len(gamma)):
        for q in range(len(gamma[p])):
            if gamma[p][q]:
                print(f"{p}->{q}")
    
    formula, tree = tem.bdt_classifier(theta, tem.m, tem.num_params, tem.partitions)
    from z3 import simplify
    print(f"{simplify(formula)}")
    
    

if __name__ == "__main__":
    
    
    # trs, tem = tte_usf(10)
    #trs, tem = con_sf(10000)
    n = 10
    start_time = time.time()
    for i in range(n):
        #trs, tem = term_loop_2()
        #trs, tem = cubic()
        # trs, tem = tte_sf(100)
        trs, tem = con_usf(1000)
        #trs, tem = P18()
        #trs, tem = term_loop_nd_2()
        #trs, tem = term_loop_nd_y()
        #run_and_show(trs, tem)
        print("========================")
        run_and_print(trs, tem)
        print("========================")
        print("")
    end_time = time.time()
    print("Average runtime all in all: ", (end_time-start_time)/n)
    