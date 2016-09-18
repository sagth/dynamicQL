from qspin.operators import hamiltonian
from qspin.basis import spin_basis_1d

import numpy as np



def Hamiltonian(L,J,hz,fun=None,basis=None):
	######## define physics
	if basis is None:
		basis = spin_basis_1d(L=L,kblock=0,pblock=1)
			
	zz_int =[[J,i,(i+1)%L] for i in range(L)]
	x_field=[[1.0,i] for i in range(L)]
	z_field=[[hz,i] for i in range(L)]

	static = [["zz",zz_int],["z",z_field]]
	dynamic = [["x",x_field,fun,[]]]

	kwargs = {'dtype':np.float64,'basis':basis,'check_symm':False,'check_herm':False}
	H = hamiltonian(static,dynamic,**kwargs)

	return H, basis
