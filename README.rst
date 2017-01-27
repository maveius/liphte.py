LiphtePY is a fork of Python template engine called Breve that is designed to be clean and elegant with minimal syntax. LiphtePY was heavily inspired by rudykocur.

A short example::

 T.html [
     T.head [
         T.title [ 'A LiphtePY Template' ]
     ],

     T.body [
         T.h1 [ 'Briefly, LiphtePY' ], T.br,
         T.div ( style = 'text-align: center;' ) [
             T.span [ '''
                 As you can see, LiphtePY maps very
                 directly to the final HTML output.
             ''' ]
         ]
     ]
 ]

