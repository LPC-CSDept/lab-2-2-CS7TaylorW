def main():
    ##################################################
    # Comlete your code here
    ##################################################
    workhours = float (input ("Please enter the number of hours you have worked."))
    reg_hours = float (40)
    reg_rate = float (18.25)
    o_rate = float (27.78)
    o_hours = (workhours - 40)
    w_hours = (workhours - o_hours) 
    reg_charge = (w_hours * reg_rate)
    o_charge = (o_hours * o_rate)
    total_wage = (reg_charge + o_charge)
    print (reg_charge)
    print (o_charge)
    print (total_wage)

    pass


if __name__ == '__main__':
    main()

