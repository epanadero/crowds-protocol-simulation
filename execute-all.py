import os

def p(s):
    #Make the first string point to the root of the project with respect to the directory this process is running 
    #return './Project\\ 1/'+s
    return './'+s

cor = ['cor', 'nocor']
uniform = ['uniform', 'nouniform']
phis = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.92, 0.94, 0.96, 0.98, 0.99]
fix = ['last-honest', 'initiator']

simulate_path = p('simulate.py')
map_path = p('map_observables.py')
generate_fbleau_input = p('generate_fbleau_input.py')

for c in cor:
    for u in uniform:
        for phi in phis:
            for f in fix:

                # 1. SIMULATE
                #phi
                graph = p('data/adj-matrices/adj-10-70')
                if c == 'cor':
                    corrupted = p('data/corrupt/cor')
                else:
                    corrupted = p('data/corrupt/nocor')
                users = p('data/users/users-'+c+'-'+u)
                broken = 3
                #f
                simulate_out = p('data/simulation-outputs/simulate/'+c+'-'+u+'-'+f+'-'+str(phi))
                simulate = 'python3 {} {} {} {} {} {} {} > {}'.format(simulate_path, phi, graph, corrupted, users, broken, f, simulate_out)
                
                print(simulate)
                os.system(simulate)

                # 2. MAP
                map_out = p('data/simulation-outputs/map/'+c+'-'+u+'-'+f+'-'+str(phi)+'.csv')
                map_ = 'python3 {} {} {} {}'.format(map_path, simulate_out, users, map_out)
                
                print(map_)
                os.system(map_)

                # 3. GENERATE FBLEAU INPUT
                fbleau_train = p('data/simulation-outputs/fbleau-input/'+c+'-'+u+'-'+f+'-'+str(phi)+'-train.csv')
                fbleau_test = p('data/simulation-outputs/fbleau-input/'+c+'-'+u+'-'+f+'-'+str(phi)+'-test.csv')
                fbleau_input = 'python3 {} {} {} {}'.format(generate_fbleau_input, map_out, fbleau_train, fbleau_test)

                print(fbleau_input)
                os.system(fbleau_input)

                # 4. EXECUTE FBLEAU
                fbleau_output = p('data/simulation-outputs/fbleau-output/'+c+'-'+u+'-'+f+'-'+str(phi))
                fbleau_execute = 'fbleau nn {} {} > {}'.format(fbleau_train, fbleau_test, fbleau_output)
                
                print(fbleau_execute)
                os.system(fbleau_execute)