import numpy as np

#we need a dictionary with the number of valence electrons for every atom in the trajectory 
valence={
"H":1,
"C":4,
"N":5,
"O":6,
"S":6
}

#index for the 4 molecules the we want to track 
idx1=[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20, 21]
idx2=[31, 32, 33, 35, 38, 39, 41, 42, 44, 45, 46, 48, 49, 51, 53, 54, 57, 58, 59, 60, 61, 34]
idx3=[23,24,25,26,27,28,29,30]
idx4=[36, 37, 40, 43, 47, 50, 52, 55]
protoni=[22,56]

#open trajectory file and get the number of atom in the box
filename="traj.xyz"
xyz=open(filename)
n_atoms=xyz.readline() # I need the number of atoms in the box before starting 
xyz.close()


class eof(Exception): pass

def read_line(xyz):
	line=xyz.readline()
	if("" == line):
		raise eof #exception in caso of end of file
	else:
		return line		
	
#frame_extractor return a vector with dimensione [n_atoms,[atom,x,y,z,electron probabilty density]]

def frame_extract(xyz):
	n_atoms=read_line(xyz)
	title=read_line(xyz)
	frame=np.empty(shape=[0,5],dtype=object)
	for i in range(int(n_atoms)):
		line=read_line(xyz)
		atom,x,y,z,e=line.split()[0:5]
		e=valence[atom]-float(e)
		tmp=np.array([[atom,float(x),float(y),float(z),float(e)]],dtype=object)
		frame=np.append(frame,tmp,0)
	return frame


#--------------------------------------------#
# import all the trajectory i a numpy array  #
#--------------------------------------------#

xyz=open(filename)   #open file
#traject will be the union of all frame vectors
traject=np.empty(shape=[0,int(n_atoms),5],dtype=object)

j=0
try:
	while True:
		traject=np.append(traject,[frame_extract(xyz)],0)
		j+=1
		print(r'Frame=%i'%j)
except eof:
	print("eof")
	pass

#------------------------------------------------------------------------------------#
#all trajectory is loaded in a np.array of shape [n_step,n_atoms,5(x,y,z,elettrons)] #
#------------------------------------------------------------------------------------#





