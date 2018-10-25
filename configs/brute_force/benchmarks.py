def get_benchmark_info(benchmark):

	base_dir = '/home/tubitak/Desktop/cpu2006'
	cwd = base_dir + '/' + benchmark

	# return working directory, input, options

	if benchmark == 'astar':
		inp = ''
		options = ['rivers.cfg']

	if benchmark == 'bwaves':
		inp = ''
		options = []

	if benchmark == 'bzip2':
		inp = ''
		options = ['input.source'] + ['280']

	if benchmark == 'calculix':
		inp = ''
		options = ['-i'] + ['hyperviscoplastic']

	if benchmark == 'gamess':
		inp = base_dir + '/gamess/cytosine.2.config'
		options = []

	if benchmark == 'gems':
		inp = ''
		options = []

	if benchmark == 'gobmk':
		inp = base_dir + '/gobmk/13x13.tst'
		options = ['--quiet'] + ['--mode'] + ['gtp']

	if benchmark == 'gromacs':
		inp = ''
		options = ['-silent'] + ['-deffnm'] + ['gromacs'] + ['-nice'] + ['0']

	if benchmark == 'h264':
		inp = ''
		options = ['-d'] + ['foreman_ref_encoder_baseline.cfg']

	if benchmark == 'hmmer':
		inp = ''
		options = ['nph3.hmm'] + ['swiss41']

	if benchmark == 'lbm':
		inp = ''
		options = ['3000'] + ['reference.dat'] + ['0'] + ['0'] + ['100_100_130_ldc.of']

	if benchmark == 'leslie3d':
		inp = base_dir + '/leslie3d/leslie3d.in'
		options = []

	if benchmark == 'libquantum':
		inp = ''
		options = ['1397'] + ['8']

	if benchmark == 'mcf':
		inp = ''
		options = ['inp.in']

	if benchmark == 'milc':
		inp = base_dir + '/milc/su3imp.in'
		options = []

	if benchmark == 'namd':
		inp = ''
		options = ['--input'] + ['namd.input'] + ['--output'] + ['namd.out'] + ['--iterations'] + ['38']

	if benchmark == 'omnetpp':
		inp = ''
		options = ['omnetpp.ini']

	if benchmark == 'povray':
		inp = ''
		options = ['SPEC-benchmark-ref.ini']

	if benchmark == 'sjeng':
		inp = ''
		options = ['ref.txt']

	if benchmark == 'soplex':
		inp = ''
		options = ['-m45000'] + ['pds-50.mps']

	if benchmark == 'tonto':
		inp = ''
		options = []

	if benchmark == 'xalanc':
		inp = ''
		options = ['t5.xml'] +  ['xalanc.xsl']

	if benchmark == 'zeusmp':
		inp = ''
		options = []



	if benchmark == 'parallel':
		inp = ''
		options = []

	return cwd, inp, options


def get_benchmark_fastforward(benchmark):

	ff_block = 0

	simpoints = {}
	simpoints['astar'] = 8
	simpoints['bwaves'] = 2
	simpoints['bzip2'] = 38		# Not the best, but the other one is further away
	simpoints['calculix'] = 0
	simpoints['gamess'] = 7
	simpoints['gems'] = 36
	simpoints['gobmk'] = 3
	simpoints['gromacs'] = 12
	simpoints['h264'] = 10
	simpoints['hmmer'] = 10
	simpoints['lbm'] = 6
	simpoints['leslie3d'] = 10
	simpoints['libquantum'] = 3
	simpoints['mcf'] = 4
	simpoints['milc'] = 10
	simpoints['namd'] = 13
	simpoints['omnetpp'] = 11
	simpoints['povray'] = 59
	simpoints['sjeng'] = 3
	simpoints['soplex'] = 2
	simpoints['tonto'] = 10
	simpoints['xalanc'] = 4


	if not benchmark in simpoints:
		print('SIMPOINT BEGINNING BLOCK COULD NOT BE FOUND')

	ff_block = simpoints[benchmark]

	return ff_block * 200000000