build/X86/gem5.opt configs/tbtk/test.py --mem-size=4096MB --caches --l2cache --sys-clock=1GHz --l1d_size=16kB --l1d_assoc=4 --l1i_size=16kB --l1i_assoc=4 --l2_size=128kB --l2_assoc=8 --cpu-type=DerivO3CPU --cpu-clock=2GHz --fast-forward=10000000 --maxinsts=10000000 --cmd="calculix" -p 1000

