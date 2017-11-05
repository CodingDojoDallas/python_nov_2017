name =["Anna","Eli"," Pariece","Brendan","Amy","Shane","Oscar"]
favorite_animal =["horse","cat","spider","giraffe","ticks","dolphins","llamas"]
new_dic={}
def makedict(arr1,arr2):
	new_dic =dict(zip(arr1,arr2))
	return new_dic 

new_dic = makedict(name,favorite_animal)
print new_dic
 