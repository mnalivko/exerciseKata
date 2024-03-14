import re

class StringCalculator:
    def calculate(self,arg):
        if not arg:
            return 0 # an empty sting retums zero
        delimiter = ',' 
        try:
            if arg.startswith("//"): 
                end_of_delimiter_line = arg.find('\n')
                delimiter_definition = arg[2:end_of_delimiter_line]
                if delimiter_definition.startswith('['):  # multi-character delimiters
                    delimiters = delimiter_definition.strip('[]').split('][')
                    delimiter = '|'.join(map(re.escape, delimiters))
                else:  # single-character delimiter
                    delimiter = re.escape(delimiter_definition)

                arg = arg[end_of_delimiter_line+1:]  
            numbers = re.split(delimiter, arg)

            if ',' in arg:  # comma-delimited case
                numbers = arg.split(',')
            elif '\n' in arg:  # newline-delimited case
                numbers = arg.split('\n')
            else:  
                return int(arg) # single number case

            if len(numbers) == 3:
                numbers = [int(x) for x in numbers]
                negative_numbers = [x for x in numbers if x < 0]  # negative numbers
                if negative_numbers:
                    raise ValueError(f"Negatives not allowed: {negative_numbers}")
                numbers = [x for x in numbers if x <= 1000] # numbers greater than 1000
                return sum(numbers)
            if len(numbers) != 2:
                raise ValueError("Invalid input")
            return sum(int(x) for x in numbers)
        except ValueError:
            raise ValueError("Invalid input")
        

        
        
    