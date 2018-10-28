input = File.readlines(ARGV.first, chomp: true)

good_tris = 0

input.each do |line|
  sides = line.split(" ").map(&:to_i).sort
  if sides[0] + sides[1] > sides[2] 
    good_tris += 1
  end
end

puts good_tris
