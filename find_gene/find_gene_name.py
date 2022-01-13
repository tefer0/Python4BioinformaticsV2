
def get_genes(x,y):
            with open(x, 'r') as gene_file:
                with open(y, 'w') as gene_names: 
                    count = 0
                    flag = False
                    for line in gene_file:
                        if line.startswith('______________'):
                            flag = True
                            count += 1
                            continue
                        elif line.startswith('-'):
                            flag = False
                        if flag and count==2:
                            gene_names.write(line.split(" ")[0] + '\n')