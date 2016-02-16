#!/usr/bin/ruby -w
require 'singleton'

class PointStats
	include Singleton

	def initialize
		@n, @totalX, @totalY = 0, 0.0, 0.0
	end

	def record(point)
		@n += 1
		@totalX += point.x
		@totalY += point.y
	end

	def report
		puts "#{@n} -- points"
		puts "#{@totalX/@n} -- Average x"
		puts "#{@totalY/@n} -- Average y"		
	end

end

class Point
	attr_reader :x, :y

	def initialize(x,y)
		@x,@y = x,y
		PointStats.instance.record(self)
	end

	def self.unrecorded(x,y)
		instance = new(x,y)
	end

	ORIGIN = Point.unrecorded(0,0)
	UNIT_X = Point.unrecorded(1,0)
	UNIT_Y = Point.unrecorded(0,1)

	include Enumerable
	include Comparable

	def to_s
		"(#{@x},#{@y})"
	end

	def +(other)
		Point.new(@x + other.x, @y + other.y)
	rescue
		raise TypeError,
			"Point like argument expected"
	end

	def -@
		Point.new(-@x, -@y)
	end

	def *(scalar)
		Point.new(@x*scalar, @y*scalar)
	end

	def coerce(other)
		[self, other]
	end

	def [](index)
		case index
		when 0, -2: @x
		when 1, -1: @y
		when :x, "x": @x
		when :y, "y": @y
		else nil
		end
	end

	def each
		yield @x
		yield @y
	end

	def ==(o)
		if 0.is_a? Point
			@x==o.x && @y==o.y
		else
			false
		end
	end

	def eql?(o)
		if o.instance_of? Point
			@x.eql?(o.x) && @y.eql?(o.y)
		else
			false
		end
	end

	def hash
		code = 17
		code = 37*code + @x.hash
		code = 37*code + @y.hash
		code
	end

	def <=>(other)
		return nil unless other.instance_of? Point
		@x**2 + @y**2 <=> other.x**2 + other.y**2
	end

	def self.sum(*points)
		x = y = 0
		points.each { |p| x+=p.x; y+=p.y }
		Point.new(x,y)
	end

end

#demo :)

p first = Point.new(7,31)
first.each {|x| p x}
print first.to_s + "\n"
p second = Point.new(11,10)
p third = first + second
p fourth = -first
p first*3
p 3*first
p third.eql?(fourth)
p test = first.hash
p first[1]
p first < second
p second < first
p total = Point.sum(first + second + third + fourth)
PointStats.instance.report
