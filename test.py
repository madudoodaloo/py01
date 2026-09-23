#!/usr/bin/env python3

import builtins

for dunder in dir(builtins):
	if dunder.startswith("__"):
		value = getattr(builtins, dunder)
		print(dunder, "-", value)

print()
for method in dir(str):
	print(method.__class__)

print()
for function in dir(builtins):
	if function.find("function"):
		print(function)

