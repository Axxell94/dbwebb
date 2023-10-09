
def main():
    stop = False
    while not stop:
    
        print("13) country_data")
        print("14) emission change")
        print("15) find_all_indexes")
        
        print("q) Quit.")

        choice = input("--> ")
        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            stop = True

         elif choice == "13":
            hej = input("Search a country: ")
            search_country(hej)        
            if ValueError:  
                print("Country does not exist!")

         elif choice == "13":
            hej = input("Search a country: ")
            emission_functions.search_country(hej)        
            #if ValueError:  
               # print("Country does not exist!")
               # ska fånga exception som jag raise i functionen, hur?
            

         elif choice == "14":
            hej = input(" Search for a country and 1-2 years (1990, 2005, 2017) ")
            hej = hej.split(" ")
        
            if len(hej) == 3:
                get =emission_functions.get_country_change_for_years(hej[0], hej[1], hej[2])
                print(get)
            elif len(hej) == 2:
                get=emission_functions.get_country_year_data_megaton(hej[0], hej[1])
                print(get)  
            elif len(hej) == 4: #Hong Kong och sen även United States of America sabbar de övre
                hej= ((hej[0]+ " " + hej[1]), hej[2], hej[3])
                get =emission_functions.get_country_change_for_years(hej[0], hej[1], hej[2])
                print(get)    
            elif len(hej) > 4:
                print("Too many inputs")
            else:    
                print("Too few inputs")
            # ska fånga exception som jag raise

        elif choice == "15":
            country_name = input("Enter a country: ")
            data= emission_functions.get_country_data(country_name) 
            emission_functions.print_country_data(data)
    
main()
