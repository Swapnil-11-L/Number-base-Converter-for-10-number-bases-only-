while True:
    number = int(input("Enter the number (type in 69420 to exit): "))
    if number == 69420:
        break
    current_base = int(input("Which base is the number right now? "))
    number_base = int(input("Enter the number base you wanna convert in: "))
    def lenght(n):
        len_count = 0
        while True:
            result = n // 10
            n = result
            len_count += 1
            if (result ==0):
                return len_count

    def converter(n , number_bose):
        temp = n
        count =0
        array =[]
        while True:
            result = temp // number_bose
            reminder = temp % number_bose
            temp = result
            count+=1
    #print("count=", count)
    #print (f"temp = {temp} , result = {result} and reminder = {reminder}")
            array.append(reminder)
            if result == 0:
                break

        for i in range (count-1,-1,-1):
            print(array[i], end="")

    tenth_base_number = 0
    if current_base != 10:
        temp_number = number
        i=0
        while True:
            new_result = temp_number // 10
            new_reminder = temp_number % 10
            tenth_base_number += (new_reminder)*(current_base**i)
        #print(f"for {i} the number is {tenth_base_number}")
            temp_number = new_result
            i+=1
            if new_result == 0:
                break
        converter(tenth_base_number , number_base)
        print('\n')

    else:
        converter(number, number_base)
        print('\n')

