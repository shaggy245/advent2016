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
dirkey = [1, 1, -1, -1]
current_point = [0, 0]
last_point = [0, 0]
visited_points = []
first_cross = nil

# Iterate over each move in the input and determine the new facing direction
# create list of horizontal lines and vertical lines and check if the current line
# crosses a line in the opposite list
catch (:found) do 
  input[0].split(", ").each do |move|
    # Split input into direction and spaces
    dir = move[0]
    spaces = move[1..-1].to_i

    # Determine new direction-facing based on current direction and new direction
    if dir == "R"
      facing += 1
    elsif dir == "L"
      facing -= 1
    end
    facing %= 4

    # Determine new current point
    # Iterate over points between last current point and new current point
    # Check if any of those points have been hit before, otherwise add each
    # point to the visited_points list
    # Each direction must be handled separately since it changes how the points
    # between the endpoints are iterated over.
    if facing == 0 
      current_point[1] += spaces * dirkey[facing]

      (last_point[1]..(current_point[1] - 1)).each do |y|
        if visited_points.include? [current_point[0], y]
          first_cross = [current_point[0], y]
          throw :found
        else
          visited_points.append([current_point[0], y])
        end
      end
    elsif facing == 2
      current_point[1] += spaces * dirkey[facing]

      ((current_point[1] + 1)..last_point[1]).reverse_each do |y|
        if visited_points.include? [current_point[0], y]
          first_cross = [current_point[0], y]
          throw :found
        else
          visited_points.append([current_point[0], y])
        end      
      end
    elsif facing == 1
      current_point[0] += spaces * dirkey[facing]
    
      (last_point[0]..(current_point[0] - 1)).each do |x|
        if visited_points.include? [x, current_point[1]]
          first_cross = [x, current_point[1]]
          throw :found
        else
          visited_points.append([x, current_point[1]])
        end
      end
    elsif facing == 3
      current_point[0] += spaces * dirkey[facing]

      ((current_point[0] + 1)..last_point[0]).reverse_each do |x|
        if visited_points.include? [x, current_point[1]]
          first_cross = [x, current_point[1]]
          throw :found
        else
          visited_points.append([x, current_point[1]])
        end
      end
    end
    
    last_point = current_point.dup
  end
end

puts "FINAL:"
puts "First cross: #{first_cross}"
puts "Total distance: #{first_cross[0].abs + first_cross[1].abs}"

