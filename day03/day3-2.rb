input = File.readlines(ARGV.first, chomp: true)

good_tris = 0

# Iterate over 3 lines at a time
# so we can check 3 triangles at a time
input.each_slice(3) do |tris|
  # Take the array of 3 strings, split each string into an array, transpose the multi-dim array,
  # and to_i and sort the new array items
  tris = tris.each.map { |x| x.split(" ")}.transpose.each.map { |x| x.map(&:to_i).sort }
  tris.each do |tri|
    if tri[0] + tri[1] > tri[2]
      good_tris += 1
    end
  end
end
puts good_tris
