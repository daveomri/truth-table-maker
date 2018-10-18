# truth-table-maker
Insert logical formula and get tree and table of truth

Hello there, as the text above says, this program is designed for evaluation of logical formulas. 
Expected input is through stdin, but you can change it if you want, simply add your logical formula 
to self.formula, and all should be set up.

In this program is really important the syntax of input. Don't worry about bad inputs, I add a function, that gives you NaLF, 
Not a Logical Formula, if you use wrong syntax. Soo, easier is to get NaF then output you want.
I don't really know, how to describe what you should do, therefore I will show you a few of rihgt formated inputs, 
you can find them in input file.

For example logical formula for implication   ->  (A)i(B)
            logical formula for conjuction    ->  (A)c(B)
            logical formula for disjunction   ->  (A)d(B)
            logical formula for equivalence   ->  (A)e(B)
            logical formula for negation      ->  n(A)

It's nessesary to use correctly brackets. 
For example this is right syntax (((A)d(B))i((C)c(D)))
((atomic formula)logical component(atomic formula))
Example of some more complex logical formula.
(((atomic formula)logical component(atomic formula))logical component((atomic formula)logical component(atomic formula)))
And so on..

Thanks for reading this file and have fun.
