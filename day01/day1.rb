input = File.readlines(ARGV.first)

# 
facing = 0
dirkey = {0 => 1, 1 => 1, 2 => -1, 3 => -1} 
ns = 0
ew = 0

# Iterate over each move in the input and determine the new facing direction
# and keep track of distance from 0, 0 in north/sourth and east/west directions
input[0].split(", ").each do |move|
  dir = move[0]
  spaces = move[1..-1].to_i

  # Determine new direction
  if dir == "R"
    facing += 1
  elsif dir == "L"
    facing -= 1
  end
  facing %= 4

  # Determine distance from 0, 0
  if facing == 0 || facing == 2
    ns += spaces * dirkey[facing]
  elsif facing == 1 || facing == 3
    ew += spaces * dirkey[facing]
  end
end

puts ns.abs + ew.abs
