input = File.readlines(ARGV.first)

def is_hor?(pt_1, pt_2)
  if pt_1[1] == pt_2[1] && pt_1[0] != pt_2[0]
    true
  else
    false
  end
end

# Some initial variables
facing = 0
dirkey = {1, 1, -1, -1} 
last_point = [0, 0]
current_point = [0, 0]
hor_lines = []
vert_lines = []

# Iterate over each move in the input and determine the new facing direction
# create list of horizontal lines and vertical lines and check if the current line
# crosses a line in the opposite list
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

  # Determine new current point
  if facing == 0 || facing == 2
    current_point[1] += spaces * dirkey[facing]
  elsif facing == 1 || facing == 3
    current_point[0] += spaces * dirkey[facing]
  end

  last_point = current_point
end

