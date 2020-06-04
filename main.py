import example_module

print("Whoa, it just works??")
print(example_module.test_method())

print("\n")
print(example_module.SOME_CONSTANT)
example_module.SOME_CONSTANT = 34
print(example_module.SOME_CONSTANT)
print("But.. it's actually not a constant. Just don't go changing it like this..!")
