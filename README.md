Scripts
=======

A simply class to normalize all outputs in console

Instalation
-----------

### Old School

    git clone https://github.com/madeindjs/writer.git
    cd writter
    python setup.py install

### New School

    pip install writer


### API usage


~~~Python
>>> from writer import Writer
>>> Writer.title('Hellow World!')
--------------------------------------------------------------------------------
                                 Hellow World!                                 
--------------------------------------------------------------------------------
>>> Writer.unsorted_list('hello', 'world', 'how r U?')
    -   hello
    -   world
    -   how r U?
>>> Writer.sorted_list('hello', 'world', 'how r U?')
    0 - hello
    1 - world
    2 - how r U?
>>> Writer.ask_int('give me an integer!')
give me an integer! (must be an integer)? ...a
give me an integer! (must be an integer)? ...b
give me an integer! (must be an integer)? ...1
>>> Writer.event('Something hapend..')
[x] Something hapend..
>>> Writer.event('Something goes wrong..', False)
[ ] Something goes wrong..
~~~

To Do
-----

* add units test (I know. I should begin with this..)
* support colors

Author
------

[Rousseau Alexandre][madeindjs]

License
-------

[MIT](https://opensource.org/licenses/MIT)


[madeindjs]: https://github.com/madeindjs/