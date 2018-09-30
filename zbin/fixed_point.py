

def float2fixed(num, fb):
	scaling_factor = float(2**fb)
	fixed = num * scaling_factor

	return int(round(fixed))

def fixed2float(num, fb):
	return num / (2** fb)
