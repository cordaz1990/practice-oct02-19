def process_file(reader: TextIO) -> int:
    """ Read and process reader, which must start with a time_series header.
    Return the largest value after the header. There may be multiple pieces of data on each each line.
    
    >>> infile = StringIO('Example\\n 20. 3.\\n 100. 17. 15.\\n')
    >>> process_file(infile)
    100
    """
    
    line = time_series.skip_header(reader).strip()
    #The largest value so far is the largest on this first line of data.
    largest = find_largest(line)
    
    #check the rest of the line for largerger values.
    for line in reader:
      large = find_largest(line)
      if large > largest:
        largest = large
        
    return largest
  
 if __name__ == '__main__':
    with  open ('lynx.txt','r') as input_file:
      print(process_file(input_file))
