from important import do_important

def main():
    '''business logic for when running this module as the primary one!'''
    #setup()
    foo = do_important()
    print('business logic for when running this module as the primary one!')

if __name__ == '__main__':
    # Do something appropriate here, like calling a
    # main() function defined elsewhere in this module.
    main()
else:
	foo = do_important()
    # Do nothing. This module has been imported by another
    # module that wants to make use of the functions,
    # classes and other useful bits it has defined.
