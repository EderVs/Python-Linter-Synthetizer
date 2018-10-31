import re
from default_functions import *

VARS_PATTERN  = re.compile(r"^_[a-zA-Z0-9_]*|^[a-z][_a-zA-Z0-9]*")

PYTHON_KEYWORDS = { "False"    : 0,
					"True"     : 0,
					"class"    : 0,
					"finally"  : 0,
					"is"       : 0,
					"return"   : 0,
					"None"     : 0,
					"continue" : 0,
					"for"      : 0,
					"lambda"   : 0,
					"try"      : 0,
					"def"      : 0,
					"from"     : 0,
					"nonlocal" : 0,
					"while"    : 0,
					"and"      : 0,
					"del"      : 0,
					"global"   : 0,
					"not"      : 0,
					"with"     : 0,
					"as"       : 0,
					"elif"     : 0,
					"if"       : 0,
					"else"     : 0,
					"or"       : 0,
					"yield"    : 0,
					"assert"   : 0,
					"import"   : 0,
					"pass"     : 0,
					"break"    : 0,
					"except"   : 0,
					"in"       : 0,
					"raise"    : 0					 
				}

def transformation_generator(inputoutputs, terminals):
	"""
		Receives an array of examples called inputoutputs and an array of
		functions, which are the terminal functions specified in default_functions.
		Returns a function that satifies the output representation of the 
		given inputs.
		The output transfromation will be a composition of functions defined in 
		default_functions.py,
		in particular, the functions in vars_transformation array defined above.
		The output composition is based on synthesis bottom-up technique.
	"""

	global_bnd = 4
	terminals_indices = [[i] for i in range(len(terminals))]
	compositions = []	
	c = 0
	while c < global_bnd:
		if c == 0:
			compositions = [[i] for i in range(len(terminals))]
		else:
			compositions = grow(terminals_indices, compositions)
		
		for composition in compositions:
			if is_correct(composition, terminals, inputoutputs):
				return [terminals[i] for i in composition] 
		c += 1

	return None


def grow(transformations, built_functions):
	"""
		Receives an array called transformations which contains indices of 
		the terminals functions.
		Receives an array called built_functions which are the compositions.
		The composition of functions is an array of indices, where each index 
		relates to a terminal function.
		This function will create a new array of indices that represents a 
		new composition, takes each built_function and compose it with 
		every temrinal function. 
		Returns a new array of compositions.
	"""

	new_transformations = []
	
	for bf in built_functions:
		for t in transformations:
			new_transformations.append(bf + t)

	return new_transformations

def is_correct(composition, functions, inputoutputs):
	"""
		Receives the composition that will be evaluated, remember that
		composition is an array of indices, where the index maps to 
		a function in the array functions.
		Functions is the array that contains the terminal functions
		that transforms a string.
		The array inputoutputs will be the testing for the composition.
		The input will be evaluated with the given composition and 
		it'll be tested against it's output. If the 
		composition satisfies these constraints, then the function 
		returns True.
		Returns False if the evaluation with the composition doesn't 
		satisfy at most one of the constraints in inputoutputs.
	"""
	for example in inputoutputs:
		ex_in = example[0]
		ex_out = example[1]
		f = functions[composition[0]]
		eval = f(ex_in)
		i = 1
		while i < len(composition):
			f_index = composition[i]
			f = functions[f_index]
			eval = f(eval)
			i += 1
		if eval != ex_out:
			return False

	return True

def eval_composition(composition, input):
	"""
		Receives the composition that is an array of indices, 
		each index maps to an element of functions.
		Input that will be evaluated on the composition.
		Returns the evaluation of the composition with the input.
	"""

	f = composition[0]
	eval = f(input)
	i = 1
	while i < len(composition):
		f = composition[i]
		eval = f(eval)
		i += 1

	return eval


def map_variables(program_name, composition):
	"""
		Receives the name of the program where will search the variables.
		Each variable will be tracked with the regular expression defined in
		the constant VARS_PATTERN.
		Composition is the that will be applied to every varaible
		in the file.
		Terminals is the array of terminals functions
	"""

	file = open(program_name, 'r')
	variables_mapping = {}
	for line in file:
		non_space_line = line.strip("\t ")
		for var in re.findall(VARS_PATTERN, non_space_line):
			var = var.strip("\n\t ")      						
			if var not in PYTHON_KEYWORDS and var not in variables_mapping:
				new_var = eval_composition(composition, var)
				variables_mapping.update({var : new_var})

	return variables_mapping
					
def change_variables(program_name, terminals, inputoutputs):
	"""
		Receives the name of the program that will be read.
		Receives an array of terminals functions. This
		functions can be seen as the terminals of our grammar.
		Inputsoutputs are the provided examples by the user.
		This function will need to find a composed function
		that can change the variables names, this special function
		is generated using the synthesis technique called bottom-up.
		Now that the special function is defined, the function
		replaces all the variables names with the new ones.
		The output will be in the file new_[program_name].
	"""
		
	composition = transformation_generator(inputoutputs, terminals)
	if composition == None:
		file.close()
		return

	mapping = map_variables(program_name, composition)
	
	new_name = "new_" + program_name 
	new_file = open(new_name, 'w')	
	file = open(program_name, 'r')
	for line in file:
		new_line = line
		for word in line.split(" "):
			if word in mapping:
				mapped = mapping[word]
				new_line = new_line.replace(word, mapped)
		new_file.write(new_line)

	file.close()
	new_file.close()


# The program will search for a function that holds the constraints 
# of these examples.
inputoutputs = [["ejemplo_1", "_ejemplo_1_"], 
				 ["este_es_el_ejemplo_2", "_este_es_el_ejemplo_2_"]]

# The construction of the composed function is delimited by the 
# the terminal functions that we can use, so if there's an update 
# to the file default_functions.py that helps to build new variables names,
# that function must be added to this terminals array.
terminals = [all_upper, 
			 all_lower, 
			 first_upper, 
			 first_lower, 
			 to_upper_case, 
			 remove_underscores,
			 insert_first_underscore,
			 insert_last_underscore]

program_name = "example.py"
change_variables(program_name, terminals, inputoutputs)
print(" ~ Ver archivo new_%s" % program_name)


