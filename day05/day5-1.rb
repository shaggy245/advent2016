require 'digest'

input = File.readlines(ARGV.first, chomp: true)

input.each do |line|
  counter = 0
  coded = ''
  password = ''
  until password.length == 8 do
    md5 = Digest::MD5.new
    coded = md5.hexdigest line + counter.to_s
    if coded.start_with?('00000') 
      password = password + coded[5]
      puts coded[5]
    end
    counter += 1
  end
  puts password
end

