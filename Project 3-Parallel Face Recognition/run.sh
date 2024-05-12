echo "**************************************16 threads k =1********" >> alba_mustafaj.output
export OMP_NUM_THREADS=16 && ./lbp_omp 1 >> alba_mustafaj.output
