inputfile = open("../headbadges.train.arff");

ignore = "true";

for line in inputfile:
	if "@data" in line.strip():
		ignore="false"
		continue

	if ignore == "false":



