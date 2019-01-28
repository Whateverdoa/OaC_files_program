#  function that provides one roll
#  begin nummer en een aantal per rol


def roll_maker(start, per_rol):
	""" 1 rol , x length , n voorloop """
	a = '5'  # filling out with zeros string
	b = '>'  # before , determine with an if else loop
	c = '<' # after

	for n in range(start, per_rol + 1):
		# print(n)
		print(f'{n :>0{a}}', end=";leeg.pdf\n")
		n += 1

# start = 1
# roll_maker(1,4)


for i in range(4):		# 4 banen onder elkaar
	i = 1				# hard coded variables
	roll_maker(i,4)
	if i < 4:
		print("\n.;stans.pdf"*4, end="\n")  # regel voor wikkel wordt ook variable

