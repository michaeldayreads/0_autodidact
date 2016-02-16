class Point

	@n = 0
	@totalX = 0
	@totalY = 0

	def initialize(x,y)
		@x, @y = x, y
	end

	def self.new(x,y)
		@n +=1
		@totalX += x
		@totalY += y

		super

	end

	def self.report
		puts "#{@n} -- points"
		puts "#{@totalX.to_f/@n} -- Average x"
		puts "#{@totalY.to_f/@n} -- Average y"
	end

	class << self
		attr_accessor :n, :totalX, :totalY
	end

	ORIGIN = Point.new(0,0)
	UNIT_X = Point.new(1,0)
	UNIT_Y = Point.new(0,1)

	include Enumerable
	include Comparable

	attr_reader :x, :y

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

#Struct.new("PointStruct", :x, :y)
PointStruct = Struct.new(:x, :y)

class PointStruct
	
	#undef x=,y=,[]=

	def add!(other)
		self.x += other.x
		self.y += other.y
		self
	end

	include Comparable

	def <=>(other)
		return nil unless other.instance_of?(Point)
		self.x**2 + self.y**2 <=> other.x**2 + other.y**2
	end

end

first = Point.new(7,31)
p first
first.each {|x| p x}
print first.show + "\n"
p second = Point.new(11,10)
third = first + second
p third
fourth = -first
p fourth
p first*3
p 3*first
p third.eql?(fourth)
p test = first.hash
p first[1]
p first < second
p second < first
p mp = PointStruct.new(8,8)
p mp.add! first
p total = Point.sum(first + second + third + fourth)
Point.report
