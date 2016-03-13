# tinkering to try to better understand code blocks...

# a few pearls from "The Ruby Programing Language", Flanagan, Matsumato (2008):

# Blocks may not stand alone; they are only legal following a method invocation. 
# You can, however, place a block after any method invocation; 
# if the method is not an iterator and never invokes the block with yield, the block will be silently ignored.

# Blocks define a new variable scope: 
# variables created within a block exist only within that block and are undefined outside of the block.
# Be cautious, however; the local variables in a method are available to any blocks within that method.

# ----------

# So... blocks pass code to methods, which then use 'yield' to return appropriate results as needed. 

# define my own iterators using yield

# empty
def md0
end

def md1
	yield "a - md1"
end

def md2
	yield "a - md2"
	yield "b - md2"
end

def mdputs
	puts "there is no yield in this method, so it never yields control to the block of code passed to it and that block is silently ignored."
end

def lev1
	puts 'In lev1. An invocation here of "lev2 {}" results in no code block being executed.\nIf we instead invoke "lev2 {yield}" then we can pass the code block further along...'
	lev2 {yield}
end

def lev2
	puts 'In lev2, which is called from level 1. If the "yield" in this level is commented out, then the code block silently fails at *this* level...' 
	yield
end

puts 'invoke "md0" -- no block, no params'
md0
puts '>> no result'

puts 'invoke "md0 {} -- empty block, no params'
md0 {}
puts '>> no result'

puts 'invoke "md0 do end -- alternate to above'
md0 do end
puts '>> no result'

puts 'invoke "md1" -- one yield, no block, no params'
# md1
puts '>> would produce an ERROR of: no block given -- yield in def means ruby expects a block, params optional'

puts 'invoke md1 {|x|}  -- block of param only. Nothing to execute, so presumably the method passes control to the block at (each) yield, but there is no code to execute, and the method continues.'
md1 {|x|}
puts '>> no result'

puts 'invoke "mdputs {puts "this code silendtly ignored"} -- in this case, we have a block of code, but there is no point at which the method yields control to it.'
mdputs {puts "this code silently ignored"}
puts '>> no result'

puts 'invoke "lev1 {puts "is this code silently ignored?"} -- can we pass code into nested invocations?'
lev1 {puts 'is this code silently ignored?'}
puts '>> NO! As long as lev2 includes a yield to lev1 which in turn invokes lev2 with a yield to the initial code, the block is executed in lev2 only.'

puts 'invoke md2 {|x| puts x}'
md2 {|x| puts x}
puts '>> just to illustrate that we can have multiple yields per iteration...'

puts 'invoke 1.upto(2) {|x| puts x} -- more traditional use of built in iterator method on number object.'
1.upto(2) {|x| puts x}
puts '>> simple iteration.'

puts 'invoke 1.upto(2) do |x| md2 {|y| puts x,y} end -- to show multiple yields per iteration, custom iterators, && nesting'
1.upto(2) do |x|
	md2 {|y| puts x,y}
end
puts '>> End Demo. As a result of all this tinkering, the way I am now thinking of a code bock is a means to pass code (and optional parameters) to a method, which in turn will *yield* control to the code block as defined within that method. The built in iterators (each, upto, etc.) are common examples, but any method can use "yield" as often as needed, for as many iterations as makes sense, to best use a block of code passed to it.'

